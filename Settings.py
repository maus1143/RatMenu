# Settings.py

import os
import time
from RatMenu import Version, main_color_theme, Secondary_color_theme
os.system("cls")
print(main_color_theme)
print("Guten Tag,")
time.sleep(1.5)
print(f"RatSpread {Secondary_color_theme}{Version}{main_color_theme} wird nun gestartet...\n")
time.sleep(0.8)

Settings_Version = "0.0.4"

username = 'user'
city = 'Salzburg'
birthday = '11.11.1111'
api_key = '41f0e608343eaec9c51769c4b41c019a' 

shortcuts = {
    1: "https://www.google.at",
    2: "https://www.github.com",
    3: "https://x.com", 
    4: "https://www.stackoverflow.com",
    5: "https://www.python.org",
    6: "https://www.amazon.de",  
    7: "https://www.wikipedia.org",
    8: "https://www.bing.com",
    9: "https://www.example.com",
    10: "https://www.reddit.com",
    11: "https://www.x.com",
    12: "https://www.test.com"
        }

AllOfThemVars = [username, city, birthday, api_key, shortcuts]

if username != "user":
    Custom = True
else:
    Custom = False

def print_delay(toprint, toprint2, toprint3, toprint4, toprint5):
    import time
    if Custom is True:
        print("Einstellungen werden geladen...")
        time.sleep(0.4)
        print(f"Username: {Secondary_color_theme}{toprint}{main_color_theme}")
        time.sleep(0.4)
        print(f"City: {Secondary_color_theme}{toprint2}{main_color_theme}")
        time.sleep(0.4)
        print(f"Birthday: {Secondary_color_theme}{toprint3}{main_color_theme}")
        time.sleep(0.4)
        print(f"API-Key: {Secondary_color_theme}{toprint4}{main_color_theme}")
        time.sleep(0.4)
        print(f"Shortcuts: {Secondary_color_theme}{toprint5}{main_color_theme}")
        print("Einstellungen erfolgreich geladen")
    else:
        print("Standart Einstellungen wurden geladen")

print_delay(username, city, birthday, api_key, shortcuts)
