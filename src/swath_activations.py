# Imports
import math
import random 

# Random seed
random.seed(1337)

# 1. Random RGB Fill
def fill_swath_with_random_rgb_new(img, color={0,0,0}):
  """ 
  Filling method 1: 
  Input: image with missing data (numpy array)
  Output: numpy array with swath filled by random RGB values chosen from Gaussian distribution
  """
  arr = img.copy()
  x, y, z = np.where(arr==color)
  for i in range(len(x)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    arr[x[i]][y[i]]=color
  return arr

# 2. Random RGB From Image Fill
def get_random_pixel_from_image(x_arr, y_arr):
  """ 
  Selects random non-missing pixel from image
  Input: x_arr (non-missing x coords), y_arr (non-missing y coords)
  Output: random non-missing pixel coordinates (x_pix, y_pix)
  """
  index = random.randint(0, len(x_arr)-1)
  return x_arr[index], y_arr[index]

def fill_swath_with_random_pixel_from_image_new(img, color={0,0,0}):
  """ 
  Filling method 2: 
  Input: image with missing data (numpy array)
  Output: numpy array with swath filled by random RGB values randomly selected from non-missing pixel portions of the image
  """
  img = img.copy()
  (x_non_swath, y_non_swath, z_non_swath) = np.where(img != color)
  (x_swath, y_swath, z_swath) = np.where(img == color)
  for i in range(len(x_swath)):
    x_pixel, y_pixel = get_random_pixel_from_image(x_non_swath, y_non_swath)
    img[x_swath[i]][y_swath[i]] = img[x_pixel][y_pixel]

  return img

# 3. Fill swath with neighboring pixel
def get_neighboring_pixel(img, x, y, current_window_size):
  """ 
  Dynamically selects non-missing points within a radius of the target missing pixel. As selection fails, radius size increases automatically.
  Inputs: img (numpy array)
          x, y: coordinates of the target missing pixel to fill
  Outputs: dynamically-selected non-missing pixel (x_neighbor, y_neighbor)
  """
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
    
def fill_swath_with_neighboring_pixel(img, color = {0,0,0}, current_window_size = 10):
  """ 
  Filling method 3: 
  Input: image with missing data (numpy array)
  Output: numpy array with missing data filled by random RGB values from non-missing pixel portions of the image selected with probability inversely proportional to distance
  """
  img_with_neighbor_filled = img.copy()
  (x_swath, y_swath, z_swath) = np.where(img == color)

  for i in range(len(x_swath)):
    x_rand, y_rand = get_neighboring_pixel(img, x_swath[i], y_swath[i], current_window_size)
    img_with_neighbor_filled[x_swath[i]][y_swath[i]] = img[x_rand][y_rand]
  return img_with_neighbor_filled

