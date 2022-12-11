#----------------------------------------------------------------------------------#
# GAME COMPANY NAME: Paper Trails(TM)                                              #
#                                                                                  #
# Names: Philip Rickey (Programmer), Gerald Freeze (Lead Designer)                 #
#        Hung-Yu Chen (Background Designer), Evan Sanders (Character Designer)     #
#                                                                                  #
# Made for a class at Washington State University in Fall of 2022                  #
#                                                                                  #
# Music used: "01 Ghosts I" by Nine Inch Nails, "Throw Myself" by Snow Strippers,  #
#             https://soundcloud.com/myuu (Nightmares by Myuu)                     #
#----------------------------------------------------------------------------------#

# CHARACTERS (uses one or two letter(s) to make typing dialogue/scripting easier)

define ni = Character("Not Important") # Character doesn't matter

define q = Character("Quesadilla Burrito") # QUESARITO

define t = Character("Taco") # TACO

define f = Character("Fries") # FRIES

define w = Character("Widget") # WIDGET (TACO DOG)

define gf = Character("Amy") # Girlfriend character

define j = Character("Jerry") # Cult leader Jerry character
#-------------------------------------------------------------------------------------#
# Cult Leader Jerry character:                                                        #
# Attributes:                                                                         #
#   -Slime                                                                            #
#   -Cult leader                                                                      #
#   -Speaks only in latin                                                             #
#-------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------#

    # VARIABLES FOR CHOICES

$ a = 0 

$ b = 0 

$ s = 0

default smile = False

#----------------------------------------------------------------------------------------------------------#    


label start: # Starts the game


    scene bg blacksquare # Black square background
    with Dissolve(0.5) # Smooth transition to fade in scene
    
    stop music fadeout 1.0 # Fades out music

    $ i = renpy.input("{i}What is your name?{/i}") # Asks player for MC name, if nothing is typed, gives default name, italics means MC is talking to player
    $ i = i.strip() # Removes leading and trailing characers

    if i == "": # Default name if nothing is typed
        $ i = "Kyle"

#----------------------------------------------------------------------------------------------------------#

    # TRANSFORMS
    
    transform moveRight: # Transform for smooth animation for character to move right (best used before menu choices) 
        xalign 0.5 yalign 1.0
        linear 0.25 xalign 1.0 yalign 1.0

    transform moveCenter: # Transform to have the character move to the center
        xalign 1.0 yalign 1.0
        linear 0.25 xalign 0.5 yalign 1.0  

    transform moveLeft: # Transform for smooth animation for character to move left 
        xalign 1.0 yalign 1.0
        linear 0.25 xalign 0.0 yalign 1.0

    transform rightLeft: # Transform for smooth animation for character to move right to left
        xalign 1.0 yalign 1.0
        linear 0.25 xalign 0.0 yalign 1.0 

    transform leftRight: # Transform for smooth animation for character to move left to right
        xalign 0.0 yalign 1.0
        linear 0.25 xalign 1.0 yalign 1.0        

    transform right: # Puts character to the right
        xalign 1.0 yalign 1.0

    transform left: # Puts character to the left
        xalign 0.0 yalign 1.0        

    transform center:
        xalign 0.5 yalign 1.0 # Centers character      

    transform centerScreen:
        xalign 0.5 yalign 0.5 # Puts character at center of screen    

#----------------------------------------------------------------------------------------------------------#       

    # SPEAKING ANIMATIONS

    image gf animated: # Speaking animation for girlfriend character
        "gf happy"
        pause 0.25
        "gf vhappy"
        pause 0.25
        repeat

    image mc animated: # Speaking animation for main character
        "mc happy"
        pause 0.25
        "lucy mad"
        pause 0.25
        repeat

    image jerry animated:
        "jerry happy"
        pause 0.25
        "jerry vhappy"
        pause 0.25
        repeat

#----------------------------------------------------------------------------------------------------------#

    scene bg blacksquare # Sets scene to black square
    
    label continueGame:

    play music "creepy.mp3" fadein 1.5    

    menu:
        "Do you want to continue the game or jump to a chapter?"
        "----->Continue Game<-----":
            jump firstMenu

        "----->Chapter Selection<-----":
            jump chapterSelection

    label chapterSelection:            

    menu:
        "Select a place to jump to"   
        "----->Disco<-----":
            jump mainGame
        
        "----->Date<-----":    
            jump date1

        "----->Cult<-----":
            jump caveInside

#----------------------------------------------------------------------------------------------------------#
    # Start of dialogue (PRE-TACO DOG)
 
    label firstMenu:    

    menu:
        "{cps=50}{b}Options will be presented to you, {a=jump:a_label}hover your mouse over an option or blue text and click with the left mouse button/touchpad{/a}{/b}"
        "----->Ok!!!!<-----":
            jump agree

        "----->Wait I can click on the highlighted blue text?<-----":
            jump a_label        

#----------------------------------------------------------------------------------------------------------#   

    label agree:
        
    "{cps=50}{b}Good luck and have fun! Lets get on with the game{/b}"

    jump mainGame

#----------------------------------------------------------------------------------------------------------#

    label a_label:
    
    "{cps=50}{i}Clicking highlighted words in the text will give you more information about the environment{/i}"

    "{cps=50}{i}It could also give you more insight on the MC's feelings, or things he notices that have not been explicitely stated{/i}"

    jump firstMenu

