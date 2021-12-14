# from utils.autoanchor import kmean_anchors
# if __name__ == '__main__':
#     kmean_anchors(path='./data/vedai.yaml', n=9, img_size=512, thr=4.0, gen=1000, verbose=True)
#     #22,9,  10,21,  22,15,  18,20,  14,30,  34,13,  29,31,  64,19,  40,76
#     #22,9,  9,21,  12,23,  17,19,  23,13,  13,33,  22,20,  41,14,  29,36
#     #9,21,  22,9,  12,22,  22,14,  18,20,  14,34,  40,14,  27,27,  40,76
#     #22,9,  10,21,  15,21,  21,17,  13,32,  31,14,  27,28,  83,19,  35,66

# -*- coding=utf-8 -*-
import glob
import os
import sys
import xml.etree.ElementTree as ET
import numpy as np
from kmeans import kmeans, avg_iou

# 根文件夹
ROOT_PATH = '/home/data/zhangjiaqing/dataset/VEDAI' #'/data/DataBase/YOLO_Data/V3_DATA/'
# 聚类的数目
CLUSTERS = 9
# 模型中图像的输入尺寸，默认是一样的
SIZE = 512

# 加载YOLO格式的标注数据
def load_dataset(path):
    jpegimages = os.path.join(path, 'images')
    if not os.path.exists(jpegimages):
        print('no JPEGImages folders, program abort')
        sys.exit(0)
    labels_txt = os.path.join(path, 'labels')
    if not os.path.exists(labels_txt):
        print('no labels folders, program abort')
        sys.exit(0)

    label_file = os.listdir(labels_txt)
    print('label count: {}'.format(len(label_file)))
    dataset = []

    for label in label_file:
        with open(os.path.join(labels_txt, label), 'r') as f:
            txt_content = f.readlines()

        for line in txt_content:
            line_split = line.split(' ')
            roi_with = float(line_split[len(line_split)-2])
            roi_height = float(line_split[len(line_split)-1])
            if roi_with == 0 or roi_height == 0:
                continue
            dataset.append([roi_with, roi_height])
            # print([roi_with, roi_height])

    return np.array(dataset)

data = load_dataset(ROOT_PATH)
out = kmeans(data, k=CLUSTERS)

print(out)
print("Accuracy: {:.2f}%".format(avg_iou(data, out) * 100))
print("Boxes:\n {}-{}".format(out[:, 0] * SIZE, out[:, 1] * SIZE))

ratios = np.around(out[:, 0] / out[:, 1], decimals=2).tolist()
print("Ratios:\n {}".format(sorted(ratios)))