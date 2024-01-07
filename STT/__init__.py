import io
import speech_recognition as sr
from faster_whisper import WhisperModel

from datetime import datetime, timedelta
from queue import Queue
from tempfile import NamedTemporaryFile
from time import sleep

recognizer = sr.Recognizer()
recognizer.energy_threshold = 1000
recognizer.dynamic_energy_threshold = False

with sr.Microphone() as microphone:
    recognizer.adjust_for_ambient_noise(microphone)