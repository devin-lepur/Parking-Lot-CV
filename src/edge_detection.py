'''
Test file to test github CI
'''

import cv2
import os

def edge_detection(input_path, output_path):
    # Load the image
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Perform edge detection using Canny
    edges = cv2.Canny(image, 100, 200)

    # Save the output image
    cv2.imwrite(output_path, edges)

if __name__ == "__main__":
    input_image = "images/input.jpg"
    output_image = "output/edges.jpg"
    edge_detection(input_image, output_image)