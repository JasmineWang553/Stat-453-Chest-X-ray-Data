import pandas as pd
import os
import numpy as np
import shutil


path_to_radio = '..\\COVID-19_Radiography_Dataset'
path_to_coronahack = '..\\Coronahack-Chest-XRay-Dataset\Coronahack-Chest-XRay-Dataset'
df = pd.read_csv('..\\Chest_xray_Corona_Metadata.csv', index_col=0)

normal = [df.iloc[i, 0] for i in range(len(df)) if df.iloc[i, 1] == 'Normal']
covid = [df.iloc[i, 0] for i in range(len(df)) if df.iloc[i, 3] == 'COVID-19']
pnemonia_virus = [df.iloc[i, 0] for i in range(len(
    df)) if df.iloc[i, 4] == 'Virus' and df.iloc[i, 3] != 'COVID-19' and df.iloc[i, 1] == 'Pnemonia']
pnemonia_bac = [df.iloc[i, 0] for i in range(
    len(df)) if df.iloc[i, 4] == 'bacteria' and df.iloc[i, 1] == 'Pnemonia']

# make new folder
os.makedirs('.\\Combined_data')

target_path = '.\\Combined_data'

folders = ['Normal', 'COVID', 'Viral Pneumonia', 'Lung_Opacity']
arrays = [normal, covid, pnemonia_virus, pnemonia_bac]

# combine test train in coronahack
os.makedirs(os.path.join(path_to_coronahack, 'all_data'))
source1 = os.path.join(path_to_coronahack, 'test')
source2 = os.path.join(path_to_coronahack, 'train')

filnames1 = os.listdir(source1)
filnames2 = os.listdir(source2)

for f in filnames1:
    shutil.move(os.path.join(source1, f), os.path.join(
        path_to_coronahack, 'all_data'))

for f in filnames2:
    shutil.move(os.path.join(source2, f), os.path.join(
        path_to_coronahack, 'all_data'))


# move files from radio to hello123

def move_files(foldername, source, target):
    os.makedirs(os.path.join(target, foldername))  # make a new dir

    for file_name in os.listdir(os.path.join(source, foldername)):

        shutil.move(os.path.join(os.path.join(source, foldername),
                                 file_name), os.path.join(target, foldername))


for f in folders:
    move_files(f, path_to_radio, target_path)


# move each pic from corona hack (all_data) to join corresponding folder in Combined_data

def move_files2(arr, folder):

    for file_name in arr:

        shutil.move(os.path.join(os.path.join(path_to_coronahack, 'all_data'),
                                 file_name), os.path.join(target_path, folder))


for arr, fold in zip(arrays, folders):
    move_files2(arr, fold)
