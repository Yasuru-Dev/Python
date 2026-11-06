import os,shutil
path = r"C:/Users/Yasuru Dhanushka/Desktop/Python/Automatic File Sorter in File Explorer/images/"
#this r tells python to treat r as literal character
files=os.listdir(path)
print(files)

folder_names = ["Image_Files","Txt_Files","Excel_Files,Power_point_Files"] #list
for i in range(0,4):
    if not os.path.exists(path + folder_names[i]):
        print(path + folder_names[i])
        os.makedirs(path + folder_names[i])

for file in files:
    if ".jpg" in file and not os.path.exists(path + "Image_Files/" + file):
        shutil.move(path + file, path + "Image_Files/" + file)
    elif ".txt" in file and not os.path.exists(path + "Txt_Files/" + file):
        shutil.move(path + file, path + "Txt_Files/" + file)
    elif ".xlsx" in file and not os.path.exists(path + "Excel_Files/" + file):
        shutil.move(path + file, path + "Excel_Files/" + file)
    elif ".pptx" in file and not os.path.exists(path + "Excel_Files/" + file):
        shutil.move(path + file, path + "Power_point_Files/" + file)
        
    

    
