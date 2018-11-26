#import the following python libraries:
import gzip
from PIL import Image #image library
import numpy as np 

# Reference
# https://docs.python.org/3/library/gzip.html
# https://www.youtube.com/watch?v=oYndcjlzwX8

# File is broken into 4 parts for notebook number 5 describing this file

# Part one
# function to read label files. Adapted from notebook 3.
def read_labels(filename):
    with gzip.open(filename,'rb') as f: # use gzip to open the file
        magic = f.read(4) # magic number is the first 4 bytes
        magic = int.from_bytes(magic,'big') # Convert bytes to integers.
        print("Magic Number:", magic) # print to console

        labelN = f.read(4) #label bytes
        labelN = int.from_bytes(labelN,'big') # Convert
        print("Labels:", labelN)

        # for looping through labels
        labels = [f.read(1) for i in range(labelN)]
        labels = [int.from_bytes(label, 'big') for label in labels]
    return labels
print() # line break
train_labels = read_labels("train-labels-idx1-ubyte.gz")
test_labels = read_labels("t10k-labels-idx1-ubyte.gz")

# Part two
# function to read image files. Adapted from notebook 3.
def read_images(filename):
    with gzip.open(filename,'rb') as f:
        magic = f.read(4) # magic number is the first 4 bytes
        magic = int.from_bytes(magic,'big') # Convert bytes to int
        print("Magic Number:", magic)

        imgN = f.read(4) # Number of images in next 4 bytes
        imgN = int.from_bytes(imgN,'big')
        print("Image:", imgN)

        rowN = f.read(4) # Number of rows in next 4 bytes
        rowN = int.from_bytes(rowN,'big')
        print("Rows:", rowN)
    
        colN = f.read(4) # Number of columns in next 4 bytes
        colN = int.from_bytes(colN,'big')
        print("Columns:", colN)

        images = [] # create array for images
        #for loop
        for i in range(imgN): #images
            rows = [] # rows array
            for r in range(rowN): # rows
                cols = [] # columns array
                for c in range(colN): # columns
                    cols.append(int.from_bytes(f.read(1), 'big')) # append the current byte for every column
                rows.append(cols) # append columns array for every row
            images.append(rows) # append rows for every image
    return images
    # append Updates the list by adding an object to the list. append(): It is basically used in Python to add one element.
print() #line break

# Part three
# Call the functions and run them to read the files
train_images = read_images("train-images-idx3-ubyte.gz")
test_images = read_images("t10k-images-idx3-ubyte.gz")

# Part four
# Download the image and label files. 
img = Image.fromarray(np.array(train_images[750]).astype(np.uint8)) # Have Python decompress and read them byte by byte into appropriate data structures in memory.
img = img.convert('RGB') 
img.show() # show image in paint or photo application
img.save('train-750-7.png') # save image as png