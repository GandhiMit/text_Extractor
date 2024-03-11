import os
import time
import pygetwindow as gw
import pyautogui
from PIL import Image
import numpy as np
import easyocr


# Function to take a screenshot of the active browser window
def take_browser_screenshot():
    # Get the active browser window
    browser_window = gw.getActiveWindow()

    # Get the position and size of the browser window
    x, y, width, height = browser_window.left, browser_window.top, browser_window.width, browser_window.height

    # Capture the content of the browser window
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save('browser_screenshot.png')


# Function to extract text using OCR from the browser screenshot
def extract_text_from_browser_screenshot():
    reader = easyocr.Reader(['en'])
    image_path = 'browser_screenshot.png'

    # Open the image and convert it to a NumPy array
    image = np.array(Image.open(image_path))

    result = reader.readtext(image)

    # Extracted text is stored in result variable
    extracted_text = ' '.join([entry[1] for entry in result])

    return extracted_text


# Main script
try:
    # Take a screenshot of the active browser window
    take_browser_screenshot()

    # Wait for a moment to ensure the screenshot is saved
    time.sleep(1)

    # Extract text from the browser screenshot
    extracted_text = extract_text_from_browser_screenshot()

    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)

finally:
    # Cleanup: Close the image file and then delete it
    if os.path.exists('browser_screenshot.png'):
        image = Image.open('browser_screenshot.png')
        image.close()
        os.remove('browser_screenshot.png')
