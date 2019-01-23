## Problem Statement : Generate pictures in realtime
import pyaudio
import numpy as np
import wave
import random
import speech_recognition as sr
from threading import Thread


##function to recognize text from speech
def recognizeAudio(filename):
    try:
        r=sr.Recognizer()
        speech=sr.AudioFile(filename)
        with speech as source:
            speech_extracted=r.record(speech)
            print(r.recognize_google(speech_extracted))
    except Exception as e:
        print(str(e))


#set properties of audio
CHUNK = 2**11
RATE = 44100
CHANNELS = 2

#open stream
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16, channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK)

##Listen to Microphone
listening=False
while(True):
    frames=[]
    i=0
    peak=0
    while(True):
        data=np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        
        #check if silent
        if(peak<200): ##do some tuning here boi
            ##Cut words and save words from microphone
            if(listening):

                ##Save the audio to disk
                filename='test'+str(random.randint(0,10000))+'.wav'
                wavefile=wave.open(filename,'wb')
                wavefile.setnchannels(1)
                wavefile.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
                wavefile.setframerate(RATE)
                wavefile.writeframes(b''.join(frames))
                wavefile.close
                
                frames=[]
                listening=False
                print("SAVED")
                ##Start a new thread
                t=Thread(target=recognizeAudio, args=(filename,))
                t.start()

            #print("Not listening")
        else:
            listening=True
            #print("Listening")
            #data_audio=stream.read(CHUNK)
            frames.append(data)
            
##display words

stream.stop_stream()
stream.close()
p.terminate()

