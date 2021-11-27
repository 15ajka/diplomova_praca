#This script renders image from xml model into png
# To run this script mujoco and mujoco-py must be installed
# Run: python3 save_rgb.py <model_with_path> <name_of_used_camera> <output_image_with_path> 
import sys
from matplotlib import pyplot as plt
from mujoco_py import load_model_from_path, MjSim, functions
import numpy as np

model_path = sys.argv[1]
camera_name = sys.argv[2]
out_img_path = sys.argv[3]

model = load_model_from_path(model_path)
sim = MjSim(model)

img = sim.render(width=500, height=500, camera_name=camera_name)
print(img)
plt.imshow(img, interpolation='nearest')
plt.savefig('out_images/' + out_img_path)
plt.show()

