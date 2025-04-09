import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt

def create_small_filter():
    return np.ones((3, 3)) / 9

def create_large_filter():
    return np.ones((15, 15)) / (15*15)

def process_image(input_file):
    img = plt.imread(input_file)
    small_filter = create_small_filter()
    large_filter = create_large_filter()
    small_result = sim.convolve(img, small_filter)
    large_result = sim.convolve(img, large_filter)
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 3, 2)
    plt.imshow(small_result, cmap='gray')
    plt.title('3×3 Filter Result')
    plt.subplot(1, 3, 3)
    plt.imshow(large_result, cmap='gray')
    plt.title('15×15 Filter Result')
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    process_image('data/bwCat.tif')
