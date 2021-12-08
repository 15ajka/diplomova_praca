import sys
#This script creates scene model with camera, parameters from arguments will be added later on
#RUN: python3 create_xml.py <camera_name>

xml_prefix = """\
<mujoco>
   <asset>
      <texture file="../textures/checkerboard.png" type="cube" name="checker" />
      <texture file="../textures/sphere.png" type="2d" name="checker-sph" />
      
      <texture name="builtin_checker" builtin="checker" type="2d" rgb1="1 1 0" rgb2="0 0 1" width="200" height="200"/>
      <texture name="builtin_gradient" builtin="gradient" rgb1="0 .9 .3" rgb2="1 1 1" width="200" height="200"/>
      <texture name="builtin_flat" builtin="flat" rgb1="1 0 0" rgb2="1 0 0"  width="200" height="200"/>

      <material name="checker_mat" reflectance="0.9" texrepeat="3 3" texture="builtin_checker" texuniform="false" />
      <material name="gradient_mat" reflectance="1" texrepeat="1 1" texture="builtin_gradient" texuniform="true"/>
      <material name="flat_mat" reflectance="1" texrepeat="1 1" texture="builtin_flat" texuniform="true"/>
   </asset>

   <worldbody>
      <light diffuse=".9 .9 .9" pos="0 0 3" dir="0 0 -1"/>
     <geom type="plane" size="1 1 1" rgba="0.3 0.3 0.3 1"/>
     <body pos="0.5 0 0.1">
         <joint type="free"/>
         <geom type="box" size=".1 .1 .1" material="checker_mat" rgba="1 0 0 1"/>
      </body>
      <body pos="0.5 0.5 0.1">
         <joint type="free"/>
         <geom type="box" size=".1 .2 .1" material="gradient_mat"/>
      </body>
      <body pos="-0.2 0.3 0.1">
         <joint type="free"/>
         <geom type="cylinder" size=".1 .2 .1" material="checker_mat" rgba="0 1 1 1" />
      </body>
    <body pos="-0.2 0.5 0.1">
         <joint type="free"/>
         <geom type="sphere" size="0.1 0.1 .1" material="checker_mat" />
      </body>
"""


xml_suffix = """\
   </worldbody>
</mujoco>\
"""

camera_name = sys.argv[1]
camera_line = f"""\
        <camera axisangle="1 0 0 1" fovy="60" name="{camera_name}" pos="0.3 0.3 2"></camera>
"""

xml_string = xml_prefix + camera_line + xml_suffix

print(xml_string)
xml_file = open(sys.argv[2], "w+")
xml_file.write(xml_string)
