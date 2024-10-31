# Aim Trainer Automation Script

## Overview
This Python script automates the Aim Trainer test on Human Benchmark's website. It utilizes the following libraries:

- **selenium**: To control a web browser and navigate to the webpage.
- **mss**: To capture screenshots of the screen.
- **opencv (cv2)**: To process image data and detect targets.
- **numpy**: For efficient array manipulations related to the screenshot data.
- **pywin32**: To simulate mouse actions like clicking.

## How It Works
1. The script opens the Human Benchmark Aim Trainer page using Selenium.
2. It initializes a `ScreenGrabber` object to capture screen data.
3. The script continuously takes screenshots of a specified area of the screen and processes the images to detect white circular targets.
4. Once a target is detected, it simulates a mouse click at the target's coordinates.
5. The script is designed to automate the clicking action based on visual detection of targets appearing on the screen.

## ScreenGrabber Class
The `ScreenGrabber` class is a utility that captures screenshots and retrieves pixel data for automation tasks.
- It can save screenshots and display them using OpenCV for debugging purposes.
- It allows fetching specific screen segments and pixel data to monitor changes in the Aim Trainer test.

## Prerequisites
Ensure the following Python libraries are installed:

- selenium
- mss
- opencv-python (cv2)
- numpy
- pywin32

You can install them via pip:

```bash
pip install selenium mss opencv-python numpy pywin32
```

Additionally, ensure that ChromeDriver is installed and accessible from your system's PATH, as the script uses the Chrome browser for automation.

## Customization
- **Screen resolution adjustments**: In the `ScreenGrabber` initialization within the script, adjust the `top_left_x`, `top_left_y_from_top`, `width`, and `height` values based on your screen resolution and the location of the Aim Trainer test on your screen.
- **Target detection settings**: Modify the target detection parameters in the `detect_white_circle_center` function if you need to fine-tune the detection process for different conditions.

## License
This project is open-source and available under the MIT License.
