import cPickle as pkl
import glob
import os

import numpy as np
from skimage.io import imsave


# PIXELS_DIR = "pixel_data"
PIXELS_DIR = "DIR_TO_SAVE_THE_IMAGE_DATA"
LABEL_FILE = "../test_labels.txt"


def unpack_file(fname):
    """
        Unpacks a CIFAR-100 file.
    """

    with open(fname, "r") as f:
        result = pkl.load(f)

    return result


def save_as_image(img_flat, fname):
    """
        Saves a data blob as an image file.
    """

    # consecutive 1024 entries store color channels of 32x32 image
    img_R = img_flat[0:1024].reshape((32, 32))
    img_G = img_flat[1024:2048].reshape((32, 32))
    img_B = img_flat[2048:3072].reshape((32, 32))
    img = np.dstack((img_R, img_G, img_B))

    imsave(os.path.join(PIXELS_DIR, fname), img)


def main():
    """
        Entry point.
    """

    labels = {}

    # use "data_batch_*" for just the training set
    for fname in glob.glob("../cifar-100-python/test"):
        data = unpack_file(fname)

        for i in range(10000):
            img_flat = data["data"][i]
            fname = data["filenames"][i]
            fine_label = data["fine_labels"][i]
            coarse_label = data["coarse_labels"][i]

            # save the image and store the label
            save_as_image(img_flat, fname)
            labels[fname] = str(coarse_label) + " " + str(fine_label)

    # write out labels file
    with open(LABEL_FILE, "w") as f:
        for (fname, label) in labels.iteritems():
            f.write("{0} {1}\n".format(fname, label))


if __name__ == "__main__":
    main()
