# -*- coding: utf-8 -*-
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
 
DIR = 'speech_commands_v0.01'
fns = ['/off/00b01445_nohash_0.wav',
       '/go/00b01445_nohash_0.wav',
       '/yes/00f0204f_nohash_0.wav']
SAMPLE_RATE = 16000
 
def read_wav_file(x):
    # Read wavfile using scipy wavfile.read
    _, wav = wavfile.read(x) 
    # Normalize
    wav = wav.astype(np.float32) / np.iinfo(np.int16).max
        
    return wav
 
fig = plt.figure(figsize=(14, 8))
for i, fn in enumerate(fns):
    wav = read_wav_file(DIR + fn)
 
    ax = fig.add_subplot(3,1,i+1)
    ax.set_title('Raw wave of ' + fn)
    ax.set_ylabel('Amplitude')
    ax.plot(np.linspace(0, SAMPLE_RATE/len(wav), SAMPLE_RATE), wav)
fig.tight_layout()
plt.show();
