#!/bin/sh

#This script runs python for model creation and then renders rgb image
#RUN: sh pipeline.sh <image_folder> <image_suffix>


prefix=$1

name=$2

#camera=$3
camera="camera_a"

mkdir "${prefix}_images"
mkdir "${prefix}_models"

model_with_path="${prefix}_models/${name}.xml" 

python3 create_xml.py camera_a $model_with_path 

python3 save_rgb.py $model_with_path $camera "${prefix}_images/${name}.png"
