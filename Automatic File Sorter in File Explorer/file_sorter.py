import os,shutil
path = r"C:/Users/Yasuru Dhanushka/Desktop/Python/Automatic File Sorter in File Explorer/images/"
#this r tells python to treat r as literal character
files=os.listdir(path)
print(files)

folder_names = ["Image_Files","Txt_Files","Excel_Files"] #list
for i in range(0,3):
    if not os.path.exists(path + folder_names[i]):
        print(path + folder_names[i])
        os.makedirs(path + folder_names[i])

    
