# Imports
import math
import random 
import PIL
from PIL import Image, ImageDraw
import numpy as np
from itertools import chain
import cv2
from matplotlib import pyplot as plt
import subprocess
import threading 
import sys
from os import path
from statistics import mean
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Model

# Random seed
random.seed(1337)

# Download data
def get_ucmerced_dataset():
  !wget https://www.dropbox.com/s/daryz3bbhvrrvd5/UCMerced_LandUse.zip
  !unzip -q UCMerced_LandUse.zip
  !rm '/content/UCMerced_LandUse.zip'
  
get_ucmerced_dataset()

# 1. Random RGB Fill
# input: img (np array)
# output: arr (np array with swath filled by random RGB)
def fill_swath_with_random_rgb(img):
  arr = img.copy()
  x, y, z = np.where(arr==[0, 0, 0])
  for i in range(len(x)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    arr[x[i]][y[i]]=color
  return arr

# 2. Random RGB From Image Fill
# input: x_arr (non-swath x coords), y_arr (non-swath y coords)
# output: a random non-swath pixel
def get_random_pixel_from_image(x_arr, y_arr):
  index = random.randint(0, len(x_arr)-1)
  return x_arr[index], y_arr[index]

# input: img (np array)
# output: img (np array with random other pixels from image)
def fill_swath_with_random_pixel_from_image(img):
  img = img.copy()
  (x_non_swath, y_non_swath, z_non_swath) = np.where(img != [0, 0, 0])
  (x_swath, y_swath, z_swath) = np.where(img == [0, 0, 0])
  for i in range(len(x_swath)):
    x_pixel, y_pixel = get_random_pixel_from_image(x_non_swath, y_non_swath)
    img[x_swath[i]][y_swath[i]] = img[x_pixel][y_pixel]

  return img

# 3. Fill swath with neighboring pixel
# Dynamically tries finding non empty points in neighbourhood
# When it fails few times, it increases neighbourhood size automatically
def get_neighboring_pixel(img, x, y):
  x_rand, y_rand = 0,0

  max_num_tries = 30
  max_tries_per_neighbourhood = 3
  neighbourhood_size_increment = 10
  current_window_size = 10
  total_tries = 0
  for _ in range(math.ceil(max_num_tries/max_tries_per_neighbourhood)):
    for _ in range(max_tries_per_neighbourhood):
      min_x = max(0, x-current_window_size)
      max_x = min(224, x+current_window_size)
      min_y = max(0, y-current_window_size)
      max_y = min(224, y+current_window_size)
      x_rand = random.randint(min_x, max_x-1)
      y_rand = random.randint(min_y, max_y-1)
      total_tries += 1
      if not(img[x_rand][y_rand][0]==0 and img[x_rand][y_rand][1]==0 and img[x_rand][y_rand][2]==0):
        return x_rand, y_rand
    current_window_size += neighbourhood_size_increment

  return x_rand, y_rand
    
def fill_swath_with_neighboring_pixel(img):
  img_with_neighbor_filled = img.copy()
  (x_swath, y_swath, z_swath) = np.where(img == [0, 0, 0])

  for i in range(len(x_swath)):
    x_rand, y_rand = get_neighboring_pixel(img, x_swath[i], y_swath[i])
    img_with_neighbor_filled[x_swath[i]][y_swath[i]] = img[x_rand][y_rand]
  return img_with_neighbor_filled

