
import os
import fnmatch

dirpath='/home/pi/ftp/'
print len(fnmatch.filter(os.listdir(dirpath), '*.jpg'))

#list = os.listdir(/home/pi/ftp) # dir is your directory path
#number_files = len(list)
#print number_files
