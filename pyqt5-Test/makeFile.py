import os
import subprocess
import sys

# Funktion zur Konvertierung einer .ui-Datei in eine .py-Datei
def convert_ui_to_py(ui_file):
    py_file = ui_file.replace('.ui', '.py')
    print(f'{py_file} wird erstellt...')
    cmd = f'pyuic5 -o {py_file} {ui_file}'
    subprocess.run(cmd, shell=True)

# Funktion zum Erstellen der ausführbaren Datei mit PyInstaller
def create_executable():
    cmd = 'pyinstaller --onefile --noconsole main.py'
    subprocess.run(cmd, shell=True)

# Funktion zum Ausführen der erstellten ausführbaren Datei
def run_executable():
    if not os.path.exists('dist\main.exe'):
        print("Die ausführbare Datei 'main.exe' existiert nicht!")
        return
    subprocess.run(['dist\main.exe'])

def start_main_script():
    subprocess.run(['python', 'main.py'])

# Hauptprogramm
if __name__ == '__main__':
    if '-run' in sys.argv and not '-fertig' in sys.argv:
        print("Diese datei ist möglicherweise veraltet!")
        run_executable()
        exit(0)
    # Liste der .ui-Dateien im aktuellen Verzeichnis
    ui_files = [f for f in os.listdir() if f.endswith('.ui')]

    if not ui_files:
        print("Keine .ui-Dateien gefunden.")
        exit(1)

    # Konvertiere .ui-Dateien in .py-Dateien
    for ui_file in ui_files:
        convert_ui_to_py(ui_file)

    # Starte die main.py-Datei
    if '-fertig' in sys.argv:
        create_executable()
        print("main.exe erfolgreich erstellt.")
        if '-run' in sys.argv:
            print("starte main.exe...")
            run_executable()
    else:
        start_main_script()
