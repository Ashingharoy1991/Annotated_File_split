import os
import shutil
import random

# Specify the directory path
directory_path = 'E:/DH_data/data_dh/Data/obj_train_data'

# List all files in the directory
all_files = os.listdir(directory_path)

# Filter files to get only .txt files
txt_files = [file for file in all_files if file.endswith('.txt')]

# Filter files to get only .jpg files
PNG_files = [file for file in all_files if file.endswith('.PNG')]

# Shuffle the list of .txt files
random.shuffle(txt_files)

# Calculate the number of files for each set
total_files = len(txt_files)
train_size = int(0.6 * total_files)
val_size = int(0.2 * total_files)


# Divide the .txt files into training, validation, and test sets
train_files = txt_files[:train_size]
val_files = txt_files[train_size:train_size + val_size]
test_files = txt_files[train_size + val_size:]


os.mkdir(os.path.join("E:/DH_data/data_dh/Data","train"))
os.mkdir(os.path.join("E:/DH_data/data_dh/Data","val"))
os.mkdir(os.path.join("E:/DH_data/data_dh/Data","test"))

#creating folders in side train folder
if os.path.exists(os.path.join("E:/DH_data/data_dh/Data","train")):
     os.mkdir(os.path.join("E:/DH_data/data_dh/Data","train","images"))
     os.mkdir(os.path.join("E:/DH_data/data_dh/Data","train","labels"))

#creating folders in side val folder
if os.path.exists(os.path.join("E:/DH_data/data_dh/Data","val")):
    os.mkdir(os.path.join("E:/DH_data/data_dh/Data","val","images"))
    os.mkdir(os.path.join("E:/DH_data/data_dh/Data","val","labels"))

#creating folders in side test folder
if os.path.exists(os.path.join("E:/DH_data/data_dh/Data","test")):
    os.mkdir(os.path.join("E:/DH_data/data_dh/Data","test","images"))
    os.mkdir(os.path.join("E:/DH_data/data_dh/Data","test","labels"))

# Print the list of selected .txt files (first 60%)
for i in train_files:
    file_name = os.path.splitext(i)[0]
    for file in PNG_files:
        PNG_file_name = file.split('.PNG')[0]

        if file_name == PNG_file_name:

            src_img_path=os.path.join("E:/DH_data/data_dh/Data/obj_train_data",file_name + ".PNG")
            des_img_path=os.path.join("E:/DH_data/data_dh/Data","train","images")

            src_txt_path=os.path.join("E:/DH_data/data_dh/Data/obj_train_data",file_name + ".txt")
            des_txt_path=os.path.join("E:/DH_data/data_dh/Data","train","labels")

            shutil.copy(src=src_img_path,dst=des_img_path)
            shutil.copy(src=src_txt_path,dst=des_txt_path)

            print(file_name,"copied successfully!!!")


for j in val_files:
    file_name_val = os.path.splitext(j)[0]
    for file in PNG_files:
        PNG_file_name = file.split('.PNG')[0]

        if file_name_val == PNG_file_name:

            src_img_path=os.path.join("E:/DH_data/data_dh/Data/obj_train_data",file_name_val + ".PNG")
            des_img_path=os.path.join("E:/DH_data/data_dh/Data","val","images")

            src_txt_path=os.path.join("E:/DH_data/data_dh/Data/obj_train_data",file_name_val + ".txt")
            des_txt_path=os.path.join("E:/DH_data/data_dh/Data","val","labels")

            shutil.copy(src=src_img_path,dst=des_img_path)
            shutil.copy(src=src_txt_path,dst=des_txt_path)

            print(file_name_val,"copied successfully!!!")

for k in test_files:
    file_name_test = os.path.splitext(k)[0]
    for file in PNG_files:
        PNG_file_name = file.split('.PNG')[0]

        if file_name_test == PNG_file_name:

            src_img_path=os.path.join("E:/DH_data/data_dh/Data/obj_train_data",file_name_test + ".PNG")
            des_img_path=os.path.join("E:/DH_data/data_dh/Data","test","images")

            src_txt_path=os.path.join("E:/DH_data/data_dh/Data/obj_train_data",file_name_test + ".txt")
            des_txt_path=os.path.join("E:/DH_data/data_dh/Data","test","labels")

            shutil.copy(src=src_img_path,dst=des_img_path)
            shutil.copy(src=src_txt_path,dst=des_txt_path)

            print(file_name_test,"copied successfully!!!")