import os
import subprocess
import time
from datetime import datetime
import sys
import locale
import platform
import requests
import importlib
import threading
import random
Placeholder = r""" 
______      _   _____                          _      
| ___ \    | | /  ___|                        | |     
| |_/ /__ _| |_\ `--. _ __  _ __ ___  __ _  __| |     
|    // _` | __|`--. \ '_ \| '__/ _ \/ _` |/ _` |     
| |\ \ (_| | |_/\__/ / |_) | | |  __/ (_| | (_| |     
\_| \_\__,_|\__\____/| .__/|_|  \___|\__,_|\__,_|     
                     | |                              
                     |_|                              
______ _                _           _     _           
| ___ \ |              | |         | |   | |          
| |_/ / | __ _  ___ ___| |__   ___ | | __| | ___ _ __ 
|  __/| |/ _` |/ __/ _ \ '_ \ / _ \| |/ _` |/ _ \ '__|
| |   | | (_| | (_|  __/ | | | (_) | | (_| |  __/ |   
\_|   |_|\__,_|\___\___|_| |_|\___/|_|\__,_|\___|_|"""
try:
    import RatSpreadVars
except ImportError:
    print("RatSpreadVars konnte nicht importiert werden. Verwende Platzhalter.")
    time.sleep(2)
    class RatSpreadVars:
        ascii = f"{Placeholder}"
        titel = "=== RatSpread Menu ==="
        RatSave_titel = f"{Placeholder}"
try:
    import Settings
    username = getattr(Settings, 'username', 'DefaultUser')
    city = getattr(Settings, 'city', 'DefaultCity')
    birthday = getattr(Settings, 'birthday', '01.01.1900')
    api_key = getattr(Settings, 'api_key', '41f0e608343eaec9c51769c4b41c019a')
except ImportError:
    print("Settings konnte nicht importiert werden. Verwende Platzhalter.")
    time.sleep(2)
    class Settings:
        username = 'DefaultUser'
        city = 'Salzburg'
        birthday = '01.01.1900'
        api_key = '41f0e608343eaec9c51769c4b41c019a'
    username = Settings.username
    city = Settings.city
    birthday = Settings.birthday
    api_key = Settings.api_key

DEBUG_MODE = False #Eingabe: 99
STREAMER_MODE = False #Eingabe: 100
Show_Ascii = True #Eingabe: 200
Show_Welcomme = True #Eingabe: 250
Light_mode = False #Eingabe: 300

SCRIPT_CHECK_ENABLED = False
threshold_temp = 23
 
Version = "0.0.7"

DoNotChangeColor = False

Show_Streamermode = True
Show_Debugmode = True
Show_Version =  True
Show_Welcomme = True

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
Rat_save_yt = None

today_date = datetime.now().strftime("%d.%m.%Y")
aktuelle_zeit = time.strftime("%H:%M")
current_os = platform.system().lower()

end = '\033[0m'
red = '\033[91m'
green = '\033[92m'
white = '\033[97m'
dgreen = '\033[32m'
yellow = '\033[93m'
back = '\033[7;91m'
run = '\033[97m[~]\033[0m'
que = '\033[94m[?]\033[0m'
bad = '\033[91m[👎]\033[0m'
info = '\033[93m[!]\033[0m'
debug_symbol = '\033[92m[</>]\033[0m'
good = '\033[92m[+]\033[0m'
not_loadet = '\033[91m[✗]\033[0m'
loadet = '\033[92m[🗸]\033[0m'

def Start():
    if Light_mode is True:
        force_clear()
        color()
    else:
        clear()
        color()
        start_titles()
        version()
        show_debug()
        show_streamer()
        willkommen()
        weather()

def clear():
    if not DEBUG_MODE:
        os.system("cls" if os.name == "nt" else "clear")

def force_clear():
    os.system("cls" if os.name == "nt" else "clear")

def color():
    if DoNotChangeColor == True:
        if os.name == "nt":
            if DEBUG_MODE is True:
                os.system("color 0f")
            else:
                os.system("color 0a")

