import sys

import os
import processing as p

import numpy as np


def test_process_data():
    INPUT_DATA_PATH = os.path.join("data/input")
    
    X_TRAIN_KEY= "train-images.idx3-ubyte"
    Y_TRAIN_KEY= "train-labels.idx1-ubyte"
    X_TEST_KEY= "t10k-images.idx3-ubyte"
    Y_TEST_KEY= "t10k-labels.idx1-ubyte"
    
    os.mkdir("data/output")
    OUTPUT_DATA_PATH = os.path.join("data/output", "mnist.npz")
    p.process_data(
        INPUT_DATA_PATH,
        OUTPUT_DATA_PATH,
        X_TRAIN_KEY,
        Y_TRAIN_KEY,
        X_TEST_KEY,
        Y_TEST_KEY
        )
    
    dataset = np.load(OUTPUT_DATA_PATH)
     
    assert list(dataset.keys()) == ['x_test', 'x_train', 'y_train', 'y_test']


