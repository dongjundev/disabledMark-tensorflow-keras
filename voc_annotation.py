import xml.etree.ElementTree as ET
from os import getcwd
import glob

classes = ["mark"]

def convert_annotation(annotation_voc, train_all_file):
    tree = ET.parse(annotation_voc)     # xml 파일 parse
    root = tree.getroot()       # xml 문서의 최상단 루트 읽기

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1: continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        train_all_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

train_all_file = open('./data/light/train_all.txt', 'w')

# Get annotations_voc list
for className in classes:
    print(className)
    annotations_voc = glob.glob(f'./data/light/label/train/*.xml')
    for annotation_voc in annotations_voc:
        image_id = annotation_voc.split('/')[-1].split('.')[0]+'.JPG'
        print(image_id)
        train_all_file.write(f'./data/light/image/{image_id}')
        convert_annotation(annotation_voc, train_all_file)
        train_all_file.write('\n')
train_all_file.close()