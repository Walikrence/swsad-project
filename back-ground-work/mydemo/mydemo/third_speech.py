from aip import AipSpeech
from pydub import AudioSegment
import io

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def changesound(filePath):
	print('begin: '+filePath)
	audio = AudioSegment.from_file(filePath)
	print('read: '+filePath)
	mono = audio.set_frame_rate(16000).set_channels(1)
	print('set: '+filePath)
	mono.export('test.pcm', format="s16le")
	print('export: '+filePath)

if __name__ == '__main__':
	APP_ID = ''
	API_KEY = ''
	SECRET_KEY = ''

	client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

	client.setConnectionTimeoutInMillis(2000)
	client.setSocketTimeoutInMillis(60000)

	path = 'C:\\school\\test.pcm'
	song = AudioSegment.from_file(path)
	mss = len(song)
	start = 0
	while start < mss:
		print(str(start/1000)[:-2]+': ', end='')
		end = start + 30000
		if end > mss:
			end = mss
		buff = song[start:end].raw_data
		start = end
		dic = client.asr(buff, 'pcm', 16000, {
		    'dev_pid': 1536,
		})
		try :
			print(dic['result'])
		except:
			print(dic['err_msg'])