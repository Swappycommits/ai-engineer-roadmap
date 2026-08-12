import numpy as np
from PIL import Image

img =Image.open('demo_image.jpg')
img_array = np.array(img)

print(img_array.shape)
print(img_array[0][0])

R = img_array[:,:,0]
G = img_array[:,:,1]
B = img_array[:,:,2]

print(R.shape)
print(G.shape)
print(B.shape)

gray = 0.2989*R + 0.5870*G + 0.1140*B

print(gray.shape)
print(gray[0][0])

gray_img = Image.fromarray(gray.astype(np.uint8))
gray_img.save('grayscale_output.jpg')