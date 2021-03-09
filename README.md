# EEEGCG_FYP
Energy Expenditure Estimations through Gesture Controlled Gaming

Greetings People!!

This repo contains the data and code to train and test the MobileNet v2 object detection model for Stand and Duck postures.

Have a close look on these (be mindful to change the path in the code, if you want to alter the directory structure):

-research
<br>&nbsp;&nbsp;&nbsp;&nbsp;	-object_detection_tutorial [to detect stand and duck postures from the rezultz folder(or any folder specified in the pathlib {or from webcam using cv2 and creating a cv2 instace}) and visualize the output]
<br>&nbsp;&nbsp;&nbsp;&nbsp;	-object_detection.zip [zip file for easy upload to google drive]
<br>&nbsp;&nbsp;&nbsp;&nbsp;	-object_detection [the root dir holding all the code the model needs]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		-object_detection [the complete copy of the original research dir (leave it as it is)]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		-inference_graph [stores the saved model inference of the model we've trained on our custom set]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	        -colab_tutorials
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-twoActDet_gcolab  [run this ipynb file on Google Colab to train your model and get the infrence graph]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-twoActDet
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;			-data [stores the csv, record and label_map files]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;			-rezultz [place the images you'd like to test by running `twoActDet_gcolab`]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;			-twoActDet_images
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;			-training [stores the model config and label_map files]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;			-ssd_mobilenet_v2_320x320_coco17_tpu-8 [the model config file]
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;			-xmlc and tfrec1 files [to convert xml-csv-tfrec formats]
		
-Install-Tensorflow-Python3.7 [bash script for necessary install on Windows (do not try this for other OS)]
