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

model_path="${prefix}_models" 
for i in `seq 1 $img_count`
do
  python3 create_xml.py camera_a "$model_path/${name}_${i}.xml"
  python3 save_rgb.py "$model_path/${name}_${i}.xml" $camera "${prefix}_images/${name}_${i}.png"
  echo ${i}
done
