# COVID-CTSCAN-Deep-Learning
For Transfer Learning code, open Covid-Densenet.ipynb<br/>
 For Gaussian Noise code, open Gaussian-Noise-code.ipynb<br/>
For results after adding Gaussian Noise to original images, refer to Gaussian Noise.ipynb<br/>
For offline data augmentation code, refer augcov.py. It contains rotation, zooming and horizontal flipping.<br/>
Thus, every image in Train set is converted into 4 new images by:<br/>
1) Rotation<br/>
2) Zooming<br/>
3) Horizontal flipping<br/>
4) Gaussian Noise<br/>
Train set before offline augmentation: COVID-191 images, NON-COVID-234 images<br/>
Train set after offline augmentation:  COVID-955 images, NON-COVID-1170 images<br/>
