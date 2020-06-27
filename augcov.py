import Augmentor
import os
import warnings
warnings.filterwarnings('ignore')
import keras
import glob

for img in glob.glob("C:\\Users\\joshi\\OneDrive\\Desktop\\NIT Surat\\COVID-CT-master\\Data\\Train\\NON-COVID"):
    p = Augmentor.Pipeline(img)
    p.rotate(probability=1, max_left_rotation=10, max_right_rotation=10)
    p.process()
    p.zoom(probability=1, min_factor=1.1, max_factor=1.5)
    p.process()
    p.flip_left_right(probability=1)
    p.process()