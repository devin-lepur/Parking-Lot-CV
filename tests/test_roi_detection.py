'''
File: test_roi_detection.py
Description: test roi detection file
Author: Devin Lepur
Date: 8/30/2024
'''

import os
import cv2

from src.roi_detection import pre_process_image, edge_detection

def test_pre_process_image():
    input_image = "tests/input_test.jpg"
    output_image = "tests/output_test.jpg"

    # Check if output image already exists and delete if so
    if os.path.exists(output_image):
        os.remove(output_image)

    # Run preprocessing and write to output
    input_image = cv2.imread(input_image)
    processed_image = pre_process_image(input_image)
    cv2.imwrite(output_image, processed_image)


    assert os.path_exists(output_image), "Pre-process image was not created"

def test_edge_detection():
    input_image = "tests/input_test.jpg"
    output_image = "tests/output_test.jpg"

    # Check if output image already exists and delete if so
    if os.path.exists(output_image):
        os.remove(output_image)

    # Run preprocessing and edge detection and write to output
    input_image = cv2.imread(input_image)
    processed_image = pre_process_image(input_image)
    edges_image = edge_detection(processed_image)
    cv2.imwrite(output_image, edges_image)


    assert os.path_exists(output_image), "Edge detection image was not created"

