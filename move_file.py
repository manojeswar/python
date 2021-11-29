# Python code to search files in current
# folder (We can change file type/name and path
# according to the requirements.
import shutil, os
  
# This is to get the directory that the program 
# is currently running in.
moveto = "/home/manoj/Downloads/HDD_manoj/moved/"
dir_path = os.path.dirname(os.path.realpath(__file__))
  
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('sss.txt'):
			dst=moveto+file
			shutil.move(file,dst)
#            print (root+'/'+str(file))
