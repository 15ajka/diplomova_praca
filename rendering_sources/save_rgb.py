import sys
"""
Shows how to access internal functions from MuJoCo.
"""
from matplotlib import pyplot as plt
from mujoco_py import load_model_from_path, MjSim, functions
import numpy as np

model = load_model_from_path("box.xml")
sim = MjSim(model)

img = sim.render(width=500, height=500, camera_name=sys.argv[1])
print(img)
plt.imshow(img, interpolation='nearest')
plt.savefig('upper_view.png')
plt.show()

