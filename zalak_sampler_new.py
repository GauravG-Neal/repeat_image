zalak_annotate = open('sampler_annotate_list.txt','r')
zalak_raw = open('sampler_raw_list.txt','r')

zalak_annotate_last = (str.split(zalak_annotate.read()))[-1][:-3]+'jpg'
all_images = (str.split(zalak_raw.read()))

last_labeled_index = all_images.index(zalak_annotate_last)
sampled_images = all_images[last_labeled_index::10]

with open(f'sampled_image_srate_10.txt', 'w') as f:
    for item in sampled_images:
        f.write("%s\n" % item)