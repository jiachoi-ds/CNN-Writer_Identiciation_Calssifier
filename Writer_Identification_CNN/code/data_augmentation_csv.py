# (추가) data augmentation image로 csv 파일 만들기

import hashlib
from PIL import Image
import numpy as np
import pandas as pd
import csv
import os


def average_hash(fname, size=64):
    img = Image.open(fname) # 이미지 데이터 열기
    img = img.convert('L')  # 그레이 스케일
    img = img.resize((size,size), Image.ANTIALIAS) # resize
    pixel_data = img.getdata()  # 픽셀데이터
    pixels = np.array(pixel_data)   # 1차원 픽셀데이터
    avg = pixels.mean() # 픽셀의 평균
    diff = 1 * (pixels > avg) # 픽셀 평균보다 크면 1, 작으면 0
    return diff

columns=[]

for i in range(4096):
    columns.append('pixel'+str(i))
columns.append('label')


df1 = pd.DataFrame(index=np.arange(9120), columns=columns)
count=0
for person in range(1,11):
    for num in range(0,912):
        path1 = "contourfinal/train/%d" %(person)
        file_list1 = os.listdir(path1)
        numpy_ahash = average_hash("contourfinal/train/%d/%s" %(person, file_list1[num]))
        list_ahash = numpy_ahash.tolist()
        labeled_ahash = np.array(list_ahash + [person])
        df1.loc[count] = labeled_ahash
        count+=1
        print('ok train' + str(num))
        df1.to_csv("handwritten_train_aug_contour.csv", index_label="index")


df2 = pd.DataFrame(index=np.arange(3120), columns=columns)
count=0
for person in range(1,11):
    for num in range(0,312):
        path2 = "data_augmentation/valid/%d" %(person)
        file_list2 = os.listdir(path2)
        numpy_ahash = average_hash("data_augmentation/valid/%d/%s" %(person,file_list2[num]))
        list_ahash = numpy_ahash.tolist()
        labeled_ahash = np.array(list_ahash + [person])
        df2.loc[count] = labeled_ahash
        count+=1
        print('ok valid'+ str(num))
        df2.to_csv("handwritten_valid_aug.csv", index_label="index")

df3 = pd.DataFrame(index=np.arange(2880), columns=columns)
count=0
for person in range(1,11):
    for num in range(0,288):
        path3 = "data_augmentation/test/%d" %(person)
        file_list3 = os.listdir(path3)
        numpy_ahash = average_hash("data_augmentation/test/%d/%s" %(person, file_list3[num]))
        list_ahash = numpy_ahash.tolist()
        labeled_ahash = np.array(list_ahash + [person])
        df3.loc[count] = labeled_ahash
        count+=1
        print('ok test'+str(num))
        df3.to_csv("handwritten_test_aug.csv", index_label="index")