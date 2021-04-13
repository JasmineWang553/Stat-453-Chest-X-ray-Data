# Stat-453-Chest-X-ray-Data


## Structure
- jupyter notebooks (currently 2):
  1. Logistic Regression (1 model -- from scratch)
  2. AlexNet (2 models -- from scratch & import pretrained)

- helper functions (3): they are written by professor

- ```create_combinedata.py```:

1. use this to combine data from two datasets 
  - https://www.kaggle.com/praveengovi/coronahack-chest-xraydataset
  - https://www.kaggle.com/tawsifurrahman/covid19-radiography-database
3. download from 2 websites above and extract them
4. make sure folder is in this structure (NOT in compressed form)!!!
5. after running ```create_combinedata.py``` in terminal or other ways you will have ```Combined_data``` folder with 4 folders inside COVID, Lung_Opacity, Normal, Viral Pneumonia
6. (optional) you can delete COVID-19_Radiography_Dataset and Coronahack-Chest-XRay-Dataset (only images with no label are left in there)

```
finalProjectfolder
+-- create_combinedata.py
+-- COVID-19_Radiography_Dataset
|   +-- COVID
|   +-- Lung_Opacity
|   +-- Normal
|   +-- Viral Pneumonia
+-- Coronahack-Chest-XRay-Dataset
|   +-- test
|   +-- train
|   +-- Chest_xray_Corona_dataset_Summary
|   +-- Chest_xray_Corona_Metadata


```
