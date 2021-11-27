#!/bin/sh

#This script runs python for model creation and then renders rgb image
#RUN: sh pipeline.sh <image_suffix>

img_num=$1

python3 create_xml.py camera_a 

python3 save_rgb.py box_camera.xml camera_a out_img${img_num}.png
