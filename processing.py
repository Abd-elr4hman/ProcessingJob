import boto3
import idx2numpy
import numpy as np
from os.path  import join

import logging
from botocore.exceptions import ClientError
import os

import argparse


s3 = boto3.client("s3")

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)



def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True





def process_data(input_path, x_train_key, y_train_key, x_test_key, y_test_key):
    """
    A function to process mnist data raw files into numpy arrays for training.

    Args:
        x_train_key: raw mnist training images byte file key in s3.
        y_train_key: raw mnist training labeles byte file key in s3.
        x_test_key: raw mnist testing images byte file key in s3.
        y_test_key: raw mnist testing labels byte file key in s3.
    """
    # s3.download_file(
    #     "training-data-sagemaker-tensorflow-mnist",
    #     s3_path + x_train_key,
    #     x_train_key
    # )
    # logging.info("Dowloaded training images file successfully")


    # s3.download_file(
    #     "training-data-sagemaker-tensorflow-mnist",
    #     s3_path + y_train_key,
    #     y_train_key
    # )
    # logging.info("Dowloaded training labels file successfully")

    # s3.download_file(
    #     "training-data-sagemaker-tensorflow-mnist",
    #     s3_path + x_test_key,
    #     x_test_key
    # )
    # logging.info("Dowloaded testing images file successfully")

    # s3.download_file(
    #     "training-data-sagemaker-tensorflow-mnist",
    #     s3_path + y_test_key,
    #     y_test_key
    # )
    # logging.info("Dowloaded testing labels file successfully")

    # input_path = ''

    training_images_filepath = join(input_path, x_train_key)
    training_labels_filepath = join(input_path, y_train_key)
    test_images_filepath = join(input_path, x_test_key)
    test_labels_filepath = join(input_path, y_test_key)


    x_train = idx2numpy.convert_from_file(training_images_filepath)
    y_train = idx2numpy.convert_from_file(training_labels_filepath)
    x_test = idx2numpy.convert_from_file(test_images_filepath)
    y_test = idx2numpy.convert_from_file(test_labels_filepath)


    train_output_path = os.path.join("/opt/ml/processing/output", "mnist.npz")
    np.savez(train_output_path, x_test=x_test, x_train=x_train, y_train=y_train, y_test=y_test)
    logging.info("Saved numpy file successfully")


    # upload_file("mnist.npz", "training-data-sagemaker-tensorflow-mnist","processing_output/mnist.npz")
    # logging.info("uploaded numpy file to s3 successfully")
    


if __name__ == "__main__":


    parser = argparse.ArgumentParser()

    input_data_path = os.path.join("/opt/ml/processing/input")
    

    # s3_path = "processing_input/"
    x_train_key= "train-images.idx3-ubyte"
    y_train_key= "train-labels.idx1-ubyte"
    x_test_key= "t10k-images.idx3-ubyte"
    y_test_key= "t10k-labels.idx1-ubyte"
    process_data(input_data_path, x_train_key, y_train_key, x_test_key, y_test_key)