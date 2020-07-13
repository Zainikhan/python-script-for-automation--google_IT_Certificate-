#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
path = os.path.expanduser('~') + "/supplier-data/images"

for image_name in os.listdir(path):
  if len(image_name.split(".")) >1:
    if image_name.split(".")[1] == "jpeg":
       with open(path+"/{}".format(image_name), 'rb') as opened:
          r = requests.post(url , files={'file': opened})

