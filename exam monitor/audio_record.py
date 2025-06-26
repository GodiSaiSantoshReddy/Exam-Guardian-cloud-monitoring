import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(output_file, duration=5, fs=44100):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write(output_file, fs, audio)
