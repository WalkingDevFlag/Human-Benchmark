# Reaction Time Test Automation Script

## Overview
This Python script automates the Reaction Time test on Human Benchmark's website. It uses the following libraries:

- **selenium**: To control a web browser and navigate to the webpage.
- **mss**: To capture screenshots of the screen.
- **opencv (cv2)**: To display screenshots and process image data.
- **pyautogui**: To simulate mouse actions like clicking.
- **numpy**: For efficient array manipulations related to the screenshot data.

## How It Works
1. The script opens the Human Benchmark Reaction Time test page using Selenium.
2. It initializes a `ScreenGrabber` object to capture screen data.
3. The script continuously monitors a specified pixel's color to detect when the green "GO" signal appears on the page.
4. Once the green color is detected, it simulates a mouse click on the reaction test area to record the reaction time.
5. The script is designed to capture and analyze screen pixels to automate the clicking action based on color changes.

### ScreenGrabber Class:
- **`ScreenGrabber`** is a utility class that captures screenshots and retrieves pixel data for automation. 
- It can save screenshots and display them using OpenCV for debugging purposes.
- Allows fetching specific screen segments and pixel colors to monitor the changes in the Reaction Time test.

## Prerequisites
Ensure the following Python libraries are installed:

- selenium
- mss
- opencv-python (cv2)
- pyautogui
- numpy

You can install them via pip:

```bash
pip install selenium mss opencv-python pyautogui numpy
```

Additionally, make sure you have **ChromeDriver** installed and accessible from your system's PATH, as the script uses the Chrome browser for automation.

### Customization
- **Screen resolution adjustments**: In the `ScreenGrabber` initialization within `main.py`, adjust the `top_left_x`, `top_left_y_from_top`, `width`, and `height` values based on your screen resolution and the location of the Reaction Time test on your screen.
- **Pixel color detection**: Modify the `(x, y)` coordinates in the script to target different areas of the screen for detection, if needed.

## Future Enhancements (pls exclude)
Potential improvements for the script include:

- Adding more flexible methods for pixel location selection by interacting with the screen dynamically.
- Adding more robust error handling to deal with webpage loading issues.
- Incorporating dynamic support for multiple screen resolutions and monitor setups.
- Implementing logging for detailed performance tracking over multiple tests.

## License
This project is open-source and available under the MIT License.
