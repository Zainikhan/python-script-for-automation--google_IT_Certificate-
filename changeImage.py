#!/usr/bin/env python3

import os
from PIL import Image

path = os.path.expanduser('~') + "/supplier-data/images"

for image_name in os.listdir(path):
  if image_name[0] != "." and image_name not in ["README", "LICENSE"]:
     img = Image.open(path+"/"+image_name).convert('RGB')
     new_img_path = path +"/{}.jpeg".format(image_name.split(".")[0])
     img.resize((600,400)).save(new_img_path, "JPEG") 
