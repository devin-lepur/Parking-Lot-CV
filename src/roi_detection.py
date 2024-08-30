'''
File: roi_detection.py
Description: Automatically detect regions of interest (ROI) from empty parking lot images
Author: Devin Lepur
Date: 8/30/2024
'''
import cv2

# Pre-processing (maybe contrast adjustment, grayscale, and noise reduction)
def pre_process_image(input_image):
    """
    pre-process an input image to prepare for edge detection

    Params:
    input_image (numpy.ndarray): numpy array of an empty parking lot for auto ROI detection

    Returns:
    numpy.ndarray
    """
    grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Adjust contrast based on histogram distribution
    equil_image = cv2.equalizeHist(grayscale_image)

    # Reduce noise in the image
    guass_image = cv2.medianBlur(equil_image, 5)

    # CONSIDER ADDING color thresholds for difficulty detecting edges between paint and asphalt

    return guass_image


# Edge detection
def edge_detection(input_image):
    """
    Detect edges of 
    """
    # Set upper and lower threshold for selecting edges
    T_upper = 250
    T_lower = 100

    # Use Canny for edge detection
    edges_image = cv2.Canny(input_image, T_lower, T_upper)

    return edges_image


# Line detection like Hough Transform to detect straight lines representing parking spaces



# ROI Generation: based on lines, create rectangular ROIs to mark each space


# For testing and debugging purposes only
if __name__ == "__main__":
    # Read image
    image = cv2.imread("images/mostly_empty.jpg")

    # Preprocess image
    processed_image = pre_process_image(image)

    # Detect Edges
    edges_image = edge_detection(processed_image)

    # Output image
    cv2.imwrite("output/empty_test_output.jpg", edges_image)
