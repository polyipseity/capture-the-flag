from matplotlib import pyplot
import tifffile

im = tifffile.imread("aura.tif", maxworkers=6)
binsize = 25
height = im.shape[1]  # binsize
width = im.shape[2]  # binsize
im = im[:, : height * binsize, : width * binsize]
im = im.reshape(im.shape[0], height, binsize, width, binsize)
im = im.sum((0, 2, 4), dtype="uint32")

pyplot.imshow(im, cmap="gray")
pyplot.show()
