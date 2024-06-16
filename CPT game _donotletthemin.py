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
BUTTON_COLOR = (225, 225, 225)
BUTTON_HOVER_COLOR = (150, 150, 150)
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
button_pos_y_store = SCREEN_HEIGHT / 2 + 375

Button_start = pygame.Rect(button_pos_x, button_pos_y_start, 200, 50)
Button_options = pygame.Rect(button_pos_x, button_pos_y_options, 200, 50)
Button_achieve =pygame.Rect(button_pos_x, button_pos_y_store, 200, 50)

#store buttons
Button_openbox = pygame.Rect(button_pos_x, button_pos_y_options, 225, 50)

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
bar_y = SCREEN_HEIGHT / 2 + 425
slider_x = bar_x
sliderspeed = 15    

#critbar(gungame)
#critbar_pos_x_variable = 960

#music   
def musicplay(musicindex):
    mixer.init()
    mixer.music.load(misc[musicindex]) 
    mixer.music.set_volume(1)
    mixer.music.play(-1) 

misc = ["music_sfx/startup_ambient.mp3"]

def soundfx(sfxindex):
    mixer.init()
    mixer.music.load(sfx[sfxindex]) 
    mixer.music.set_volume(5)
    mixer.music.play(1) 

sfx = ["music_sfx/knocking.mp3", "music_sfx/abnormal_encounter.mp3", "music_sfx/door_creak.mp3"]

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
DOOROPENING = 7
NEWCHARACTER = 8

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
        musicplay(0)

    if GUNGAME == gamestate:
        soundfx(1)

    if DOOROPENING == gamestate:
        soundfx(0)

    if NEWCHARACTER == gamestate:
        soundfx(2)

#=================================================

def startupmenu(): 
    global shotgun_shells, normals_saved, normals_rejected, abnormals_killed, abnormals_rejected

    gamestate = STARTUP
    music_sfx_logic(gamestate)    

    shotgun_shells = 3

    normals_saved = 0
    normals_rejected = 0
    abnormals_killed = 0
    abnormals_rejected = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button_start.collidepoint(event.pos): 
                    cutscene() # main_game() #switch out gungame for cutscene --> main game.
                    #direct player to gungame if thier life is in danger.
                if Button_options.collidepoint(event.pos):
                    preference_menu()
                if Button_achieve.collidepoint(event.pos):
                    stickergallery()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape()

        screen.fill(BLACK) 

        startuplogo = pygame.image.load("Game stills/cutscenes/start/Startupscreen_withname.png")
        screen.blit(startuplogo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        button_color_start = get_button_color(Button_soundpref, mouse_pos)
        button_color_preferences = get_button_color(Button_back, mouse_pos)
        button_color_achieve = get_button_color(Button_achieve, mouse_pos)

        draw_button(screen, Button_start, button_color_start, "Start")
        draw_button(screen, Button_options, button_color_preferences, "Preferences")
        draw_button(screen, Button_achieve, button_color_achieve, "Gallery")

        pygame.display.flip()
        clock.tick(60)

#===========================================

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
                    if counter % 2 == 0:
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

    gamestate = STARTUP
    music_sfx_logic(gamestate) 

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

#--------------------------

cutscenes = ["Game stills/cutscenes/start/Cutscene_1.png", "Game stills/cutscenes/start/cutscene_2.png"]
tutorialtext = ["As you walk through the forest, the sound of crunching snow can be heard under your feet.", 
                "\"its getting dark\" you think to yourself as you near the hiker's cabin.",
                "You look at your watch as the freezing wind blows raw against your skin. \"8:00PM\"",
                "\"I should get back on the road at 8:00AM...\"", 
                "\"There should be a blizzard on the way. I should help any other people that might be stuck out here.\"", 
                "As you open the door to the empty cabin, the wind swings the doors open. *The radio's on...*", 
                "*You enter the cabin* The radio buzzes and switches to a news announcement.",
                "\"Channel 9 News station reporting from Sagebush county\"",
                "\"Shocking reports of \"human-like\" creatures roaming around the forests and residential parks of the Sagebush area.",
                "\"Reports say that these creatures have the ability to imitate human speech and characteristics\"",
                "\"Please keep all of your doors and windows locked at night and don't call the police. They will not help you.\"",
                "\"And if a police officer comes to your door, DO NOT open it. There are no patrol members around this area.\"", 
                "\"Travel in groups during the daytime and stay inside during the night.\"",
                "\"Moving on to more important news, The Sage Bush Ski Resort has opened a new moutain trail near a cemetary---\"",
                "*You stop listening as the news reporter moves on and starts to ramble on about random stuff*",
                "What the hell??? *you say to yourself as you stand inside the cabin shaken by the news.*", 
                "*Suddenly, a knock is heard from your door...*",
                "PRESS SPACE TO ADVANCE DIALOUGE IN CUTSCENES. PRESS \"F\" KEY OR SPACE TO SHOOT YOUR SHOTGUN.",
                "COMMUNICATION IS IMPORTANT.",
                "YOU HAVE *3* SHOTGUN SHELLS. BE QUICK TO ATTACK, DO NOT WASTE TIME.",
                "GOOD LUCK"]


def cutscene():
    tutorialtextindx = 0
    cutscindx = 0

    gamestate = STARTUP
    music_sfx_logic(gamestate) 

    global screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:
                    tutorialtextindx += 1
                    if tutorialtextindx == 7:
                        cutscindx += 1 #switches scenes
                    if tutorialtextindx == len(tutorialtext) - 1:
                        main_game() #directs to main game after finishing cutscene

        cutscimg = pygame.image.load(cutscenes[cutscindx])

        screen.fill(BLACK)

        screen.blit(cutscimg, (0 , 0))

        rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 125, 1280, 30) 
        draw_text(screen, rect, WHITE, (tutorialtext[tutorialtextindx]))

        pygame.display.flip()
        clock.tick(60)           


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