def start_titles():
    if Show_Ascii is True:
        print(f"{RatSpreadVars.ascii}")
        print(f"{RatSpreadVars.titel}")
    else:
        return

def show_ascii():
        global Show_Ascii
        if Show_Ascii is True:
            debug("Ascii Art deaktiviert")
            Show_Ascii = False
        elif Show_Ascii is False:                        
            debug("Asci Art aktiviert")
            Show_Ascii = True 

def show_debug():
    global show_debug
    if Show_Debugmode is True:
        if DEBUG_MODE is True:
            print(f"{debug_symbol} Debug Modus: Aktiv")
    if Show_Debugmode is False:
        return
    if show_streamer and STREAMER_MODE is True:
        space(1)

def Abstand():
    print(" ")

def space(Value):
    global space
    if Value == 1:
        Abstand()
    elif Value == 2:
        Abstand()
        Abstand()
    elif Value == 3:
        Abstand()
        Abstand()
        Abstand()

def show_streamer():
    if Show_Streamermode is True:
        if STREAMER_MODE is True:
            print(f"Streamer Modus: Aktiv") 
    if Show_Streamermode is False:
        return 

def version():
    if Show_Version is True:
        print(f"RatSpread {Version}")
    if show_debug and DEBUG_MODE is True:
        space(1)
    else: 
        return

def weather():
    weather_info = get_weather()
    if weather_info:
        print(weather_info)
        print(" ")

def debug(message):
    global debug
    if DEBUG_MODE is True:
        print(f"{debug_symbol} DEBUG: {message}")
        time.sleep(4)

def error(message):
    global error
    print(f"{bad} {message}")
    time.sleep(2)

def debug_switch():
        global DEBUG_MODE
        if DEBUG_MODE is True:
            debug("Debug modus deaktiviert")
            DEBUG_MODE = False
        elif DEBUG_MODE is False:
            debug("Debug modus aktiviert")
            DEBUG_MODE = True

def streamer_Switch():
        global STREAMER_MODE
        if STREAMER_MODE is True:
            debug("Streamer modus deaktiviert")
            STREAMER_MODE = False
        elif STREAMER_MODE is False:                        
            debug("Streamer modus aktiviert")
            STREAMER_MODE = True 

def show_wellcome():
        global Show_Welcomme
        if Show_Welcomme is True:
            debug("Wilkommens anzeigen deaktiviert")
            Show_Welcomme = False
        elif Show_Welcomme is False:                        
            debug("Willkommens anzeigen aktiviert")
            Show_Welcomme = True 

def lightmode_switch():
        global Light_mode
        if Light_mode is True:
            debug("Light Mode deaktiviert")
            Light_mode = False
        elif Light_mode is False:
            debug("Light Mode aktiviert")
            Light_mode = True

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
        print(f"{bad} Fehler beim Ausführen des Skripts {script_path}: {e}")
        return False

def get_weather():
    if not city:
        return "Stadt nicht gesetzt."

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        return f"{bad} Fehler bei der API-Anfrage: {e}"

    if response.status_code != 200:
        return f"{bad} Fehler bei der API-Anfrage: {data.get('message', 'Unbekannter {bad} Fehler')}"
    
    if 'list' in data:
        current_temp = data['list'][0]['main']['temp']
        current_time = datetime.fromtimestamp(data['list'][0]['dt'])
        exceed_time = None

        for forecast in data['list']:
            temp = forecast['main']['temp']
            forecast_time = datetime.fromtimestamp(forecast['dt'])

            if temp > threshold_temp:
                exceed_time = forecast_time
                break

        if STREAMER_MODE is False:
            temp_info = f"Aktuelle Temperatur in {city}: {current_temp}°C um {current_time.strftime('%H:%M')}"
            if exceed_time:
                temp_info += f"\nDie Temperatur wird voraussichtlich {threshold_temp}°C überschreiten am {exceed_time.strftime('%d.%m.%Y %H:%M')}."
            else:
                temp_info += f"\nDie Temperatur wird in den nächsten 5 Tagen voraussichtlich nicht {threshold_temp}°C überschreiten."

        if STREAMER_MODE is True:
            temp_info = f"Aktuelle Temperatur in Zensiert: {current_temp}°C um {current_time.strftime('%H:%M')}"
            if exceed_time:
                temp_info += f"\nDie Temperatur wird voraussichtlich {threshold_temp}°C überschreiten am {exceed_time.strftime('%d.%m.%Y %H:%M')}."
            else:
                temp_info += f"\nDie Temperatur wird in den nächsten 5 Tagen voraussichtlich nicht {threshold_temp}°C überschreiten."
        
        return temp_info
    else:
        return f"{bad} Fehler: Keine Vorhersagedaten gefunden."

