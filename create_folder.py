#! usr/bin/python

import datetime
import time
import os
import shutil

today=time.strftime('%Y%m%d')
SECONDS_IN_DAY = 24 * 60 * 60
src = "/home/pi/ftp/"

try:
   dst = os.system("mkdir /home/pi/fotos/"+str(today))
except OSError:
   Print('Folder already exist')

# dst = os.system("mkdir /home/pi/fotos/"+str(today))



now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join("src","fname")
    try:
       if last_mod_time(src_fname) > before:
         dst_fname = os.path.join(dst,fname)
         shutil.move(src_fname,dst_fname)
    except OSError:
        print('ERROR')