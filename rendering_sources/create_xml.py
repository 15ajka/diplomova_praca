#This script creates scene model with camera, parameters from arguments will be added later on
#RUN: python3 create_xml.py <camera_name> <c_x> <c_y> <c_z>

import sys
import random as r

def random_rgb():
    return round(r.uniform(0,1),1), round(r.uniform(0,1),1), round(r.uniform(0,1),1)
    

objects = ["cube", "box", "sphere", "cylinder"]
builtin = ["checker", "gradient", "flat"]
materials = ["checker_mat", "gradient_mat", "flat_mat"]
obj_count = r.randint(4,7)

tex_strings = []
rgb_bg, rgb_bg2 = random_rgb(), random_rgb()
tex_strings.append(f"<texture type=\"skybox\" builtin=\"gradient\" rgb1=\"{rgb_bg[0]} {rgb_bg[1]} {rgb_bg[2]}\" rgb2=\"{rgb_bg2[0]} {rgb_bg2[1]} {rgb_bg2[2]}\" width=\"256\" height=\"256\"/>")

mat_strings = []
mat_names = []
for i in range(obj_count):
    b = r.choice(builtin)
    r1, g1, b1 = round(r.uniform(0,1),1), round(r.uniform(0,1),1), round(r.uniform(0,1),1), 
    r2, g2, b2 = round(r.uniform(0,1),1), round(r.uniform(0,1),1), round(r.uniform(0,1),1), 
    if b == "checker":
        repeat = r.randint(2,10)
        tex_strings.append(f"<texture name=\"{b}_{i}\" builtin=\"checker\" type=\"2d\" rgb1=\"{r1} {g1} {b1}\" rgb2=\"{r2} {g2} {b2}\" width=\"200\" height=\"200\"/>")       
        mat_strings.append(f"<material name=\"{b}_{i}_mat\" reflectance=\"0.9\" texrepeat=\"{repeat} {repeat}\" texture=\"{b}_{i}\" texuniform=\"false\" />")
    if b == "gradient":
        tex_strings.append(f"<texture name=\"{b}_{i}\" builtin=\"gradient\" rgb1=\"{r1} {g1} {b1}\" rgb2=\"{r2} {g2} {b2}\" width=\"200\" height=\"200\"/>")
        mat_strings.append(f"<material name=\"{b}_{i}_mat\" reflectance=\"1\" texture=\"{b}_{i}\" texuniform=\"true\"/>")
    if b == "flat":
        tex_strings.append(f"<texture name=\"{b}_{i}\" builtin=\"flat\" rgb1=\"{r1} {g1} {b1}\" rgb2=\"{r1} {g1} {b1}\"  width=\"200\" height=\"200\"/>")
        mat_strings.append(f"<material name=\"{b}_{i}_mat\" reflectance=\"1\" texture=\"{b}_{i}\" texuniform=\"true\"/>")
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
      <light diffuse=".9 .9 .9" pos="0 0 3" dir="0 0 -1"/>
     <geom type="plane" size="1 1 0.1" rgba="{r_p} {g_p} {b_p} 1"/>
"""

obj_type = []
obj_strings = []
obj_positions = []
obj_sizes = []
obj_materials = []
for i in range(obj_count):
    obj = r.choice(objects)
    mat = mat_names[i]
    #size of object
    a, b, c = round(r.uniform(0.1, 0.3), 2), round(r.uniform(0.1, 0.3), 2), round(r.uniform(0.1, 0.3), 2)
    if obj in ("cube", "sphere"):
        s_x, s_y, s_z = a, a, a
    if obj in ("cylinder", "box"):
        s_x, s_y, s_z = a, b, c
    if obj == "cube":
        obj = "box"
    intersects = 1
    while intersects > 0:
        x, y, z = round(r.uniform(-1 + s_x, 1-s_x), 2), round(r.uniform(-1 + s_y, 1-s_y), 2), s_z 
        intersects = len(obj_positions)
        if intersects == 0:
            continue
        #print("POS1:", x, y, "\nSIZ1", s_x, s_y)
        #print("POS2:", obj_positions[0][:2], "\nSIZ2:", obj_sizes[0][:2])
        for idx, t in enumerate(obj_positions):
            if t[0] + obj_sizes[idx][0] < x - s_x:
                intersects -= 1
         #       print("HERE1")
                continue
            if t[0] - obj_sizes[idx][0] > x + s_x:
                intersects -= 1
         #       print("HERE2")
                continue
            if t[1] + obj_sizes[idx][1] < y - s_y:
                intersects -= 1
         #       print("HERE3")
                continue
            if t[1] - obj_sizes[idx][1] > y + s_y:
                intersects -= 1
         #       print("HERE4")
                continue
    #print("------------------", s_x, s_y, s_z, x, y, z)
    obj_string =  f"<geom type=\"{obj}\" pos=\"{x} {y} {z}\" size=\"{s_x} {s_y} {s_z}\" material=\"{mat}\" />"
    obj_sizes.append((s_x, s_y, s_z))
    obj_positions.append((x, y, z))
    obj_type.append(obj)
    obj_materials.append(mat)
    obj_strings.append(obj_string)

xml_suffix = """\
   </worldbody>
</mujoco>\
"""

camera_name = sys.argv[1]
camera_line = f"<camera euler=\"60 0 180\" fovy=\"60\" name=\"{camera_name}\" pos=\"0 -1.5 1\"></camera>"
#upper_camera = f"<camera euler=\"0 0 0\" fovy=\"60\" name=\"{camera_name}\" pos=\"0 0 2\"></camera>"

xml_string = xml_prefix + "\n".join(obj_strings) + camera_line + xml_suffix
#xml_string = xml_prefix + "\n".join(obj_strings) + upper_camera + xml_suffix

#print(xml_string)
xml_file = open(sys.argv[2], "w+")
xml_file.write(xml_string)
