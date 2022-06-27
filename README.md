# Exploring Machine Intelligence： The way of using StyleGan2 in music visualisation  
  

Msc Creative Computing  
Yuwei Chen  
21014257  


### Github：https://github.com/DebraChen/ML---Coding3  	

The code of ‘Lucid Sonic Dreams’ which was introduced by Terence inspired me a lot, I love the way that images interact with music, So I tried to run the original code using its sample datasets and music. Then changed some music that was made by my friends and myself, we all liked it, and decided to use it to make visuals for our experimental music, to prepare for further performing. So I decided to check out how could I change the dataset.   
I checked the GitHub, and found that the .pkl files are its input style datasets, I googled some code and tried it out, then I found two ways to turn the png dataset into .tfr, then to .pkl. I will describe the process of how it works, and also the bugs that I ran into. Thanks to Rebeca, Terence, Luis, and Pete for offering help, and encouraging me to face the challenge as a beginner.  
  
  
## References  
Lucid Sonic Dreams code:  
https://colab.research.google.com/drive/1Y5i50xSFIuN3V4Md8TB30_GOAtts7RQD?usp=sharing#scrollTo=YNnHbJgB2EWk  
  
Images collecting tutorial:  
Pindown is easy to use with a limited amount of imaged downloads in a free account:  
https://www.youtube.com/watch?v=BwMk1Ik7aCM&t=1s. 
Fatkun, Free to download some more images at once, suits insta, Pinterest, etc., the shortage is it will download extra icons and images, sort by size could help me delete some images that I don’t need.  
https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf  
    
Cut images into specific sizes, Code from Terence during the class    
https://github.com/dvschultz/dataset-tools    
  
   
Data preparing code choice 1 (images to TFRecords) — required windows laptop:    
Tutorial video: https://www.bilibili.com/video/BV1854y1B7cd?vd_source=c3241b1f3625c229f82c3d090e4df18f  
  
Data preparing code 2 (images to TFRecords) — in Colab:  
https://colab.research.google.com/github/dvschultz/ai/blob/master/StyleGAN2_Colab_Train.ipynb#scrollTo=lJazuNYurryY  
Resume training,  
https://www.reddit.com/r/StyleGan/comments/pry0ah/how_to_resume_training_pytroch_style_gan_2_ada/  
  
Data Training code:  
(Dataset trained from PyTorch does not work well in Lucid dreams, so we need StyleGan2-ADA)  
https://colab.research.google.com/github/ArthurFDLR/GANightSky/blob/main/GANightSky.ipynb  
  
## Process plans  
1. Collect and download datasets  
2. Cut dataset images in 512*512  
3. Turn images into weight (.pkl)  
4. Train the model in Lucid dreams  
  
## Process and notes  
### A. Preparing images  
It goes all good with tools, Pindown and Fatkun.  
One of my collect boards goes here, https://www.pinterest.co.uk/chenqupei/dataset01/  
  
    
### B. Crop dataset images  
B1, Cut in terminal (Code from Terence):  
yuweichen@Yuweis-MBP ~ % ls  
yuweichen@Yuweis-MBP ~ % cd dataset-tools  
yuweichen@Yuweis-MBP dataset-tools % ls  
yuweichen@Yuweis-MBP dataset-tools % pip3 install imutils  
yuweichen@Yuweis-MBP dataset-tools % python3 dataset-tools.py --width 512 --height 512 --input_folder ~/Desktop/0001 --output_folder ~/Desktop/0001_512  
Notes:   
Download dataset-tools from https://github.com/dvschultz/dataset-tools  
Need to pip install all of the libraries that it mentioned in the process  
Errors:  
Miss use pip and pip3  
Miss use of python and python3  
  
