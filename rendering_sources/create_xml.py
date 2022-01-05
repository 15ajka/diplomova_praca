#This script creates scene model with camera, parameters from arguments will be added later on
#RUN: python3 create_xml.py <model_path_without_suffix>

import sys
import random as r
from shapely.geometry.point import Point
from shapely.geometry import Polygon
from shapely import affinity
import matplotlib.pyplot as plt

def random_rgb():
    return round(r.uniform(0,1),1), round(r.uniform(0,1),1), round(r.uniform(0,1),1)
    
def get_polygon(obj, s_x, s_y, s_z, x, y, z, x_rot):
    if obj in ["sphere", "cylinder"]:
        return Point(x, y).buffer(s_x)
    basic = Polygon([(x-s_x, y+s_y), (x+s_x, y+s_y), (x+s_x,y-s_y), (x-s_x, y-s_y)])
    return affinity.rotate(basic, x_rot, 'center')

min_obj_size = 0.1
max_obj_size = 0.2

objects = ["cube", "box", "sphere", "cylinder"]
builtin = ["checker", "gradient", "flat"]
materials = ["checker_mat", "gradient_mat", "flat_mat"]
obj_count = r.randint(4,7)

tex_strings = []
rgb_bg, rgb_bg2 = random_rgb(), random_rgb()
tex_strings.append(f"<texture type=\"skybox\" builtin=\"gradient\" rgb1=\"{rgb_bg[0]} {rgb_bg[1]} {rgb_bg[2]}\" rgb2=\"{rgb_bg2[0]} {rgb_bg2[1]} {rgb_bg2[2]}\" width=\"500\" height=\"500\"/>")

mat_strings = []
mat_names = []
for i in range(obj_count):
    b = r.choice(builtin)
    reflect = r.uniform(0,1)
    r1, g1, b1 = round(r.uniform(0,1),1), round(r.uniform(0,1),1), round(r.uniform(0,1),1), 
    r2, g2, b2 = round(r.uniform(0,1),1), round(r.uniform(0,1),1), round(r.uniform(0,1),1), 
    if b == "checker":
        repeat = r.randint(2,10)
        tex_strings.append(f"<texture name=\"{b}_{i}\" builtin=\"checker\" rgb1=\"{r1} {g1} {b1}\" rgb2=\"{r2} {g2} {b2}\" width=\"500\" height=\"500\"/>")       
        mat_strings.append(f"<material name=\"{b}_{i}_mat\" reflectance=\"{reflect}\" texrepeat=\"{repeat} {repeat}\" texture=\"{b}_{i}\" texuniform=\"false\" />")
    if b == "gradient":
        tex_strings.append(f"<texture name=\"{b}_{i}\" builtin=\"gradient\" rgb1=\"{r1} {g1} {b1}\" rgb2=\"{r2} {g2} {b2}\" width=\"500\" height=\"500\"/>")
        mat_strings.append(f"<material name=\"{b}_{i}_mat\" reflectance=\"{reflect}\" texture=\"{b}_{i}\" texuniform=\"true\"/>")
    if b == "flat":
        tex_strings.append(f"<texture name=\"{b}_{i}\" builtin=\"flat\" rgb1=\"{r1} {g1} {b1}\" rgb2=\"{r1} {g1} {b1}\"  width=\"500\" height=\"500\"/>")
        mat_strings.append(f"<material name=\"{b}_{i}_mat\" reflectance=\"{reflect}\" texture=\"{b}_{i}\" texuniform=\"true\"/>")
    mat_names.append(f"{b}_{i}_mat")     

xml_prefix = """\
<mujoco>
   <asset>
"""

xml_prefix = xml_prefix + "\n".join(tex_strings) + "\n".join(mat_strings)

r_p, g_p, b_p = round(r.uniform(0,1),1), round(r.uniform(0,1),1), round(r.uniform(0,1),1), 

xml_prefix += f"""
   </asset>

   <worldbody>
     <geom type="plane" size="1 1 0.1" rgba="{r_p} {g_p} {b_p} 1" />
"""