#----------------------------------------------------------------------------------------------------------#


    label mainGame: # Path where MC meets gf

    i "{i}On my first day in college, I hosted a dance party because I was THAT GUY{/i}"

    i "{i}Let me set the scene, because it wasn't just any party, it was a disco party{/i}"

    stop music fadeout 1.0

    scene bg disco
    with blinds

    i "{i}A disco party with disco music{/i}"
    
    play music "disco.mp3" fadein 1.0 # Fades in music

    pause 1.0

    i "{i}{a=https://www.youtube.com/watch?v=urb8ZX8cuhE&ab_channel=SnowStrippers-Topic}There we go{/a}{/i}"

    menu:
        "{i}I can't believe this {a=jump:lookAround}club!{/a}{/i}"
        "----->Shred Dance Floor<-----":
            jump dance

#----------------------------------------------------------------------------------------------------------#     

    label lookAround:

    i "{i}I look around the club I rented{/i}"

    i "{i}The club is just one big room, the dimensions (feet) in length, width, and height are 30.5, 30, and 20 respectively{/i}"

    i "{i}There are bathrooms on one side of the room, and there is the entrance to the club at the opposite side of the bathroom{/i}"

    i "{i}Adjacent to both, there is a DJ who is playing music{/i}"

    i "{i}To describe the people there...{/i}"

    # INSERT GRAPHIC OF A CIRCLE IN THE MIDDLE OF A CROWD WHERE PEOPLE SHRED

    i "{i}Imagine a piece of bread with the center of the bread cut out by a cup and removed{/i}"

    i "{i}The left over bread is the people and the empty center is the dance circle that was naturally created{/i}"

    # SWITCH BACK TO DISCO PICTURE

    i "{i}Of course there are people dancing in the center, but they aren't at MY level, to even compare us is an insult to dancing{/i}"

    label dance:  
    
    show mc happy:
        xalign 0.5 yalign 1.0
        block:
            linear 0.5 xalign 0.5
            linear 0.5 xalign 0.7
            linear 0.5 xalign 0.3
            repeat  

    i "{i}Anyways, I entered the dance floor, {a=jump:shredding}shredding it inside the dance circle with ROLLER SKATES{/a}{/i}"

    jump skipShredding

    label shredding:

    i "{i}I was doing popshuvits, kickflips, ollies, you name it I was executing it on the dance floor{/i}"  

    label skipShredding:

    stop music fadeout 0.10    
    
    scene bg door 
    with pushright
    
    play sound "impact.mp3"
    show gf happy

    play music "disco.mp3" fadein 2.0

    gf "So, why did you take me here? We don't even know the host" 

    gf "Just stick by me ok? I don't want to get lost in the crowd by myself, I get too anxious"

    gf "H-hey! Where are you going?!"

    "{b}[ni] dissapears into the crowd{/b}"

    scene bg disco
    with pushleft

    show mc happy: # "Dancing" animation for main character
        xalign 0.5 yalign 1.0
        block:
            linear 0.5 xalign 0.5
            linear 0.5 xalign 0.7
            linear 0.5 xalign 0.3
            repeat

    hide mc happy

    show gf happy at center:
    with Dissolve(0.5)

    gf "(UGH! Where is she? There are so many people here I can't find her!)"

    scene bg blacksquare
    with Dissolve(0.5)

    stop music fadeout 1.0

    "{cps=50}{i}[gf] then pushed through the crowd to see where her friend went, that was when...{/i}"

    play music "creepy.mp3" fadein 0.5    

    scene bg disco
    with Dissolve(0.5) 

    gf "Excuse me, excuse me, excu-"

    show gf happy at left

    show mc happy:
        xalign 1.0 yalign 1.0
        linear 0.25 xalign 0.25 yalign 1.0
        linear 0.30 xalign 0.5 yalign 1.0
        linear 0.28 rotate 90

    pause 0.25
    play sound "collision.wav"    
    with vpunch

    scene bg blacksquare
    with Dissolve(0.5)

    i "{i}It was straight out of a visual novel, she walked into the dance circle and I just bumped into her{/i}"

    i "{i}That is how [gf] and I met{/i}"

    scene bg disco 
    with Dissolve(0.5)

    play music "disco.mp3" fadein 2.0

    show gf animated at left
    
    gf "O-ow"

    show gf happy at left

    show mc animated at right

    i "Oh shoot, I'm so sorry! I was moving too fast to stop, are you ok?"

    show mc happy at right

    show gf animated at left

    gf "I-I'm fine, as you can see I work out a little bit so this is nothing, but what about you? Are you alright?"

    show gf happy at left

    "{b}[gf] extends her hand out to [i], [i] grabs it and is helped up{/b}"

    menu:
        i "{i}I grabbed her hand and we immediately began dancing{/i}"
        "----->Fast dance<-----":
            $ b = 1 # Sets b to 1 for slow dance choice

        "----->Slow dance<-----": 
            $ b = 2 # Sets b to 2 for slow dance choice  

