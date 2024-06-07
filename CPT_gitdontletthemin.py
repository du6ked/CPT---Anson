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


#====================================================================
#score

normals_saved = 0
normals_rejected = 0
abnormals_killed = 0
abnormals_rejected = 0

#======================

class Character:
    def __init__(self, name, portrait, isAbnormal, dialoguelist) -> None:
        self.name = name
        self.portrait = portrait
        self.dialogue = dialoguelist
        self.isAbnormal = isAbnormal

Backpacker = Character("Backpacker", "backpacker 1920x1080.png", False,
                      ["Hello... uhm, sorry for the trouble, do you mind if I stay here a bit?... Please I'm cold and it's getting darker.",
                       "Is anyone home? I'm so sorry to bother you, but I'm in a really tough spot.",
                       "My name's Alex, and I'm a backpacker who got caught in this blizzard.",
                       "I'm freezing out here, and I'm really scared I won't make it much longer.",
                       "Please, I don't mean any harm—I just need a place to warm up and ride out the storm. I promise I won't be any trouble.", 
                        "I was hiking around in deeper in the forest when the blizzard hit. I wasn't expecting such weather so I only wore this thin red jacket.",
                          "The bacpack? Oh- I-I have some food and supplies I can share if that helps.",
                           "I just really need some shelter right now. Can you please let me in? I would be so grateful."])

Mother = Character("Mother", "Mother 1920x1080.png", True, 
                   ["H-hello, m-my baby... He's freezing out here. Would you be so kind as to let us in your cabin?", 
                    "W-what? What's wrong with my baby?",
                    "He's just different... More importantly, can you let us in?"])

Zipperman = Character("Zipper", "Zipperman 1920x1080.png", True, ["Hey man! It's abosolutely freezing outside out here don't you agree? hehehe..." ,
                   "Mind if I kick my feet up for a bit, preferably inside, um, the cabin? hehehe... *he smiles intently*" ,
                   "Yeah, uhh inside the cabin, um I need to be inside the cabin to be warm... heh.", 
                   "So let me in because I need to, heh, be w-warm? uhm... *he looks from side to side nervously as you continue to interrogate him*", 
                   "p-please?",
                   "*Within the span of a few seconds, his eyes widen and smile widens within his saggy skin*",
                    "PLEASE MAN!! I HAVENT EATEN IN DAYYYSSSS! AND I CAN TELL THERE ARE A FEW OF YOU IN THERE.... HEH",
                    "I CAN SMELL YOU.... EH HEH HE" ] )

Alonewoman = Character("Woman", "Alone Woman 1920x1080.png", True, ["Hey, I was out hiking with some friends and...",
                        "Well, long story short, we got lost and separated.", 
                        "I come alone.", 
                        "You know the woods here near the cemetary are dangerous. You should really get out of this area.",
                        "Bbbbuttt I guess that's not for me to say because I'm lost as well...", 
                        "Oh- which brings me to my main point. Can you let me sleep here tonight?", 
                        "Hello? *The door handle shakes as she tries to open the door*",
                        "I can tell somebody's here by the fact that the door is locked."])

Gravekeeper = Character("Gravekeeper", "Gravekeeper 1920x1080.png", False, ["Aye! *he bangs on the door* Who be in there? *He attempts to peer through the cracks of the wooden door.*",
                        "Aye these youngins nowadays...",
                        "*he clicks his tounge and spits on the snow as he take a swig of what looks like whiskey out of a small metal flask.*",
                        "Least I know that I made the dead bolts strong enough...", 
                        "Aye! Whoever's in there, just so ye'know I made this cabin for myself, not you pesky hikers.", 
                        "*His dememor becomes more frustrated as he starts to bang on the door*",
                        "*He stops as he realizes that its pointless, and sits down in front of the door.*", 
                        "*He mutters quietly* This blasted blizzard's gotten out of hand, but I'm not too worried about that.", 
                        "there are \"things\" out here you know?",
                        "The name's John. I'm the gravekeeper around these here parts.", 
                        "Just let me in sonny... I don't bite. I promise."])

Hehe = Character("Hehe", " hehe.png", True, ["*heavy breathing can be heard from the other side of the door.*"])

characters = [Backpacker, Gravekeeper, Alonewoman, Mother, Zipperman]
#NOTE: REMEMBER TO ADD CHARACTER TO LIST AFTER CREATION.
#--------------------------

ch_id = 0

dialogue_id = 0

current_character = characters[ch_id]

def switch_character(id):
    global ch_id, dialogue_id, current_character, peephole

    ch_id = id
    dialogue_id = 0#
    
    if ch_id == len(characters):
            finishscreen()

    current_character = characters[ch_id]

    peephole = pygame.image.load(current_character.portrait)

#---------------------------------

font_1 = pygame.font.Font("Dimurphic-Gl6Z.ttf", 20)

# peephole = pygame.image.load(current_character.portrait)
door = pygame.image.load("door_1920x1080.png")

def draw_text(screen, rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surf = font_1.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

#-------------------------------
#door opening

def dooropening(ignore):

    timer = 0
    delay = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        timer += 1/60
        if timer >= delay:
            return

        rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 125, 1280, 30) 
        if ignore:
            draw_text(screen, rect, WHITE, ("You ignored the knocking..."))
        else:
            draw_text(screen, rect, WHITE, ("You let them in..."))

        pygame.display.flip()
        clock.tick(60)           


#-------------------------------

switch_character(0)

def main_game():
    global dialogue_id, normals_saved, normals_rejected, abnormals_killed, abnormals_rejected, ignore

    hour = 8

    period = "PM"

    (looking) = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_ESCAPE:
                    escape()
                if event.key == pygame.K_SPACE:
                    dialogue_id += 1
                    if dialogue_id >= len(current_character.dialogue):
                        dialogue_id = 0
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if Button_talk.collidepoint(event.pos):
                    dialogue_id += 1
                    if dialogue_id >= len(current_character.dialogue):
                        dialogue_id = 0
                if Button_look.collidepoint(event.pos):
                     (looking) = not (looking)
                if Button_letin.collidepoint(event.pos):
                    hour += 1
                    dooropening(False)
                    if current_character.isAbnormal:
                        gungame()
                    else:
                        normals_saved += 1
                        switch_character(ch_id + 1)
                if Button_ignore.collidepoint(event.pos):
                    hour += 1
                    dooropening(True)
                    if current_character.isAbnormal:
                        abnormals_rejected += 1
                    else:
                        normals_rejected += 1
                    switch_character(ch_id + 1)
            

        screen.fill(BLACK)

        time = f"{hour}:00{period}"

        if hour > 12:
            period = "AM"
            hour = 1

        if ((looking)):
            screen.blit(peephole, (0,0))
        else:
            screen.blit(door, (0,0))

        mouse_pos = pygame.mouse.get_pos()
        button_color_talk = get_button_color(Button_talk, mouse_pos)
        button_color_look = get_button_color(Button_look, mouse_pos)
        button_color_letin = get_button_color(Button_letin, mouse_pos)
        button_color_ignore = get_button_color(Button_ignore, mouse_pos)

        draw_button(screen, Button_talk, button_color_talk, "Talk")
        draw_button(screen, Button_look, button_color_look, "Look")
        draw_button(screen, Button_letin, button_color_letin, "Let Them In")  
        draw_button(screen, Button_ignore, button_color_ignore, "Ignore")

        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"{time}", True, WHITE)
        screen.blit(text_surface, (100, 100))

        rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 75, 1500, 40) 
        draw_text(screen, rect, WHITE, (current_character.dialogue[dialogue_id]))

        pygame.display.flip()

#=======================================================
