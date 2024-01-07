import sys
from PySide6.QtCore import *
from PySide6.QtCore import QObject
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from UI.UI_MAIN import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from functools import partial
import pygame
from pygame import mixer
import pygame._sdl2.audio as sdl2_audio
import playsound

from webbrowser import open_new
from datetime import datetime
from shutil import rmtree
import tempfile

from TTS import *
from STT import *
from TRANSLATOR import *

class Load_Model(QThread):
    def __init__(self, window):
        QThread.__init__(self)
        self.window = window

    def stop(self):
        self.window.centralwidget.setEnabled(True)
        self.terminate()

    def run(self):
        self.window.label_current_status.setText('모델 로드 중')
        self.window.centralwidget.setEnabled(False)
        model_name = self.window.cb_char_name.currentText().strip()
        model_file = f'MODEL/{model_name}.pth'
        config_file = f"MODEL/{model_name}.json"
        
        hps = utils.get_hparams_from_file(config_file)
        self.window.hps = hps

        self.window.cb_lang_name.clear()
        self.window.cb_lang_name.addItems(list(hps.languages))

        text.symbols = list(hps.symbols.pad + hps.symbols.punctuation + hps.symbols.letters + hps.symbols.letters_ipa)
        net_g = SynthesizerTrn(
            len(text.symbols),
            hps.data.filter_length // 2 + 1,
            hps.train.segment_size // hps.data.hop_length,
            **hps.model).to(self.window.device)
        _ = net_g.eval()
        _ = utils.load_checkpoint(model_file, net_g, None)
        self.window.net_g = net_g
        self.window.centralwidget.setEnabled(True)
        self.window.label_current_status.setText('모델 로드 완료')
        


class Run_TTS(QThread):
    change_text = Signal(str)

    def __init__(self, window):
        QThread.__init__(self)
        self.window = window

    def stop(self):
        self.terminate()

    def send_local(self):
        playsound.playsound(self.window.tmp_filename, block=True)

    def translate(self, text, language_code):
        try:
            return translate_v2(text, language_code)
        except:
            try:
                return translate_v1(text, language_code)
            except:
                return text

    def run(self):
        self.window.tmp_filename = self.window.tmp_dir+'/'+datetime.now().strftime("%d%m%Y%H%M%S")+".wav"
        text = self.window.text_edit.toPlainText().strip()
        language_code = self.window.cb_lang_name.currentText().strip()
        if self.window.check_is_translate.isChecked():
            text = self.translate(text, language_code.lower())
            self.change_text.emit(text)
            self.window.label_current_status.setText("번역 완료")

        speed = self.window.vs_speed.value()/10
        if speed == 0:
            speed += 0.01

        self.window.label_current_status.setText('음성 합성 중')
        hps = self.window.hps
        net_g = self.window.net_g
        stn_tst = get_text(text, hps)
        with torch.no_grad():
            x_tst = stn_tst.to(self.window.device).unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).to(self.window.device)
            audio = net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1/speed)[0][0,0].data.cpu().float().numpy()
        wav_write(self.window.tmp_filename, hps.data.sampling_rate, audio)
        self.window.label_current_status.setText('음성 합성 완료')
        self.window.mixer.music.load(self.window.tmp_filename)
        self.window.mixer.music.play()
        self.window.mixer.music.set_volume(self.window.volume)
        self.send_local()
        self.window.label_current_status.setText('음성 송출 완료')



