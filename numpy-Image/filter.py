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

shifted_right = np.roll(gray,1,axis = 1)
shifted_left = np.roll(gray,-1,axis= 1)
shifted_up = np.roll(gray,-1,axis =0)
shifted_down = np.roll(gray,1,axis=0)

blurred = (gray + shifted_right + shifted_left + shifted_up + shifted_down)/5

blurred_img = Image.fromarray(blurred.astype(np.uint8))
blurred_img.save('blurred_output.jpg')

horizontal_edges = gray - shifted_right
vertical_edges = gray - shifted_down

edges = np.abs(horizontal_edges) + np.abs(vertical_edges)

edges_img = Image.fromarray(edges.astype(np.uint8))
edges_img.save('edges_output.jpg')
