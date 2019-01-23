## Problem Statement : Generate pictures in realtime


import pyaudio
import numpy as np
import wave
import random
import speech_recognition as sr
from threading import Thread

##Listen to Microphone

#set properties of audio
CHUNK = 2**11
RATE = 44100
CHANNELS = 1

#open stream
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16, channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK)

#listen to stream
listening=False
while(True):
    frames=[]
    i=0
    while(True):
        data=np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        
        #check if silent
        if(peak<400): ##do some tuning here boi
            if(listening):

                ##Save the audio to disk
                filename='test'+str(random.randint(0,10000))+'.wav'
                wavefile=wave.open(filename,'wb')
                wavefile.setnchannels(CHANNELS)
                wavefile.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
                wavefile.setframerate(RATE)
                wavefile.writeframes(b''.join(frames))
                wavefile.close
                frames=[]
                listening=False
                print("SAVED")

            print("Not listening")
        else:
            listening=True
            print("Listening")
            data_audio=stream.read(CHUNK)
            frames.append(data_audio)
            

            
            


##Cut words and save words from microphone



##Start a new thread and recognize the text



##display words