import xml.etree.ElementTree as ET
import os
import shutil
import cv2
# tree = ET.parse('/media/techpro/Data/home/techpro/hieupm12/new/YOLOX/datasets/VOCdevkit/VOC2007/Annotations2/PartA_00000.xml')
# root = tree.getroot()

rootdirXML = '/media/techpro/Data/home/techpro/hieupm12/new/YOLOX/datasets/VOCdevkit/VOC2007/Annotations2/data/'

rootdirImage = '/media/techpro/Data/home/techpro/hieupm12/new/YOLOX/datasets/VOCdevkit/VOC2007/JPEGImages/'

for item in os.listdir(rootdirXML):
    tree = ET.parse(rootdirXML + str(item))
    root = tree.getroot()

    # current w, h
    w = int(root[4][0].text)
    h = int(root[4][1].text)

    if w == 0 or h == 0:
        print('item width 0: ---', item)
        image_path = rootdirImage + str(item).replace(".xml", ".jpg")
        img_file = cv2.imread(str(image_path))
        new_h, new_w, _ = img_file.shape
        print('height: ', new_h, ' - width: ', new_w)

        # new_w = int(w.text) - 11
        # w.text = str(new_w)
        root[4][0].text = str(new_w)
        root[4][1].text = str(new_h)
        
        tree.write(rootdirXML + str(item))
