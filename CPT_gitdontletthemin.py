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

red = (255, 0, 0)
gold = (255, 215, 0)

#variables
width = 1920
height = 1080
size = (width, height)

#buttons
button_pos_x = width / 2 - 100
button_pos_y_start = height / 2 + 210
button_pos_y_options = height / 2 + 275

Button_start = pygame.Rect(button_pos_x, button_pos_y_start, 200, 50)
Button_options = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#preference buttons
Button_soundpref = pygame.Rect(button_pos_x, button_pos_y_start, 200, 50)
Button_back = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#escape buttons
Button_quit = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#restart(gameover)
Button_restart = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)

#slider(gungame)
slider_pos_x = width / 2 - 375
slider_pos_y = height / 2 + 300
slider_pos_x_moveable = slider_pos_x
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
                    gungame() #switch out gungame for cutscene --> main game.
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
