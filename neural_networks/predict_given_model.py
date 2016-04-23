
from __future__ import print_function
import numpy as np
import sys

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import csv
import pickle
import time

input_size=(3,100,100)

def convert_numeric(row):
	new_row = []
	for a in row:
		new_row.append(int(a))
	return new_row

def givenfilenameLoadModel(filename):
    model = pickle.load(open(filename,"r"))
    return model

def evaluate(filename):
    path = "/media/neha/WorkSpace/YelpPhotoDataSetChallenge/validation_files/"
    model = givenfilenameLoadModel(filename)

    filerreader= open(path +"100x100all_data_red_val.csv","r")
    filegreader = open(path + "100x100all_data_green_val.csv","r")
    filebreader = open(path + "100x100all_data_blue_val.csv","r")
    filetreader = open(path + "validation_target.csv","r")
    rreader= csv.reader(filerreader)
    greader= csv.reader(filegreader)
    breader = csv.reader(filebreader)
    treader = csv.reader(filetreader)
    counter =0
    while counter<5:
        batch_X = []
        grow = convert_numeric(greader.next()[1:])
        rrow = convert_numeric(rreader.next()[1:])
        brow = convert_numeric(breader.next()[1:])
        trow= convert_numeric(treader.next()[2:])
        print (trow)
        batch_X = rrow + brow+ grow
        batch_x = np.asarray(batch_X).reshape((1,input_size[0],input_size[1],input_size[2]))
        counter = counter+1
        print (batch_x.shape)
        predictions = model.predict(batch_x,verbose=1)
        print (predictions)
    filerreader.close()
    filegreader.close()
    filebreader.close()
    filetreader.close()

evaluate("localdump_19_1460222050.91.pkl")