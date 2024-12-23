RatCreate_Version = None

import time
from RatMenu import *
from RatColors import *
from RatCreate import RatCreate_Version
from Settings import Settings_Version

main_color_theme = f"{white}"

Secondary_color_theme = f"{yellow}"

Script_status_color_found = f"{white}"

Script_status_color_not_found = f"{red}"

options_color = f"{white}"

normal_input = f"{main_color_theme}Bitte wähle eine Option: {Secondary_color_theme}"

lightmode_input = f"You sick Bastard: "

def rat_print(message):
    print(f"{message}")

def rat_repeat(command_list, times):
    commands = command_list.split(", ")             
    
    for _ in range(times):
        for command in commands:
            eval(command)

def rat_times(command, times):
    for _ in range(times):
        eval(command)
      
def clear():
  import os
  os.system("cls" if os.name == "nt" else "clear")

def sleep(settime):
    from time import sleep
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

def format_value(text):
    try:
        value = float(text)
        return f"{yellow}{text}{white}"
    except ValueError:
        if text in ["True", "False", "true", "false"]:
            return f"{yellow}{text}{white}"
        return text

def debug(text):
    import datetime
    global debug
    formatted_text = " ".join([format_value(word) for word in text.split()])

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{blue}{current_time}{end} {debug_symbol} {white}{formatted_text}{end}")
    sleep(4)

def error(message):
    global error
    print(f"{bad}: {message}")
    sleep(2)

print_it = True

def rat_print_condition(Message, condtion):
    if condtion is True:
        rat_print(Message)
        sleep(0.08)

RatSave_titel = r"""
 _____                                                                            _____ 
( ___ )                                                                          ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                            |   | 
 |   | ooooooooo.                 .    .oooooo..o                                 |   | 
 |   | `888   `Y88.             .o8   d8P'    `Y8                                 |   | 
 |   |  888   .d88'  .oooo.   .o888oo Y88bo.       .oooo.   oooo    ooo  .ooooo.  |   | 
 |   |  888ooo88P'  `P  )88b    888    `"Y8888o.  `P  )88b   `88.  .8'  d88' `88b |   | 
 |   |  888`88b.     .oP"888    888        `"Y88b  .oP"888    `88..8'   888ooo888 |   | 
 |   |  888  `88b.  d8(  888    888 . oo     .d8P d8(  888     `888'    888    .o |   | 
 |   | o888o  o888o `Y888""8o   "888" 8""88888P'  `Y888""8o     `8'     `Y8bod8P' |   | 
 |   |                                                                            |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                          (_____)"""

RatSave_titel_YT = r"""
 _____                                                                                                                          _____ 
( ___ )                                                                                                                        ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                                                                          |   | 
 |   | ooooooooo.                 .    .oooooo..o                                                   oooooo   oooo ooooooooooooo |   | 
 |   | `888   `Y88.             .o8   d8P'    `Y8                                                    `888.   .8'  8'   888   `8 |   | 
 |   |  888   .d88'  .oooo.   .o888oo Y88bo.       .oooo.   oooo    ooo  .ooooo.                      `888. .8'        888      |   | 
 |   |  888ooo88P'  `P  )88b    888    `"Y8888o.  `P  )88b   `88.  .8'  d88' `88b                      `888.8'         888      |   | 
 |   |  888`88b.     .oP"888    888        `"Y88b  .oP"888    `88..8'   888ooo888      8888888          `888'          888      |   | 
 |   |  888  `88b.  d8(  888    888 . oo     .d8P d8(  888     `888'    888    .o                        888           888      |   | 
 |   | o888o  o888o `Y888""8o   "888" 8""88888P'  `Y888""8o     `8'     `Y8bod8P'                       o888o         o888o     |   | 
 |   |                                                                                                                          |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                                                        (_____)"""

RatStealer_titel = r"""
 _____                                                                                                 _____ 
( ___ )                                                                                               ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   |
 |   |                                                                                                 |   |
 |   | ooooooooo.                 .    .oooooo..o     .                       oooo                     |   |
 |   | `888   `Y88.             .o8   d8P'    `Y8   .o8                       `888                     |   |
 |   |  888   .d88'  .oooo.   .o888oo Y88bo.      .o888oo  .ooooo.   .oooo.    888   .ooooo.  oooo d8b |   |
 |   |  888ooo88P'  `P  )88b    888    `"Y8888o.    888   d88' `88b `P  )88b   888  d88' `88b `888""8P |   |
 |   |  888`88b.     .oP"888    888        `"Y88b   888   888ooo888  .oP"888   888  888ooo888  888     |   |
 |   |  888  `88b.  d8(  888    888 . oo     .d8P   888 . 888    .o d8(  888   888  888    .o  888     |   |
 |   | o888o  o888o `Y888""8o   "888" 8""88888P'    "888" `Y8bod8P' `Y888""8o o888o `Y8bod8P' d888b    |   |
 |   |                                                                                                 |   |
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___|
(_____)                                                                                               (_____)"""  

