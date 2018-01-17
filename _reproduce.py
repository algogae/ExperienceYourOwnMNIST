import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from resizeimage import resizeimage

# mat = np.matrix('0 1; 1 0')
# plt.imshow(mat, cmap='gray', interpolation='none')

img = Image.open('4.jpg')
img_arr = np.array(img.resize((28, 28), Image.ANTIALIAS).convert('L'), dtype='float32')
print(img_arr)
# img_arr = np.ones((28,28), dtype='float32') - img_arr/255

print('\n conversion \n')
# print(img_arr)
img_arr = 1 - img_arr/255
print(img_arr)

# Threshold
threshold = 0.5

# Original image
plt.imshow(img_arr, cmap='gray', interpolation='none')
plt.show()

# REPRODUCE_BY_SHIFTING_LEFT
shift_dist = 27
for i in range(28):
    for j in range(28):
        if (threshold < img_arr.item((i, j)) and j < shift_dist):
            shift_dist = j
            break

for shift in range(shift_dist):
    img_shift = np.zeros((28, 28))
    img_shift[:,:28-shift] = img_arr[:,shift:]
    plt.imshow(img_shift, cmap='gray', interpolation='none')
    plt.show()

# Original image
plt.imshow(img_arr, cmap='gray', interpolation='none')
plt.show()

# REPRODUCE_BY_SHIFTING_RIGHT
shift_dist = 0
for i in range(28):
    for j in reversed(range(28)):
        if (threshold < img_arr.item((i, j)) and shift_dist < j):
            shift_dist = j
            break

for shift in range(28-shift_dist):
    img_shift = np.zeros((28, 28))
    img_shift[:, shift:shift_dist+shift] = img_arr[:, :shift_dist]
    plt.imshow(img_shift, cmap='gray', interpolation='none')
    plt.show()

# Original image
plt.imshow(img_arr, cmap='gray', interpolation='none')
plt.show()

# REPRODUCE_BY_SHIFTING_ABOVE
img_arr_trans = img_arr.transpose()
shift_dist = 27
for i in range(28):
    for j in range(28):
        if (threshold < img_arr_trans.item((i, j)) and j < shift_dist):
            shift_dist = j
            break

for shift in range(shift_dist):
    img_shift = np.zeros((28, 28))
    img_shift[:28-shift,:] = img_arr[shift:,:]
    plt.imshow(img_shift, cmap='gray', interpolation='none')
    plt.show()

# Original image
plt.imshow(img_arr, cmap='gray', interpolation='none')
plt.show()

# REPRODUCE_BY_SHIFTING_BELOW
shift_dist = 0
for i in range(28):
    for j in reversed(range(28)):
        if (threshold < img_arr_trans.item((i, j)) and shift_dist < j):
            shift_dist = j
            break

for shift in range(28-shift_dist):
    img_shift = np.zeros((28, 28))
    img_shift[shift:shift_dist+shift,:] = img_arr[:shift_dist,:]
    plt.imshow(img_shift, cmap='gray', interpolation='none')
    plt.show()