def initialize_scripts():
    global start_stealer, Rat_crypter, Rat_encrypter, Rat_setup, Rat_phisher, Rat_spreader, Rat_nuker, Rat_crawler, Rat_dehasher, Rat_save, Rat_save_yt

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
    Rat_save_yt = find_script("RatSave_yt.py")  

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
        rat_save_yt_executable = check_script_executable(Rat_save_yt)  
    else:
        start_stealer_executable = bool(start_stealer)
        rat_crypter_executable = bool(Rat_crypter)
        rat_encrypter_executable = bool(Rat_encrypter)
        rat_setup_executable = bool(Rat_setup)
        rat_phisher_executable = bool(Rat_phisher)
        rat_spreader_executable = bool(Rat_spreader)
        rat_nuker_executable = bool(Rat_nuker)
        rat_crawler_executable = bool(Rat_crawler)
        rat_dehasher_executable = bool(Rat_dehasher)
        rat_save_executable = bool(Rat_save) 
        rat_save_yt_executable = bool(Rat_save_yt)  

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
        "Rat_save": rat_save_executable,
        "Rat_save_yt": rat_save_yt_executable

    }

def print_menu(script_status):

#==========================================    
    Start() #Start Anzeige, Ascii, etc
#==========================================

    def mark_script(name, status):
        if status:
            return f"{loadet}{name}"
        else:
            return f"{not_loadet}{name}"
    
    print(mark_script('Stealer', script_status['start_stealer']))
    print(mark_script('Nuker', script_status['Rat_nuker']))
    print(mark_script('Crawler', script_status['Rat_crawler']))
    print(mark_script('DeHasher', script_status['Rat_dehasher']))
    print(mark_script('Crypter', script_status['Rat_crypter']))
    print(mark_script('Encrypter', script_status['Rat_encrypter']))
    print(mark_script('Setup', script_status['Rat_setup']))
    print(mark_script('Phisher', script_status['Rat_phisher']))
    print(mark_script('RatSave', script_status['Rat_save'])) 
    print(mark_script('RatSave YT', script_status['Rat_save_yt'])) 
    print(" ")

    for key, value in menu_options.items():
        print(f"{key}: {value}")

def willkommen():
    global show_wellcome, Show_Welcomme
    if Show_Welcomme is True:
        print(" ")
        try:
            stunde = int(time.strftime("%H"))
        except ValueError:
            stunde = 12  

        try:
            locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
        except locale.Error:
            locale.setlocale(locale.LC_TIME, '')  

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
        if STREAMER_MODE is True:
            print(f"{gruß}, Zensiert! Heute ist {wochentag} der {today_date}")
        else:
            print(f"{gruß}, {username}! Heute ist {wochentag} der {today_date}")
        print(f"Wir haben {aktuelle_zeit} {grußend}")
    else:
        return

def get_birthday():
    try:
        with open('Settings.py', 'r') as settings_file:
            for line in settings_file:
                if line.startswith('birthday'):
                    return line.split('=')[1].strip().strip("'").strip('"')
    except FileNotFoundError:
        return None
    except IOError as e:
        error_menu(f"{bad} Fehler beim Lesen der Datei: {e}")

