# Typing Test Automation Script

## Overview

This Python script automates the typing test on [Human Benchmark's Typing Test](https://humanbenchmark.com/tests/typing). It uses the following libraries:

- `selenium` to control a web browser and load the webpage.
- `BeautifulSoup` to scrape the text required for the typing test.
- `pyautogui` to simulate keystrokes and automate typing of the extracted text.

## How It Works

1. The script opens the Human Benchmark Typing Test page using `selenium`.
2. It waits for the page to load (with a delay of 10 seconds).
3. Using `BeautifulSoup`, it scrapes the text that needs to be typed from the webpage.
4. The script then uses `pyautogui` to simulate typing the text automatically into the input field of the test.

## Prerequisites

Ensure that the following Python libraries are installed:
- `selenium`
- `beautifulsoup4`
- `pyautogui`

You can install them via `pip`:

```bash
pip install selenium beautifulsoup4 pyautogui
```

Additionally, make sure that you have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and accessible from your system's PATH, as the script uses the Chrome browser for automation.


## Future Enhancements

- Personally i dont feel any need to enhance this program but increase the 14k wpm record ig
- Add error handling to manage unexpected webpage loading issues.
- Allow dynamic browser selection (currently supports only Chrome).
- Make the delay time customizable or dynamic based on the page load time.

## License

This project is open-source and available under the MIT License.