#----------------------------------------------------------------------------------------------------------#            

    # Fast dance sequence
    if b == 1: 

        show mc happy at right:
            rotate 0 
            linear 2.0 rotate 360
            repeat

        pause 2.0

        show gf happy at left:  
            rotate 0 
            linear 2.0 rotate 360 
            repeat  

    # Slow dance sequence
    if b == 2:
    
        show mc happy at right:
            rotate 0 
            linear 10.0 rotate 360
            repeat

        pause 2.0

        show gf happy at left:  
            rotate 0 
            linear 10.0 rotate 360 
            repeat 

    i "{i}I can tell she had never danced before, so I mostly led and she followed{/i}"

    i "{i}After a while I didn't need to lead anymore, we just danced in sync, it was a sight straight out of Dirty Dancing{/i}"

    show gf happy at left:
        rotate 0
        linear 10.0 rotate 360
        repeat

    show mc happy at right:
        rotate 0
        linear 10.0 rotate 360
        repeat       

    i "{i}We danced for{cps=15}...I don't know how long, but I started to feel tired and noticed her eyelids get heavier{/i}"

    hide gf happy

    hide mc happy

    show mc happy at right
    
    show gf happy at left

    hide mc happy

    show mc animated at right

    i "It's getting late huh? I think you should try to find your friend now"

    show mc happy at right

    show gf animated at left

    gf "O-Oh yeah! It is getting late, yeah I should g-go"

    hide gf animated

    show gf happy at left

    i "..."

    gf "..."

    i "{i}Oh, I see what is going on here!{/i}"

    hide mc happy

    show mc animated at right:

    i "Oh yeah, {a=jump:phoneNumber}let me give you my phone number{/a}! You're a pretty good dancer so maybe we can destroy the dance floor again sometime!"

    jump skipConvo

    label phoneNumber:           

    $ phoneNumber = True 

    if phoneNumber:
        $ smile = True
        i "{i}My phone number is 425-749-****, I gave it to her and she {a=jump:smile}smiled{/a}{/i}."
    else:
        jump skipConvo    

    label skipConvo:

    $ smile = False    

    label smile:

    if smile:     
        i "{i}It was the cutest, most genuine smile I've ever seen, my heart couldn't stop feeling warm{/i}"    
    
    hide gf happy

    show gf animated at left

    gf "Sounds good!"

    "{b}[gf] starts walking to her friend who was watching this whole time{/b}"

    "{b}but instead of being angry, she is all smiles{\b}"

    scene bg blacksquare
    with Dissolve(0.5)

    stop music fadeout 1.0

    # TIMESKIP
 
#----------------------------------------------------------------------------------------------------------#

    # WATCH ROM-COM FOR DATE DIALOGUE, MAYBE THE NOTEBOOK???

    label date1:    

    play music "background.mp3" fadein 1.0

    scene bg tacodog 
    with Dissolve(0.5)    

    i "{i}Ah taco dog, home of the taco{/i}"

    i "{i}This of course was not the {a=jump:dateStory}first date I ever been on{/a}, but it turns out it was her first ever date{/i}"

    jump skipDateStories

    label dateStory:
    
    stop music 

    play music "creepy.mp3" fadein 2.0    

    i "{i}I've been on some dates throughout highschool, actually there is one that stands out{/i}"

    i "{i}This one girl I went out with always talked about this game called SpineCraft{/i}"

    i "{i}It was a game where you could choose how your body would decompose, and in the end you always turned into something without a spine{/i}"

    i "{i}...She was such a weird person, who would play such a game? I guess that explains why she was always so jittery{/i}"    

    stop music fadeout 1.0

    play music "background.mp3" fadein 0.5    

    label skipDateStories:

    i "{i}I brought [gf] to the greatest eating establishment at our college, Taco Dog{/i}"

    i "{i}Authentic mexican cuisine, 3 michelin stars, THE place to go on campus{/i}"
    
    show gf happy at left:
    with Dissolve(0.5) 

    show mc happy at right:
    with Dissolve(0.5)

    hide gf happy
    
    show gf animated at left

    gf "Hey [i]! How are you doing?"

    show gf happy at left

    show mc animated at right

    i "Hey [gf], I am doing INCREDIBLE as always, what about you?"

    show mc happy at right

    hide gf happy

    hide mc happy 

    scene bg tacodoginside
    with Dissolve(0.5)

    i "{i}After greeting each other, we go into the restaurant, and take our seat{/i}"

    play music "dog.mp3" fadein 1.0
    show widget happy at center:
    with Dissolve(0.5)

    i "{i}I couldn't believe it! The owner of this place, [w] taking our order!{/i}"

    show mc happy at right:
    with Dissolve(0.5)

    show gf happy at left:
    with Dissolve(0.5)

    i "{i}The owner of this place doesn't talk at all, many say it is because he shows his pride in silence{/i}"

    stop music fadeout 0.25

    pause 0.25

    play music "background.mp3" fadein 1.0

    menu:
        i "{i}He has a menu attached to his back along with a pen where we choose what we want{/i}"
        "----->[q]<-----":
            $ s = 0
            jump quesoBurrito
        "----->[t]<-----":
            $ s = 1
            jump quesoBurrito
        "----->[f]<-----":
            $ s = 2
            jump quesoBurrito

    label quesoBurrito:            

    if s == 0:    

        i "{i}I order the [q], [gf] then looks at me in astonishment{/i}"

    if s == 1:
        
        i "{i}I order the [t], [gf] then looks at me in astonishment{/i}"

    if s == 2:

        i "{i}I order the [f], [gf] then looks at me in astonishment{/i}"

    hide gf happy

    show gf animated at left
   
    gf "Wait what? I don't see that on the menu"

    hide gf animated

    show gf happy at left

    i "{i}I thought she was just playing a funny joke at the time so I just laughed it off{/i}"

    show gf animated at left

    gf "Why do you look so nervous? Are you doing alright?"

    hide gf animated

    show gf happy at left

    show mc animated at right

    i "Y-yeah! I'm doing perfectly fine, what about you?"

    hide mc animated

    show mc happy at right

    hide gf happy

    show gf animated at left

    gf "About the same as I was a few minutes ago, unlike you who is PRETTY {a=jump:aFewMinutesAgo}different from a few minutes ago *chuckles*{/a}"

    hide gf animated

    show gf happy at left

    jump skipAFewMinutesAgo

    label aFewMinutesAgo:

    i "{i}Her laugh was so adorable, my heart <3{/i}"   

    hide mc happy 

    show mc animated at right

    i "*chuckles* yeah, I mean being in the presence of Aphrodite will make any man nervous"

    hide mc animated 

    show mc happy at right

    "{b}[gf]'s face turns cherry red{/b}"

    i "{i}I now feel less nervous{/i}"

    label skipAFewMinutesAgo:
    
    i "{i}After waiting for a while, [w] comes back with our food, which is on a tray on his back{/i}"

    menu:
        "----->Take Food<-----":
            jump takeFood

    label takeFood:        

    if s == 0:    

        i "{i}I take a bite out of my [q], then something weird happens{/i}"

    if s == 1:

        i "{i}I take a bit out of my [t], then something weird happens{/i}"    

    if s == 2:

        i "{i}I take a bite out of my [f], then something weird happens{/i}"     

    i "{i}W-what is happeni-{/i}{nw}"

    stop music

    scene bg blacksquare   

    play sound "jumpscare.mp3"

    show food:
        ease 1.0 zoom 1.5

    pause(2.75)    

    scene bg tacodoginside

    play music "dramatic.mp3" fadein 1.0

    i "{i}W-What was that? I-don't feel well, I think I am going to throw up{/i}"

    i "{i}My vision is starting to get weird and strange, the world is turning into an unrecognizable mess{/i}"

    gf "H-hey! Are you ok? [i]? [i]!!!!"

    i "{i}It was like she didn't exist anymore, I can't hear her or even acknowledge her{/i}"

    i "{i}Then...{/i}"

    show widget happy at center
    with Dissolve(0.5)

    w "Greetings [i]"

    i "{i}[w]??? What is going on?{/i}"

    label menu1:

    menu:
        i "{i}Only I could understand him, no one else could{/i}"
        "Conversation Information":
            jump widget

