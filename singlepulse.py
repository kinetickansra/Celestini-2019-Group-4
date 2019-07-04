# Author - Bhrigu Kansra
# Language - Python 3

#Import modules and packages

import numpy as np                                  #numerical computation
import pandas as pd                                 #importing dataframes
import librosa as lr                                #feature extraction(read and manipulate audio files)
#from glob import glob                               #reading files 
#import librosa.display                              #idk why but this has to be imported explicitly
#import warnings                                     #to supress warnings
#warnings.simplefilter('ignore')

def mfccExtract(in_path):
	src = in_path
	sr = 22050
	audio_data = lr.load(in_path, sr=22050)[0]
	mfcc_feature_list = lr.feature.mfcc(y=audio_data,sr=sr) # create mfcc features
	print(mfcc_feature_list)
	return mfcc_feature_list

mfccExtract('/home/bhrigu/Desktop/Colab/cry4.wav')
