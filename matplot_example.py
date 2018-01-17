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
plt.imshow(img_arr, cmap='gray', interpolation='none')
plt.show()

# REPRODUCE_BY_BLURRING
# algorithm_design
# initialization of noise
noise = np.zeros((28, 28))

# examine all entries
for i in range(28):
    for j in range(28):
        temp = img_arr.item((i, j))
        # first_row
        if (i == 0):
            # detect nonzero entry
            if (temp > 0):
                # add noise
                noise[i+1,j] += temp*np.random.random()
                if (j > 0):
                    noise[i,j-1] += temp*np.random.random()
                    noise[i+1,j-1] += temp*np.random.random()
                if (j < 27):
                    noise[i,j+1] += temp*np.random.random()
                    noise[i+1,j+1] += temp*np.random.random()
        # last_row
        elif (i == 27):
            # detect nonzero entry
            if (temp > 0):
                # add noise
                noise[i-1,j] += temp*np.random.random()
                if (j > 0):
                    noise[i,j-1] += temp*np.random.random()
                    noise[i-1,j-1] += temp*np.random.random()
                if (j < 27):
                    noise[i,j+1] += temp*np.random.random()
                    noise[i-1,j+1] += temp*np.random.random()
        # others
        else:
            # detect nonzero entry
            if (temp > 0):
                # add noise
                noise[i-1,j] += temp*np.random.random()
                noise[i+1,j] += temp*np.random.random()
                if (j > 0):
                    noise[i-1,j-1] += temp*np.random.random()
                    noise[i,j-1] += temp*np.random.random()
                    noise[i+1,j-1] += temp*np.random.random()
                if (j < 27):
                    noise[i-1,j+1] += temp*np.random.random()
                    noise[i,j+1] += temp*np.random.random()
                    noise[i+1,j+1] += temp*np.random.random()


print(noise)
print('\n\n conversion \n\n')

for i in range(28):
    for j in range(28):
        if (noise.item((i,j)) > 1):
            noise[i,j] = 1

print(noise)

img_noise = img_arr + noise
plt.imshow(img_noise, cmap='gray', interpolation='none')
plt.show()

print(img_noise.shape[0])
print(img_noise.shape[1])