#----------------------------------------------------------------------------------------------------------#

    label widget:

    # WRITE MORE DIALOGUE ABOUT WHAT MC AND WIDGET TALKED ABOUT

    i "{i}We talked about-{/i}"

    i "{i}W-we uhhhh{/i}"

    "{i}I feel light headed, what i-{/i}"
    
    scene bg blacksquare:
    with Dissolve(0.5)    

    i "{b}[i] blacks out{/b}"

    "{i}NEXT DAY{/i}"

    i "{i}I didn't remember anything that happened yesterday{/i}"

    if s == 0:

        i "{i}What happened after I took a bite of the [q]?{/i}"

    if s == 1:

        i "{i}What happened after I took a bite of the [t]?{/i}"

    if s == 2 :

        i "{i}What happened after I took a bite of the [f]?{/i}"    
    
    i "{i}I was feeling sick, so I went to the bathroom and then...{/i}"

    stop music fadeout 0.5

    scene bg bald 
    with Dissolve(0.5)

    play sound "collision.wav"

    show mc vhappy at center:
    with Dissolve(0.5)

    play music "dramatic.mp3" fadein 1.0

    i "{i}Yes, a cheesy-gordoggy-crunch appeared on my forehead!{/i}"

    i "I-I can't believe it!"

    play sound "breaking.mp3"
    scene bg bald
    with hpunch

    i "WIIDDGGEETTTTT"
    
    i "{i}I was furious, my hands now bloodied from shattering the mirror{/i}"

    scene bg bathroom
    with pushup

    i "{i}But then, I heard a voice in my head, and an image appeared in front of me{/i}"

    show widget happy at center:
    with Dissolve(0.5)

    i "{i}It was [w]!{/i}" 

    i "WIDGET!"

    w "Konnichiwassup [i], hisashi been a while, daijouokay?"

    i "{i}I should have been angry, but when I heard him speak so eloquently, my anger dissapeared{/i}"

    i "W-what are you?"

    w "I am the divine"

    w "Let me guide you"

    scene bg eme
    with Dissolve(0.5)

    # SLIME CULT PATH

    i "{i}I was lead to a mysterious building on campus{/i}"

    i "{i}Building ************{/i}"

    scene bg cultentrance
    with Dissolve(0.5)
    
    i "{i}I was not going crazy! This was never here before, where did this come from?{/i}"

    i "{i}Even though I felt scared, the urge to jump grew greater as the seconds passed{/i}"

    i "{i}And before I knew it...{/i}"

    stop music

    scene bg blacksquare
    with Dissolve(0.5)

    play sound "screaming.wav"

    pause(3.0)

    # ADD FALLING SOUND EFFECTS, LIKE AIR OR SOMETHING IDK, ADD THUD AFTER A FEW SECONDS
    play sound "splat.mp3"

    "{b}*SQUISH*{\b}"

    i "{i}I fell on something soft, what broke my fall?{/i}"

    label caveInside:

    play music "ambience.mp3" fadein 1.0

    scene bg cult
    with Dissolve(0.5)

    i "{i}I found myself in a cave{/i}"

    $ a = 0

    jump choicesNow

    label walkBack:

    if a == 5:

        i "{i}I walked back to the main room of the cave{/i}"

    label choicesNow:

    if a == 9:
        
        menu:
            "----->Die<-----":
                jump die
            "----->Continue On<-----":
                jump continueOn            

    label continueOn:

    menu:
        "----->Look around cave<-----":
            if a == 9:
                jump choicesNow2
            else:        
                jump lookAroundCave
        "----->Look at pile<-----":
                jump lookAtPile    

    # ENTER MENU CHOICE TO LOOK AROUND THE CAVE (MAYBE USE PUSHLEFT/PUSHRIGHT AND CHANGE BACKGROUNDS), DESCRIBE SCENES, 
    # AFTER ALL CHOICES EXAUHSTED (INCREMENT VARIABLE AFTER EACH CHOICE), PLAYER FINDS ALTER           

