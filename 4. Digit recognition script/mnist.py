#import the following python libraries:
import gzip
# In shell, run pip install image..
from PIL import Image #image library
import numpy as np 

# Download the image and label files. 
# Have Python decompress and read them byte by byte into appropriate data structures in memory.

#function to read label files
def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as f: #use gzip to open the file in read binary mode
        magic = f.read(4) # magic number is the first 4 bytes
        magic = int.from_bytes(magic,'big') # Convert bytes to integers.
        print("Magic Number:", magic) # print to console

        # the same as above but with labels
        labelN = f.read(4)
        labelN = int.from_bytes(labelN,'big')
        print("Labels:", labelN)
        # for looping through labels
        labels = [f.read(1) for i in range(labelN)]
        labels = [int.from_bytes(label, 'big') for label in labels]
    return labels
print()
train_labels = read_labels_from_file("train-labels-idx1-ubyte.gz")
test_labels = read_labels_from_file("t10k-labels-idx1-ubyte.gz")