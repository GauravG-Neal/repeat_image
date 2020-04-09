import glob
all_images = (glob.glob("C:\walgreens_images\Code\*.jpg"))
sampling_rate=7
sampled_images=[]
for i,image_path in enumerate(all_images):
    if(i%sampling_rate==0):
        sampled_images.append(image_path)
        
with open(f'sampled_image_srate_{sampling_rate}.txt', 'w') as f:
    for item in sampled_images:
        f.write("%s\n" % item)
        