import pyautogui
import cv2
import numpy as np
import time
import pydirectinput



def screenshot():
    # x496, y300
    # x1334, y778
    image = pyautogui.screenshot(region=(496, 300, 838, 478))
    image.save("screenshot.png")

def find_object_on_screen(template_path, screenshot):
    # Read the template (target) image and the screenshot.
    template = cv2.imread(template_path)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Use template matching to find the object in the screenshot.
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Set a threshold for similarity (adjust as needed).
    threshold = 0.4
    if max_val >= threshold:
        # The object is found, and max_loc contains its top-left corner coordinates.
        # Calculate the center of the object.
        object_center = (max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2)
        return object_center
    
    return None

def click_object(position):
    x, y = position
    # move the mouse to the center of the object and click it.
    pydirectinput.moveTo(x, y)
    pydirectinput.doubleClick()



while True:
    # If keyboard interr
    time.sleep(1)
    screenshot()
    read_screenshot = cv2.imread("screenshot.png")
    template_path = "target2.png"

    result = find_object_on_screen(template_path, read_screenshot)

    if result is not None:
        print("Found target.")
        # Result needs to be offset by the region coordinates. 1920x1080 screen.
        print("Target location: " + str(result[0] + 496) + ", " + str(result[1] + 300))
        click_object((result[0] + 496, result[1] + 300))

    else:
        print("Target not found.")
    
    # Wait 1 second before trying again.
