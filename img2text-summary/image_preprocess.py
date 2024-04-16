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
# colab link: https://colab.research.google.com/drive/1EXp9DXgn8-GITrmtOk1_40PV6RT3q1zy?usp=sharing
from PIL import Image
image = Image.open(file_path)#to be replaced

def grayscale(image):
    width, height = image.size
    greyscaled_img = Image.new('L', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            gray_value = int(0.3 * pixel[0] + 0.59 * pixel[1] + 0.11 * pixel[2])  # Convert to grayscale
            greyscaled_img.putpixel((x, y), gray_value)

    return greyscaled_img

def noise_reduction(image):
    width, height = image.size
    filtered_img = Image.new('L', (width, height))

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            neighbors = [image.getpixel((x + dx, y + dy)) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
            avg_value = sum(neighbors) // len(neighbors)
            filtered_img.putpixel((x, y), avg_value)

    return filtered_img

def contrast_stretching(image):
    width, height = image.size
    stretched_img = Image.new('L', (width, height))

    min_pixel = min(image.getdata())
    max_pixel = max(image.getdata())
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            stretched_value = int((pixel - min_pixel) * 255 / (max_pixel - min_pixel))  # Stretch contrast
            stretched_img.putpixel((x, y), stretched_value)

    return stretched_img

def resize_image(image, new_width, new_height):
    resized_img = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_img

def binarize_image(image, threshold=128):
    binarized_img = image.point(lambda p: 0 if p < threshold else 255, '1')
    return binarized_img

def normalize_image(image):
    norm_img = Image.new('L', image.size)

    max_pixel = max(image.getdata())
    min_pixel = min(image.getdata())

    for x in range(image.width):
        for y in range(image.height):
            pixel_value = image.getpixel((x, y))
            normalized_value = int((pixel_value - min_pixel) / (max_pixel - min_pixel) * 255)
            norm_img.putpixel((x, y), normalized_value)

    return norm_img

def preprocessing(image):
  g_i=grayscale(image)
  n_i=noise_reduction(g_i)
  c_i=contrast_stretching(n_i)
  r_i=resize_image(c_i,224, 224)
  # b_i=binarize_image(r_i)
  # norm_image=normalize_image(b_i)
  return r_i

preprocessing(image)
