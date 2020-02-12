import os.path, time

#print("last modified: %s" % time.ctime(os.path.getmtime(file)))
#print("created: %s" % time.ctime(os.path.getctime(file)))

import os, time
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
print("last modified: %s" % time.ctime(mtime))