#----------------------------------------------------------------------------------------------------------#

    label lookAroundCave:

    i "{i}I stumbled around the cave, my eyes adjusting after a few seconds{/i}"

    # ENTER IMAGE WITH INCREASED SASTURATION/BRIGHTNESS

    i "{i}After my eyes adjusted, I looked around to better assess my situation{/i}"

    i "{i}There was this strange rectangular-bed in front of me{/i}"

    i "{i}It seemed to be surrounded by...candles...?{/i}"

    i "{i}What kind of place is this...?{/i}"

    label choicesNow2:

    if a == 9:

        i "{i}There is no way out of here, I am trapped{/i}"

        jump continueOn

    label choicesNow3:    

    if a == 10:

        i "{i}I leave the pile alone{/i}"

    menu:
        "----->Explore rectangular bed<-----":
            jump lookAtAltar

        "----->Find a way out<----":
            if a == 9:
                jump choicesNow2
            else:
                jump wayOut    

#----------------------------------------------------------------------------------------------------------#

label lookAtPile:

    if a == 9:

        i "{i}Here it is again, this green pile{/i}"

        i "{i}Maybe it has an answer to how to get out of here? I just need some semblance of hope at this point{/i}"

        jump pile2
        
    i "{i}I stumbled around the cave, my eyes adjusting after a few seconds{/i}"

    i "{i}I look back at the pile that broke my fall{/i}"

    i "{i}It was all... green{/i}"

    i "{i}...What is this?{/i}"
    
    label pile2:

    menu:
        "----->Touch pile<-----":
            jump touchPile

        "----->Leave it alone<-----": 
            $ a = 10           
            jump choicesNow3
#----------------------------------------------------------------------------------------------------------#

label touchPile:

    i "{i}I leaned in and touch the pile{/i}"    

    i "{i}The texture was like the surface of a slug{/i}"

    i "{i}It was slimey, but at the same time oddly smooth{/i}"

    i "{i}I-It's so pleasant, I can't stop touching it!{/i}"

    i "{i}It was like it was made for touching! I CANT STOP{/i}"

    i "{cps=50}{i}TOUCH TOUCH TOUCH TOUCH TOUCH TOUCH{/i}"

    i "{cps=70}{i}TOUCH TOUCH TOOUUUCCHHHH{/i}"

    i "{cps=80}{i}AAAAAAAAAAAAAAA{/i}"

    i "{b}You get absorbed by the pile{/b}"

    scene bg credits
    with Dissolve(0.5)

    "{b}END 1/100{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    scene main_menu
    with Dissolve(0.5)


    return 

#----------------------------------------------------------------------------------------------------------#

    label die:
    
    i "{i}...{/i}"

    i "{i}I'm done{/i}"

    scene bg credits
    with Dissolve(0.5)

    "{b}END 2/100{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    scene main_menu
    with Dissolve(0.5)

    return

#----------------------------------------------------------------------------------------------------------#

    label lookAtAltar:

    i "{i}I walk closer to the rectangular looking shape{/i}"

    i "{i}That rectangular bed shaped figure turned out to be an alter, and the moment I got closer-{/i}"

    # HAVE 2 BACKGROUNDS, 1 WITH CANDLES OFF, BUT THEN ONE WITH CANDLES ON TO GIVE AFFECT CANDLES TURNED ON

    i "{i}After the alter lit up, all the sudden I see that the slime I fell on was a giant slime!{/i}"

    i "{i}They all scattered from the pile, revealing one giant slime that was in the center of it all{/i}"

    show jerry happy at centerScreen:
    with Dissolve(0.5)

    # SHOW PNG OF JERRY

    i "W-WHAT?"

    i "W-WHAT ARE YOU? WHATS GOING ON"

    hide jerry happy

    show jerry animated at centerScreen   

    j "(speaking latin)" # JERRY SPEAKING LATIN, ASK EVAN ABOUT WHAT HE SAYS!!!! Make this clickable and jump to a label where MC says that he understands the latin perfectly or smth

    hide jerry animated

    show jerry happy at centerScreen  

    i "{i}I understood his latin prefectly despite never learning the language{/i}"

    i "H-How are you...? What is going on! Tasks? Why can I understand-"

    show jerry animated at centerScreen

    j "(Speaking latin)"

    hide jerry animated

    show jerry happy at centerScreen 

    i "M-me? Chosen for what?"

    show jerry animated at centerScreen

    j "(Speaking latin)"

    hide jerry animated

    show jerry happy at centerScreen

    i "Bu-"

    show jerry animated at centerScreen

    j "(Speaking latin)"

    hide jerry animated

    show jerry happy at centerScreen

    i "I-I see"

    show jerry animated at centerScreen

    j "(Speaking latin)"

    hide jerry animated

    show jerry happy at centerScreen

    i "{i}At this point I fully submitted, I accepted that I have a divine entity in front of me{/i}"

    i "{i}I hung onto every word, eventually deciding to carry out the first task it laid before me{/i}"

    # PLAYER DOES TASKS, PUT MENU FOR TASKS, DIFFERENT PATHS AND ALL THAT STUFF

    i "{i}And that task was...{/i}"

    hide jerry happy

    menu:
        "----->To take the life of another<-----":
            jump takeLife 

