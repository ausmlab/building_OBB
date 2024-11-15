import json
import numpy as np
import os
import cv2

def polygon_to_obb(polygon):
    """
    Convert polygon coordinates to an oriented bounding box (OBB).
    
    Parameters:
    polygon (list of tuples): List of (x, y) coordinates representing the polygon vertices.
    
    Returns:
    box (list of tuples): List of (x, y) coordinates representing the vertices of the OBB.
    """
    # Convert the list of points to a numpy array for OpenCV
    points = np.array(polygon, dtype=np.float32)

    # Get the minimum area rectangle
    rect = cv2.minAreaRect(points)
    
    # Extract the box points from the rect, and convert them to integer
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    # Convert to list of tuples for easy readability
    obb = [(int(point[0]), int(point[1])) for point in box]
    
    return obb



# Change 'DATA_ROOT' into your own data path.
DATA_ROOT = '/nas2/YJ/DATA/WHUbuilding'


datasets = ['train', 'test', 'val']
for dataset in datasets :
    print ("Transforming {} dataset".format(dataset))
    with open(os.path.join(DATA_ROOT, './annotations/instances_{}.json'.format(dataset)), 'r') as f:
        bldg_data = json.load(f)
        
    Img_indexes = {}
    for img_info in bldg_data['images'] :
        Img_indexes[img_info['id']]=[]
        
    for i, anno in enumerate(bldg_data['annotations']) :
        img_id = anno['image_id']
        Img_indexes[img_id].append(i)
        
    ROOT = os.path.join(DATA_ROOT, 'OBB/{}'.format(dataset))
    if not os.path.exists(ROOT) :
        os.makedirs(ROOT)
        
    for img_info in bldg_data['images'] :
        img_id = img_info['id']
        filename = os.path.join(ROOT, '{}.txt'.format(img_id))
        with open(filename, 'w') as f :
            for i in Img_indexes[img_id] :
                anno = bldg_data['annotations'][i]
                polygon = np.array(anno['segmentation'])
                obb = np.array(polygon_to_obb(polygon.reshape(polygon.shape[1]//2,2))).reshape(-1)
                bbox = np.array(anno['bbox'])
                area = bbox[2] * bbox[3]
                if area < 1024 :
                    difficulty = 2
                elif area < 9216 :
                    difficulty = 1
                else :
                    difficulty = 0
                outputs = ''
                for coord in obb :
                    outputs += '{} '.format(coord)
                outputs += 'building {}\n'.format(difficulty)
                f.write(outputs)
    print ('{} files are completed'.format(len(bldg_data['images'])))
