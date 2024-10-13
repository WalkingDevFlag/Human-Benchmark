# Monkeytype Typing Automation Script

## Overview
This Python script automates typing on the [Monkeytype](https://monkeytype.com) website. It uses the following libraries:

- `selenium` to control a web browser and load the webpage.
- `BeautifulSoup` to scrape the text required for the typing test.
- `pyautogui` to simulate keystrokes and automate the typing of the extracted text.

## How It Works
1. The script opens the Monkeytype typing test page using `selenium`.
2. It waits for the page to load (with a delay of 10 seconds).
3. Using `BeautifulSoup`, it scrapes the words from the typing test.
4. The script then uses `pyautogui` to simulate typing the extracted text at a specified interval.

## Prerequisites
Ensure that the following Python libraries are installed:

- `selenium`
- `beautifulsoup4`
- `pyautogui`

You can install them via `pip`:

```bash
pip install selenium beautifulsoup4 pyautogui
```

### Additional Requirements
- You need to have `ChromeDriver` installed and accessible from your system's PATH, as the script uses Chrome for automation. Download it from [ChromeDriver](https://chromedriver.chromium.org/downloads) and ensure it matches your installed Chrome version.

## Future Enhancements
- Add error handling for cases where the text cannot be extracted due to website layout changes.
- Improve typing accuracy by adding a randomized delay between keystrokes to mimic human typing.
- Make the browser selection customizable (currently only supports Chrome).
- Add a feature to handle dynamic page load times more effectively.

## License
This project is open-source and available under the MIT License.
