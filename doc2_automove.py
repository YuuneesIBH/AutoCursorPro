import pyautogui
import time

# ENKEL HIER AANPASSEN: gebruik get-mouse-position.py om de coordinaten te vinden en pas deze hieronder aan
coordinaten = {
    "initial": (-1446, -1779),
    "constant_x": -1889,
    "start_y": -1723,
    "step_y": 103,
    "steps": 14,
    "final": (-2228, -1065),
}

print("Bezig met uitvoeren... Beweeg de muis handmatig buiten de coördinaten om het script te stoppen.")
def beweeg_en_check(x, y, duur=0.2):
    pyautogui.moveTo(x, y, duration=duur)
    huidige_x, huidige_y = pyautogui.position()
    if abs(huidige_x - x) > 5 or abs(huidige_y - y) > 5:
        print(f"\nMuisafwijking gedetecteerd bij X: {huidige_x}, Y: {huidige_y}. Script gestopt.")
        raise KeyboardInterrupt

try:
    aantal_cycli = int(input("Hoeveel cycli wil je uitvoeren? "))
    if aantal_cycli <= 0:
        print("Aantal cycli moet minimaal 1 zijn.")
        exit()

    for cyclus in range(aantal_cycli):
        print(f"Start cyclus {cyclus + 1} van {aantal_cycli}...")

        beweeg_en_check(*coordinaten["initial"], duur=1.2)
        pyautogui.click()

        beweeg_en_check(coordinaten["constant_x"], coordinaten["start_y"])
        
        for i in range(coordinaten["steps"]):
            current_y = coordinaten["start_y"] + i * coordinaten["step_y"]
            beweeg_en_check(coordinaten["constant_x"], current_y)
            pyautogui.click()

        beweeg_en_check(coordinaten["constant_x"], current_y, duur=1.5)
        pyautogui.mouseDown()
        beweeg_en_check(*coordinaten["final"], duur=0.3)
        pyautogui.mouseUp()

        print("Cyclus voltooid.")

    print("Alle cycli voltooid!")

except ValueError:
    print("Ongeldige invoer. Voer een geheel getal in.")
except KeyboardInterrupt:
    print("\nScript gestopt door gebruiker of muisafwijking.")