'''
Step 1: Preprocess the image

Functionalities: 
1. Get the image
2. Preprocess the image
  a. Apply grayscale
  b. Apply noise reduction
  c. Enhance the text contrast
  d. Resize the image
  e. Convert it into binary image
'''
from PIL import Image
import numpy as np
image = Image.open(file_path)//to be replaced
def grayscale(image):
  greyscaled_img=np.average(image, axis=2)
  return greyscaled_img
def resize(image, new_shape):
  height, width = new_shape
  resized_img=image[:height, :width]
  return resized_img
def normalize(image):
  normalized_img=image.astype(np.float32) / 255.0
  return normalized_img
def preprocess_image(image, target_shape=(224, 224)):
  image = grayscale(image)
  image = resize(image, target_shape)
  image = normalize(image)
  if len(image.shape) == 2:
    image = np.expand_dims(image, axis=-1)
  return image
