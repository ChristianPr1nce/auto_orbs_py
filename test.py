import cv2
import numpy as np

def find_object_on_screen(template_path, screenshot):
    template = cv2.imread(template_path, 0)
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Set a threshold for similarity (adjust as needed).
    threshold = 0.8
    if max_val >= threshold:
        # Calculate the center point of the detected object.
        h, w = template.shape
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y)
    else:
        return None

screenshot = cv2.imread("sc1.png")
template_path = "target1.png"

result = find_object_on_screen(template_path, screenshot)