RatCrypter_titel = r"""
 _____                                                                                                        _____ 
( ___ )                                                                                                      ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                                                        |   | 
 |   | ooooooooo.                 .     .oooooo.                                       .                      |   | 
 |   | `888   `Y88.             .o8    d8P'  `Y8b                                    .o8                      |   | 
 |   |  888   .d88'  .oooo.   .o888oo 888          oooo d8b oooo    ooo oo.ooooo.  .o888oo  .ooooo.  oooo d8b |   | 
 |   |  888ooo88P'  `P  )88b    888   888          `888""8P  `88.  .8'   888' `88b   888   d88' `88b `888""8P |   | 
 |   |  888`88b.     .oP"888    888   888           888       `88..8'    888   888   888   888ooo888  888     |   | 
 |   |  888  `88b.  d8(  888    888 . `88b    ooo   888        `888'     888   888   888 . 888    .o  888     |   | 
 |   | o888o  o888o `Y888""8o   "888"  `Y8bood8P'  d888b        .8'      888bod8P'   "888" `Y8bod8P' d888b    |   | 
 |   |                                                      .o..P'       888                                  |   | 
 |   |                                                      `Y8P'       o888o                                 |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                                      (_____)"""

RatCoder_titel = r"""
 _____                                                                                     _____ 
( ___ )                                                                                   ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                                     |   | 
 |   | ooooooooo.                 .     .oooooo.                   .o8                     |   | 
 |   | `888   `Y88.             .o8    d8P'  `Y8b                 "888                     |   | 
 |   |  888   .d88'  .oooo.   .o888oo 888           .ooooo.   .oooo888   .ooooo.  oooo d8b |   | 
 |   |  888ooo88P'  `P  )88b    888   888          d88' `88b d88' `888  d88' `88b `888""8P |   | 
 |   |  888`88b.     .oP"888    888   888          888   888 888   888  888ooo888  888     |   | 
 |   |  888  `88b.  d8(  888    888 . `88b    ooo  888   888 888   888  888    .o  888     |   | 
 |   | o888o  o888o `Y888""8o   "888"  `Y8bood8P'  `Y8bod8P' `Y8bod88P" `Y8bod8P' d888b    |   | 
 |   |                                                                                     |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                   (_____)"""

Ratdecoder_titel = r"""
 _____                                                                                                          _____ 
( ___ )                                                                                                        ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                                                          |   | 
 |   | ooooooooo.                 .   oooooooooo.                                       .o8                     |   | 
 |   | `888   `Y88.             .o8   `888'   `Y8b                                     "888                     |   | 
 |   |  888   .d88'  .oooo.   .o888oo  888      888  .ooooo.   .ooooo.   .ooooo.   .oooo888   .ooooo.  oooo d8b |   | 
 |   |  888ooo88P'  `P  )88b    888    888      888 d88' `88b d88' `"Y8 d88' `88b d88' `888  d88' `88b `888""8P |   | 
 |   |  888`88b.     .oP"888    888    888      888 888ooo888 888       888   888 888   888  888ooo888  888     |   | 
 |   |  888  `88b.  d8(  888    888 .  888     d88' 888    .o 888   .o8 888   888 888   888  888    .o  888     |   | 
 |   | o888o  o888o `Y888""8o   "888" o888bood8P'   `Y8bod8P' `Y8bod8P' `Y8bod8P' `Y8bod88P" `Y8bod8P' d888b    |   | 
 |   |                                                                                                          |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                                        (_____)"""

RatPhisher_titel = r"""
  _____                                                                                                       _____
( ___ )                                                                                                     ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   |
 |   |                                                                                                       |   |
 |   | ooooooooo.                 .   ooooooooo.   oooo         o8o           oooo                           |   |
 |   | `888   `Y88.             .o8   `888   `Y88. `888         `"'           `888                           |   |
 |   |  888   .d88'  .oooo.   .o888oo  888   .d88'  888 .oo.   oooo   .oooo.o  888 .oo.    .ooooo.  oooo d8b |   |
 |   |  888ooo88P'  `P  )88b    888    888ooo88P'   888P"Y88b  `888  d88(  "8  888P"Y88b  d88' `88b `888""8P |   |
 |   |  888`88b.     .oP"888    888    888          888   888   888  `"Y88b.   888   888  888ooo888  888     |   |
 |   |  888  `88b.  d8(  888    888 .  888          888   888   888  o.  )88b  888   888  888    .o  888     |   |
 |   | o888o  o888o `Y888""8o   "888" o888o        o888o o888o o888o 8""888P' o888o o888o `Y8bod8P' d888b    |   |
 |   |                                                                                                       |   |
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___|
(_____)                                                                                                     (_____)"""