lights_count = r.randint(1,2)
light_s = ""
for i in range(lights_count):
    x,y = r.uniform(-1,1), r.uniform(-1, 1)
    light_s += f"<light pos=\"{x} {y} 2\" dir=\"0 0 -1\" cutoff=\"90\" diffuse=\"1 1 1\" specular=\"1 1 1\"/>\n"

xml_prefix += light_s

obj_type = []
obj_strings = []
obj_positions = []
obj_sizes = []
obj_materials = []
obj_polygons = []
plane = Polygon([(-1, -1), (1,-1), (1,1), (-1,1)])
for i in range(obj_count):
    obj = r.choice(objects)
    mat = mat_names[i]
    #size of object
    a, b, c = round(r.uniform(min_obj_size, max_obj_size), 2), round(r.uniform(min_obj_size, max_obj_size), 2), round(r.uniform(min_obj_size, max_obj_size), 2)
    if obj in ("cube", "sphere"):
        s_x, s_y, s_z = a, a, a
    if obj == "box":
        s_x, s_y, s_z = a, b, c
    if obj == "cylinder":
        s_x, s_y, s_z = a, a, b
    if obj == "cube":
        obj = "box"
    intersects = 1
    tries = 0
    x_rot = r.randint(0,89)
    current_poly = get_polygon('circle', 1, 1, 1, 0, 0, 0, 0)
    while intersects > 0:
        tries += 1
        x, y, z = round(r.uniform(-1 + s_x, 1-s_x), 2), round(r.uniform(-1 + s_y, 1-s_y), 2), s_z 
        current_poly = get_polygon(obj, s_x, s_y, s_z, x, y, z, x_rot)
        intersects = len(obj_positions)
        if intersects == 0:
            continue
        for poly in obj_polygons:
            if not current_poly.intersects(poly):   
                intersects -= 1
    obj_polygons.append(current_poly)
    #print("------------------", s_x, s_y, s_z, x, y, z)
    # due to cylinder having y hight on second pozition not z
    if obj == "cylinder":
        obj_sizes.append((s_x, s_y, s_z))
        s_y = s_z
    obj_string =  f"<geom type=\"{obj}\" pos=\"{x} {y} {z}\" size=\"{s_x} {s_y} {s_z}\" material=\"{mat}\" euler=\"0 0 {x_rot}\" />"
    obj_sizes.append((s_x, s_y, s_z))
    obj_positions.append((x, y, z))
    obj_type.append(obj)
    obj_materials.append(mat)
    obj_strings.append(obj_string)

#obj_polygons.append(plane)
#for pol in obj_polygons:
#    x,y = pol.exterior.xy
#    plt.plot(x,y)
#plt.savefig(f'final_composition_{sys.argv[2]}.png')
#plt.show()


xml_suffix = """\
   </worldbody>
   <visual>
      <headlight diffuse="0.7 0.7 0.7"/>
   </visual>
</mujoco>\
"""

camera_line1 = f"<camera euler=\"60 0 180\" fovy=\"60\" name=\"camera1\" pos=\"-0.2 -1.5 1\"></camera>"
camera_line2 = f"<camera euler=\"60 0 180\" fovy=\"60\" name=\"camera2\" pos=\"0.2 -1.5 1\"></camera>"

#upper_camera = f"<camera euler=\"0 0 0\" fovy=\"60\" name=\"{camera_name}\" pos=\"0 0 2\"></camera>"

xml_string1 = xml_prefix + "\n".join(obj_strings) + camera_line1 + xml_suffix
xml_string2 = xml_prefix + "\n".join(obj_strings) + camera_line2 + xml_suffix

#print(xml_string)
xml_file1 = open(sys.argv[1] + '_c1.xml', "w+")
xml_file2 = open(sys.argv[1] + '_c2.xml', "w+")
xml_file1.write(xml_string1)
xml_file2.write(xml_string2)

