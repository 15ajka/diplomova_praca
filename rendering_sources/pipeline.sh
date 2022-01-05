#!/bin/sh

#This script runs python for model creation and then renders rgb image
#RUN: sh pipeline.sh <folder> <model_name> <img_count>

prefix=$1

name=$2

img_count=$3

#camera=$3
camera1="camera1"
camera2="camera2"

mkdir "${prefix}_images"
mkdir "${prefix}_models"

mkdir "${prefix}_images/c1"
mkdir "${prefix}_images/c2"

model_path="${prefix}_models" 
for i in `seq 1 $img_count`
do
  python3 create_xml.py  "$model_path/${name}_${i}" $i 
  python3 save_rgb.py "$model_path/${name}_${i}_c1.xml" $camera1 "${prefix}_images/c1/${name}_${i}_c1.png"
  python3 save_rgb.py "$model_path/${name}_${i}_c2.xml" $camera2 "${prefix}_images/c2/${name}_${i}_c2.png"
  echo ${i}
done
