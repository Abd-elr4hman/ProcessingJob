import os
from os.path  import join
import logging
import argparse

import boto3
import idx2numpy
import numpy as np

s3 = boto3.client("s3")
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def process_data(
        input_data_path,
        output_data_path,
        x_train_key,
        y_train_key,
        x_test_key,
        y_test_key
        ):
    """
    A function to process mnist data raw files into numpy arrays for training.

    Args:
        x_train_key: raw mnist training images byte file key in s3.
        y_train_key: raw mnist training labeles byte file key in s3.
        x_test_key: raw mnist testing images byte file key in s3.
        y_test_key: raw mnist testing labels byte file key in s3.
    """

    # create file paths
    training_images_filepath = join(input_data_path, x_train_key)
    training_labels_filepath = join(input_data_path, y_train_key)
    test_images_filepath = join(input_data_path, x_test_key)
    test_labels_filepath = join(input_data_path, y_test_key)

    # convert byte files to numpy arrays
    x_train = idx2numpy.convert_from_file(training_images_filepath)
    y_train = idx2numpy.convert_from_file(training_labels_filepath)
    x_test = idx2numpy.convert_from_file(test_images_filepath)
    y_test = idx2numpy.convert_from_file(test_labels_filepath)

    # save the processed data into the directory specified to the sagemaker processing job
    np.savez(output_data_path, x_test=x_test, x_train=x_train, y_train=y_train, y_test=y_test)
    logging.info("Saved numpy file successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    INPUT_DATA_PATH = os.path.join("/opt/ml/processing/input")
    X_TRAIN_KEY= "train-images.idx3-ubyte"
    Y_TRAIN_KEY= "train-labels.idx1-ubyte"
    X_TEST_KEY= "t10k-images.idx3-ubyte"
    Y_TEST_KEY= "t10k-labels.idx1-ubyte"
    
    OUTPUT_DATA_PATH = os.path.join("/opt/ml/processing/output", "mnist.npz")
    process_data(
        INPUT_DATA_PATH,
        OUTPUT_DATA_PATH,
        X_TRAIN_KEY,
        Y_TRAIN_KEY,
        X_TEST_KEY,
        Y_TEST_KEY
        )
