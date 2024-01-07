import torch
from . import commons
from . import utils
from .models import SynthesizerTrn
from .text import text_to_sequence
import re
from scipy.io.wavfile import write as wav_write


def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm