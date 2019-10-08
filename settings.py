# game options

import pygame as pg
from os import path
TITLE = 'Jumpy!'
WIDTH=480
HEIGHT=600
FPS=60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"
#player properties
PLAYER_ACC = 1
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 2
PLAYER_JUMP = 25

#game settings
BOOST_POWER = 60
POW_SPAWN_PCT = 7
TREE_SPAWN_PCT = 40
MOB_FREQ = 3000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0
#starting platforms
PLATFORM_LIST = [(0 , HEIGHT - 60 ),
                (WIDTH / 2 - 50 , HEIGHT * 3/4),
                (125 , HEIGHT - 250 ),
                (350 , 200 ),
                (175 , 100)]
#colours
white = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
lightblue = (0,255,255)
bgcolor = lightblue
