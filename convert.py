import os
import xml.etree.ElementTree as ET
 
dirpath = 'box'     #原来存放xml文件的目录
newdir = 'label'  #修改label后形成的txt目录

dic = {'holothurian':0, 'echinus':1, 'scallop':2, 'starfish':3} 
cout = 0

if not os.path.exists(newdir):
    os.makedirs(newdir)
 
for fp in os.listdir(dirpath):
    cnt = 0
    root = ET.parse(os.path.join(dirpath,fp)).getroot()
    for child in root.findall('object'):         # 找到图片中的所有框, 如果 object = [], 则直接跳过
        label = child.find('name').text
        if label == 'waterweeds':
            continue
        else:
            if label != 'scallop':
                cnt += 1
            sub = child.find('bndbox')               # 找到框的标注值并进行读取
            # print(label)
            xmin = float(sub[0].text)
            ymin = float(sub[1].text)
            xmax = float(sub[2].text)
            ymax = float(sub[3].text)

            sz = root.find('size')
            width = float(sz[0].text)
            height = float(sz[1].text)
            # print(width, height)
        

            try:                                     # 转换成yolov3的标签格式，需要归一化到（0-1）的范围内
                x_center = (xmin + xmax) / (2 * width)
                y_center = (ymin + ymax) / (2 * height)
                w = (xmax - xmin) / width
                h = (ymax - ymin) / height
            except ZeroDivisionError:
                print(fp,'的 width有问题')
            with open(os.path.join(newdir, fp.split('.')[0] + '.txt'), 'a+') as f:
                f.write(' '.join([str(dic[label]), str(x_center), str(y_center), str(w), str(h) + '\n']))    

    if not cnt and 'u' in fp:
        try:
            os.remove(os.path.join(newdir, fp.split('.')[0] + '.txt'))
        except FileNotFoundError:
            cout += 1

print(cout)
#     xmin, ymin, xmax, ymax = 0,0,0,0
#     sz = root.find('size')
#     # print(root)
#     width = float(sz[0].text)
#     height = float(sz[1].text)
#     filename = root.find('filename').text
#     for child in root.findall('object'):         #找到图片中的所有框
#         #print(child.find('name').text)
    
#         sub = child.find('bndbox')               #找到框的标注值并进行读取
#         label = 0
#         xmin = float(sub[0].text)
#         ymin = float(sub[1].text)
#         xmax = float(sub[2].text)
#         ymax = float(sub[3].text)
#        
 

 
# print('ok')