Backpacker = Character("Backpacker", "Game stills/portraits/backpacker 1920x1080.png", False,
                      ["Hello... uhm, sorry for the trouble, do you mind if I stay here a bit?... Please I'm cold and it's getting darker.",
                       "...Is anyone home? I'm so sorry to bother you, but I'm in a really tough spot.",
                       "My name's Alex, and I'm a backpacker who got caught in this blizzard.",
                       "I'm freezing out here, and I'm really scared I won't make it much longer.",
                       "Please, I don't mean any harm—I just need a place to warm up and ride out the storm. I promise I won't be any trouble.", 
                        "I was hiking around in deeper in the forest when the blizzard hit. I wasn't expecting such weather so I only wore this thin red jacket.",
                          "The bacpack? Oh- I-I have some food and supplies I can share if that helps.",
                           "I just really need some shelter right now. Can you please let me in? I would be so grateful."])

Mother = Character("Mother", "Game stills/portraits/mother 1920x1080.png", True, 
                   ["H-hello, m-my baby... He's freezing out here. Would you be so kind as to let us in your cabin?", 
                    "I was out on at a trail near here and got lost.", 
                    "Now it's starting to snow and I'm worried there might be a blizzard coming...", 
                    "Please let us in, my baby is going to freeze to death out here, and so am I.", 
                    "I dont have anything to give you, thats why I ask you nicely.", 
                    "Don't make a mother watch her baby freeze to death."])

Zipperman = Character("Zipper", "Game stills/portraits/zipperman 1920x1080.png", True, ["Hey man! It's abosolutely freezing outside out here don't you agree? hehehe..." ,
                   "Mind if I kick my feet up for a bit, preferably inside, um, the cabin? hehehe... *he smiles intently*" ,
                   "Yeah, uhh inside the cabin, um I need to be inside the cabin to be warm... heh.", 
                   "So let me in because I need to, heh, be w-warm? uhm... *he looks from side to side nervously as you continue to interrogate him*", 
                   "p-please?",
                   "*Within the span of a few seconds, his eyes widen and smile widens within his saggy skin*",
                    "PLEASE MAN!! I HAVENT EATEN IN DAYYYSSSS! AND I CAN TELL THERE ARE A FEW OF YOU IN THERE.... HEH",
                    "I CAN SMELL YOU.... EH HEH HE" ] )

