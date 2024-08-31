'''
File: roi_detection.py
Description: Automatically detect regions of interest (ROI) from empty parking lot images
Author: Devin Lepur
Date: 8/30/2024
'''


import cv2
import numpy as np
import math

from src.color_mask import get_color_mask, apply_color_mask, convert_to_hsv

# Pre-processing (maybe contrast adjustment, grayscale, and noise reduction)
def pre_process_image(input_image):
    """
    pre-process an input image to prepare for edge detection

    Params:
    input_image (numpy.ndarray): numpy array of an empty parking lot for auto ROI detection

    Returns:
    numpy.ndarray
    """
    # Create grayscale of the image
    grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Create CLAHE object and apply to the image
    clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(30,30))
    equil_image = clahe.apply(grayscale_image)

    # Reduce noise in the image
    bilateral_image = cv2.bilateralFilter(equil_image, d=9, sigmaColor=50, sigmaSpace=50)

    return bilateral_image


# Edge detection
def edge_detection(input_image):
    """
    Detect edges of a preprocessed image

    Params:
    input_image (numpy.ndarray): nump.ndarray of a preprocessed image

    Returns:
    COMPLETE THIS
    """
    # Set upper and lower threshold for selecting edges
    T_upper = 50
    T_lower = 150

    # Use Canny for edge detection
    edges_image = cv2.Canny(input_image, T_lower, T_upper, L2gradient=True)

    return edges_image


def line_detection(input_image, original_image):
    """
    Detect lines in the edge-detected image and draw them on the original image.

    Params:
    input_image (numpy.ndarray): Binary edge-detected image.
    original_image (numpy.ndarray): Original image for drawing lines.

    Returns:
    numpy.ndarray: Image with detected lines drawn.
    """
    # Use Probabilistic Hough Transform to detect line segments
    lines = cv2.HoughLinesP(input_image, 1, np.pi/180, 50, minLineLength=50, maxLineGap=10)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(original_image, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)

    return original_image





# ROI Generation: based on lines, create rectangular ROIs to mark each space




# For testing and debugging purposes only
if __name__ == "__main__":
    # Read image
    image = cv2.imread("images/empty_lot_1.jpg")

    # Convert to HSV
    hsv_image = convert_to_hsv(image)

    # Get color mask
    color_mask = get_color_mask(hsv_image)

    # Apply the mask to the original image
    masked_image = apply_color_mask(image, color_mask)

    # Preprocess the masked image
    processed_image = pre_process_image(masked_image)

    # Detect edges
    edges_image = edge_detection(processed_image)

    # Run line detection
    line_image = line_detection(edges_image, image)

    # Output images
    cv2.imwrite("output/empty_lot_1_masked_output.jpg", masked_image)
    cv2.imwrite("output/empty_lot_1_pre_output.jpg", processed_image)
    cv2.imwrite("output/empty_lot_1_edges_output.jpg", edges_image)
    cv2.imwrite("output/empty_lot_1_line_output.jpg", line_image)
