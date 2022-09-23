from matplotlib import image
from matplotlib import pyplot
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
flagname = path + '/' + 'flag-square-500.png'
lenna = image.imread(filename)
flag = image.imread(flagname)*255

print(flag.shape)
print(flag.shape[0]) #0 is height, 1 is width

plot_lenna = lenna.copy()

plot_lenna[:flag.shape[0], lenna.shape[1]-flag.shape[1]:,:] = flag[:, :,0:3]

#for width in range(flag.shape[1]):
    #for height in range(flag.shape[0]):
        #plot_lenna[height, width+12,:] = flag[height, width,0:3]

pyplot.imshow(plot_lenna)
pyplot.show()
