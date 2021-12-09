#!/bin/sh

#This script runs python for model creation and then renders rgb image
#RUN: sh pipeline.sh <prefix> <suffix>

prefix=$1

name=$2

img_count=$3

#camera=$3
camera="camera_a"

mkdir "${prefix}_images"
mkdir "${prefix}_models"

model_with_path="${prefix}_models/${name}.xml" 
for i in `seq 1 $img_count`
do
  python3 create_xml.py camera_a $model_with_path
  python3 save_rgb.py $model_with_path $camera "${prefix}_images/${name}_${i}.png"
  echo ${i}
done
