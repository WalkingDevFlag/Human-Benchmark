# Number Memory Test Automation Script

## Overview

This Python script automates the Number Memory test on Human Benchmark's website. It utilizes the following libraries:

- **selenium**: To control a web browser and navigate to the webpage.
- **BeautifulSoup**: To scrape the number displayed on the page.
- **time**: To manage delays between actions.

## How It Works

1. The script opens the Human Benchmark Number Memory Test page using Selenium.
2. It waits for the page to load, then clicks the "Start" button to begin the test.
3. For a specified number of iterations, it:
   - Scrapes the number displayed on the page using BeautifulSoup.
   - Increases the delay before inputting the number with each iteration.
   - Simulates typing the number into the input field.
   - Clicks the "Submit" button to record the answer.
   - Proceeds to the next round by clicking the "NEXT" button.

## Prerequisites

Ensure that the following Python libraries are installed:

- **selenium**
- **beautifulsoup4**

You can install them via pip:

```bash
pip install selenium beautifulsoup4
```

Additionally, make sure you have ChromeDriver installed and accessible from your system's PATH, as the script uses the Chrome browser for automation.

## Future Enhancements

While the current implementation is functional, potential enhancements could include:

- Adding error handling to manage unexpected webpage loading issues.
- Allowing dynamic browser selection (currently supports only Chrome).
- Making the iteration count customizable via command-line arguments.
- Implementing logging to track performance over multiple runs.

## License

This project is open-source and available under the MIT License.