ascii = r"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████░░░░░░░░
░░░░░░▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒████░░░░░░░░░░░░░░▒▒▒▒░░
░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒██▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▓▓▒▒▒▒░░░░██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒██
░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓░░
░░░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░██████░░░░░░
░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▓▓▓▓░░▓▓▓▓░░██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░██░░▒▒██░░▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░████████▒▒▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░████░░░░░░▒▒▒▒░░██▓▓░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░██░░░░▒▒██▒▒▒▒▒▒▒▒▒▒░░██░░░░░░░░░░░░░░░░░░░░░░
░░░░░░██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██░░░░░░░░░░░░░░░░░░░░
░░░░░░████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒██▒▒██████░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░██████████▒▒██████░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░████████████▒▒████▒▒██░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▓▓░░██▒▒▒▒██░░▒▒██▒▒▒▒██░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░██▒▒██▒▒▒▒██▒▒██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░████░░▒▒▒▒██▒▒▒▒░░▒▒██░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░██░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░██░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓░░▒▒▒▒██░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▒████░░▒▒██▓▓████░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▒██░░░░▒▒██░░▒▒██░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░████░░░░▒▒██░░▓▓██░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░"""

titel = r"""
 _____                                                                                               _____ 
( ___ )                                                                                             ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                                               |   | 
 |   | ooooooooo.                 .    .oooooo..o                                               .o8  |   | 
 |   | `888   `Y88.             .o8   d8P'    `Y8                                              "888  |   | 
 |   |  888   .d88'  .oooo.   .o888oo Y88bo.      oo.ooooo.  oooo d8b  .ooooo.   .oooo.    .oooo888  |   | 
 |   |  888ooo88P'  `P  )88b    888    `"Y8888o.   888' `88b `888""8P d88' `88b `P  )88b  d88' `888  |   | 
 |   |  888`88b.     .oP"888    888        `"Y88b  888   888  888     888ooo888  .oP"888  888   888  |   | 
 |   |  888  `88b.  d8(  888    888 . oo     .d8P  888   888  888     888    .o d8(  888  888   888  |   | 
 |   | o888o  o888o `Y888""8o   "888" 8""88888P'   888bod8P' d888b    `Y8bod8P' `Y888""8o `Y8bod88P" |   | 
 |   |                                             888                                               |   | 
 |   |                                            o888o                                              |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                             (_____)"""

RatSpreadVarsVersion = "0.0.9"

rat_print_condition(f"{main_color_theme}{RatPhisher_titel}", print_it)
rat_print_condition(f"{main_color_theme}{RatCoder_titel}", print_it) 
rat_print_condition(f"{main_color_theme}{RatCrypter_titel}", print_it) 
rat_print_condition(f"{main_color_theme}{Ratdecoder_titel}", print_it) 
rat_print_condition(f"{main_color_theme}{RatSave_titel}", print_it)
rat_print_condition(f"{main_color_theme}{RatCoder_titel}", print_it)
rat_print_condition(f"{main_color_theme}{RatStealer_titel}", print_it)
rat_print_condition(f"{main_color_theme}{titel}", {print_it}) 
rat_print_condition(f"{main_color_theme}{ascii}", {print_it})
sleep(1)
rat_print(f"{main_color_theme}Running RatSpreadVars Version: {Secondary_color_theme}{RatSpreadVarsVersion}{end}")
sleep(1)
rat_print(f"{main_color_theme}Running RatColors Module Version: {Secondary_color_theme}{RatColorsVersion}{end}")
sleep(1)
rat_print(f"{main_color_theme}RatMenu Version: {Secondary_color_theme}{Version}{end}")
sleep(1)
rat_print(f"{main_color_theme}Settings Version: {Secondary_color_theme}{Settings_Version}{end}")
sleep(1)
rat_print(f"{main_color_theme}RatCreate Version: {Secondary_color_theme}{RatCreate_Version}{end}")
sleep(1)
# By Mausi Schmausi
