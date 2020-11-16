import numpy as np
import cv2
import os
import time
for i in range(8,24):
    fggb=cv2.createBackgroundSubtractorKNN()
    path= 'exp_calib/{}/'.format(str(i))
    mask= 'exp_mask/'+path.split('/')[1]+'/'
    if not os.path.exists(mask):
        os.mkdir(mask)
    #path='exp_stable/5/'
    files=os.listdir(path)
    for file in files:
        start=time.time()
        frame=cv2.imread(path+file)
        fgmask=fggb.apply(frame)
        cv2.imwrite(mask+file,fgmask)
        end=time.time()
        print(end-start)
        cv2.imshow('fgmask',fgmask)
        # cv2.imshow('frame',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cv2.destroyAllWindows()