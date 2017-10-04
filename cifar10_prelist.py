import cPickle as cpk
import glob
import os
import numpy as np

def unpack_file(fname):
    """
        Unpacks a CIFAR-10 file.
    """

    with open(fname, "r") as f:
        result = cpk.load(f)

    return result

def main():
    """
        Entry point.
    """

    for fname in glob.glob("../cifar-10-batches-py/*_batch*"):
        data = unpack_file(fname)
        info = data['batch_label'].split(" ")
        filelist = info[0] + "_" + info[2]

        with open(os.path.join("../", filelist), "w") as sfh:
            for i in range(len(data['labels'])):
                img_name = data['filenames'][i]
                label = data['labels'][i]
                sfh.write("{0} {1}\n".format(img_name, label))

if __name__ == "__main__":
    main()
