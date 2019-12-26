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
