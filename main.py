import pyautogui

def screenshot():
    # x496, y300
    # x1334, y778
    image = pyautogui.screenshot(region=(496, 300, 838, 478))
    image.save("screenshot.png")



