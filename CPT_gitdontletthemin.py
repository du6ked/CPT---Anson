# things to do.

#not even started -->
#----------------------------- 
#cutscenes and pngs -----------> Next up
#lives/shotgun shell mechanic 
#switch character
#more preference options
#win screen
#charcter progamming and dialouge 
#listing and bug fixes
#sfx for encounters -----------> Next up

#NOTE: consider learning classes and reprogramming some of the code to make use of classes.
#-----------------------------

#in progress -->
#-----------------------------
#sound toggle and ambience
#drawing scenes and characters (12%)
#gun game mini game (probably about 80% done)
#code optimization 
#-----------------------------

#done -->
#------------------------
#pressable buttons.
#startup menu(kind done, still subject to change and modification)
#bar and combat slider for gun game
# Game state tracker
# Escape menu (pause)
# game over menu
#-------------------------
# 
import pygame
from pygame import mixer
import sys
import random

pygame.init()

#constants
BUTTON_COLOR = (192, 192, 192)
BUTTON_HOVER_COLOR = (120, 120, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GOLD = (255, 215, 0)

#variables
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
size = (SCREEN_WIDTH, SCREEN_HEIGHT)

#buttons
button_pos_x = SCREEN_WIDTH / 2 - 100
button_pos_y_start = SCREEN_HEIGHT / 2 + 225
button_pos_y_options = SCREEN_HEIGHT / 2 + 300

Button_start = pygame.Rect(button_pos_x, button_pos_y_start, 200, 50)
Button_options = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#preference buttons
Button_soundpref = pygame.Rect(button_pos_x, button_pos_y_start, 200, 50)
Button_back = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#escape buttons
Button_quit = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#restart(gameover)
Button_restart = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#Main buttons
button_pos_x_main= SCREEN_WIDTH / 2 - 600
button_pos_y_main = SCREEN_HEIGHT / 2 - 300

Button_talk = pygame.Rect(button_pos_x_main, button_pos_y_main, 175, 70)
Button_look = pygame.Rect(button_pos_x_main, button_pos_y_main + 150, 175, 70)
Button_letin = pygame.Rect(button_pos_x_main, button_pos_y_main + 300, 225, 70)
Button_ignore = pygame.Rect(button_pos_x_main, button_pos_y_main + 450, 175, 70)

#slider(gungame)
bar_x = SCREEN_WIDTH / 2 - 375
bar_y = SCREEN_HEIGHT / 2 + 300
slider_x = bar_x
sliderspeed = 8.5

#critbar(gungame)
#critbar_pos_x_variable = 960

#music
def musicplay(musicindex):
    mixer.init()
    mixer.music.load(misc[musicindex]) 
    mixer.music.set_volume(1)
    mixer.music.play(-1) 

misc = ["startup_ambient.mp3"]

def soundfx(sfxindex):
    mixer.init()
    mixer.music.load(sfx[sfxindex]) 
    mixer.music.set_volume(5)
    mixer.music.play(-1) 

sfx = ["knocking.mp3", "abnormal_encounter.mp3"]

#char

#images 

#dialouge

#==========================================================
#game state tracker

STARTUP = 1
PREFERENCES = 2
ESCAPE = 3
GUNGAME = 4
GAMEOVER = 5
MAIN_GAME = 6

#==========================================================
#screen
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("dontletthemin")

#==========================================================
#font/ font size
font = pygame.font.Font("Dimurphic-Gl6Z.ttf", 30)

def draw_button(screen, rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

#======================================================

def get_button_color(button_rect, mouse_pos):
    if button_rect.collidepoint(mouse_pos):
        return BUTTON_HOVER_COLOR
    else:
        return BUTTON_COLOR
    
#==================================================

def music_sfx_logic(gamestate):
    if STARTUP or PREFERENCES or ESCAPE or GAMEOVER or MAIN_GAME  == gamestate:
        mixer.music.pause
        musicplay(0)

    if GUNGAME == gamestate:
        mixer.music.pause
        soundfx(1)
        print(True)

#=================================================

def startupmenu(): 

    gamestate = STARTUP
    music_sfx_logic(gamestate)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button_start.collidepoint(event.pos): 
                    gungame() # main_game() #switch out gungame for cutscene --> main game.
                    #direct player to gungame if thier life is in danger.
                if Button_options.collidepoint(event.pos):
                    preference_menu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape()

        screen.fill(BLACK) 

        mouse_pos = pygame.mouse.get_pos()
        button_color_start = get_button_color(Button_soundpref, mouse_pos)
        button_color_preferences = get_button_color(Button_back, mouse_pos)

        draw_button(screen, Button_start, button_color_start, "Start")
        draw_button(screen, Button_options, button_color_preferences, "Preferences")

        pygame.display.flip()
        clock.tick(60)

#=============================================

misccounter = 1

def preference_menu():

    gamestate = PREFERENCES
    music_sfx_logic(gamestate)

    global screen
    global misccounter
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button_soundpref.collidepoint(event.pos):
                    counter += 1
                    if counter %2 == 0:
                        mixer.music.pause() 
                    else:
                        mixer.music.unpause()
                if Button_back.collidepoint(event.pos):
                    return  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape()

        screen.fill(BLACK) 

        mouse_pos = pygame.mouse.get_pos()
        button_color_soundpref = get_button_color(Button_soundpref, mouse_pos)
        button_color_back = get_button_color(Button_back, mouse_pos)

        draw_button(screen, Button_soundpref, button_color_soundpref, "Music ON/OFF")
        draw_button(screen, Button_back, button_color_back, "Back")

        pygame.display.flip()
        clock.tick(60)

#=====================================================

def escape():
    global screen 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button_quit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        screen.fill(BLACK) 

        mouse_pos = pygame.mouse.get_pos()
        button_color_quit = get_button_color(Button_soundpref, mouse_pos)

        draw_button(screen, Button_quit, button_color_quit, "Quit Game")

        pygame.display.flip()
        clock.tick(60)

#=======================================================

def gungame():

    gamestate = GUNGAME
    music_sfx_logic(gamestate)

    global slider_x
    global sliderspeed
    global critbar_pos_x_var
    global critbar_size_var
    global hit_flag

    critbar_pos_x_var = random.randrange(585, 1185)
    critbar_size_var = random.randrange(75, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    hit_flag = slider_x >= critbar_pos_x_var and slider_x <= critbar_pos_x_var + critbar_size_var #critbar determinate
                    if hit_flag:
                        print ('hit') #contine game
                    else:
                        gameover() #call game over screen
                if event.key == pygame.K_ESCAPE:
                    escape()

        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE, (bar_x, bar_y, 750, 25))

        #-----------------------------------------------------------------
        #crit bar

        pygame.draw.rect(screen, RED, (critbar_pos_x_var, bar_y, critbar_size_var, 25))

        #-----------------------------------------------------------------
        # Combat slider

        slider_x += sliderspeed #get it started

        if slider_x <= bar_x or slider_x + 20 >= bar_x + 750: #rebounder
            sliderspeed = -sliderspeed

        pygame.draw.rect(screen, GOLD, (slider_x, bar_y - 7.5, 20, 40))

        pygame.display.flip()
        clock.tick(60)

#================================================

#gameover screen & win screen

#unfinished

def gameover():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_restart.collidepoint(event.pos):
                        startupmenu()
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_ESCAPE:
                    escape()      
                    
        screen.fill(BLACK) 

        mouse_pos = pygame.mouse.get_pos()
        button_color_restart = get_button_color(Button_restart, mouse_pos)

        draw_button(screen, Button_restart, button_color_restart, "Restart")

        pygame.display.flip()
        clock.tick(60)

# ===============================================
#creating characters and stuff (more coming)

class Character:
    def __init__(self, name, portrait, isAbnormal, dialoguelist) -> None:
        self.name = name
        self.portrait = portrait
        self.dialogue = dialoguelist
        self.isAbnormal = isAbnormal



Backpacker = Character("Backpacker", "backpacker 1920x1080.png", False,
                      ["Hello... uhm, sorry for the trouble, do you mind if I stay here a bit?... Please I'm cold and it's getting darker.",
                        "I was hiking around in deeper in the forest when the blizzard hit. I wasn't expecting such weather so I only wore this thin red jacket.",
                          "The bacpack? Oh, there's a few cans of tomato soup, I'm willing to share, just let me in please."])

Zipperman = Character("Zipper", "zipper.png", True, ["Hey man! It's abosolutely freezing outside out here don't you agree? hehehe..." ,
                   "Mind if I kick my feet up for a bit, preferably inside, um, the cabin? hehehe... *he smiles intently*" ,
                   "Yeah, uhh inside the cabin, um I need to be inside the cabin to be warm... heh.", 
                   "So let me in because I need to, heh, be w-warm? uhm... *he looks from side to side nervously as you continue to interrogate him*", 
                   "p-please?",
                   "*Within the span of a few seconds, his eyes widen and smile widens within his saggy skin*",
                    "PLEASE MAN!! I HAVENT EATEN IN DAYYYSSSS! AND I CAN TELL THERE ARE A FEW OF YOU IN THERE.... HEH",
                    "I CAN SMELL YOU.... EH HEH HE" ] )

characters = [Backpacker, Zipperman]

#========================================

ch_id = 0

dialogue_id = 0

current_character = characters[ch_id]

def switch_character(id):
    global ch_id, dialogue_id, current_character, peephole

    ch_id = id
    dialogue_id = 0#
    
    # if ch_id == len(characters):
    #         print("you finish good job") #replace with finish screen
    #         quit()

    current_character = characters[ch_id]

    peephole = pygame.image.load(current_character.portrait)

#---------------------------------