class Run_SR(QThread):
    sig_is_end = Signal(str)
    def __init__(self, window):
        super().__init__()
        self.window = window

    def stop(self):
        self.terminate()

    def run(self):
        recognizer.listen_in_background(microphone, self.sr_callback)
        while True:
            sleep(0.1)

    def sr_callback(self, recognizer, audio):
        try:
            if self.window.run_tts.isRunning():
                return False
            temp_file = NamedTemporaryFile().name
            open(temp_file, "wb").write(audio.get_wav_data())
            segments, _ = self.window.audio_model.transcribe(
                temp_file,
                beam_size=5,
                vad_filter=True,
                vad_parameters=dict(min_silence_duration_ms=300)
            )
            text = ''.join([s.text for s in segments]).strip()
            del audio, segments
            if not text:
                return None
            print(text)
            self.sig_is_end.emit(text)
        except Exception as e:
            print(e)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.hps = None
        self.net_g = None
        self.volume = None
        self.tmp_filename = ""
        self.tmp_dir = tempfile.gettempdir()+'/chattts'
        self.load_model = Load_Model(self)
        self.run_tts = Run_TTS(self)
        self.run_tts.change_text.connect(self.translation_finished)
        self.run_sr = Run_SR(self)
        self.run_sr.sig_is_end.connect(self.sr_finished)
        self.mixer = mixer
        self.cable_name = 'CABLE Input(VB-Audio Virtual Cable)'
        self.mixer.init(devicename=self.cable_name)

        QObject.connect(self.btn_run_tts, SIGNAL('clicked()'), self.send_voice)
        QObject.connect(self.dev_github, SIGNAL('triggered()'), partial(open_new, 'https://github.com/kdrkdrkdr'))
        QObject.connect(self.support, SIGNAL('triggered()'), partial(open_new, 'https://www.buymeacoffee.com/kdrkdrkdr'))
        QObject.connect(self.cb_char_name, SIGNAL('currentIndexChanged(int)'), self.load_tts_model)
        QObject.connect(self.vs_sound, SIGNAL('valueChanged(int)'), self.show_sound_value)
        QObject.connect(self.vs_speed, SIGNAL('valueChanged(int)'), self.show_speed_value)
        QObject.connect(self.check_is_sr, SIGNAL('stateChanged(int)'), self.get_text_with_sr)


        if torch.cuda.is_available():
            self.device = 'cuda'
            compute_type = 'float16'
        else:
            self.device = 'cpu'
            compute_type = 'int8'
        # self.device = 'cpu'
        # compute_type = 'int8'
        self.audio_model = WhisperModel(
            model_size_or_path='base',
            device=self.device, 
            compute_type=compute_type,
        )

        char_name_list = ['캐릭터 선택']+[os.path.splitext(i)[0] for i in os.listdir('MODEL') if i.endswith('.pth')]
        cb_char_height = self.cb_char_name.height()
        self.cb_char_name.setIconSize(QSize(cb_char_height, cb_char_height))
        for idx, cname in enumerate(char_name_list):
            self.cb_char_name.addItem(cname)
            if idx != 0:
                self.cb_char_name.setItemIcon(idx, QIcon(f'MODEL/{cname}.png'))

        if not self.is_vbcable_installed():
            QMessageBox.information(
                self, '경고',
                'VB-Cable을 인식할 수 없습니다.\nVB-Cable을 설치하세요.',
                QMessageBox.Yes
            )
            open_new('https://vb-audio.com/Cable/')
            sys.exit()


    def is_vbcable_installed(self):
        init_by_me = not pygame.mixer.get_init()
        if init_by_me: pygame.mixer.init()
        devices = tuple(sdl2_audio.get_audio_device_names(False))
        if init_by_me: pygame.mixer.quit()
        if not self.cable_name in devices:
            return False
        else:
            return True

    def get_text_with_sr(self, _):
        self.run_sr.stop()
        if self.check_is_sr.isChecked():
            self.run_sr.start()
        else:
            self.label_current_status.setText('-')

    def sr_finished(self, text):
        self.label_current_status.setText("음성 인식 완료")
        self.text_edit.setPlainText(text)
        self.run_tts.stop()
        self.send_voice()

    def translation_finished(self, text):
        self.text_edit.setPlainText(text)

    def load_tts_model(self):
        current_model = self.cb_char_name.currentIndex()
        if current_model:
            self.load_model.stop()
            self.load_model.start()
        else:
            self.cb_lang_name.clear()
            self.cb_lang_name.addItems(['언어 선택'])

    def send_voice(self):
        if self.cb_char_name.currentIndex() != 0:
            self.run_tts.stop()
            if self.mixer.music.get_busy():
                self.stop_voice()
            self.volume = self.vs_sound.value()/100
            if self.volume == 0:
                self.volume += 0.01
            self.run_tts.start()

    def stop_voice(self): 
        self.mixer.music.stop()
        self.mixer.music.unload()

    def show_speed_value(self, value):
        QToolTip.showText(self.mapToGlobal(self.sender().pos()), f'{value/10}')

    def show_sound_value(self, value):
        QToolTip.showText(self.mapToGlobal(self.sender().pos()), f'{value}')



if __name__ in '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    if not os.path.isdir(mw.tmp_dir): os.mkdir(mw.tmp_dir)
    mw.show()
    app.exec()
    mw.stop_voice()
    rmtree(mw.tmp_dir)
    sys.exit()
