#Usage: python3 create_metrics.py <folder_name>
import json
import numpy as np
import sys
import os
from os.path import exists
import matplotlib.pyplot as plt


#From annotation/network_output file return list of objects containing only necessary fields
def read_objects_from_json(inference_json):
    f = open(inference_json)
    data = json.load(f)
    counter = 1
    objects=[]
    for obj in data['objects']:
        #print(f'OBJECT {counter}\nCLASS:{obj["class"]}\nLOC:{obj["location"]}\nROT:{obj["quaternion_xyzw"]}')
        objects.append({'class':obj["class"], 'loc':obj["location"],'rot':obj["quaternion_xyzw"], 'matched':False})
        counter += 1
    f.close()
    return objects

# Return euclidean distance of 2 3D points
def distance_of_2_points(point1, point2):
    p1 = np.array(point1)
    p2 = np.array(point2)
    dist = np.linalg.norm(p1-p2)
    return dist

#Find closest annotated object (dist + idx) to inference obj
def find_closest_object(obj, gt_objects):
    min_dist = np.inf
    min_idx = 0
    for idx,gt_obj in enumerate(gt_objects):
        #If object has different class or is already matched, skip
        if obj['class'] != gt_obj['class']:
            #Uncomment if you use multiple types of objects
            #continue
            pass
        if gt_obj['matched'] == True:
            continue
        #print("POINTS", obj['loc'], gt_obj['loc'])
        dist = distance_of_2_points(obj['loc'], gt_obj['loc'])
        #print('dist:',obj['loc'], gt_obj['loc'],dist,idx)
        #Find closest object
        min_dist, min_idx = min((min_dist, min_idx), (dist, idx))
    return(min_dist, min_idx)

#For annotation file and inference file find distances of cubes and their annotation. If there is no match for annotation
# distance is set to np.inf
def find_avg_distance(inference_json, gt_json):
    inference_objects = read_objects_from_json(inference_json)
    #print("\nINFERENCE\n",inference_objects)
    gt_objects = read_objects_from_json(gt_json)
    #print("\nGT\n",gt_objects)

    # Pair objects from inference to object from gt based on smallest distances
    # Indexes of matched pairs
    matches = []
    #Distances of matched pairs
    distances = []
    # How many objects we already paired
    matched_count = 0
    #For each found object, find which one of annotated(not yet paired) is closest
    while matched_count < len(inference_objects) and matched_count < len(gt_objects):
        object_distances = []
        #Go through all gt object and find minimal for each inference object
        for idx, obj in enumerate(inference_objects):
            if obj['matched'] == True:
                continue
            object_distances.append((*find_closest_object(obj, gt_objects), idx))
        #print("Minimal_distances:",object_distances)
        #print("MIN:", min(object_distances))
        # Get best match and setobjects as matched
        best_match = min(object_distances)
        #idx of inference object, idx of gt object, their distance
        matches.append((best_match[2], best_match[1], best_match[0]))
        distances.append(best_match[0])
        matched_count += 1
        inference_objects[best_match[2]]['matched'] = True
        gt_objects[best_match[1]]['matched'] = True
    #We have all the matches
    #print("MATCHES:",matches)
    #Count average distance of objects
    if len(distances) > 0:
        avg_distance = sum(distances)/len(distances)
    else:
        print('NO MATCHES FOuND')
        avg_distance = -1
    if len(distances) < len(gt_objects):
        dif = len(gt_objects) - len(distances)
        print(f'Found {len(distances)} cubes out of {len(gt_objects)}')
        distances.extend([np.inf] * dif)    
        print(f'distances:{distances}')
    print("AVERAGE DISTANCE", avg_distance)
    return distances


def main():
    #Get folder name and create graph and metrics for full dataset
    folder_name = sys.argv[1]
    inference_folder = '/home/angelikafedakova/Deep_Object_Pose/scripts/train2/inference_outputs/' + folder_name
    gt_folder = '/home/angelikafedakova/Deep_Object_Pose/scripts/nvisii_data_gen/output/' + folder_name
    
    avg_distances = []
    all_distances = []
    # since dataset has structure <dataset_name>/000,...,<dataset_name>/n we have to dive into all folders
    for dirname in os.listdir(inference_folder):
        subdir = os.path.join(inference_folder, dirname)
        # checking if it is a dir
        if os.path.isdir(subdir):
            #print(subdir)
            #Go through all images/annotaion files
            for filename in os.listdir(subdir):
                inference_json = os.path.join(subdir, filename)
                if os.path.isfile(inference_json) and 'json' in inference_json:
                    print(inference_json)
                    #Find corresponding annotation file to inference file
                    gt_json = gt_folder + '/' + '/'.join(inference_json.split('/')[-2:])
                    print("GT:", gt_json)
                    if not exists(gt_json):
                        raise ValueError('No annotation for file:' + inference_json + '\nNo such file:' + gt_json)
                    #Find and add distances of cubes for one file
                    all_distances.extend(find_avg_distance(inference_json, gt_json))
                    #if dist != -1 and dist < 10:
                     #   all_distances.extend(find_avg_distance(inference_json, gt_json))
    
    #Distances of all annotated objects to found objects
    print(all_distances)
    points_x = []
    points_y = []
    #Create graf, x axis is for distance, y axis has percentage of cubes with distance smaller than value on x axis
    for i in np.arange (0, 10, 0.1):
        percentage = sum(d < i for d in all_distances) / len(all_distances)
        points_x.append(i)
        points_y.append(percentage)
    plt.plot(points_x, points_y)
    plt.show()
    plt.savefig('distances.png')
    print(f'All Cubes:{len(all_distances)}')
    print('Cubes with smaller distance than 2cm', sum(i < 2 for i in all_distances))
    print('Cubes with inf distance', sum(i == np.inf for i in all_distances))
    print('MEDIAN', np.median(all_distances))
    print('1st quartile', np.percentile(all_distances, 25))
    #print('DATASET AVG DIST:', sum(avg_distances)/len(avg_distances))
    #print(inference_json, gt_json)
    #read_inference_objects(inference_json)


    #print('\nDISTANCE')
    #distance_of_2_points([-0.5555294752120972,0.5686306953430176, -1.4284099340438843],[0.6361290812492371,-0.24096433818340302,-1.7248599529266357])

if __name__ == "__main__":
    main()

