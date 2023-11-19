import pyaudio,wave
from tqdm import tqdm
import keyboard

def audio_record(out_file):
    CHUNK=1024
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=16000
    ##
    p=pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    wf = wave.Wave_write(out_file)
    wf.setnchannels(CHANNELS)
    wf.setframerate(RATE)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    print('开始录制。。。')

    frames = []

    keyboard.wait()
    while True:
        data = stream.read(CHUNK)
        wf.writeframes(data)
        if keyboard.press_and_release('space'):
            break
            print("录音结束")


    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()


out = str('test.wav')
keyboard.add_hotkey('space', print, audio_record(out) )