#----------------------------------------------------------------------------------------------------------#

    label takeLife:        

    i "To take the life of another"

    i "{i}After waiting for a bit, I was presented with a {a=jump:observe}person with a bag over their head{/a}{/i}"

    label returnFromObserve:

    i "{i}I heard their muffled screams, I could tell they were crying underneath that bag{/i}"

    i "{i}No matter{/i}"

    show jerry animated at centerScreen

    j "(Speaking latin)"

    hide jerry animated

    show jerry happy at centerScreen

    i "..."

    hide jerry happy

    menu:
        "----->Take Knife<-----":
            jump knife

    label knife:        

    i "{i}I was handed a regular kitchen knife{/i}"

    menu:
        i "{i}{a=jump:observe2}Their crying got more intense{/a}{/i}"
        "----->COMMENCE SACRIFICE<-----":
            jump sacrificeNow
    
#----------------------------------------------------------------------------------------------------------#     

    label sacrificeNow: # UHHHHH YEAH TRY TO MAKE IT FUNNY MAYBE IDK ASK GERALD HES THE DESIGNER

    i "I ignored the crying, why should I care? This person is human trash, [j] told me"

    show jerry animated at centerScreen
    
    j "(Speaking latin)"

    hide jerry animated

    i "Yes Jerry, right away"

    menu:
        "----->Raise Knife<-----":
            jump raiseKnife

    label raiseKnife:        

    i "{i}I raised the knife like how Rafiki rased Simba{/i}"
 
    menu:
        "----->Lower Knife<-----":
            jump lowerKnife

    label lowerKnife:        

    play sound "knife.mp3"    

    i "{i}I thrust the knife into their chest and let go{/i}"

    # ENTER SOME KIND OF STABBING SOUND EFFECT??? SEARCH FOR FREE STAB SOUND EFFECT!!! YATTA DESU NEEEEE

    menu:
        i "{i}I hear but faint whispers from their exhausted vocal chords, their body telling me all I need to know{/i}"
        "----->Grip Knife<-----":
            jump gripKnife

    label gripKnife:

    if s == 3:

        i "{b}{i}It's too late for that{/i}{/b}"

    menu:
        i "{i}I grip the knife{/i}"
        "----->Twist Knife<-----":
            jump twistKnife
        "----->Take Knife Out<-----":
            $ s = 3
            jump  gripKnife    

    label twistKnife:

    i "{i}I twist the knife"                

    i "{i}They started to flail, like a fish out of water{/i}"

    menu:
        i "{i}They started to flail, like a fish out of water{/i}"
        "----->Apply Pressure<-----":
            jump applyPressure

    label applyPressure:

    i "{i}{a=jump:knifeStab}I applied pressure on the knife as it pierced the sacrifices heart{/a}{/i}"

    jump skipKnifeStab

    label knifeStab:

    i "{i}I kept the knife in longer because why would I want it to end sooner?{/i}"

    i "{i}The knife itself is like a seal, keeping the sacrifice alive{/i}"

    i "{i}And for a moment like this, I want it to last as {cps=10}looooong as possible{/i}"    

    label skipKnifeStab:    

    menu:
        i "{i}They continued to flail{/i}"
        "----->Take Knife Out<-----":
            jump knifeOut

    label knifeOut:        

    i "{i}I wait {cps=10}.....and then slowly pull it out"

    i "I-I've done it!"

    i "[j], I did it!"

    j "(Speaking latin)"

    i "Huh? The identity doesn't matter right? Who cares who this is"

    i "{i}At the time, I knew what he was alluding to{/i}"

    i "{i}I....I-{/i}"

    i "{i}I take off the bag to reveal{/i} {a=jump:her}{b}HER{/b}{/a} {i}face{/i}" # E REVEAL PERFECT BRO CHANGING FROM THEIR TO HER

    play sound "collision.wav"

    show mystery at center:
    with Dissolve(0.5)

    hide mystery

    show gf happy at center:
    with Dissolve(0.5)        

    jump skipHer
    
    label her:

    "{b}...{/b}"    

    label skipHer:

    i "I-I didn't know it was [gf]! NO! I WON'T ACCEPT THIS!"

    hide gf happy

    i "{i}It didn't matter what I said, words can't change what is aleady done{/i}"

    i "{i}Because all shepherds eventually eat their herds{/i}"

    i "I am ready"

    play music "absorbtion.mp3" fadein 1.0

    i "{i}I then walk over to [j], then hug him{/i}"

    i "{i}I start to get absorbed into [j]{/i}"

    i "{i}I feel so euphoric! Did I really deserve to be this happy?{/i}" 

    i "{i}I go deeper into [j], he definitely feels me now!{/i}"

    i "{i}After a few minutes, my body starts decomposing{/i}"

    i "{i}My flesh and bones become mush{/i}"

    i "{i}It hurts, it hurts so good{/i}"

    i "{i}My skin bruning in hellfire, itching all over, my bones being broken one by one{/i}"

    i "{i}My insides being twisted and contorted into impossible geometry, my blood on fire{/i}"

    i "{i}Great pain, but even greater pleasure{/i}"

    i "{i}This lasts for what feels like an eternity, my screams muted, my body frozen{/i}"

    i "{i}After a few minutes...{/i}"

    hide jerry happy

    stop music

    scene bg blacksquare:
    with Dissolve(0.5)    

    i "{i}I get spat out, in a new form{/i}"

    scene bg cult:
    with Dissolve(0.5)    

    play music "trap.mp3"

    pause(4.4)

    show kyle slime at centerScreen:
    with Dissolve(0.5)    

    i "Behold my new form"

    # SHOW MC SLIME FORM

    scene bg credits
    with Dissolve(0.5)

    "{b}END 3/100{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    return   

