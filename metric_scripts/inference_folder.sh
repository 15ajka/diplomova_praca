#!/bin/sh

out_dir=$1

for dir in $1/*/ ; do
	echo "Inference for directory: $dir"
	output=$(echo $dir | rev | cut -d '/' -f 2,3 | rev) 
	python3 inference.py --data $dir --outf ./inference_outputs/$output

done

