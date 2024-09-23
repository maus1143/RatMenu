import os
import subprocess
import time
import traceback
import datetime
from datetime import datetime
import sys
import locale
import platform
import requests
import importlib
import threading
import random

Version = "0.1.1"

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

#-------------------
#True = An
#False = Aus 
#-------------------

DEBUG_MODE = False #Eingabe: 99
STREAMER_MODE = False #Eingabe: 100
DARKMODE = True #Bitte... bei allem was heilig ist.... lass den Darkmode an
Show_Ascii = True #Eingabe: 200
Show_Welcomme = True #Eingabe: 250
Light_mode = False #Eingabe: 300 # mitr light ist Leicht gemeint
DoNotChangeColor = True
SCRIPT_CHECK_ENABLED = False

threshold_temp = 20

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
    end = ''
    red = ''
    blue = ''
    green = ''
    white = ''
    dgreen = ''
    yellow = ''
    back = ''
    run = '[~]'
    que = '?]'
    bad = '[✗]'
    info = '[!]'
    debug_symbol = '[</>]'
    good = '[🗸]'
    not_loadet = '[✗]'
    loadet = '[🗸]'

normal_input = f"{white}Bitte wähle eine Option: {yellow}"

lightmode_input = f"You sick Bastard: "

main_color_theme = f"{white}"

Secondary_color_theme = f"{yellow}"

Script_status_color_found = f"{white}"

Script_status_color_not_found = f"{red}"

options_color = f"{white}"

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
        print(f"{main_color_theme}{RatSpreadVars.ascii}")
        print(f"{main_color_theme}{RatSpreadVars.titel}")
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
            print(f"{main_color_theme}Debug Modus: {Secondary_color_theme}Aktiv{end}")
    if Show_Debugmode is False:
        return
    if show_streamer and STREAMER_MODE is True:
        space(1)

def sleep(settime):
    time.sleep(settime)

def Abstand():
    print(" ")

def space(Value):
    global space
    if Value == 1:
        Abstand()
    elif Value == 2:
        Abstand()
        Abstand()
        Abstand()
    elif Value == 3:
        Abstand()
        Abstand()
        Abstand()

def show_streamer():
    if Show_Streamermode is True:
        if STREAMER_MODE is True:
            print(f"{main_color_theme}Streamer Modus: {Secondary_color_theme}Aktiv{end}") 
    if Show_Streamermode is False:
        return 

def version():
    if Show_Version is True:
        print(f"{main_color_theme}RatSpread Version: {Secondary_color_theme}{Version}")
    if show_debug and DEBUG_MODE is True:
        space(1)
    else: 
        return

def weather():
    weather_info = get_weather()
    if weather_info:
        print(weather_info)
        print(" ")

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
    
        print(f"{blue}{current_time}{end} {debug_symbol} {main_color_theme}{formatted_text}{end}")
        sleep(4)

def error(message):
    global error
    print(f"{bad}: {message}")
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

def print_menu(script_status):

#==========================================    
    Start() #Start Anzeige, Ascii, etc
#==========================================

    def mark_script(name, status):
        if status:
            return f"{loadet}{Script_status_color_found}{name}"
        else:
            return f"{not_loadet}{Script_status_color_not_found} {name}"
    
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
    print(mark_script('RatCreate', script_status['Rat_create'])) 
    print(" ")

    for key, value in menu_options.items():
        print(f"{options_color}{key}: {value}")

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
            gruß = f"{main_color_theme}Herzlichen Glückwunsch zum Geburtstag, {Secondary_color_theme}{username}!"
        if STREAMER_MODE is True:
            print(f"{main_color_theme}{gruß}, {Secondary_color_theme}Zensiert!{main_color_theme} Heute ist {Secondary_color_theme}{wochentag}{main_color_theme} der {green}{today_date}")
        else:
            print(f"{main_color_theme}{gruß}, {Secondary_color_theme}{username}{main_color_theme}! Heute ist {Secondary_color_theme}{wochentag}{main_color_theme} der {green}{today_date}")
        print(f"{main_color_theme}Wir haben {Secondary_color_theme}{aktuelle_zeit}{main_color_theme} Uhr {grußend}")
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
        clear()
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

def RatCreate():
    if Rat_create:
        debug("RatCreate-Skript wird ausgeführt")
        try:
            subprocess.run(["python", Rat_create], check=True)
        except subprocess.CalledProcessError as e:
            error_menu(f"{bad} Fehler beim Ausführen des RatCreate-Skripts: {e}")
    else:
        debug("RatCreate-Skript nicht gefunden.")
        print("RatCreate.py konnte nicht gefunden werden.")

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
    
    print(f"Ein {bad} Fehler ist aufgetreten:")
    print(f"{error_message}")
    print("\nDetaillierter Fehlerbericht:")
    print(error_report)
    
    input("Drücke Enter, um fortzufahren...")
    
    with open("error_log.txt", "a") as log_file:
        log_file.write(error_report)

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
        print("Der Disco modus wird nur unter Windows unterstützt.")

def start_disco():
    global disco_running
    disco_running = True
    threading.Thread(target=disco, daemon=True).start()

def stop_disco():
    global disco_running
    disco_running = False
        
def Reload():
    print(f"{main_color_theme}RatSpread wird Neugeladen")
    debug("Programm wird neu geladen")
    os.system("call RatMenu.py")
    sys.exit(0)

def wko():
    global wko
    force_clear()
    start_disco()
    print("test")
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
                print(f"Unbekanntes Dateiformat: {file_extension}")
        except Exception as e:
            print(f"Fehler beim Ausführen des Skripts: {e}")
    else:
        print(f"Skript '{script_name}' nicht gefunden.")

def main_menu():
    script_status = initialize_scripts()
    while True:
        try:
            if DARKMODE is True:
                print_menu(script_status)
                option = input(f'{Secondary_color_theme}{normal_input}').lower()
                print(f"{end}")
            else:
                print_menu(script_status)
                option = input(f'{lightmode_input}').lower()

            if option == "disco start":
                start_disco()
                continue

            if option.startswith("color "):
                change_color(option)
                continue

            if option.startswith("start "):
                script_name = option[6:].strip() 
                start_script(script_name)
                sys.exit(0) 

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
            
            try:
                option = int(option)
            except ValueError:
                debug(f'"{option}" ist keine gültige Eingabe')
                print(f'{main_color_theme}Ungültige Eingabe. Bitte eine Zahl eingeben ...')
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
                print(f'{main_color_theme}RatSpread wird beendet')
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
                print(f'{main_color_theme}Ungültige Option. Bitte eine Zahl zwischen 1 und 10 eingeben.')
        except KeyboardInterrupt:
            if DEBUG_MODE is True:
                stop_disco()
                print(" ")
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