B2, Crop Multiple Images in Photoshop (crop each faces, product, and so on in different position in each picture).  
Tutorial:   
https://www.youtube.com/watch?v=AdTEeXYfENc  
https://www.16xx8.com/photoshop/jiaocheng/29410_all.html  
  
    
### C. Transfer the dataset images into TFRecords  
C1, use visual studio in windows or Terminal in Apple–Intel architecture(not M1):  
yuweichen@Yuweis-MacBook ~ % cd desktop  
yuweichen@Yuweis-MacBook desktop % cd dataset-tools  
yuweichen@Yuweis-MacBook dataset-tools %   
yuweichen@Yuweis-MacBook dataset-tools % python3 dataset_tools.py create_from_images ./images ./dataset01output1024  
Notes:   
Download dataset-tools from https://github.com/NVlabs/stylegan2  
Need to pip install all of the libraries that it mentioned in the process  
Errors:  
I tried M1, apple-intel chip and windows, it was only M1 that could not make it yet.  
  
C2, turn images toTFRecord in Colab:  
My work, https://colab.research.google.com/drive/1VGcLuHQ-Yjsth5BAYOS2KxSu-M-YMz7N?usp=sharing  
Notes:  
Use those two lines to cal google drive in Colab  
from google.colab import drive  
drive.mount(‘/content/drive’)  
Errors:   
One of the students used PyTorch to train the data, but it doesn’t work well, so I decided to stick to trying styleGan2 and styleGan2-ada.  
I could use the TFRecords from the process, but the .pkl files trained from the code could not be used, it was not been fully trained. We could tell from the size of the weights that I trained using this code, it was just 2kb for each .pkl. The weight was not trained well, but I did not realise at that time, that it made me lost in the process for a week, to ‘debug’ the code and download the ‘missing’ library to let the broken file run in the code.  
  
### D. Training the .pkl  
My work, https://colab.research.google.com/drive/1CCXqgTq1MeHifXdzDjGrxcQC5KKCKtdL?usp=sharing  
Notes:   
Firstly, delete the local path cells, and add ‘!pip install -U numpy==1.18.5’ to make sure we have the right version according to the error.  
Then, upload the images dataset into Google drive, and change the path of the last cell from ‘Convert dataset to .tfrecords’.  
Train the code, then save .tfr from the preset file.  
Tips:  
If the training shutdown in the process,   
after   
--metrics={metric_list}   
in the same line, add  
 two space   
and  
--resume /content/drive/MyDrive/StyleGAN2-ADA/training/yw/00002-outputgan-mirror-auto1-bgc-resumecustom/network-snapshot-000016.pkl #—dry-run  
remember to change the newest path of .pkl.  
(https://www.reddit.com/r/StyleGan/comments/pry0ah/how_to_resume_training_pytroch_style_gan_2_ada/)  
  
### E. Training the model  
My work, https://colab.research.google.com/drive/1omSj-oHqZf37M3mpGCjg-SLjatrjpGqa?usp=sharing  
Notes:  
I failed so many times, because of battery low, restart or reconnecting the runtime, and wrong datasets, I found example 2 could use .pkl as input, so I don’t need to overwrite the code, (which I did in examples 1 and ran into bugs). Also, uploading the files and music into google drive and using the code that I mentioned previously could help to call the drive file in the Colab code  
from google. colab import drive  
drive.mount(‘/content/drive’)  
Which saves a bit of time after restarting the collab.  
There were so many errors, caused by a broken dataset.   
  
  
## Summary  
There are still some more ways that I could prepare a dataset to use in the code, I was just focused on one way at this time, my output is still a bit raw, need some more time to train it to learn some more details.  
  
I felt white background and grey pics took less time to train the weight compared to the colourful, full pixels, or full of details images.  
  
The output visual is good to use for a music video but to make it more interactive with real-time control or music, I still need to work more on it. Before that, I will training more datasets to cooperate with other musicians and preparing for the up coming shows. Hopefully, I could make more exciting projects. I felt it is not easy to train machine learning, but once it works, I feel so proud of it. Thanks CCI, Thanks to Rebeca and Terence.  
  
Github：https://github.com/DebraChen/ML---Coding3  
