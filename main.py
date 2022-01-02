# Python Text RPG
# Adventure game

import cmd
import textwrap
import sys
import os
import time
import random

screenWidth = 100

def titleScreen() :
    os.system('cls')
    print("                 _                 _                                                ")
    print("        /\      | |               | |                                               ")
    print("       /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___    __ _  __ _ _ __ ___   ___  ")
    print("      / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \  / _` |/ _` | '_ ` _ \ / _ \ ")
    print("     / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ | (_| | (_| | | | | | |  __/ ")
    print("    /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|  \__, |\__,_|_| |_| |_|\___| ")
    print("                                                         __/ |                      ")
    print("                                                        |___/                       ")
    print("                           copyright Thomas Mathécade 2022                          ")
    print("                                      - play -                                      ")
    print("                                      - quit -                                      ")
    print("                                      - help -                                      ")
    
    homeSrceen()

def homeSrceen() :
    while True :
        homeSceenOption = input("> ")

        if homeSceenOption.lower()==("play") :
            startGame()
        elif homeSceenOption.lower()==("quit") :
            sys.exit()
        elif homeSceenOption.lower()==("help") :
            helpMenu()
            continue
        else :
            print("Commande invalide !")
            continue

def helpMenu() :
    print ("avant")


class Player :
    def __init__(self, name: str = "", hp: int=0, hpMax: int = 0, mp: int=0, mpMax: int = 0, location: str="start"):
        self.name = name
        self.hp = hp
        self.hpMax = hpMax
        self.mp = mp
        self.mpMax = mpMax
        self.location = location

        if self.name == "" :
            self.getName()

    def getName(self) :
        print("Nom de votre personnage")
        self.name = input("> ")

###### FONCTIONNALITÉS DU JEU ######
def startGame() :
    player = Player()
    sys.exit()

###### MAP ######
"""
Le joueur commence en : b2
---------------------
| a1 | a2 | a3 | a4 |
---------------------
| b1 | b2 | b3 | b4 |
---------------------
| c1 | c2 | c3 | c4 |
---------------------
| e1 | e2 | e3 | e4 |
---------------------
"""

ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examin"
SOLVED = False
UP = "haut", "nord"
DOWN = "bas", "sud"
LEFT = "gauche", "ouest"
RIGHT = "droite", "est"

solvedPlaces = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'e1': False, 'e2': False, 'e3': False, 'e4': False
    }

zoneMap = {
        'a1': {
            ZONENAME : "Le Village d'Osmon",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "",
            DOWN : "b1",
            LEFT : "a2",
            RIGHT : ""
        },
        'a2': {
            ZONENAME : "Le Quartier nord",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "",
            DOWN : "a1",
            LEFT : "a3",
            RIGHT : "b2"
        },
        'a3': {
            ZONENAME : "La Paine d'almaraine",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "",
            DOWN : "b3",
            LEFT : "a2",
            RIGHT : "a4"
        },
        'a4': {
            ZONENAME : "Le Francomté",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "",
            DOWN : "b4",
            LEFT : "a3",
            RIGHT : ""
        },
        'b1': {
            ZONENAME : "Le Quartier ouest",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "a1",
            DOWN : "c1",
            LEFT : "",
            RIGHT : "b2"
        },
        'b2': {
            ZONENAME : "Le Marché des buses",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "a2",
            DOWN : "c2",
            LEFT : "b1",
            RIGHT : "b3"
        },
        'b3': {
            ZONENAME : "Le Quartier est",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "a3",
            DOWN : "c3",
            LEFT : "b2",
            RIGHT : "b4"
        },
        'b4': {
            ZONENAME : "Le Fort lointain",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "a4",
            DOWN : "c4",
            LEFT : "b3",
            RIGHT : ""
        },
        'c1': {
            ZONENAME : "Le Cimetière infecte",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "b1",
            DOWN : "e1",
            LEFT : "",
            RIGHT : "c2"
        },
        'c2': {
            ZONENAME : "Le Quartier sud",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "b2",
            DOWN : "e2",
            LEFT : "c1",
            RIGHT : "c3"
        },
        'c3': {
            ZONENAME : "La forêt d'éternité",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "b3",
            DOWN : "e3",
            LEFT : "c2",
            RIGHT : "c4"
        },
        'c4': {
            ZONENAME : "Le Champ paumé",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "b4",
            DOWN : "e4",
            LEFT : "c3",
            RIGHT : ""
        },
        'e1': {
            ZONENAME : "La Terre morte",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "c1",
            DOWN : "",
            LEFT : "",
            RIGHT : "e2"
        },
        'e2': {
            ZONENAME : "Le Champ défraîchit",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "c2",
            DOWN : "",
            LEFT : "e1",
            RIGHT : "e3"
        },
        'e3': {
            ZONENAME : "Le Désert d'os",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "c3",
            DOWN : "",
            LEFT : "e2",
            RIGHT : "e4"
        },
        'e4': {
            ZONENAME : "Le bout du monde",
            DESCRIPTION : "description",
            EXAMINATION : "examin",
            SOLVED : False,
            UP : "c4",
            DOWN : "",
            LEFT : "e3",
            RIGHT : ""
        }
}

# def printLocation() :
#     print("\n"+ ('#' * (4 + len(player.location))))
#     print("# " + player.location)

titleScreen()