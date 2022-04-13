import os, time, sys

from reverseGeoCodeing.settings import BASE_DIR

def deleteOutdatedFiles():

    
    path =  os.path.join(BASE_DIR, 'static')
    now = time.time()

    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < now - 1 * 3600:
            if os.path.isfile(f):
                os.remove(os.path.join(path, f))
   