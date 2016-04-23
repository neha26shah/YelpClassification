# This code is to get the image size of all the images in the train folder.
from PIL import Image
import os
import csv

csv_filename = "processed_data/image_dimensions.csv"
fp = open(csv_filename,"w")
writer = csv.writer(fp)
folder=  "/media/neha/WorkSpace/YelpPhotoDataSetChallenge/train_photos/"
writer.writerow(["ImageName","Width","Height"])
for image_name in os.listdir(folder):
	im=Image.open(folder+image_name)
	name_print = image_name.split(".")
	width,height = im.size
	writer.writerow([name_print[0],width,height])
