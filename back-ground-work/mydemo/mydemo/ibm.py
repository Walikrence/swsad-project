import speech_recognition as sr
from pydub import AudioSegment
import time

if __name__ == '__main__':
    IBM_USERNAME = ''
    IBM_PASSWORD = ''
    
    song=AudioSegment.from_wav('C:\\school\\test.wav')
    mss = len(song)
    start = 1620*1000
    while start < mss:
        print(str(start/1000)[:-2]+': ', end='')
        end = start + 60000
        if end > mss:
            end = mss
        buff = song[start:end]
        start = end
        buff.export('tmp.wav', format='wav')
        r = sr.Recognizer()
        with sr.WavFile("tmp.wav") as source:
            audio = r.record(source)
            text = r.recognize_ibm(audio, username = IBM_USERNAME, password = IBM_PASSWORD, language = 'zh-CN')
            try :
                with open('result.txt', 'a') as f:
                    f.write(text)
                print(text)
            except e:
                print(e)
        time.sleep(5)