#As all the images are not of same size so resizing them
from PIL import Image
import os, sys

path = ""#Enter the url of the foldar containing the images of a category
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item).convert('RGB')
            f, e = os.path.splitext(path+item)
            print(item)
            imResize = im.resize((512,512), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)#Saves the image with the save name in .jpg format 
            

resize()
