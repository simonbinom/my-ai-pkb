import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("Aufnahme startet...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    scipy.io.wavfile.write(filename, fs, audio)
    print("Fertig.")

def transcribe(filename="input.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result['text']