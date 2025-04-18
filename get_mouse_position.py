import pyautogui
import time

print("Beweeg je muis naar de juiste locatie en druk op CTRL+C om te stoppen.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nEindlocatie vastgelegd.")