def set_birthday(date):
    global birthday
    birthday = date
    try:
        with open('Settings.py', 'a') as settings_file:
            settings_file.write(f"\nbirthday = '{date}'\n")
    except IOError as e:
        error_menu(f"{bad} Fehler beim Schreiben der Datei: {e}")

def RatStealer():
    if start_stealer:
        debug("Stealer-Skript wird ausgeführt")
        try:
            if current_os == "windows":
                subprocess.run(["cmd", "/c", "call", start_stealer], check=True)
            else:
                subprocess.run(["bash", start_stealer], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Stealer-Skripts: {e}")
    else:
        debug("Stealer-Skript nicht gefunden.")
        print("start_stealer_win.bat konnte nicht gefunden werden.")

def RatNuker():
    if Rat_nuker:
        debug("Nuker-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_nuker], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Nuker-Skripts: {e}")
    else:
        debug("Nuker-Skript nicht gefunden.")
        print("RatSpreadSystemNuker.py konnte nicht gefunden werden.")

def RatCrawler():
    if Rat_crawler:
        debug("Crawler-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_crawler], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Crawler-Skripts: {e}")
    else:
        debug("Crawler-Skript nicht gefunden.")
        print("RatCrawler.py konnte nicht gefunden werden.")

def RatDehasher():
    if Rat_dehasher:
        debug("DeHasher-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_dehasher], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des DeHasher-Skripts: {e}")
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
        print("\nVerschlüsselungsmenü:")
        for key, value in verschluesselungs_menu_options.items():
            print(f"{key}: {value}")
        
        try:
            option = int(input('Bitte wähle eine Option: '))
            if option == 1:
                RatCrypter()
            elif option == 2:
                RatEnCrypter()
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

def RatCrypter():
    if Rat_crypter:
        debug("Verschlüsselungs-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_crypter], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Verschlüsselungs-Skripts: {e}")
    else:
        debug("Verschlüsselungs-Skript nicht gefunden.")
        print("Ratcodierung.py konnte nicht gefunden werden.")

def RatEnCrypter():
    if Rat_encrypter:
        debug("Entschlüsselungs-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_encrypter], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Entschlüsselungs-Skripts: {e}")
    else:
        debug("Entschlüsselungs-Skript nicht gefunden.")
        print("Ratuncode.py konnte nicht gefunden werden.")

def RatSetup():
    if Rat_setup:
        debug("Setup-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_setup], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Setup-Skripts: {e}")
    else:
        debug("Setup-Skript nicht gefunden.")
        print("start_setup.py konnte nicht gefunden werden.")

def RatPhisher():
    if Rat_phisher:
        debug("Phisher-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_phisher], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Phisher-Skripts: {e}")
    else:
        debug("Phisher-Skript nicht gefunden.")
        print("RatPhisher.py konnte nicht gefunden werden.")

def RatSave_menu():
    debug("RatSave aufgerufen")

    RatSave_menu_options = {
        1: "RatSave (StreamTape)",
        2: "RatSave (Youtube)",
        3: "Zurück zum Hauptmenü"
    }
    while True:
        clear()
        print(f"{RatSpreadVars.RatSave_titel}")
        print("\nRatSave Menu:")
        for key, value in RatSave_menu_options.items():
            print(f"{key}: {value}")
        try:
            option = int(input('Bitte wähle eine Option: '))
            if option == 1:
                RatSave()
            elif option == 2:
                RatSave_yt()
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
def RatSave():
    if Rat_save:
        debug("RatSave-Skript wird ausgeführt (StreamTape)")
        try:
            subprocess.run(["python", Rat_save], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des RatSave-Skripts: {e}")
    else:
        debug("RatSave-Skript nicht gefunden.")
        print("RatSave.py konnte nicht gefunden werden.")

def RatSave_yt():
    if Rat_save_yt:
        debug("RatSave-Skript wird ausgeführt (Youtube)")
        try:
            subprocess.run(["python", Rat_save_yt], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des RatSave-Skripts: {e}")
    else:
        debug("RatSave-Skript nicht gefunden.")
        print("RatSave_yt.py konnte nicht gefunden werden.")

menu_options = {
    1: "Stealer starten",
    2: "Nuker starten",
    3: "Crawler starten",
    4: "DeHasher starten",
    5: "Verschlüsselungsmenü starten",
    6: "Setup starten",
    7: "Phisher starten",
    8: "RatSaveMenu starten", 
    9: "Beenden" 
}

def error_menu(error_message):
    debug(f"{bad} Fehler aufgetreten: {error_message}")
    clear()
    color()
    print(F"Ein {bad} Fehler ist aufgetreten:")
    print(f"{error_message}")
    input("Drücke Enter, um fortzufahren...")

def change_color(option):
    global change_color
    color_code = option.split()[-1]
    if os.name == "nt": 
        try:
            os.system(f"color {color_code}") 
            debug(f"Farbe geändert zu: {color_code}")
        except Exception as e:
            debug(f"{bad} Fehler beim Ändern der Farbe: {e}")
    else:
        print("Farbänderung wird nur unter Windows unterstützt.")

def random_color():
    colors = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    return "0" + random.choice(colors)

def disco():
    if os.name == "nt":
        try:
            while disco_running:
                color_code = random_color()
                os.system(f"color {color_code}")
                time.sleep(0.1)
        except Exception as e:
            error_menu(f"{bad} Fehler: {e}")
    else:
        print("Farbänderung wird nur unter Windows unterstützt.")

def start_disco():
    global disco_running
    disco_running = True
    threading.Thread(target=disco, daemon=True).start()

def stop_disco():
    global disco_running
    disco_running = False
        
def Reload():
    print("RatSpread wird Neugeladen")
    debug("Programm wird neu geladen")
    os.system("call RatMenu.py")
    sys.exit(0)

def wko():
    global wko
    force_clear()
    start_disco()
    print("ᶠᶸᶜᵏᵧₒᵤ!")
    time.sleep(1)
    debug("ᶠᶸᶜᵏᵧₒᵤ!")
    wko()

def main_menu():
    script_status = initialize_scripts()
    while True:
        try:
            print_menu(script_status)
            option = input('Bitte wähle eine Option: ').lower()

            if option == "disco start":
                start_disco()
                continue

            if option == "disco stop":
                stop_disco()
                continue

            if option in ["rl", "reload"]:
                Reload()
                continue

            if option == "clear":
                force_clear()
                continue
            if option == "wko":
                wko()

                continue
            if option.startswith("color "):
                change_color(option)
                continue
            
            try:
                option = int(option)
            except ValueError:
                debug("Ungültige Eingabe: keine Zahl")
                print('Ungültige Eingabe. Bitte eine Zahl eingeben ...')
                continue

            if option == 1:
                RatStealer()
            elif option == 2:
                RatNuker()
            elif option == 3:
                RatCrawler()
            elif option == 4:
                RatDehasher()
            elif option == 5:
                verschluesselungs_menu()
            elif option == 6:
                RatSetup()
            elif option == 7:
                RatPhisher()
            elif option == 8:
                RatSave_menu()
            elif option == 9:
                stop_disco()
                debug("Programm wird beendet")
                print('RatSpread wird beendet')
                sys.exit(0)
            elif option == 99:
                debug_switch()
            elif option == 100:
                streamer_Switch()
            elif option == 200:
                show_ascii()
            elif option == 250:
                show_wellcome()
                show_wellcome
            elif option == 300:
                lightmode_switch()
            else:
                debug(f"Ungültige Option ausgewählt: {option}")
                print('Ungültige Option. Bitte eine Zahl zwischen 1 und 9 eingeben.')
        except KeyboardInterrupt:
            if DEBUG_MODE is True:
                stop_disco()
                debug("Strg+C im Hauptmenü gedrückt, Script wird beendet")
                sys.exit(0)
            else:
                clear()
                main_menu()
        except Exception as e:
            error_menu(str(e))

if __name__ == "__main__":
    disco_running = False
    main_menu()
