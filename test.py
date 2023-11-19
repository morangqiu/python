import SparkApi
#以下密钥信息从控制台获取
appid = "2f65421f"     #填写控制台中获取的 APPID 信息
api_secret = "NGRkZWU4MGRkMjM3MzBmOGM3ZGE4NzQ1"   #填写控制台中获取的 APISecret 信息
api_key ="e71d05993b66721b8701e3657c6a9efc"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
#domain = "general"   # v1.5版本
domain = "generalv2"    # v2.0版本
#云端环境的服务地址
#Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址


text =[]

# length = 0

def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    

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
oldPath = r'C:\Users\PeterRuan\Desktop\static_16919367030710594_SparkApi_Python\output.wav'
# oldPath='temp-1.wav'



if __name__ == '__main__':
    text.clear
    while(1):
        record_audio(filename)
        baidu_Speech_To_Text(oldPath)
        print(context)

        question = checklen(getText("user",context))
        SparkApi.answer =""
        print("星火:",end = "")
        SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
        getText("assistant",SparkApi.answer)
        # print(str(text))




