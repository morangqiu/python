import keyboard
import pyaudio
import wave
import speech_recognition as sr

def record_audio(filename):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
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


filename = "output2.wav"





from aip import AipSpeech

def baidu_Speech_To_Text(filePath):  # 百度语音识别
    aipSpeech = AipSpeech('42239107','Y33QC1dmfyC0yto3CgZE7gAI', 'plrG91Tp87FiBl1mZ9dSyzG6CdM9ur2z')  # 初始化AipSpeech对象
    # 读取文件
    with open(filePath, 'rb') as fp:
        audioPcm = fp.read()
    json = aipSpeech.asr(audioPcm, 'wav', 16000, {'dev_pid':1737, })
    print(json)
    global context
    if 'success' in json['err_msg']:
        context = json['result'][0]
        print('成功，返回结果为：', context)
    else:
        context = '=====识别失败====='
        print('识别失败！')
    return context


# oldPath='./audio/韩红 - 家乡.mp3'
oldPath = r'C:\Users\PeterRuan\Desktop\static_16919367030710594_SparkApi_Python\output2.wav'
# oldPath='temp-1.wav'

if __name__ == '__main__':
    while True:
        record_audio(filename)
        baidu_Speech_To_Text(oldPath)
        print(context)