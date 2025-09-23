#!/usr/bin/env python3
#shebang line for linux / mac

from copy import deepcopy
import glob
import cv2  # import the opencv Library
import numpy as np

# main function, where our code should be
def main():
    print("python main function")

    dataset_path = '/home/mike/GoogleDrive/UA/Aulas/2025-2026/1ºSem/SAVI_25-26/savi_25-26/Parte02/cat_dog_savi'

    # Check all image filenames in disk
    image_filenames = glob.glob(dataset_path + "/*.jpeg")
    image_filenames.sort()
    print(image_filenames)

    # Read all images | initialize an empty image list
    images = []
    for image_filename in image_filenames:
        image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
        images.append(image)

    # Show all images
    # for image in images:
    #     cv2.imshow('Image X', image)
    #     cv2.waitKey(0)

    # Read the labels file
    labels_filename = '/home/mike/GoogleDrive/UA/Aulas/2025-2026/1ºSem/SAVI_25-26/savi_25-26/Parte02/cat_dog_savi/labels.txt'
    file_handle = open(labels_filename)
    labels = []
    for line in file_handle:
        print(line)
        labels.append(line)

    print('labels = ' + str(labels))

    exit(0)

   
if __name__ == "__main__":
    main()
