import glob
all_images = (glob.glob("C:\walgreens_images\Code\*.jpg"))

with open('image_list.txt', 'w') as f:
    for item in all_images:
        f.write("%s\n" % item)
        