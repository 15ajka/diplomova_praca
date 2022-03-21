import json
import numpy as np

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
        print('dist:',obj['loc'], gt_obj['loc'],dist,idx)
        #Find closest object
        min_dist, min_idx = min((min_dist, min_idx), (dist, idx))
    return(min_dist, min_idx)

def main():
    #Read objects from annotation and output from trained network
    inference_json='inference.json'
    gt_json='gt.json'
    #print(inference_json, gt_json)
    #read_inference_objects(inference_json)
    inference_objects = read_objects_from_json(inference_json)
    print("\nINFERENCE\n",inference_objects)
    gt_objects = read_objects_from_json(gt_json)
    print("\nGT\n",gt_objects)

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
        print("Minimal_distances:",object_distances)
        print("MIN:", min(object_distances))
        # Get best match and setobjects as matched
        best_match = min(object_distances)
        #idx of inference object, idx of gt object, their distance
        matches.append((best_match[2], best_match[1], best_match[0]))
        distances.append(best_match[0])
        matched_count += 1
        inference_objects[best_match[2]]['matched'] = True
        gt_objects[best_match[1]]['matched'] = True
    #We have all the matches
    print("MATCHES:",matches)
    #Count average distance of objects
    print("AVERAGE DISTANCE", sum(distances)/len(distances))


    #print('\nDISTANCE')
    #distance_of_2_points([-0.5555294752120972,0.5686306953430176, -1.4284099340438843],[0.6361290812492371,-0.24096433818340302,-1.7248599529266357])

if __name__ == "__main__":
    main()

