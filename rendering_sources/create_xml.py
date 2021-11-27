import sys
#This script creates scene model with camera, parameters from arguments will be added later on
#RUN: python3 create_xml.py <camera_name>

xml_prefix = """\
<mujoco>
   <worldbody>
      <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
      <geom type="plane" size="1 1 0.1" rgba=".9 1 0 1"/>
     <body pos="0.5 0 0.1">
         <joint type="free"/>
         <geom type="box" size=".1 .1 .1" rgba="0 .9 1 1"/>
      </body>
      <body pos="0 0 0.1">
         <joint type="free"/>
         <geom type="box" size=".1 .1 .1" rgba="0 .1 0.1 1"/>
      </body>
"""


xml_suffix = """\
   </worldbody>
</mujoco>\
"""

camera_name = sys.argv[1]
camera_line = f"""\
        <camera axisangle="0 1 0 180" fovy="45" name="{camera_name}" pos="0 0 2"></camera>
"""

xml_string = xml_prefix + camera_line + xml_suffix

print(xml_string)
xml_file = open("box_camera.xml", "w+")
xml_file.write(xml_string)
