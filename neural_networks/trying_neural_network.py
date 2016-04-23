'''Train a simple convnet on the MNIST dataset.
Run on GPU: THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python mnist_cnn.py
Get to 99.25% test accuracy after 12 epochs (there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
'''
# ami 5cc6e636

from __future__ import print_function
import numpy as np
import sys
np.random.seed(1337)  # for reproducibility

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import csv
import pickle
import time
from boto.s3.connection import S3Connection
from boto.s3.key import Key
conn = S3Connection(, )

bucket = conn.get_bucket('yelptrainingdata')
def convert_numeric(row):
	new_row = []
	for a in row:
		new_row.append(int(a))
	return new_row
	

#input size
input_size=(3,100,100)
# Number of classes in data
nb_classes= 9
# The number of rows and cols in first convolution layer
input_filter_row= 3
input_filter_col=3
#How to initialize weights
init_function = 'lecun_uniform'
#activation function
act_func= 'tanh'
#border mode
border_mode= 'valid'
# pool_size for first convolutional layer
fpoolsize=(2,2)
#batch size
batch_size = 20
num_iterations =20
total_samples =172440
#total_samples = 200


model = Sequential()
model.add(Convolution2D(3 , input_filter_row , input_filter_col , init = init_function , activation = act_func , input_shape = input_size , 				border_mode = border_mode))
model.add(MaxPooling2D(pool_size=fpoolsize, border_mode = border_mode ))
#model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(20,init=init_function,activation = act_func))
#model.add(Dropout(0.25))
model.add(Dense(nb_classes,init=init_function,activation = "tanh"))

model.compile(loss="mean_squared_error",optimizer='sgd')



	
for i in range(num_iterations):
	filerreader= open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_files/100x100all_data_red_train.csv","r")
	filegreader = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_files/100x100all_data_green_train.csv","r")
	filebreader = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_files/100x100all_data_blue_train.csv","r")
	filetreader = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_files/training_target.csv","r")
	rreader= csv.reader(filerreader)
	greader= csv.reader(filegreader)
	breader = csv.reader(filebreader)
	treader = csv.reader(filetreader)
	counter =0
	print(i)
	while counter < total_samples:
		list_batch_x=[]
		list_batch_y = []
		#print ("Next example")
		for i in range(0,batch_size):
			grow = convert_numeric(greader.next()[1:])
			rrow = convert_numeric(rreader.next()[1:])
			brow = convert_numeric(breader.next()[1:])
			trow= convert_numeric(treader.next()[2:])
			list_batch_y = list_batch_y + trow
			list_batch_x= list_batch_x + rrow+brow+grow
			counter = counter+batch_size
		list_batch_y = 	[-0.5 if x==0 else 0.5 for x in list_batch_y]
		batch_X = np.asarray(list_batch_x).reshape((batch_size,input_size[0],input_size[1],input_size[2]))
		batch_Y  = np.asarray(list_batch_y).reshape((batch_size,nb_classes))
		#print (model.predict_on_batch(batch_X))
		#print (model.train_on_batch(batch_X,batch_Y, accuracy=True))
		#print (model.evaluate(batch_X,batch_Y,batch_size=1))
		#print (model.predict_on_batch(batch_X))
		#print (batch_Y)
	dump_filename = "localdump_"+str(i)+"_" + str(time.time())+".pkl" 
	filedump = open(dump_filename,"w")
	pickle.dump(model,filedump)
	k = Key(bucket)
	k.key = dump_filename
	k.set_contents_from_filename(dump_filename)
	filedump.close()
	filerreader.close()
	filegreader.close()
	filebreader.close()
	filetreader.close()


