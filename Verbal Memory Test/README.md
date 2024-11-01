# Verbal Memory Automation Script

## Overview
This Python script automates the Verbal Memory test on Human Benchmark's website. It utilizes the following libraries:

- **selenium**: To control a web browser and navigate to the webpage.
- **keyboard**: To listen for keypresses to start or stop the automation.

## How It Works
1. The script opens the Human Benchmark Verbal Memory test page using Selenium.
2. It waits for the user to press a designated start key (default: "p") to begin the automation.
3. The script identifies the "SEEN" and "NEW" buttons on the page to manage the input for each displayed word.
4. A set is used to store words that have already been encountered:
   - If the word has been seen before, the script clicks the "SEEN" button.
   - If the word is new, the script clicks the "NEW" button and adds the word to the set for tracking.
5. The loop runs until the user presses the start key ("p") again, allowing them to manually exit the automation.

## Prerequisites
Ensure the following Python libraries are installed:

- selenium
- keyboard
- webdriver_manager

You can install them via pip:

```bash
pip install selenium keyboard webdriver_manager
```

Additionally, ensure that ChromeDriver is installed. This can be managed automatically with `webdriver_manager`.

## Customization
- **Start Button**: You can change the start/stop button by modifying the `start_button` variable in the script.
- **Browser Choice**: This script uses Chrome by default. To use a different browser, update the `webdriver.Chrome()` line to your preferred browser and make sure the appropriate driver is installed.

## License
This project is open-source and available under the MIT License.