#----------------------------------------------------------------------------------------------------------#

label observe2:  

    i "{i}I take a moment of solace to observe the body{/i}"

    i "{i}And that is when I realize a single strand of hair on their clothes{/i}"

    i "{i}It was blonde{/i}"

    i "{i}blonde...blonde...{cps=80}B L O N D E{/i}"

    play sound "collision.wav"

    show mystery at center:
    with Dissolve(0.5)    

    i "{i}Goddammit! This is [gf]!{/i}"

    i "{i}I-{/i}"

    i "{i}This is too much! I can't do this!{/i}"

    i "[j], this sacrifice isn't worthy of this great knife, can you please release this person and bring me another?"

    i "This person doesn't even deserve to die in this great place, lets let them live with this moment, scarring them for life"

    i "{i}I try desperately to reason with [j], making up any excuse to not kill her, but then...{/i}"

    j "(Speaking latin)"

    i "N-no! I can kill, this individual is just not...Grand enough! I need a bigger inidividual, more muscular, a titan, I ne-"

    j "(Yelling latin)"

    i "No! Please, don-"

    i "{i}I failed{/i}"

    i "{i}I'm sorry [gf]{/i}"

    i "{i}But, at least I can die with just one thought in mind{/i}"

    i "{i}At least in the darkest moment of my life{/i}"

    i "{cps=15}{i}I retained my humanity{/i}"

    scene bg credits
    with Dissolve(0.5)

    "{b}END 4/100{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    return 
#----------------------------------------------------------------------------------------------------------#      

    label wayOut:

    i "{i}I go down one of the random paths hoping for a way out{/i}"

    i "{i}Thankfully my eyes adjusted a little bit, but it is stil pitch black that I can't really see anything{/i}"

    i "{i}I wander around until I feel a wall{/i}"

    i "{i}I then put my hands on the wall and follow it, making sure my hands are firmly on the wall{/i}"

    i "{i}I start walking{/i}"

    i "{i}...{/i}{nw}"

    i "{cps=40}{i}...{/i}{nw}"

    i "{cps=50}{i}...{/i}{nw}"

    i "{cps=60}{i}...{/i}{nw}"

    i "{cps=70}{i}...{/i}{nw}"

    i "{i}How long does this go?!{/i}"

    menu:
        "----->Turn back<-----":
            $ a = 4
            jump walkBack

        "----->Keep walking<-----":
            jump keepWalking

#----------------------------------------------------------------------------------------------------------#

    label keepWalking:

    # IMPLEMENT PUZZLE WHERE SOMETHING IS FOLLOWING YOU, AND YOU NEED TO STOP WALKING WHEN YOU HEAR
    # FOOTSTEPS, THEN WALK WHEN THE FOOTSTEPS ARE SILENT. WHEN PLAYER KEEPS WALKING W\HEN FOOTSTEPS
    # ARE NOT SILENT && PLAYER WALKS, THEY DIE

    i "{i}I continue walking down this path{/i}"

    i "{i}...{/i}"

    i "{i}I{/i}"    

    "{b}TIME ELAPSED: 20 MINUTES{/b}"

    "{b}TIME ELAPSED: 1 HOUR{/b}"

    i "{i}After walking for an hour, I sit on the wall to catch my breath{/i}"

    i "{i}After taking a break, I continue walking, the wall being my only guide and friend{/i}"

    "{b}TIME ELAPSED: 2 HOURS{/b}"

    i "{i}It is dark, and I am alone here{/i}"

    i "{i}I continue onward, realizing that I cannot turn back now{/i}"

    i "{i}After 4 and a half hours in this darkness, I lose my ability to think{/i}"
    
    "{b}TIME ELAPSED: 20 HOURS{/b}"

    "{b}TIME ELAPSED: {nw}"

    pause(1.5)

    play sound "scary.mp3" fadein 1.0

    i "{i}I immediately snap out of it and I become more alert{/i}"

    play music "chase.mp3" fadein 0.5

    menu:
        i "{i}What the hell was that?!{/i}" # ADD PUZZLE WHERE THEY HAVE TO STOP MOVING AND LISTEN, IF THEY MOVE TOO MUCH PLAYER DIES
        "----->RUN<-----":
            $ a = 100
            jump eaten
        "----->Listen<-----":
            jump listen


