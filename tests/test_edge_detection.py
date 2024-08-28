'''
Test file for edge detection
'''

import cv2
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.edge_detection import edge_detection

def test_edge_detection():
    input_image = "tests/input_test.jpg"
    output_image = "tests/output_tests.jpg"

    edge_detection(input_image, output_image)
    
    assert os.path.exists(output_image), "Output image was not created"