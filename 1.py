import keyboard
import pyaudio
import wave
import speech_recognition as sr

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


filename = "output.wav"
record_audio(filename)



r = sr.Recognizer()
harvart = sr.AudioFile(r'C:\Users\PeterRuan\Desktop\static_16919367030710594_SparkApi_Python\output.wav')
with harvart as source:
    audio = r.record(source)
try:
    print('you said:'+r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print('I can not hear clearly')
except sr.RequestError as e:
    print('error;{0}'.format(e))
