import time

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

purple = '\033[95m'
cyan = '\033[96m'
orange = '\033[33m'
brown = '\033[38;5;94m'
pink = '\033[38;5;213m'
light_red = '\033[91m'
light_green = '\033[92m'
light_yellow = '\033[93m'
light_blue = '\033[94m'
light_cyan = '\033[96m'
light_purple = '\033[95m'

bg_black = '\033[40m'
bg_red = '\033[41m'
bg_green = '\033[42m'
bg_yellow = '\033[43m'
bg_blue = '\033[44m'
bg_magenta = '\033[45m'
bg_cyan = '\033[46m'
bg_white = '\033[47m'

bold = '\033[1m'
underline = '\033[4m'
blink = '\033[5m'
reverse = '\033[7m'
hidden = '\033[8m'
strikethrough = '\033[9m'

RatColorsVersion = "0.0.2"

display_load_status = True

def load_status(color_name):
    if display_load_status:
        print(f"{debug_symbol} {white}RatColors:{end} {color_name}{white} erfolgreich geladen{end}")
        time.sleep(0.1)

load_status(f"{red}Rot{end}")
load_status(f"{blue}Blau{end}")
load_status(f"{green}Grün{end}")
load_status(f"{white}Weiß{end}")
load_status(f"{dgreen}Dunkelgrün{end}")
load_status(f"{yellow}Gelb{end}")
load_status(f"{back}Hintergrund Rot{end}")
load_status(f"{purple}Lila{end}")
load_status(f"{cyan}Cyan{end}")
load_status(f"{orange}Orange{end}")
load_status(f"{brown}Braun{end}")
load_status(f"{pink}Rosa{end}")
load_status(f"{light_red}Hellrot{end}")
load_status(f"{light_green}Hellgrün{end}")
load_status(f"{light_yellow}Hellgelb{end}")
load_status(f"{light_blue}Hellblau{end}")
load_status(f"{light_cyan}Hellcyan{end}")
load_status(f"{light_purple}Helltürkis{end}")

load_status(f"{bg_black}{white}Hintergrund Schwarz{end}")
load_status(f"{bg_red}Hintergrund Rot{end}")
load_status(f"{bg_green}Hintergrund Grün{end}")
load_status(f"{bg_yellow}Hintergrund Gelb{end}")
load_status(f"{bg_blue}Hintergrund Blau{end}")
load_status(f"{bg_magenta}Hintergrund Magenta{end}")
load_status(f"{bg_cyan}Hintergrund Cyan{end}")
load_status(f"{bg_white}Hintergrund Weiß{end}")

load_status(f"{white}{bold}Fett{end}")
load_status(f"{white}{underline}Unterstrichen{end}")
load_status(f"{white}{blink}Blinkend{end}")
load_status(f"{white}{reverse}Umgekehrt{end}")
load_status(f"{hidden}Versteckt{end}")
load_status(f"{white}{strikethrough}Durchgestrichen{end}")

load_status(run + f" {yellow}Run-Symbol")
load_status(que + f" {yellow}Frage-Symbol")
load_status(bad + f" {yellow}Fehler-Symbol")
load_status(info + f" {yellow}Info-Symbol")
load_status(debug_symbol + f" {yellow}Debug-Symbol")
load_status(good + f" {yellow}Bestätigt-Symbol")
load_status(not_loadet + f" {yellow}Nicht geladen-Symbol")
load_status(loadet + f" {yellow}Geladen-Symbol")

# print(f"{debug_symbol} {white}RatColors Version: {yellow}{RatColorsVersion}{white}")