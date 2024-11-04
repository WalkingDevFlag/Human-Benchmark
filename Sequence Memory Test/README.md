# Flash Memory Automation Script

## Overview
This Python script automates a Flash Memory test by detecting white flashes on a 3x3 grid of squares, clicking on squares in the sequence that they light up. It uses `pyautogui` to detect color and simulate mouse clicks, allowing the script to run in a simple automation setup.

## How It Works
1. **Grid Position Calculation**:
   - The grid's top-left and bottom-right coordinates are provided as inputs.
   - The `compute_positions` function then divides this grid into 9 equally spaced positions (3x3 layout), returning the coordinates for each square.

2. **White Flash Detection**:
   - In the main loop, the script continuously checks if any of the 9 positions contain a white pixel (RGB value `(255, 255, 255)`).
   - If a position is white, its index is appended to `flash_list`, recording the sequence of flashes.

3. **Automated Clicking**:
   - If three seconds have passed since the last flash detection, the script clicks each recorded position in `flash_list` in sequence to replay the flash pattern.
   - After clicking, `flash_list` is cleared, ready to record a new sequence.

4. **Continuous Loop**:
   - The main loop continues to run, checking for flashes every 0.2 seconds.
   - The program can be terminated manually with a keyboard interrupt (Ctrl+C).

## Prerequisites
Ensure that the following Python library is installed:
```bash
pip install pyautogui
```

## Customization
- **Grid Positions**: Update `top_left_` and `bottom_right_` coordinates to specify the area of your grid.
- **Flash Timing**: Adjust `time.sleep()` in the main loop to change the frequency of flash checks.

## Usage
1. Run the script. 
2. Once active, the script will detect white flashes on the screen and click corresponding squares after a 3-second interval.

## Optional Visual Markers
There is an optional section in the script (commented out) that moves the mouse briefly to each grid position as a visual marker. Uncomment to use:
```python
# Move the mouse to each position briefly as a visual marker
for pos in positions:
    pyautogui.moveTo(pos[0], pos[1], duration=0.2)
    time.sleep(2)  # Pause at each point for visibility
```

## License
This project is open-source and available under the MIT License.
