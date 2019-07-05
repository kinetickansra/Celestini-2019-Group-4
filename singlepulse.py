# Author - Bhrigu Kansra
# Language - Python 3

#Import modules and packages

import numpy as np                                  #numerical computation
import pandas as pd                                 #importing dataframes
import librosa as lr                                #feature extraction(read and manipulate audio files)
import soundfile as sf 								#reading soudn file
#from glob import glob                              #reading files 
#import librosa.display                             #idk why but this has to be imported explicitly
#import warnings                                    #to supress warnings
#warnings.simplefilter('ignore')

def loadFile(ioObj, sr=22050, mono=True, offset=0.0, duration=None,
	dtype=np.float32, res_type='kaiser_best'):
	
	try:
		sf_desc = sf.SoundFile(ioObj)
		sr_native = sf_desc.samplerate
		if offset:
			# Seek to the start of the target read
			sf_desc.seek(int(offset * sr_native))
		if duration is not None:
			frame_duration = int(duration * sr_native)
		else:
			frame_duration = -1

		# Load the target number of frames, and transpose to match librosa form
		y = sf_desc.read(frames=frame_duration, dtype=dtype, always_2d=False).T
	except RuntimeError as exc:	
		# If soundfile failed, fall back to the audioread loader
		y, sr_native = __audioread_load(path, offset, duration, dtype)

	if mono:
		y = lr.core.to_mono(y)

	if sr is not None:
		y = lr.core.resample(y, sr_native, sr, res_type=res_type)

	else:
		sr = sr_native

	return y, sr
	

def mfccExtract(ioObj):
	sr = 22050
	audio_data = loadFile(ioObj, sr=22050)[0]
	mfcc_feature_list = lr.feature.mfcc(y=audio_data,sr=sr, n_mfcc=13) # create mfcc features
	print(mfcc_feature_list)
	np.savetxt('/home/bhrigu/Desktop/Colab/lololo.txt' , mfcc_feature_list, delimiter ="\t")
	return mfcc_feature_list

with open('/home/bhrigu/Desktop/Colab/cry4.wav', "rb+") as file:
	mfccExtract(file)