Alonewoman = Character("Woman", "Game stills/portraits/alonewoman 1920x1080.png", True, ["Hey, I was out hiking with some friends and...",
                        "Well, long story short, we got lost and separated.",
                        "One of my buddies was carrying my backpack so I don't have it on me right now." 
                        "I come alone.", 
                        "You know the woods here near the cemetary are dangerous. You should really get out of this area.",
                        "Bbbbuttt I guess that's not for me to say because I'm lost as well...", 
                        "Oh- which brings me to my main point. Can you let me sleep here tonight?", 
                        "Hello? *The door handle shakes as she tries to open the door*",
                        "I can tell somebody's here by the fact that the door is locked."])

Gravekeeper = Character("Gravekeeper", "Game stills/portraits/gravekeeper 1920x1080.png", False, ["Aye! *he bangs on the door* Who be in there? *He attempts to peer through the cracks of the wooden door.*",
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

Hehe = Character("Hehe", "Game stills/portraits/hehe.png", True, ["*heavy breathing can be heard from the other side of the door.*"])

Parkranger = Character("Friendly Looking Park Ranger", "Game stills/portraits/parkranger 1920x1080.png", False, ["*Loudly knocks on the door.*",
                        "HEY OPEN UP! SAGE BUSH PARK RANGER!",
                        "...",
                        "*He coughs to clear his voice.* Ahem, THIS IS THE SAGE BUSH PARK RANGER SERVICE, OPEN UP NOW!!!!",
                        "...",
                        "*he sighs*",
                        "uhhhmmm... hello? anybody in there?...",
                        "um c-could you please let me in?",
                        "I-I come from the ski resort nearby.",
                        "H-have you heard of the new moutain trail opening up soon? heh... *he stands there awkwardly, not knowing what to say.*",
                        "To be honest, the only reason im here is because the pay seemed good and I wanted alone time to work on my... Hobbies...",
                        "I was so stupid... I thought it was just going to be like a relaxing getaway where I'm getting paid to do nothing.",
                        "Turns out, they still make you go out to patrol the area even though there are barely any people that come here.",
                        "*his eyes start to tear up.* I just wanted to be alone, now I'm stuck here...",
                        "ughhh- I dont wanna die here man!! *The previous bravado he first had when he knocked is now completely gone.*",
                        "*He divulges into silence as he waits outside your door.*"])

Graverobber = Character("Grave Robber", "Game stills/portraits/graverobber 1920x1080.png", False, ["Hi. *he walks up to the door awkwardly*",
                        "I know you're in there. *he tries to peep back through the peephole.*",
                        "*Despite claiming he knows you're in there, he tries to open the door, only to be met with sorrow.*",
                        "*he sighs*",
                        "Yo guy- Hiker- Whatever... Could you let me in? Its freaking freeeing out here.",
                        "You hiker types are always so stuck up and paranoid... *he looks to the side spitting on the snow.*",
                        "Yo, I aint askin, let me in now or I break this freaking door down.",
                        "...",
                        "Alright, you asked for it.",
                        "*A long series of kicks and rattling could be heard from the other side of the door as he desperately attempts to break the door down.",
                        "*Eventually the kicking and rattling ceases, being replaced by the sound of heavy breathing.",
                        "hah- Who- hah- Made- hah- This damn door?",
                        "...",
                        "*He pulls out a dirty shovel from his backpack.*",
                        "Last resort!",
                        "*he repeatedly hits the door with the shovel.*",
                        "*Alas, it is no use.*",
                        "...",
                        "Let me in!... *his tone increases in desperation*",
                        "Let me in!... *his tone increases in desperation*",
                        "Let me in!... *his tone increases in desperation*",
                        "Uh please?"])

Evilwitch = Character("Evil Witch", "Game stills/portraits/evilwitch 1920x1080.png", False, ["*Evil Cackles are heard from the other side of the door.*",
                        "HEA HAE AHAE HAEA I AM THE EVIL WITCH OF THE WOODS!!! THE EVILEST WITCH OF THEM ALLLLL HAHAEH HEAHHEA!",
                        "I CAN TELL YOU'RE IN THERE LITTLE PADAWAN...",
                        "ANSWER MY MYSTERIOUS MYSTICAL RIDDLE!",
                        "WHAT DO YOU CALL A FLY WITH NO LEGGSSSS?????",
                        "*Even without a response, the witch continues talking to herself*",
                        "A WALK! THATS WHAT YOU WOULD CALL IT! HAEHAHEHAHE",
                        "MAGNIFICIENT!!!!!!!!!!!!!!!!!!"
                        "ANYWAYS... I SENSE A SPECIFIC MAGICAL PRESENCE IN THIS AREA...",
                        "AS SUCH, HAPPEN TO FEEL LIKE GIVING YOU A FORTUNE READING.",
                        "\"IF YOU SAVE AT LEAST 5,\"",
                        "\"YOU WILL STAY ALIVE\"",
                        "\"AS YOUR GUN, REPLENISH AND STRIVE\"",
                        "\"AND YOU FOES WILL DIMINSH, WITH EVERY SHOT THAT THRIVES.\""
                        "AN EXQUISITE FORTUNE!!!",
                        "*she glares evilly in an ambiguous direction(?)*",
                        "*it doesnt seem like she needs any help...*",
                        "*why is she just standing there?*",
                        "*let her in if you want i guess...*",
                         "*idk i'm just your inner dialogue*"])

Duplicate = Character("Duplicate", "Game stills/portraits/backpacker 1920x1080.png", True,["Hey... My name is Alex. Yo?", 
                        "I'm a backpacker because I have a backpack.",
                        "See? *he turns to show his backpack. He seems very proud of it.*",
                        "*Its a normal backpack*",
                        "It's like the coolest backpack ever, and you know what? *he gets close up to the door*",
                        "*he whispers* I'll give you it if you let me in ;) ;) ;)",
                        "An amazing offer hm?",
                        "Just irresistable.",
                        "And it can be allllll yyyourrrsss if you let me give it to you.",
                        "hurry up and make your decision.... I'm boredddddd....",
                        "*you want to let him in but you can't help but feel like you've seen him before..."])

Dog = Character("Dog", "Game stills/portraits/Dog 1920x1080.png", True, ["RRRRUUUFFF!! RRUUUFFF!",
                "*you feel stupid for even thinking that you could talk to a dog.*",
                "*he continues to barking*",
                "*why is heee kinddaaa cute tho?*",
                "the dog continues borking."])

Victim = Character("Vitcim","Game stills/portraits/Victim 1920x1080.png", False, ["*he knocks on the door frantically* PLEASE!",
                    "THERE'S SOMETHING OUT HERE MAN I'M TELLING YOU!!",
                    "*He struggles to open door*",
                    "*The door handle rattles.*",
                    "A-a-a-a thing man, it was- I was-",
                    "*The man stutters meaninglessly*",
                    "I-I-It ran out in front of my car man!",
                    "It was this thing, it looked like a human, but when I checked it out, he started like--regenerating.",
                    "And when I tried to drive off, the e-engine wouldn't start.",
                    "I didnt know what that thing was gonna do to me so I ran out here.",
                    "I'm so lost man!",
                    "There's dirt all over my clothes and..."
                    "and I think it might be following me.",
                    "please, let me in."])


characters = [Backpacker, Gravekeeper, Mother, Graverobber, Alonewoman, Dog, Evilwitch, Zipperman, Parkranger, Duplicate, Victim, Hehe]

#NOTE: REMEMBER TO ADD CHARACTER TO LIST AFTER CREATION.
#--------------------------

ch_id = 0

dialogue_id = 0

current_character = characters[ch_id]

def switch_character(id):
    global ch_id, dialogue_id, current_character, peephole

    gamestate = DOOROPENING
    music_sfx_logic(gamestate)

    ch_id = id
    dialogue_id = 0#
    
    if ch_id == len(characters):
        finishscreen()
        switch_character(0)

    current_character = characters[ch_id]

    peephole = pygame.image.load(current_character.portrait)

#---------------------------------

font_1 = pygame.font.Font("Dimurphic-Gl6Z.ttf", 20)

# peephole = pygame.image.load(current_character.portrait)
door = pygame.image.load("Game stills/main/door_1920x1080.png")

def draw_text(screen, rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surf = font_1.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

#-------------------------------
#door opening

def dooropening(ignore):

    timer = 0
    delay = 2

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

    gamestate = STARTUP
    music_sfx_logic(gamestate) 

    hour = 8

    period = "PM"

    dialogue_countdown = 0.5
    dialogue_index = 1

    DT = 1/60

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
                    if dialogue_index <  len(current_character.dialogue[dialogue_id]):
                        dialogue_index = len(current_character.dialogue[dialogue_id])
                    else:
                        dialogue_index = 0

                        dialogue_id += 1
                        if dialogue_id >= len(current_character.dialogue):
                            dialogue_id = 0
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if Button_talk.collidepoint(event.pos):
                    if dialogue_index <  len(current_character.dialogue[dialogue_id]):
                        dialogue_index = len(current_character.dialogue[dialogue_id])
                    else:
                        dialogue_index = 0

                        dialogue_id += 1
                        if dialogue_id >= len(current_character.dialogue):
                            dialogue_id = 0
                if Button_look.collidepoint(event.pos):
                     (looking) = not (looking)
                if Button_letin.collidepoint(event.pos):
                    gamestate = NEWCHARACTER
                    music_sfx_logic(gamestate)
                    hour += 1
                    dooropening(False)
                    if current_character.isAbnormal:
                        if shotgun_shells > 0:
                            gungame()
                        else:
                            gameover()
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

        dialogue_countdown -= DT
        if dialogue_countdown < 0 and dialogue_index < len(current_character.dialogue[dialogue_id]):
            dialogue_index += 1
            if current_character.dialogue[dialogue_id][dialogue_index-1] == '.':
                dialogue_countdown = 0.5
            elif current_character.dialogue[dialogue_id][dialogue_index-1] == ',':
                dialogue_countdown = 0.3
            else:
                dialogue_countdown = 0.0001

        rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 75, 1500, 40) 
        draw_text(screen, rect, WHITE, (current_character.dialogue[dialogue_id][:dialogue_index]))

        pygame.display.flip()
        DT = clock.tick(60) / 1000

#=======================================================

def afterkill():

    timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        killmessage = "you killed it...."

        timer += 1/17

        letter = int(timer)
        letter = letter

        if letter >= len(killmessage):
            return

        rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 125, 1280, 30) 
        draw_text(screen, rect, WHITE, (killmessage[:letter]))

        pygame.display.flip()
        clock.tick(60)     

#===================================================

def gungame():
    global shotgun_shells, abnormals_killed, slider_x, sliderspeed, critbar_pos_x_var, critbar_size_var, hit_flag, shotgun_shells, abnormals_killed

    gamestate = GUNGAME
    music_sfx_logic(gamestate)

    if normals_saved > 4:
        shotgun_shells += 4

    critbar_pos_x_var = random.randrange(585, 1185)
    critbar_size_var = random.randrange(75, 150)

    timer = 0
    delay = 5
    bar_color = RED

    text = pygame.font.Font("Dimurphic-Gl6Z.ttf", 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f or pygame.K_SPACE:
                    if shotgun_shells > 0:
                        hit_flag = slider_x >= critbar_pos_x_var and slider_x <= critbar_pos_x_var + critbar_size_var #critbar determinate
                        if hit_flag:
                            abnormals_killed += 1
                            shotgun_shells -= 1
                            switch_character(ch_id + 1)
                            afterkill()
                            return
                        else:
                            shotgun_shells -= 1
                            print(shotgun_shells)
                    else:
                        gameover()
                if event.key == pygame.K_ESCAPE:
                    escape()

        screen.fill(BLACK)
        killscreen = pygame.image.load("Game stills/main/killscreen 1920x1080.png")
        screen.blit(killscreen, (0,0))

        pygame.draw.rect(screen, WHITE, (bar_x, bar_y, 750, 25))

        #-----------------------------------------------------------------
        #crit bar

        pygame.draw.rect(screen, bar_color, (critbar_pos_x_var, bar_y, critbar_size_var, 25))

        #-----------------------------------------------------------------
        # Combat slider

        slider_x += sliderspeed #get it started

        if slider_x <= bar_x or slider_x + 20 >= bar_x + 750: #rebounder
            sliderspeed = -sliderspeed

        timer += 1/60
        if timer >= delay:
            gameover()

        pygame.draw.rect(screen, GOLD, (slider_x, bar_y - 7.5, 20, 40))
        
        shotgun_img = text.render(f"{shotgun_shells}", True, (255, 255, 255))
        screen.blit(shotgun_img, (SCREEN_WIDTH - shotgun_img.get_width(), 0))
        timer_text = text.render(f"you have five seconds. {round(timer, 1)}", True, (255, 255, 255))
        screen.blit(timer_text, (SCREEN_WIDTH - 500 - timer_text.get_width(), 0))

        pygame.display.flip()
        clock.tick(60)



#============================================

def scorekeepermenu():
    
    gamestate = STARTUP
    music_sfx_logic(gamestate) 

    font = pygame.font.Font("Dimurphic-Gl6Z.ttf", 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:
                    startupmenu()

        screen.fill(BLACK)

        omnipotent_duck = pygame.image.load("Game stills/main/scorebg.png")
        screen.blit(omnipotent_duck, (0 , 0))

        font = pygame.font.Font(None, 75)
        text_surface = font.render(f"Normals saved: {normals_saved}", True, WHITE)
        screen.blit(text_surface, (1200, 600))

        text_surface = font.render(f"Normals reject: {normals_rejected}", True, WHITE)
        screen.blit(text_surface, (1200, 800))

        text_surface = font.render(f"Abnormals killed: {abnormals_killed}", True, WHITE)
        screen.blit(text_surface, (200, 600))

        text_surface = font.render(f"Abnormals rejected: {abnormals_rejected}", True, WHITE)
        screen.blit(text_surface, (200, 800))

        pygame.display.flip()
        clock.tick(60)

#==============================================

#gameover screen & win screen

class Ending:
    def __init__(self, name, scene, endtext) -> None:
        self.name = name
        self.scene = scene
        self.endtext = endtext

        self.index = 0 #per letter index
        self.text_pos = 0 #track letter postion
        

hunter = Ending("Hunter", "Game stills/cutscenes/endings/hunter.png", ["The fortune the witch was talking about came true.",
                                                                              "You magically found 3 more shells in your pocket.",
                                                                              "How conspicuous...",
                                                                              "You decided to exact your revenge on these monsters.",
                                                                              "You shot all of them at point blank range with your shotgun.",
                                                                              "How nice, now there's blood all over you and 6 less monsters.",
                                                                              "The end."])

ignorance = Ending("Ignorance", "Game stills/cutscenes/endings/ignorance.png", ["Are you this much of a wimp?",
                                                                                       "Grow up.",
                                                                                       "You slowly went insane as you continued to shiver in fear while people begged for help at your door.",
                                                                                       "what a cruel, cruel player you are.",
                                                                                       "You huddle in the corner as your mind begins to play tricks on you.",
                                                                                       "You go insane even after the night ends, refusing to leave the cabin out of fear.",
                                                                                       "Paralyzed from the fear, you eventually die of starvation.",
                                                                                       "The end."])

liberation = Ending("liberation", "Game stills/cutscenes/endings/liberation.png", ["Good job!",
                                                                                           "I mean I doubt you got this first try.",
                                                                                           "But you still got the best ending! Congratulations",
                                                                                           "Yippe! Horray!",
                                                                                           "Everybody is cheering you on.",
                                                                                           "You and all 5 of the other survivors leave unharmed and safe.",
                                                                                           "Wait, 5? I thought?...",
                                                                                           "Oh right, that eccentric witch...",
                                                                                           "She flew away on her broom as you opened the door.",
                                                                                           "You vow to yourself to never come back to Sage Bush ever again.",
                                                                                           "Everyone lived happily ever after.",
                                                                                           "The end."])

escap_e = Ending("escape", "Game stills/cutscenes/endings/escape.png", ["Good job, you completed the game.",
                                                                              "As you walk out of the cabin door at the break of dawn, you run as fast as you can in one direction.",
                                                                              "You lucked out as that direction happened to lead you to a road.",
                                                                              "You waited in nervous sweat for a car to pass by, your path to safety.",
                                                                              "Over the horizon, a car!",
                                                                              "Rejoice!",
                                                                              "The person driving picks you up and both of you survive and go to lala land.",
                                                                              "This is the most boring ending by far though.",
                                                                              "The end."])

endings = [hunter, ignorance, liberation, escap_e]

current_ending = None #I AM ONLY A VESSELLLLL

achieved_endings = []

def reset_ending(ending):
    ending.index = 0
    ending.text_pos = 0

def finishscreen():
    global current_ending
    #sets ending to current ending depending on the thing

    gamestate = STARTUP
    music_sfx_logic(gamestate) 

    if abnormals_killed == 6:
        current_ending = hunter
        if "hunterending" not in achieved_endings:
            achieved_endings.append("hunterending")
    elif normals_saved == 6:
        current_ending = liberation
        if "liberationending" not in achieved_endings:
            achieved_endings.append("liberationending")
    elif normals_rejected + abnormals_rejected == 12:
        current_ending = ignorance
        if "ignoranceending" not in achieved_endings:
            achieved_endings.append("ignoranceending")
    else:
        current_ending = escap_e
        if "escapeending" not in achieved_endings:
            achieved_endings.append("escapeending")

    reset_ending(current_ending)

    letter_interval_per_mili = 10  # milliseconds
    when_last_letter_was_added = pygame.time.get_ticks()
    
    while True:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:
                    current_ending.index += 1
                    current_ending.text_pos = 0  # Reset text position
                    if current_ending.index >= len(current_ending.endtext):
                        scorekeepermenu()

        screen.fill(BLACK)

        if current_time - when_last_letter_was_added > letter_interval_per_mili: #timer loop thingy
            when_last_letter_was_added = current_time
            if current_ending.text_pos < len(current_ending.endtext[current_ending.index]):
                current_ending.text_pos += 1 # add one

        if current_ending: # checks if an object exists
            endCG = pygame.image.load(current_ending.scene)
            screen.blit(endCG, (0, 0))  
            rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 75, 1500, 40) 
            display_text = current_ending.endtext[current_ending.index][:current_ending.text_pos]
            draw_text(screen, rect, WHITE, display_text)

        pygame.display.flip()
        clock.tick(60)   


#=============================================

def stickergallery():
    global achieved_endings
    timer = 0
    delay = 1.5

    gamestate = STARTUP
    music_sfx_logic(gamestate) 
    
    shotgun = pygame.transform.scale(pygame.image.load("Game stills/trophies/shotgun_trophie.png"), (200, 200))
    insanity = pygame.transform.scale(pygame.image.load("Game stills/trophies/ignorance_trophie.png"), (200, 200))
    together = pygame.transform.scale(pygame.image.load("Game stills/trophies/liberation_trophie.png"), (200, 200))
    truck = pygame.transform.scale(pygame.image.load("Game stills/trophies/escape_trophie.png"), (200, 200))

    mrgallo = pygame.transform.scale(pygame.image.load("Game stills/trophies/mrgallo_trophie.png"), (200, 200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill(BLACK)

        if "hunterending" in achieved_endings:
            screen.blit(shotgun, (50 , 50))

        if "ignoranceending" in achieved_endings:
            screen.blit(insanity, (300, 50))

        if "liberationending" in achieved_endings:
            screen.blit(together, (550, 50))

        if "escapeending" in achieved_endings:
            screen.blit(truck, (800, 50))

        if len(achieved_endings) == 4:
            screen.blit(mrgallo, (1050, 50))


        timer += 1/60
        if timer < delay:
            rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 125, 1280, 30) 
            draw_text(screen, rect, WHITE, ("press ESC to return to main menu."))

        # screen.blit(cutscimg, (0 , 0))
        
        pygame.display.flip()
        clock.tick(60)

#=====================

def gameover():

    gamestate = STARTUP
    music_sfx_logic(gamestate) 

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

        restart = pygame.image.load("Game stills/cutscenes/endings/restart.png")
        screen.blit(restart, (0,0))

        mouse_pos = pygame.mouse.get_pos()
        button_color_restart = get_button_color(Button_restart, mouse_pos)

        draw_button(screen, Button_restart, button_color_restart, "Restart")

        pygame.display.flip()
        clock.tick(60)
                    
#================================================================

startupmenu()
pygame.quit()
sys.exit()
