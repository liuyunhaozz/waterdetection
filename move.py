##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil
# from posix import times_result
def moveFile(img_Dir, label_Dir):
    label_path = os.listdir(label_Dir)    # 取图片的原始路径
    # print(len(img_path))
    # filenumber = len(label_path)
    # rate = 0.1    # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    # picknumber = int(filenumber * rate) #按照rate比例从文件夹中取一定数量图片
    # sample = random.sample(label_path, picknumber)  # 随机选取picknumber数量的样本图片
    # print(sample)
    # for val_name in sample:
    #     shutil.move(label_Dir + val_name, val_label_tarDir + val_name)
    #     shutil.move(img_Dir + val_name[:-4] + '.jpg', val_img_tarDir + val_name[:-4] + '.jpg')
    for train_name in label_path:
        shutil.move(label_Dir + train_name, train_label_tarDir + train_name)
        shutil.move(img_Dir + train_name[:-4] + '.jpg', train_img_tarDir + train_name[:-4] + '.jpg')           
    # print(img_path)
if __name__ == '__main__':
    img_Dir = "image/"    #源图片文件夹路径
    label_Dir = "label/"

    train_img_tarDir = 'datasets/object/images/train/'    # 移动到新的文件夹路径
    # val_img_tarDir = 'datasets/object/images/val/'
    train_label_tarDir = 'datasets/object/labels/train/'
    # val_label_tarDir = 'datasets/object/labels/val/'
    moveFile(img_Dir, label_Dir)