# coding:utf-8

import sys, os
from PIL import Image
from optparse import OptionParser
import numpy as np

# 遍历指定目录下的JPG图片，返回list
def walk_dir(dir):
    image_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if (ext.lower() == 'jpg'):
                path = root + os.sep + name
                image_list.append(path)
    return image_list


# 保存图片,默认保存在图片目录下的thumb
def resize_save(im, width, path):
    image_name = im.filename.split(os.sep)[-1]
    save_name = path + os.sep + image_name
    size = auto_resize(im, width)
    new_im = im.resize(size)
    print(save_name)
    new_im.save(save_name)


# 调整宽高
def auto_resize(im, width):
    size = im.size
    #height = int(float(width) / size[0] * size[1])
    height =width
    return (int(width), height)

def getImage(dir):
    imageList =walk_dir(dir)
    images=[]
    for path in imageList:
      image = Image.open(path)
      image = np.array(image)
      images.append(image)
    return np.array(images)

if __name__ == '__main__':

    usage_msg = 'usage: %prog -p <image_path> -w <image_width>'
    parser = OptionParser(usage_msg)
    parser.add_option("-p", "--path", dest="image_path", help=u"存放相片的路径",default='D:\\matlab2017\\bin\\MerchData')
    parser.add_option("-w", "--width", dest="image_width", help=u"调整后的图片宽度(高度会自等比例缩放)",default=224)
    options, args = parser.parse_args()

    if not options.image_path or not options.image_width:
        parser.print_help()
        sys.exit(1)


    image_path = options.image_path
    width = options.image_width
    save_path = image_path + os.sep + 'thumb'
    getImage(save_path)
    if (not os.path.exists(save_path)):
        os.mkdir(save_path)

    image_list = walk_dir(image_path)
    for path in image_list:
        im = Image.open(path)
        images=np.array(im)
        resize_save(im, width, save_path)

