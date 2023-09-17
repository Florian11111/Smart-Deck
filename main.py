import serial
import subprocess
import pyautogui

ser = serial.Serial('COM3', 9600) # Passe 'COM3' entsprechend deinem Arduino an

while True:
    data = ser.readline().decode('utf-8').strip() # Lese die Daten von der seriellen Schnittstelle
    launcher_paint = "C:\Program Files\paint.net\paintdotnet.exe"
    launcher_minecraft = "C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"
    # Hier kannst du den empfangenen Wert verwenden, z.B. in einem anderen Python-Programm
    print(f"Empfangener Wert: {data}")
    if data == str(1):
        subprocess.run(launcher_minecraft)
    if data == str(2):
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('alt')
        pyautogui.press("#")
        pyautogui.keyUp('alt')
        pyautogui.keyUp('ctrl')