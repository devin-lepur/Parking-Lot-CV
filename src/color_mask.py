'''
File: color_mask.py
Description: Apply a color mask to the image based on common lot lines
Author: Devin Lepur
Date: 8/30/2024
'''


import cv2
import numpy as np

def convert_to_hsv(image):
    """
    Convert the BGR image to the HSV color space.

    Params:
    image (numpy.ndarray): Input BGR image.

    Returns:
    numpy.ndarray: Image in HSV color space.
    """
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image



def get_color_mask(hsv_image):
    """
    Create a mask for the specific colors of the parking lines (yellow and white).

    Params:
    hsv_image (numpy.ndarray): Image in HSV color space.

    Returns:
    numpy.ndarray: Binary mask isolating the color of the parking lines.
    """
    # Define range for yellow color
    yellow_lower = np.array([18, 100, 100], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)

    # Define range for white color
    white_lower = np.array([0, 0, 200], np.uint8)
    white_upper = np.array([180, 30, 255], np.uint8)

    #TODO: Define range for blue color (Handicap)



    # Create masks for the colors
    yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    white_mask = cv2.inRange(hsv_image, white_lower, white_upper)

    # Combine masks
    color_mask = cv2.bitwise_or(yellow_mask, white_mask)

    return color_mask



def apply_color_mask(image, color_mask):
    """
    Apply the color mask to the original image.

    Params:
    image (numpy.ndarray): Original image.
    color_mask (numpy.ndarray): Binary mask of the desired colors.

    Returns:
    numpy.ndarray: Image with only the masked colors.
    """
    masked_image = cv2.bitwise_and(image, image, mask=color_mask)
    return masked_image
