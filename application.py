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
CHANNELS = 2

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
        if(peak<400):
            if(listening):
                #saveFile
                listening=False
            print("Not listening")
        else:
            listening=True
            print("Listening")

            ##Save the audio to disk
            


##Cut words and save words from microphone



##Start a new thread and recognize the text



##display words