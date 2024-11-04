import pyautogui
import time
import keyboard

def compute_positions(top_left, bottom_right):
    width = (bottom_right[0] - top_left[0]) // 2
    height = (bottom_right[1] - top_left[1]) // 2

    positions_ = [
        (top_left[0], top_left[1]),
        (top_left[0] + width, top_left[1]),
        (bottom_right[0], top_left[1]),
        (top_left[0], top_left[1] + height),
        (top_left[0] + width, top_left[1] + height),
        (bottom_right[0], top_left[1] + height),
        (top_left[0], bottom_right[1]),
        (top_left[0] + width, bottom_right[1]),
        (bottom_right[0], bottom_right[1])
    ]

    return positions_

top_left_ = (1050, 500)
bottom_right_ = (1450, 900)

positions = compute_positions(top_left_, bottom_right_)


flash_list = []
last_flash_time = None

try:
    while True:
        for idx, pos in enumerate(positions):
            # If the position color is white
            if pyautogui.pixelMatchesColor(pos[0], pos[1], (255, 255, 255)):
                # Check if this position hasn't been added recently to avoid duplicate flashes
                if len(flash_list) == 0 or flash_list[-1] != idx:
                    flash_list.append(idx)
                    last_flash_time = time.time()
                    
        # If 3 seconds has passed since the last flash
        if last_flash_time and (time.time() - last_flash_time) >= 3:
            for idx in flash_list:
                pyautogui.click(positions[idx][0], positions[idx][1])

            flash_list.clear()
            last_flash_time = None

        time.sleep(0.2) # Check 10 times a second

except KeyboardInterrupt:
    print("Script terminated by the user.")
                                
'''
# Move the mouse to each position briefly as a visual marker
for pos in positions:
    pyautogui.moveTo(pos[0], pos[1], duration=0.2)
    # pyautogui.click()  # Optional click to mark each position
    time.sleep(2)  # Pause briefly at each point

print("Markers displayed at positions.")
'''
