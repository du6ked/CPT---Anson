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
Button_store =pygame.Rect(button_pos_x, button_pos_y_store, 200, 50)

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
                    cutscene() # main_game() #switch out gungame for cutscene --> main game.
                    #direct player to gungame if thier life is in danger.
                if Button_options.collidepoint(event.pos):
                    preference_menu()
                # if Button_store.collidepoint(event.pos):
                #     stickergallery()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape()

        screen.fill(BLACK) 

        startuplogo = pygame.image.load("Startupscreen_withname.png")
        screen.blit(startuplogo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        button_color_start = get_button_color(Button_soundpref, mouse_pos)
        button_color_preferences = get_button_color(Button_back, mouse_pos)
        button_color_store = get_button_color(Button_store, mouse_pos)

        draw_button(screen, Button_start, button_color_start, "Start")
        draw_button(screen, Button_options, button_color_preferences, "Preferences")
        draw_button(screen, Button_store, button_color_store, "Store")

        pygame.display.flip()
        clock.tick(60)

#=============================================

# def stickergallery():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if Button_openbox.collidepoint(event.pos):
#                     print("open")
#                     #replace with open box animation
#                     #probablity function

#         # cutscimg = pygame.image.load(cutscenes[cutscindx])

#         screen.fill(BLACK)

#         mouse_pos = pygame.mouse.get_pos()
#         button_color_openbox = get_button_color(Button_openbox, mouse_pos)
        
#         draw_button(screen, Button_openbox, button_color_openbox, "Open")

#         # screen.blit(cutscimg, (0 , 0))

#         pygame.display.flip()
#         clock.tick(60)

# def probability(sticker_id):
#     sticker_id = random.randrange(1, 12)


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

#--------------------------

cutscenes = ["cutscene_1.png", "cutscene_2.png"]
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
                "\"Ok, moving on. The Sage Bush Ski Resort has opened a new moutain trail ---\"",
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
                    "I was out on at a trail near here and got lost.", 
                    "Now it's starting to snow and I'm worried there might be a blizzard coming...", 
                    "Please let us in, my baby is going to freeze to death out here, and so am I.", 
                    "I dont have anything to give you, thats why I ask you nicely.", 
                    "Don't make a mother watch her baby freeze to death."])

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
                        "One of my buddies was carrying my backpack so I don't have it on me right now." 
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

Parkranger = Character("Friendly Looking Park Ranger", "Parkranger 1920x1080.png", False, ["*Loudly knocks on the door.*",
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

Graverobber = Character("Grave Robber", "Graverobber 1920x1080.png", False, ["Hi. *he walks up to the door awkwardly*",
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
                        "Let me in!... *his tone increases in desperation*"
                        "Let me in!... *his tone increases in desperation*"
                        "Let me in!... *his tone increases in desperation*"
                        "Uh please?"])

Evilwitch = Character("Evil Witch", "Evilwitch 1920x1080.png", False, ["*Evil Cackles are heard from the other side of the door.*",
                        "HEA HAE AHAE HAEA I AM THE EVIL WITCH OF THE WOODS!!! THE EVILEST WITCH OF THEM ALLLLL HAHAEH HEAHHEA!",
                        "I CAN TELL YOU'RE IN THERE LITTLE PADAWAN...",
                        "ANSWER MY MYSTERIOUS MYSTICAL RIDDLE!",
                        "WHAT DO YOU CALL A FLY WITH NO LEGGSSSS?????",
                        "*Even without a response, the witch continues talking to herself*",
                        "A WALK! THATS WHAT YOU WOULD CALL IT! HAEHAHEHAHE",
                        "ANYWAYS... I SENSE A SPECIFIC MAGICAL PRESENCE IN THIS AREA...",
                        "DO YOU BY CHANCE HAVE A PURPLE GEMSTONE?",
                        "I'LL MAKE A DEAL WITH YOU YOUNG ONE",
                        "GIVE ME THE GEMSTONE AND I WILL GIVE YOU *4* SHOTGUN SHELLS.",
                        "AN EXQUISITE EXCHANGE!!!",
                        "NOW, WHAT IS YOUR CHOICE?",
                        "*she taps her fingers together and awaits your answer while glaring evilly in an ambiguous direction(?)*",
                        "*you'll have to open the door to make the exchange.*"])

# Pyromaniac = Character("PyroManiac")

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

shotgun_shells = 3

def gungame():
    global shotgun_shells, abnormals_killed

    gamestate = GUNGAME
    music_sfx_logic(gamestate)

    global slider_x
    global sliderspeed
    global critbar_pos_x_var
    global critbar_size_var
    global hit_flag
    global shotgun_shells
    global abnormals_killed

    critbar_pos_x_var = random.randrange(585, 1185)
    critbar_size_var = random.randrange(75, 150)

    timer = 0
    delay = 1.8
    bar_color = RED

    shotgun_text = pygame.font.Font("Dimurphic-Gl6Z.ttf", 60)

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
                            return
                        else:
                            shotgun_shells -= 1
                            print(shotgun_shells)
                    else:
                        gameover()
                if event.key == pygame.K_ESCAPE:
                    escape()

        screen.fill(BLACK)
        killscreen = pygame.image.load("Killscreen 1920x1080.png")
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

        pygame.draw.rect(screen, GOLD, (slider_x, bar_y - 7.5, 20, 40))
        
        shotgun_img = shotgun_text.render(f"{shotgun_shells}", True, (255, 255, 255))
        screen.blit(shotgun_img, (SCREEN_WIDTH - shotgun_img.get_width(), 0))

        pygame.display.flip()
        clock.tick(60)

#================================================

#gameover screen & win screen

fcutscenetext = ["fart", "fart1"]

def finishscreen():
    fcutscenetextindx = 0
    
    timer = 0
    delay = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE:
                    fcutscenetextindx += 1
                    if fcutscenetextindx >= len(fcutscenetext):
                        scorekeepermenu()

        dooropen = pygame.image.load("startupscreen.png") # REPLACE WITH ENDING 1 - ESCAPE
        screen.fill(BLACK)

        screen.blit(dooropen, (0 , 0))

        timer += 1/60
        if timer >= delay:
            scorekeepermenu()

        rect = pygame.Rect(button_pos_x - 540, button_pos_y_options + 125, 1280, 30) 
        draw_text(screen, rect, WHITE, (fcutscenetext[fcutscenetextindx]))

        pygame.display.flip()
        clock.tick(60)   

#unfinished
#score keeper


def scorekeepermenu():
    
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

        font = pygame.font.Font(None, 75)
        text_surface = font.render(f"Normals saved: {normals_saved}", True, WHITE)
        screen.blit(text_surface, (400, 200))

        text_surface = font.render(f"Normals reject: {normals_rejected}", True, WHITE)
        screen.blit(text_surface, (400, 400))

        text_surface = font.render(f"Abnormals killed: {abnormals_killed}", True, WHITE)
        screen.blit(text_surface, (400, 600))

        text_surface = font.render(f"Abnormals rejected: {abnormals_rejected}", True, WHITE)
        screen.blit(text_surface, (400, 800))

        pygame.display.flip()
        clock.tick(60)
