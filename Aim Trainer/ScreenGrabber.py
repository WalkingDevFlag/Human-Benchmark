import numpy as np
import cv2
import time
import screeninfo
from mss import mss
import os

class ScreenGrabber:
    def __init__(self, top_left_x, top_left_y_from_top, width, height):
        self.screen_shot = None
        monitor_number = 1

        with mss() as sct:
            mon = sct.monitors[monitor_number]
            self.monitor = {
                "top": mon["top"] + top_left_y_from_top,
                "left": mon["left"] + top_left_x,
                "width": width,
                "height": height,
                "mon": monitor_number
            }


    def take_screen_shot(self):
        with mss() as sct:
            sct_img = sct.grab(self.monitor)
            self.screen_shot = np.array(sct_img)

    def setup_screen_output(self, output_monitor_number, output_window_position_offset_x, output_window_position_offset_y):
        monitors = screeninfo.get_monitors()
        self.target_output_monitor = monitors[output_monitor_number]

        cv2.namedWindow("Hello", cv2.WINDOW_NORMAL)
        cv2.moveWindow("Hello", self.target_output_monitor.x + output_window_position_offset_x, self.target_output_monitor.y + output_window_position_offset_y)

    def show_screen_shot(self):
        cv2.imshow("Hello", self.screen_shot)
        cv2.waitKey(1)

    def save_screenshot(self):
        os.makedirs('screenshots', exist_ok=True)
        cv2.imwrite('screenshots/image.jpg', self.screen_shot)

    def get_pixel(self, x, y):
        return self.screen_shot[y][x]

    def get_screenshot_segment(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        screen_shot_segment = self.screen_shot[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
        return screen_shot_segment
