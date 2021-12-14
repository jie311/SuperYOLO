# 1: car, 2:trucks, 4: tractors, 5: camping cars, 7: motorcycles, 8:buses, 9: vans, 10: others, 11: pickup, 23: boats , 201: Small Land Vehicles, 31: Large land Vehicles

import os
import pandas as pd
import numpy as np
from PIL import Image
def update_annotations(filename):

    data = pd.read_csv(filename, sep=' ', index_col=None, header=None, names=['class','x_center', 'y_center', 'weight', 'height'])

    for x in data['class']:
        if x==6:
            print('boat',filename)
            break
        elif x==7:
            print('van',filename)
        if x==6 or x==7:
            image = Image.open(filename.replace('labels','images').replace('.txt','_co.png'))
            image.save(filename.replace('labels','images_boat_van').replace('.txt','_co.png'))
            a=os.path.dirname(filename.replace('labels','map_reference').replace('.txt','.png'))
            x = str(int(filename.replace('labels','map_reference').replace('.txt','').split('/')[-1]))
            label = Image.open(a+'/'+x+'.png')
            label.save(filename.replace('labels','images_boat_van').replace('.txt','.png'))
        


lb_file='/home/data/zhangjiaqing/dataset/VEDAI/fold01.txt'
label_file = '/home/data/zhangjiaqing/dataset/VEDAI/labels/'
with open(lb_file, 'r') as f:
    lb = f.readlines()
for index in range(len(lb)):
    filename = label_file + lb[index].rstrip() + '.txt'
    update_annotations(filename)

