#! /usr/bin/env python3

import os
import requests

def convert_to_dic(file_context, image_name):
  '''This converts the given file list to dictionary that will be used to post data to website.'''
  dic = {}
  dic['name'] = file_context[0].strip('\n')
  dic['weight'] = int(file_context[1].strip('\n').split(" ")[0])
  dic['description'] = file_context[2].strip('\n')
  dic['image_name'] = image_name
  return dic

path = os.path.expanduser('~')+ "/supplier-data/descriptions"

for file_name in os.listdir(path):
  with open(path+"/"+file_name) as file:
     file_context = file.readlines()
     image_name = file_name.split('.')[0]+ ".jpeg"
     dic = convert_to_dic(file_context, image_name)
     response = requests.post('http://34.71.5.121/fruits/', data = dic)
     
