import os
import sys
import csv

r_t_file = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train.csv","r")
r_t = {}
reader = csv.reader(r_t_file)
for row in reader:
	break
for row in reader:
	businessid = int(row[0])
	targets_strings = row[1].split(" ")
	target_vector=[]
	count=0
	for i in range(0,9):
		if str(i) in targets_strings:
			target_vector.append(1)
			count= count +1
		else:
			target_vector.append(0)	
	r_t[businessid] = target_vector
	if count != len(targets_strings):
		print targets_strings, target_vector
#print r_t 
r_t_file.close()
#create a dictionary of restaurant to target vector mapping.
# create a mapping of photo to restaurant mapping
p_r={}
p_r_file = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_photo_to_biz_ids.csv","r")
reader = csv.reader(p_r_file)
for row in reader:
	break
for row in reader:
	p_r[int(row[0])] = int(row[1])
p_r_file.close()

training_target = csv.writer(open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/validation_files/validation_target.csv","w"))
order_file = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/codes/data_processing/processed_data/testing_ids.csv","r")
reader = csv.reader(order_file)
for row in reader:
	photo_id = int(row[0])
	business_id = p_r[photo_id]
	target = r_t[business_id]
	training_target.writerow([photo_id,business_id]+target)
# for each training photo id get the restaurant mapping and the corresponding target vector.
