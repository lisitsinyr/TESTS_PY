
#----------------------------------------------------------------------------
#with os.scandir(path) as it:
#    for entry in it:
#        if not entry.name.startswith('.') and entry.is_file():
#            print(entry.name)
#----------------------------------------------------------------------------

#>>>
#import os
#statinfo = os.stat('somefile.txt')
#statinfo
#os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
#st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
#st_mtime=1297230027, st_ctime=1297230027)
#statinfo.st_size
#264
#----------------------------------------------------------------------------

#import os
#from os.path import join, getsize
#for root, dirs, files in os.walk('python/Lib/email'):
#    print(root, "consumes", end=" ")
#    print(sum(getsize(join(root, name)) for name in files), end=" ")
#    print("bytes in", len(files), "non-directory files")
#    if 'CVS' in dirs:
#        dirs.remove('CVS')  # don't visit CVS directories
#In the next example (simple implementation of shutil.rmtree()), walking the tree bottom-up is essential, rmdir() doesn't allow deleting a directory before the directory is empty:
#----------------------------------------------------------------------------

# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
#import os
#for root, dirs, files in os.walk(top, topdown=False):
#    for name in files:
#        os.remove(os.path.join(root, name))
#    for name in dirs:
#        os.rmdir(os.path.join(root, name))
#Raises an auditing event os.walk with arguments top, topdown, onerror, followlinks.
#----------------------------------------------------------------------------
