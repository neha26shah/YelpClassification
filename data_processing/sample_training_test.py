import csv
filename = "/media/neha/WorkSpace/YelpPhotoDataSetChallenge/codes/data_processing/processed_data/unique_business_ids.csv"
fp = open(filename,"r")
reader =csv.reader(fp)
values = []
import random
for row in reader:
	break
for row in reader:
	values.append(int(row[0]))
random.shuffle(values)
pe80 = int(len(values) * 0.75)
training_data = values[:pe80]
test_data = values[pe80:]
print len(values), len(training_data),len(test_data)
fp.close()
phto_file = "/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_photo_to_biz_ids.csv"
fphoto = open(phto_file,"r")
reader = csv.reader(fphoto)
file1= "processed_data/training_ids.csv"
file2="processed_data/testing_ids.csv"
ftrain = open(file1,"w")
ftest = open(file2,"w")
ctrain = csv.writer(ftrain)
ctest = csv.writer(ftest)
ctrain.writerow(["photo_id","business_id"])
ctest.writerow(["photo_id","business_id"])
for row in reader:
	break
for row in reader:
	business_id = int(row[1])
	photo_id = int(row[0])
	if business_id in training_data:
		ctrain.writerow([photo_id,business_id])	
	else:
		ctest.writerow([photo_id,business_id])	
ftrain.close()
ftest.close()
fphoto.close()
