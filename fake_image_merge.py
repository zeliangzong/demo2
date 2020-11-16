import os
import cv2
import numpy as np
for i in range(10,24):
    num=str(i)
    exp_mask='exp_mask/{}/'.format(num)
    exp_calib='exp_calib/{}/'.format(num)
    exp_fake='exp_fake/{}/'.format(num)
    files=os.listdir(exp_mask)
    if not os.path.exists(exp_fake):
        os.makedirs(exp_fake)
    lenL=len(files)
    for i in range(2,lenL-2):
        mask=cv2.cvtColor(cv2.imread(exp_mask+files[i]),cv2.COLOR_RGB2GRAY)
        calib= cv2.imread(exp_calib+files[i])
        img_gray = cv2.cvtColor(calib, cv2.COLOR_RGB2GRAY)
        median=img_gray/5
        for j in range(1,3):
            calib_1 = cv2.imread(exp_calib + files[i+j])
            tmp_gray_1 = cv2.cvtColor(calib_1, cv2.COLOR_RGB2GRAY)
            calib_2 = cv2.imread(exp_calib + files[i - j])
            tmp_gray_2 = cv2.cvtColor(calib_2, cv2.COLOR_RGB2GRAY)
            median+=(tmp_gray_1+tmp_gray_2)/5
        median=median.astype(np.uint8)
        merged = cv2.merge([mask, img_gray, median])
        cv2.imwrite(exp_fake+files[i],merged)
        cv2.imshow('fgmask',median)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    #cv2.destroyAllWindows()`