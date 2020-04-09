from PIL import Image,ImageChops
import numpy as np

threshold2 = 15000
f = open("image_list.txt",'r')
last_image_path=(str.split(f.read()))[-1]
f = open("image_list.txt",'r')

unique_image=[]
last_image = False
image_path = str.rstrip(f.readline())
img1 = Image.open(image_path)
unique_image.append(image_path)
repeat_image=[]

while(last_image==False):
    image_is_same=True
    while(image_is_same==True):
        image_path = str.rstrip(f.readline())
        if(image_path==last_image_path):
            last_image=True
        img2 = Image.open(image_path)
    
        diff = ImageChops.difference(img1,img2)
        diff_array = np.array(diff)
        if(np.sum(diff_array.sum(axis=2)>200)>threshold2):
            image_is_same=False
            unique_image.append(image_path)
        else:
            repeat_image.append(image_path)
        if(last_image==True):
            break
    img1 = Image.open(image_path)
    
     
with open('repeat_list.txt', 'w') as f:
    for item in repeat_image:
        f.write("%s\n" % item)

with open('unique_list.txt', 'w') as f:
    for item in unique_image:
        f.write("%s\n" % item)    