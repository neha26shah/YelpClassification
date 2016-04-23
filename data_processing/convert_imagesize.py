import os,sys
import Image
import csv
fred_train = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_files/100x100all_data_red_train.csv","w")
fgreen_train = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_files/100x100all_data_blue_train.csv","w")
fblue_train = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_files/100x100all_data_green_train.csv","w")
fred_val = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/validation_files/100x100all_data_red_val.csv","w")
fgreen_val = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/validation_files/100x100all_data_blue_val.csv","w")
fblue_val = open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/validation_files/100x100all_data_green_val.csv","w")
wred_train  = csv.writer(fred_train)
wblue_train = csv.writer(fblue_train)
wgreen_train = csv.writer(fgreen_train)
wred_val  = csv.writer(fred_val)
wblue_val = csv.writer(fblue_val)
wgreen_val = csv.writer(fgreen_val)
training_ids = []
trainread = csv.reader(open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/codes/data_processing/processed_data/training_ids.csv" ,"r"))
for row in trainread:
	break
for row in trainread:
	training_ids.append(int(row[0]))
testing_ids = []
testread = csv.reader(open("/media/neha/WorkSpace/YelpPhotoDataSetChallenge/codes/data_processing/processed_data/testing_ids.csv" ,"r"))
for row in testread:
	break
for row in testread:
	testing_ids.append(int(row[0]))
print len(testing_ids)
print len(training_ids)
size = 100,100
sfolder = "/media/neha/WorkSpace/YelpPhotoDataSetChallenge/original_allPhotos/"
dfolder = "/media/neha/WorkSpace/YelpPhotoDataSetChallenge/100x100_allPhotos/"
for image_name in os.listdir(sfolder):
	image_no = int(image_name.split(".")[0])
	im=Image.open(sfolder+image_name)
	out = im.resize(size)
	image_data = list(out.getdata())
	out.save(dfolder+image_name,"JPEG")
	red_row = [image_no]
	green_row=[image_no]
	blue_row=  [image_no]
	for r,g,b in image_data:
		red_row.append(r)
		green_row.append(g)
		blue_row.append(b)
	if image_no in training_ids:
		wred_train.writerow(red_row)
		wblue_train.writerow(blue_row)
		wgreen_train.writerow(green_row)
	elif image_no in testing_ids:
		wred_val.writerow(red_row)
		wblue_val.writerow(blue_row)
		wgreen_val.writerow(green_row)
	else:
		print "Error couldn't find the image"
		sys.exit(1)
fred_train.close()
fblue_train.close()
fgreen_train.close()
fred_val.close()
fblue_val.close()
fgreen_val.close()
