# Writer Identification using Deep Learning Keras CNN Model


#### [Programming Language]
- Python 3.6.8

#### [Used Python Libarary]
- Keras, OpenCV

#### [Development Enviroment]
- Pycharm, Google Colaboratory, Jupyter notebook  



#### [Description]
> [code] Folder
  1.  Preprocessing Images 
  
    1_first_preprocessing(crop1).py : used to cropped the original images and resizing images
    2_second_preprocessing(crop2).py : used to second cropped(for clear images) and save images 
    3_third_preprocessing(contour).py : used to contour the cropped images(to clarify the image)
    4_preprocessing_division.py : data division and save another folder
    5_preprocessing_csv.py : image vectorization and create csv(excel) file

  2. Model
  
    6_model.py : keras cnn model 

  3. Data Augmentation
  
    data_augmentation.py : used to increasing data
    data_augmentation.csv.py : augmentation image vectorization and create csv(excel) file


> [data] Folder
  1. Handwritten Images csv files(No Data Augmentation)
  
    handwritten_test.csv : test dataset
    handwritten_train.csv : train dataset
    handwritten_valid.csv : validation dataset
    
  2. Data Augmentation csv files
  
    handwritten_test_aug_contour.csv : test dataset
    handwritten_train_aug_contour.csv : train dataset
    handwritten_valid_aug_contour.csv : validation dataset
  
  
------------------------------------------------------------------------------------------------------------------------------------- 

# 필적감정 CNN 모델 


#### [프로그래밍 언어]
- Python 3.6.8

#### [사용한 파이썬 라이브러리]
- Keras, OpenCV

#### [개발환경]
- Pycharm, Google Colaboratory, Jupyter notebook  



#### [설명]
> [code] 폴더
  1. 이미지 전처리 
  
    1_first_preprocessing(crop1).py : 원본 이미지 크기 변환, 이미지 자르기(crop)
    2_second_preprocessing(crop2).py : 잘린 이미지 명확히 하기 위해 두번째 crop
    3_third_preprocessing(contour).py : 이미지를 명확히 하기 위한 특성 추출
    4_preprocessing_division.py : 데이터 분할과 폴더를 나누어 저장
    5_preprocessing_csv.py : 이미지 벡터화, csv파일 만들기

  2. 모델
  
    6_model.py : 케라스 CNN 모델

  3. Data Augmentation(데이터 부풀리기)
  
    data_augmentation.py : 데이터의 수 늘리기(data augmentation)
    data_augmentation.csv.py : data augmentation 한 이미지들 벡터화, csv파일 만들기


> [data] 폴더
  1. 손글씨 이미지 csv 파일
  
    handwritten_test.csv : 테스트 데이터셋
    handwritten_train.csv : 훈련 데이터셋
    handwritten_valid.csv : 검증 데이터셋
    
  2. Data Augmentation 이미지 csv 파일
  
    handwritten_test_aug_contour.csv : 테스트 데이터셋
    handwritten_train_aug_contour.csv : 훈련 데이터셋
    handwritten_valid_aug_contour.csv : 검증 데이터셋