#----------------------------------------------------------------------------------------------------------#

    label listen:    

    i "{i}I listen carefully{/i}"    

    i "{i}...{/i}"   

    menu:
        i "{i}Silence{/i}"
        "----->Listen<-----":
            jump listen
        "----->Walk<-----":
            jump keepWalking2    

#----------------------------------------------------------------------------------------------------------#

    label keepWalking2:

    i "{i}I start walking{/i}"

    i "{i}...{/i}"

    play music "steps.mp3"

    pause (1.5)

    $ a = 20

    $ b = 20

    menu:
        i "{i}{a=jump:listening}I hear footsteps{/a}{/i}"
        "----->Keep Walking<-----":
            $ a = 6 
            jump eaten

#----------------------------------------------------------------------------------------------------------#            

    label listening:

    if a == 20:

        i "{i}The silence is deafening, is it not chasing me anymore?{/i}" 

        if b == 20:

            i "I decide to wait{/i}"

            i "It has become silent{/i}"

            menu:
                i "It has become silent{/i}"
                "----->Wait<-----":
                    $ b = 13
                    jump listening
               
                "----->Walk<-----":
                    $ a = 7
                    jump eaten     


        menu:
            i "{i}What should I do?{/i}"
            "----->Wait<-----":
                $ a = 21
                jump listening
            
            "----->Walk<-----":
                $ a = 6
                jump eaten

    if a == 21:

        i "...{/i}"

        i "Nothing is happening{/i}"

        $ a = 20

        jump listening                           

    $ a = 20

    i "{i}I listen again{/i}"

    i "{i}...{/i}"

    stop music

    menu:
        i "{i}{a=jump:listening}Silence{/a}{/i}"           
        "----->Walk<-----":
            jump keepWalking2

#----------------------------------------------------------------------------------------------------------#

    label eaten:

    if a == 6:

        # PLAY LOUDER FOOTSTEP AUDIO
        i "{i}I keep walking{/i}"

        if a == 20:

            play music "steps.mp3" 

            menu:
                i "{i}I hear footsteps again!{/i}"
                "---->Listen<-----":
                    $ b = 22
                    jump listening

        play music "running.mp3"

        menu:
            i "{i}The footsteps are becoming a deafening, {a=jump:listening}something is getting closer!{/a}{/i}"
            "----->RUN<-----":
                $ a = 7
                jump eaten

#----------------------------------------------------------------------------------------------------------#

    if a == 7:

        if b == 20:

            i "{i}I start walking again{/i}"

            i "I think I am in the clear! Now I {cps=10}a-{nw}{/i}"

            play music "running.mp3"

            i "{i}Whatever is chasing me is getting faster, {cps=50}the footseps start to speed up, I pick up the pace, {cps=75}I HAVE TO GET OUT OF HERE{/i}" # PUT TIE SHOELACE OPTION AT BEGINNING OF GAME ( TIE SHOELACE IF NOT EDGY)

            i "{cps=80}{i}I run as fast as I can, this thing is chasing me I-I have to run I-"

        stop music

        menu:    
            i "{i}But then, while running, {a=jump:listen3}I don't hear anything{/a}{/i}"
            "----->Keep Running<-----":
                $ a = 9  

    if a == 9:
        
        i "{i}I trust my instinct and keep running, not even thinking of looking back{/i}"

        i "{i}Eventually...I see a dim light in the distance{/i}"

        i "{i}I-Freedom! I can finally get out of here, I can-{/i}"

        scene bg blacksquare
        with Dissolve(0.5)

        "{b}[i] reaches the end of the tunnel{/b}"

        i "{i}...{/i}"

        i "{i}...I-I give up{i}" 

        i "{i}I'm done{/i}"

        i "{i}I{/i}"

        i "{i}I went in a circle{/i}"

        jump choicesNow     

    i "{i}I start hauling fat ass{/i}"

    i "{i}What is chasing me?{/i}"

    i "{cps=70}{i}I'm running as my life depends on it, I can get out of this I can-{/i}"   

    stop music

    "{cps=50}{b}[i] TRIPS ON HIS SHOELACES{/b}"

    i "{i}Shi-{/i}{nw}"   

    play sound "cheapscare.mp3"

    show jumpscare at centerScreen:
        ease 0.5 zoom 4.0 

    "{b}[i] MEETS A PAINFUL DEATH, HE SHOULD'VE TIED HIS SHOES{/b}"

    hide jumpscare

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    return   

#----------------------------------------------------------------------------------------------------------#

    label listen3:
    
    play music "heartneat.wav"

    i "{i}I stop and stay silent{/i}"

    i "{i}...{/i}"

    i "{i}All I can hear is the sound of my own heartbeat head.{/i}"

    i "{i}It's loud, and it's the only thing I can h-{/i}{nw}"

    play sound "cheapscare.mp3"

    show jumpscare at centerScreen:
        ease 0.5- zoom 4.0   

    hide jumpscare    

    scene bg credits
    with Dissolve(0.5)

    "{b}END 5/100{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    return 

#----------------------------------------------------------------------------------------------------------#

    label observe: # Make this section something that the player can click on in the text beforehand to unlock this dialogue

    i "{i}They were handcuffed with their hands behind their back, their legs connected together with a chain and collar{/i}"

    i "{i}It appeared to be the figure of a man{/i}"

    jump returnFromObserve
