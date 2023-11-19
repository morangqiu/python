import keyboard
import pyaudio
import wave
from pynput.keyboard import Listener
import logging

#def on_press()

def record_audio(filename):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("开始录音，请按下空格键停止录音")

    frames = []

    while True:
        data = stream.read(chunk)
        frames.append(data)
        if keyboard.is_pressed('space'):
            print('done')
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == '__main__':
    filename = "output.wav"
    record_audio(filename)