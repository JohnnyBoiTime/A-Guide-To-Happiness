#----------------------------------------------------------------------------------#
# GAME COMPANY NAME: Paper Trails(TM)                                              #
#                                                                                  #
# Names: Philip Rickey (Programmer), Gerald Freeze (Lead Designer)                 #
#        Hung-Yu Chen (Background Designer), Evan Sanders (Character Designer)     #
#                                                                                  #
# Made for a class at Washington State University in Fall of 2022                  #
#                                                                                  #
# Music used: "01 Ghosts I" by Nine Inch Nails, "Throw Myself" by Snow Strippers   #
#----------------------------------------------------------------------------------#

# CHARACTERS (uses one or two letter(s) to make typing dialogue/coding easier)

define ni = Character("Not Important") # Character doesn't matter

define q = Character("Quesadilla Burrito") # QUESARITO

define t = Character("Taco") # TACO

define f = Character("Fries") # FRIES

define w = Character("Widget") # WIDGET (TACO DOG)

define gf = Character("Amy") # Girlfriend character
#-------------------------------------------------------------------------------------#
# Girlfriend characters attributes, likes, and dislikes (REFERENCE ANONYMOUS):        #
# Attributes:                                                                         #
#   -Does not really talk to anyone                                                   #                                                    #
# Likes:                                                                              #
#   -Quality time together                                                            #
#   -Wide range of Music                                                              #
#   -Humor                                                                            #
# Dislikes:                                                                           #
#   -Boyfriend being pushy                                                            #
#   -Boyfriend being distant                                                          #
#   -Taco Bell (maybe boyfriend pushes her to eat taco bell and asks for rides?)      #
#-------------------------------------------------------------------------------------#

define j = Character("Jerry") # Cult leader Jerry character
#-------------------------------------------------------------------------------------#
# Cult Leader Jerry character:                                                        #
# Attributes:                                                                         #
#   -Slime                                                                            #
#   -Cult leader                                                                      #
#   -Speaks only in latin                                                             #
#-------------------------------------------------------------------------------------#

# POSSIBLE IDEA: GAME IS MADE BY A CULT TO TRY TO CONVINCE PLAYER TO JOIN (4TH WALL BREAK????)

# HAVE THE GAME BE A FUNNY META ABOUT SOME CULT UNDER WSU AND THE GAME IS A RECRUITMENT FOR THEM MAYBBBEEE?????

# IS MC THE PLAYER OR A CHARACTER? SHOULD THEY USE PRONOUNS LIKE "I", OR USE WORDS LIKE "(MC NAME) LOOKS AROUND", OR SAY SOMETHING LIKE "YOU LOOK AROUND"?????

# POSIBLE IDEA: CHARACTER GETS PUT INSIDE THIS GAME AT THE END, AND IS DOOMED TO REPEAT IT FOREVER IN TORMENT

# ADD COOKIE CLICKER TYPE MECHANICS

#----------------------------------------------------------------------------------------------------------#

    # VARIABLES FOR CHOICES

$ a = 0 

$ b = 0 

$ s = 0

default smile = False

default listen = False

#----------------------------------------------------------------------------------------------------------#    


label start: # Starts the game

    scene bg blacksquare # Black square background
    with Dissolve(0.5) # Smooth transition to fade in scene
    
    stop music fadeout 1.0 # Fades out music

    $ i = renpy.input("{i}What is your name?{/i}") # Asks player for MC name, if nothing is typed, gives default name, italics means MC is talking to player
    $ i = i.strip() # Removes leading and trailing characers

    if i == "": # Default name if nothing is typed
        $ i = "Kyle"
    #---------------------------------------------------------------------------------#
    # Main Character (COULD CHANGE BASED ON E'S PREFERENCES):                         #
    # Attributes (Pre-Taco Dog):                                                      #
    #   -Cool                                                                         #
    #   -Funny                                                                        #
    #---------------------------------------------------------------------------------#

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
        "mc vhappy"
        pause 0.25
        repeat

#----------------------------------------------------------------------------------------------------------#


    scene bg blacksquare # Sets scene to black square

    # GENIUS GERALD said to make a menu for debugging specifically, put different debugs in different places

    "Would you like to skip the intro?"

    menu: # Menu for choices
        "Continue": # Continues game
            jump continueGame

        "Skip Intro/Tutorial": # Skips intro
            jump skipIntro    

        "Debug":  # For debugging
            jump db

#----------------------------------------------------------------------------------------------------------#

    label continueGame:
    
    # Start of dialogue (PRE-TACO DOG)
    i "{cps=25}{i}It all started back in my freshman year of college{/i}"

    i "{cps=25}{i}I wasn't nervous at all making the transition into adulthood and independence{/i}"

    i "{cps=25}{i}I was actually excited to meet new people, make lifelong friends{/i}"

    i "{cps=25}{i}Maybe even meet someone to hold close, someone that will make the rest of my life something to cherish{/iS}"

    i "{cps=25}{i}...{/i}"

    i "{cps=25}{i}But life is unpredictable{/i}"

    i "{cps=25}{i}It always feels like it happens opposite of what you anticipated{/i}"

    i "{cps=25}{i}But maybe that is the way it is supposed to happen for some of us{/i}"

    i "{cps=25}{i}What do you think?{/i}"

    label firstMenu:    

    menu:
        "{cps=50}{b}Options will be presented to you, {a=jump:a_label}hover your mouse over an option or blue text and click with the left mouse button/touchpad{/a}{/b}"
        "----->Agree<-----":
            jump agree

        "----->Disagree<-----":
            jump disagree    

#----------------------------------------------------------------------------------------------------------#   

    label agree:
        
    i "{cps=25}{i}Looks like we are in the same boat{/i}"    

    "{cps=50}{b}Each choice selected will either change how the game progresses, or is simply an action{/b}"

    "{cps=50}{b}Good luck and have fun! Lets get on with the game{/b}"

    jump mainGame

#----------------------------------------------------------------------------------------------------------#

    label disagree:

    i "{cps=25}{i}I see, let's see if you still believe that later on{/i}"

    "{cps=50}{b}Each choice selected will change how the game progresses, or is simply an action{/b}"   

    "{cps=50}{b}But you probably already know this huh?{/b}"

    "{cps=50}{b}Anyawys, lets get on with the game!{/b}"

    jump mainGame

#----------------------------------------------------------------------------------------------------------#

    label a_label:
    
    "{cps=50}{i}Clicking highlighted words in the text will give you more information about the environment{/i}"

    "{cps=50}{i}It could also give you more insight on the MC's feelings, or things he notices that have not been explicitely stated{/i}"

    jump firstMenu

#----------------------------------------------------------------------------------------------------------#

    label skipIntro:

    label mainGame: # Path where MC meets gf

    i "{cps=25}{i}On my first day in college, I hosted a dance party because I was THAT GUY{/i}"

    i "{cps=25}{i}Let me set the scene, because it wasn't just any party, it was a disco party{/i}"

    scene bg disco
    with blinds

    i "{cps=25}{i}A disco party with disco music{/i}"
    
    play music "disco.mp3" fadein 1.0 # Fades in music

    pause 1.0

    i "{cps=25}{i}{a=https://www.youtube.com/watch?v=urb8ZX8cuhE&ab_channel=SnowStrippers-Topic}There we go{/a}{/i}"

    menu:
        "{cps=25}{i}I can't believe this {a=jump:lookAround}club!{/a}{/i}"
        "----->Shred Dance Floor<-----":
            jump dance

#----------------------------------------------------------------------------------------------------------#     

    label lookAround:

    i "{cps=25}{i}I look around the club I rented{/i}"

    i "{cps=25}{i}The club is just one big room, the dimensions (feet) in length, width, and height are 30.5, 30, and 20 respectively{/i}"

    i "{cps=25}{i}There are bathrooms on one side of the room, and there is the entrance to the club at the opposite side of the bathroom{/i}"

    i "{cps=25}{i}Adjacent to both, there is a DJ who is playing music{/i}"

    i "{cps=25}{i}To describe the people there...{/i}"

    # INSERT GRAPHIC OF A CIRCLE IN THE MIDDLE OF A CROWD WHERE PEOPLE SHRED

    i "{cps=25}{i}Imagine a piece of bread with the center of the bread cut out by a cup and removed{/i}"

    i "{cps=25}{i}The left over bread is the people and the empty center is the dance circle that was naturally created{/i}"

    # SWITCH BACK TO DISCO PICTURE

    i "{cps=25}{i}Of course there are people dancing in the center, but they aren't at MY level, to even compare us is an insult to dancing{/i}"

    label dance:  
    
    show mc happy:
        xalign 0.5 yalign 1.0
        block:
            linear 0.5 xalign 0.5
            linear 0.5 xalign 0.7
            linear 0.5 xalign 0.3
            repeat  

    i "{cps=25}{i}Anyways, I entered the dance floor, {a=jump:shredding}shredding it inside the dance circle with ROLLER SKATES{/a}{/i}"

    jump skipShredding

    label shredding:

    i "{cps=25}{i}I was doing popshuvits, kickflips, ollies, you name it I was executing it on the dance floor{/i}"  

    label skipShredding:

    scene bg door 
    with pushright
    
    show gf happy

    gf "So, why did you take me here? We don't even know the host" 

    ni "Because you need to get out more! You can't just {a=jump:videoGames}stay inside and play video games! You need to live a little and socialize!{/a}"

    jump skipVideoGames

    label videoGames:

    "{b}{cps=3}... {cps=50}I don't know what you expected me to say here{/b}"    

    label skipVideoGames:

    gf "Just stick by me ok? I don't want to get lost in the crowd by myself"

    ni "No promises~~~, maybe if you are all alone something special will happen~" 

    gf "...Maybe"

    gf "H-hey! Where are you going?"

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

    gf "(She really left me! I can't believe it, this is the fifth time this has happened!)"   

    gf "(...)"

    gf "(Well nevermind I guess I can believe it)"

    gf "(UGH! Where is she? There are so many people here I can't find her!)"

    scene bg blacksquare
    with Dissolve(0.5)

    "{cps=50}{i}[gf] then pushed through the crowd to see where her friend went, that was when...{/i}"

    scene bg disco
    with Dissolve(0.5) 

    gf "Excuse me, excuse me, excu-"

    show gf happy at left

    show mc happy at moveLeft:
    pause 0.25
    with vpunch

    scene bg blacksquare
    with Dissolve(0.5)

    i "{cps=25}{i}It was straight out of a visual novel, she walked into the dance circle and I just bumped into her{/i}"

    i "{cps=25}{i}That is how [gf] and I met{/i}"

    scene bg disco 
    with Dissolve(0.5)

    show gf animated at left
    
    gf "O-ow"

    show gf happy at left

    show mc animated at right

    i "Oh shoot, I'm so sorry! I was moving too fast to stop, are you ok?"

    show mc happy at right

    show gf animated at left

    gf "I'm fine, I was pushing my way through the crowd so it was entirely my bad"

    show gf happy at left

    show mc animated at right

    i "Pushing through the crowd, so you are here to dance with me huh? The dancing king, well it seems I have found my dancing queen"

    show mc happy at right

    show gf animated at left

    gf "No i-"

    show gf happy at left

    menu:
        i "{cps=25}{i}I didn't let her finish her sentence, I grabbed her hand and we began dancing{/i}"
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

    # GET DONE EARLY SO YOU CAN ADD IN A DDR MINIGAME BROOOOOOO USING "THROW MYSELF" BY SNOW STRIPPERS

    i "{cps=25}{i}I can tell she had never danced before, so I mostly led and she followed{/i}"

    i "{cps=25}{i}After a while I didn't need to lead anymore, we just danced in sync, it was a sight straight out of Dirty Dancing{/i}"

    show gf happy at left:
        rotate 0
        linear 10.0 rotate 360
        repeat

    show mc happy at right:
        rotate 0
        linear 10.0 rotate 360
        repeat       

    i "{cps=25}{i}We danced for{cps=15}...I don't know how long, but I started to feel tired and noticed her eyelids get heavier{/i}"

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

    i "{cps=25}{i}I wasn't a dense idiot, I could tell she wanted my phone number but didn't want to say it{/i}"

    hide mc happy

    show mc animated at right:

    i "Oh yeah, {a=jump:phoneNumber}let me give you my phone number{/a}! You're a pretty good dancer so maybe we can destroy the dance floor again sometime!"

    jump skipConvo

    label phoneNumber:           

    $ phoneNumber = True 

    if phoneNumber:
        $ smile = True
        i "{cps=25}{i}My phone number is 425-749-****, I gave it to her and she {a=jump:smile}smiled{/a}{/i}."
    else:
        jump skipConvo    

    label skipConvo:

    $ smile = False    

    label smile:

    if smile:     
        i "{cps=25}{i}It was the cutest, most genuine smile I've ever seen, my heart couldn't stop feeling warm{/i}"    
    
    hide gf happy

    show gf animated at left

    gf "Sounds good!"

    scene bg blacksquare
    with Dissolve(0.5)

    stop music fadeout 1.0

    i "{cps=25}{i}I used the whole dancing thing as an excuse, I just wanted to see her again{/i}"

    i "{cps=25}{i}And there you go, that is how we met{/i}" 

    i "{cps=25}{i}Anyways, after hanging out here and there we finally decided to become more than friends and went on our first ever date{/i}" # For the words hanging out, insert a path where the player can see images of them hanging out and detailing the events.

    # TIMESKIP
 
#----------------------------------------------------------------------------------------------------------#

    # WATCH ROM-COM FOR DATE DIALOGUE, MAYBE THE NOTEBOOK???

    label date1:    

    scene bg tacodog1 
    with Dissolve(0.5)    

    i "{cps=25}{i}Ah taco dog, home of the taco{/i}"

    i "{cps=25}{i}This of course was not the {a=jump:dateStory}first date I ever been on{/a}, but it turns out it was her first ever date{/i}"

    jump skipDateStories

    label dateStory:

    i "{cps=25}{i}I've been on some dates throughout highschool, actually there is one that stands out{/i}"

    i "{cps=25}{i}This one girl I went out with always talked about this game called SpineCraft{/i}"

    i "{cps=25}{i}It was a game where you could choose how your body would decompose, and in the end you always turned into something without a spine{/i}"

    i "{cps=25}{i}...She was such a weird person, who would play such a game? I guess that explains why she was always so jittery{/i}"    

    label skipDateStories:

    i "{cps=25}{i}I brought [gf] to the greatest eating establishment at our college, Taco Dog{/i}"

    i "{cps=25}{i}Authentic mexican cuisine, 3 michelin stars, THE place to go on campus{/i}"
    
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

    show bg tacodoginside
    with Dissolve(0.5)

    i "{cps=25}{i}After greeting each other, we go into the restaurant, and take our seat{/i}"
    
    i "{cps=25}{i}After chatting for a little while, our waiter finally comes to take our order{/i}"

    show widget happy at center:
    with Dissolve(0.5)

    i "{cps=25}{i}I couldn't believe it! The owner of this place, [w] taking our order!{/i}"

    show mc happy at right:
    with Dissolve(0.5)

    show gf happy at left:
    with Dissolve(0.5)

    i "{cps=25}{i}The owner of this place doesn't talk at all, many say it is because he shows his pride in silence{/i}"

    menu:
        i "{cps=25}{i}He has a menu attached to his back along with a pen where we choose what we want{/i}"
        "----->[q]<-----":
            jump quesoBurrito
        "----->[t]<-----":
            $ s = 1
            jump quesoBurrito
        "----->[f]<-----":
            $ s = 2
            jump quesoBurrito

    label quesoBurrito:            

    if s == 0:    

        i "{cps=25}{i}I order the [q], [gf] then looks at me in astonishment{/i}"

    if s == 1:
        
        i "{cps=25}{i}I order the [t], [gf] then looks at me in astonishment{/i}"

    if s == 2:

        i "{cps=25}{i}I order the [f], [gf] then looks at me in astonishment{/i}"

    hide gf happy

    show gf animated at left
   
    gf "Wait what? I don't see that on the menu"

    show gf happy at left

    i "{cps=25}{i}I thought she was just playing a funny joke at the time so I just laughed it off{/i}"

    i "{cps=25}{i}It was now just me and her, together{/i}"

    i "{cps=25}{i}...{/i}"

    i "{cps=25}{i}Shi- what do I say?{/i}"

    i "{cps=25}{i}I've been on many dates before, why do I-{/i}"

    gf "Why do you look so nervous? Are you doing alright?"

    i "Yeah! I'm doing perfectly fine, what about you?"

    i "{cps=25}{i}Wait I already asked how she was! What are you doing [i]???{/i}"

    gf "About the same as I was a few minutes ago, unlike you who is PRETTY {a=jump:aFewMinutesAgo}different from a few minutes ago *chuckles*{/a}"

    jump skipAFewMinutesAgo

    label aFewMinutesAgo:

    i "{cps=25}{i}Her laugh was so adorable, my heart <3{/i}"   

    i "*chuckles* yeah, I mean being in the presence of Aphrodite will make any man nervous"

    "{b}[gf]'s face turns cherry red{/b}"

    i "{cps=25}{i}I now feel less nervous{/i}"

    label skipAFewMinutesAgo:
    
    i "{cps=25}{i}After waiting for a while, [w] comes back with our food, which is on a tray on his back{/i}"

    menu:
        "----->Take Food<-----":
            jump takeFood

    label takeFood:        

    if s == 0:    

        i "{cps=25}{i}I take a bite out of my [q], then something wierd happens{/i}"

    if s == 1:

        i "{cps=25}{i}I order the [t], [gf] then looks at me in astonishment{/i}"    

    if s == 2:

        i "{cps=25}{i}I order the [q], [gf] then looks at me in astonishment{/i}"        

    i "{cps=25}{i}I started to feel queasy{/i}"

    show bg tacodoginside

    i "{cps=25}{i}My vision gets weird and strange, the world turns into an unrecognizable mess{/i}"

    i "{cps=25}{i}Then...{/i}"

    w "Greetings [i]"

    i "{cps=25}{i}Yes, that's right, [w] fed talking to me{/i}"

    label menu1:

    menu:
        i "{cps=25}{i}Only I could understand him, no one else could{/i}"
        "Conversation Information":
            jump widget

        "Burrito Informatin (important)":
            jump burritoDialogue 

#----------------------------------------------------------------------------------------------------------#

    label burritoDialogue:

    i "{cps=25}{i}I had the delicious [q]{/i}"

    i "{cps=25}{i}Only 650 calories{/i}"

    i "{cps=25}{i}And for oly $4.39? what a deal!{/i}"

    i "{cps=25}{i}It is also a beautifully constructed piece of art{/i}"

    i "{cps=25}{i}All contained in a warm quesadilla, the ingredients delicious and numerous{/i}"

    i "{cps=25}{i}Filled with sour cream, seasoned rice, seasoned beef, cheese, chipotle sauce, and guac{/i}"

    i "{cps=25}{i}But that is just the base [q]{/i}"

    i "{cps=25}{i}The one I had had all those ingredients in them as well as hot sauce, beans, and chicken{/i}"

    i "{cps=25}{i}I got mine fully loaded{/i}"

    i "{cps=25}{i}And what makes the [q] also special is that the burrito itself is surrounded by ANOTHER tortilla{/i}"

    i "{cps=25}{i}A tortilla filled with nacho cheese{/i}"

    i "{cps=25}{i}So the full list of ingredients are{/i}"  

    jump menu1

#----------------------------------------------------------------------------------------------------------#

    label widget:

    # WRITE MORE DIALOGUE ABOUT WHAT MC AND WIDGET TALKED ABOUT

    w ""
    
    i "{cps=25}{i}I blacked out{/i}"

    "{i}NEXT DAY{/i}"

    i "{cps=25}{i}I didn't remember anything that happened yesterday, {/i}"

    i "{cps=25}{i}What happened after I took a bite of the burrito?{/i}"

    i "{cps=25}{i}I was feeling sick, so I went to the bathroom and then...{/i}"

    scene bg bald 
    with Dissolve(0.5)

    i "{cps=25}{i}Yes, I became BALD{/i}"

    i "{cps=25}{i}I couldn't believe it, my pride and joy, dissapeared{/i}"

    scene bg bald
    with hpunch

    i "WIIDDGGEETTTTT"
    
    i "{cps=25}{i}I was furious{/i}"

    scene bg bathroom
    with pushup

    i "{cps=25}{i}But then, I heard a voice in my head, and an image appeared in front of me{/i}"

    show widget happy at center:
    with Dissolve(0.5)

    i "{cps=25}{i}It was [w], I should have been angry, but when I heard him speak, my anger dissapeared{/i}"

    w "Hello [i], it seems you have completed all of the necassary steps to be able to hear me"
    
    i "{cps=25}{i}I should have felt anger but...I could only feel like I was in the presence of something greater than myself{/i}"

    i "W-what are you?"

    w "I am a seer, I am a messanger, I am a savoir, I am a traveller"

    w "And lord above, you are lucky to be recieving my divine intervention"

    # This is a section to be saved for later, a lot of dialogue, add jumpscares, spooky shiz

    scene bg eme
    with Dissolve(0.5)

    # SLIME CULT PATH

    i "{cps=25}{i}After listening to the voices for a while, I was lead to a mysterious building on campus{/i}"

    i "{cps=25}{i}A building that was visited by students and teachers alike, 'why would the voices lead me here?' I wondered{/i}"

    i "{cps=25}{i}Building ************{/i}"

    i "{cps=25}{i}And then I noticed something that I swear was not there before{/i}"

    scene bg cultentrance
    with Dissolve(0.5)
    
    i "{cps=25}{i}I was not going crazy! This was never here before, where did this come from?{/i}"

    i "{cps=25}{i}That was when I heard...{/i}"

    w "You, the chosen, understand the urge to travel into paths uncharted by your normal peers"

    w "..."

    w "Walk"

    i "N-no, it looks like it goes forever!"

    i "{cps=25}{i}Even though I felt scared, the urge to jump grew greater as the seconds passed{/i}"

    i "{cps=25}{i}And before I knew it..{/i}"

    # ADD FALLING SOUND EFFECTS, LIKE AIR OR SOMETHING IDK, ADD THUD AFTER A FEW SECONDS

    label db:

    scene bg blacksquare
    with Dissolve(0.5)

    "{b}*SQUISH*{\b}"

    i "{cps=25}{i}I fell on something soft, 'was it the bodies of others?' What broke my fall?{/i}"

    scene bg cult
    with Dissolve(0.5)

    i "{cps=25}{i}I found myself in a cave{/i}"

    $ a = 0

    jump choicesNow

    label walkBack:

    if a == 5:

        i "{cps=25}{i}I walked back to the main room of the cave{/i}"

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

    i "{cps=25}{i}I stumbled around the cave, my eyes adjusting after a few seconds{/i}"

    # ENTER IMAGE WITH INCREASED SASTURATION/BRIGHTNESS

    i "{cps=25}{i}After my eyes adjusted, I looked around to better assess my situation{/i}"

    i "{cps=25}{i}I must have fallen for what feels like ages, I never knew such a cave system existed down here{/i}"

    i "{cps=25}{i}There were many branching holes that lead to who knwos what, but it seemed like I was in some kind of 'main room'{/i}"

    i "{cps=25}{i}The 'cieling' of the place was about 15-20 feet high{/i}"

    i "{cps=25}{i}There was this strange rectangular-bed? Shaped rock around 1-5 feet in front of me{/i}"

    i "{cps=25}{i}It was the only other thing in this room that had a shape{/i}"

    i "{cps=25}{i}It seemed to be surrounded by...candles...?{/i}"

    i "{cps=25}{i}What kind of place is this...?{/i}"

    label choicesNow2:

    if a == 9:

        i "{cps=25}{i}There is no way out of here, I am trapped{/i}"

        jump continueOn

    label choicesNow3:    

    if a == 10:

        i "{cps=25}{i}I leave the pile alone{/i}"

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

        i "{cps=25}{i}Here it is again, this green pile{/i}"

        i "{cps=25}{i}Maybe it has an answer to how to get out of here? I just need some semblance of hope at this point{/i}"

        jump pile2
        
    i "{cps=25}{i}I stumbled around the cave, my eyes adjusting after a few seconds{/i}"

    i "{cps=25}{i}I look back at the pile that broke my fall{/i}"

    i "{cps=25}{i}It was all... green{/i}"

    i "{cps=25}{i}...What is this?{/i}"
    
    label pile2:

    menu:
        "----->Touch pile<-----":
            jump touchPile

        "----->Leave it alone<-----": 
            $ a = 10           
            jump choicesNow3
#----------------------------------------------------------------------------------------------------------#

label touchPile:

    i "{cps=25}{i}I leaned in and touch the pile{/i}"    

    i "{cps=25}{i}The texture was like the surface of a slug{/i}"

    i "{cps=25}{i}It was slimey, but at the same time oddly smooth{/i}"

    i "{cps=25}{i}I-It's so pleasant, I can't stop touching it!{/i}"

    i "{cps=25}{i}It was like it was made for touching! I CANT STOP{/i}"

    i "{cps=50}{i}TOUCH TOUCH TOUCH TOUCH TOUCH TOUCH{/i}"

    i "{cps=70}{i}TOUCH TOUCH TOOUUUCCHHHH{/i}"

    i "{cps=80}{i}AAAAAAAAAAAAAAA{/i}"

    i "{b}You get absorbed by the pile{/b}"

    i "{b}END{/b}"

    return 

#----------------------------------------------------------------------------------------------------------#

    label die:
    
    i "{cps=25}{i}...{/i}"

    i "{cps=25}{i}I'm done{/i}"

    scene bg credits
    with Dissolve(0.5)

    "{b}END{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    scene main_menu
    with Dissolve(0.5)

    return

#----------------------------------------------------------------------------------------------------------#

    label lookAtAltar:

    i "{cps=25}{i}I walk closer to the rectangular looking shape{/i}"

    i "{cps=25}{i}That rectangular bed shaped figure turned out to be an alter, and the moment I got closer-{/i}"

    # HAVE 2 BACKGROUNDS, 1 WITH CANDLES OFF, BUT THEN ONE WITH CANDLES ON TO GIVE AFFECT CANDLES TURNED ON

    i "{cps=25}{i}After the alter lit up, all the sudden I see that the slime I fell on was a giant slime!{/i}"

    i "{cps=25}{i}They all scattered from the pile, revealing one giant slime that was in the center of it all{/i}"

    # SHOW PNG OF JERRY

    i "W-WHAT?"

    i "W-WHAT ARE YOU? WHATS GOING ON"

    j "(speaking latin)" # JERRY SPEAKING LATIN, ASK EVAN ABOUT WHAT HE SAYS!!!! Make this clickable and jump to a label where MC says that he understands the latin perfectly or smth

    i "{cps=25}{i}I understood his latin prefectly despite never learning the language{/i}"

    i "H-How are you...? What is going on! Tasks? Why can I understand-"

    j "(Speaking latin)"

    i "M-me? Chosen for what?"

    j "(Speaking latin)"

    j "(Speaking latin)"

    i "Bu-"

    j "(Speaking latin)"

    i "I-I see"

    i "{cps=25}{i}I was confused, I was baffled, but at the same time{/i}"

    i "I-I feel like..."

    i "{cps=25}{i}Like I had a purpose now{/i}"

    j "(Speaking latin)"

    i "{cps=25}{i}At this point I fully submitted, I accepted that I have a divine entity in front of me{/i}"

    i "{cps=25}{i}I hung onto every word, eventually deciding to carry out the first task it laid before me{/i}"

    # PLAYER DOES TASKS, PUT MENU FOR TASKS, DIFFERENT PATHS AND ALL THAT STUFF

    i "{cps=25}{i}And that task was...{/i}"

    menu:
        "----->To take the life of another<-----":
            jump takeLife 

#----------------------------------------------------------------------------------------------------------#

    label takeLife:        

    i "To take the life of another"

    i "{cps=25}{i}After waiting for a bit, I was presented with a {a=jump:observe}person with a bag over their head{/a}{/i}"

    label returnFromObserve:

    i "{cps=25}{i}On each side, a cuboid slime about 3-4 feet high with arms were escorting this individual{/i}"

    i "{cps=25}{i}I heard their muffled screams, I could tell they were crying underneath that bag{/i}"

    i "{cps=25}{i}No matter{/i}"

    j "(Speaking latin)"

    i "..."

    menu:
        "----->Take Knife<-----":
            jump knife

    label knife:        

    i "{cps=25}{i}I was handed a regular kitchen knife{/i}"

    i "{cps=25}{i}The person was then escorted over to the alter, where they were forcefully put on it{/i}"

    i "{cps=25}{i}They were struggling, but then other slimes joined in to subdue them{/i}"

    i "{cps=25}{i}They each held the individuals arms and legs, the person was laid out like a starfish{/i}"
    
    i "{cps=25}{i}The slimes then released a part of themselves onto the respective body parts{/i}"

    i "{cps=25}{i}The sacrifice was now helpless, their arms and legs now stuck to the altar{/i}"

    i "{cps=25}{i}Their crying got more intense{/i}"

    menu:
        "----->COMMENCE SACRIFICE<-----":
            jump sacrificeNow

        "----->Observe sacrifice<-----":
            jump observe2


# ENTER MENU FOR SACRIFICE SHIZ

    # ADD MENU FOR SACRIFICE
    
    # SACRIFICE SCENE
    
#----------------------------------------------------------------------------------------------------------#     

    label sacrificeNow: # UHHHHH YEAH TRY TO MAKE IT FUNNY MAYBE IDK ASK GERALD HES THE DESIGNER

    i "I ignored the crying, why should I care? This person is human trash, [j] told me"
    
    j "(Speaking latin)"

    i "Yes Jerry, right away"

    menu:
        "----->Raise Knife<-----":
            jump raiseKnife

    label raiseKnife:        

    i "{cps=25}{i}I raised the knife like how Rafiki rased Simba{/i}"
    
    i "{cps=25}{i}At this point, something happened{/i}"

    i "{cps=25}{i}Maybe it was some bizarre 6th sense for survival, but the sacrifice started crying louder and struggling even harder{/i}"

    i "{cps=25}{i}It was like they could sense the knife that would pierce their flesh{/i}"

    i "{cps=25}{i}Their arms and legs became sparratic, they have now lost their voice and fell silent{/i}"

    i "{cps=25}{i}They had a mouth, but could no longer scream{/i}"

    menu:
        "----->Lower Knife<-----":
            jump lowerKnife

    label lowerKnife:        

    i "{cps=25}{i}I thrust the knife into their chest and let go{/i}"

    # ENTER SOME KIND OF STABBING SOUND EFFECT???

    menu:
        i "{cps=25}{i}I hear but faint whispers from their exhausted vocal chords, their body telling me all I need to know{/i}"
        "----->Grip Knife<-----":
            jump gripKnife

    label gripKnife:

    if s == 3:

        i "{cps=25}{b}{i}It's too late for that{/i}{/b}"

    menu:
        i "{cps=25}{i}I grip the knife{/i}"
        "----->Twist Knife<-----":
            jump twistKnife
        "----->Take Knife Out<-----"
            $ s = 3
            jump  gripKnife    

    label twistKnife:

    i "{cps=25}{i}I twist the knife"                

    i "{cps=25}{i}They started to flail, like a fish out of water{/i}"

    menu:
        i "{cps=25}{i}They started to flail, like a fish out of water{/i}"
        "----->Apply Pressure<-----":
            jump applyPressure

    label applyPressure:

    i "{cps=25}{i}{a=jump:knifeStab}I applied pressure on the knife as it pierced the sacrifices heart{/a}{/i}"

    jump skipKnifeStab

    label knifeStab:

    i "{cps=25}{i}I kept the knife in longer because why would I want it to end sooner?{/i}"

    i "{cps=25}{i}The knife itself is like a seal, keeping the sacrifice alive{/i}"

    i "{cps=25}{i}And for a moment like this, I want it to last as {cps=10}looooong as possible{/i}"    

    label skipKnifeStab:    

    menu:
        i "{cps=25}{i}They continued to flail{/i}"
        "----->Take Knife Out<-----":
            jump knifeOut

    label knifeOut        

    i "{cps=25}{i}I wait {cps=10}.....{cps=25}and then slowly pull it out"

    i "{cps=25}{i}The body lay lifeless, it is now just a shell{/i}"

    i "{cps=25}{i}It is done{/i}"

    i "I-I've done it!"

    i "[j], I did it!"

    j "(Speaking latin)"

    i "Huh? The identity doesn't matter right? Who cares who this is"

    j "(Speaking latin)"

    i "...You aren't making sense"

    i "{cps=25}{i}At the time, I knew what he was alluding to{/i}"

    i "{cps=25}{i}I....I-{/i}"

    i "{cps=25}{i}I take off the bag to reveal{/i} {a=jump:her}{b}HER{/b}{/a} {i}face{/i}" # E REVEAL PERFECT BRO CHANGING FROM THEIR TO HER

    jump skipHer
    
    label her:

    "{b}...{/b}"    

    label skipHer:

    i "I-I'm so...I just...This wasn't-"

    i "{cps=25}{i}It didn't matter what I said, words can't change what is aleady done{/i}"

    i "{cps=25}{i}My sins fangs were already at my throat{/i}"

    i "{cps=25}{i}Jerry applauds my efforts, my devotion{/i}"

    j "(Speaking latin)"

    i "{cps=25}{i}Because of [j]'s words I quickly regain my composure and accept my actions{/i}"

    i "So, what's next?"

    j "(Speaking latin)"

    i "{cps=25}{i}I nearly vommited, this is the final step?{/i}"

    i "{cps=25}{i}But [j]'s voice is one of divine power, the sickness becomes no more{/i}"

    i "{cps=25}{i}Because all shepherds eventually eat their herds{/i}"

    i "I am ready"

    i "{cps=25}{i}I then walk over to [j], then hug him{/i}"

    i "It's all Jerry now" # SHREK IS LOVE SHREK IS LIFE REFERENCE LEL

    i "{cps=25}{i}I start to get absorbed into [j]{/i}"

    i "{cps=25}{i}I feel so euphoric! Did I really deserve to be this happy?{/i}" 

    i "{cps=25}{i}I go deeper into [j], he definitely feels me now!{/i}"

    i "{cps=25}{i}After a few minutes, my body starts decomposing{/i}"

    i "{cps=25}{i}My flesh and bones become mush{/i}"

    i "{cps=25}{i}It hurts, it hurts so good{/i}"

    i "{cps=25}{i}My skin bruning in hellfire, itching all over, my bones being broken one by one{/i}"

    i "{cps=25}{i}My insides being twisted and contorted into impossible geometry, my blood on fire{/i}"

    i "{cps=25}{i}Great pain, but even greater pleasure{/i}"

    i "{cps=25}{i}This lasts for what feels like an eternity, my screams muted, my body frozen{/i}"

    i "{cps=25}{i}After a few minutes...{/i}"

    i "{cps=25}{i}I get spat out, in a new form{/i}"

    # SHOW MC SLIME FORM

    scene bg credits
    with Dissolve(0.5)

    "{b}END{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    scene main_menu
    with Dissolve(0.5)
    
    return   

#----------------------------------------------------------------------------------------------------------#

label observe2:  

    i "{cps=25}{i}I take a moment of solace to observe the body{/i}"

    i "{cps=25}{i}And that is when I realize a single strand of hair on their clothes{/i}"

    i "{cps=25}{i}It was blonde{/i}"

    i "{cps=25}{i}blonde...blonde...{cps=80}B L O N D E{/i}"

    i "{cps=25}{i}Goddammit! This is [gf]!{/i}"

    i "{cps=25}{i}I-{/i}"

    i "{cps=25}{i}This is too much! I can't do this! WHAT HAPPENED TO HER? HOW DID SHE GET SO SKINNY?{/i}"

    i "[j], this sacrifice isn't worthy of this great knife, can you please release this person and bring me another?"

    i "This person doesn't even deserve to die in this great place, lets let them live with this moment, scarring them for life"

    i "{cps=25}{i}I try desperately to reason with [j], making up any excuse to not kill her, but then...{/i}"

    j "(Speaking latin)"

    i "N-no! I can kill, this individual is just not...Grand enough! I need a bigger inidividual, more muscular, a titan, I ne-"

    j "(Yelling latin)"

    i "No! Please, don-"

    i "{cps=25}{i}I failed{/i}"

    i "{cps=25}{i}I'm sorry [gf]{/i}"

    i "{cps=25}{i}But, at least I can die with just one thought in mind{/i}"

    i "{cps=25}{i}At least in the darkest moment of my life{/i}"

    i "{cps=15}{i}I retained my humanity{/i}"

    scene bg credits
    with Dissolve(0.5)

    "{b}END{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    scene main_menu
    with Dissolve(0.5)

    return 
#----------------------------------------------------------------------------------------------------------#      

    label wayOut:

    i "{cps=25}{i}I go down one of the random paths hoping for a way out{/i}"

    i "{cps=25}{i}Thankfully my eyes adjusted a little bit, but it is stil pitch black that I can't really see anything{/i}"

    i "{cps=25}{i}I wander around until I feel a wall{/i}"

    i "{cps=25}{i}I then put my hands on the wall and follow it, making sure my hands are firmly on the wall{/i}"

    i "{cps=25}{i}I start walking{/i}"

    i "{cps=25}{i}...{/i}"

    i "{cps=40}{i}...{/i}"

    i "{cps=50}{i}...{/i}"

    i "{cps=60}{i}...{/i}"

    i "{cps=70}{i}...{/i}"

    i "{cps=25}{i}How long does this go?!{/i}"

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

    i "{cps=25}{i}I continue walking down this path{/i}"

    i "{cps=25}{i}...{/i}"

    i "{cps=25}{i}I{/i}"    

    "{b}TIME ELAPSED: 5 MINUTES{/b}"

    "{b}TIME ELAPSED: 10 MINUTES{/b}"

    "{b}TIME ELAPSED: 20 MINUTES{/b}"

    "{b}TIME ELAPSED: 40 MINUTES{/b}"

    "{b}TIME ELAPSED: 1 HOUR{/b}"

    i "{cps=25}{i}After walking for an hour, I sit on the wall to catch my breath{/i}"

    i "{cps=25}{i}After taking a break, I continue walking, the wall being my only guide and friend{/i}"

    "{b}TIME ELAPSED: 2 HOURS{/b}"

    i "{cps=25}{i}It is dark, and I am alone here{/i}"

    i "{cps=25}{i}I continue onward, realizing that I cannot turn back now{/i}"

    i "{cps=25}{i}After 4 and a half hours in this darkness, I lose my ability to think{/i}"

    "{b}TIME ELAPSED: 5 HOURS{/b}"

    "{b}TIME ELAPSED: 20 HOURS{/b}"

    # PUT IN STEPPING NOISES OR SOMETHING

    i "{cps=25}{i}I immediately snap out of it and I become more alert{/i}"

    menu:
        i "{cps=25}{i}{a=jump:listen}What the hell was that?!{/a}{/i}" # ADD PUZZLE WHERE THEY HAVE TO STOP MOVING AND LISTEN, IF THEY MOVE TOO MUCH PLAYER DIES
        "----->RUN<-----":
            $ a = 100
            jump eaten

#----------------------------------------------------------------------------------------------------------#

    label listen:    

    i "{cps=25}{i}I listen carefully{/i}"    

    i "{cps=25}{i}...{/i}"   

    menu:
        i "{cps=25}{i}Silence{/i}"
        "----->Listen<-----":
            jump listen
        "----->Walk<-----":
            jump keepWalking2    

#----------------------------------------------------------------------------------------------------------#

    label keepWalking2:

    i "{cps=25}{i}I start walking again{/i}"

    i "{cps=25}{i}...{/i}"

    # PLAY FOOTSTEP AUDIO

    menu:
        i "{cps=25}{i}{a=jump:listening}I hear footsteps again{/a}{/i}"
        "----->Keep Walking<-----":
            $ a = 6 
            jump eaten

#----------------------------------------------------------------------------------------------------------#            

    label listening:

    i "{cps=25}{i}I listen again{/i}"

    i "{cps=25}{i}...{/i}"

    menu:
        i "{cps=25}{i}{a=jump:listening}Silence{/a}{/i}"           
        "----->Walk<-----":
            jump keepWalking2

#----------------------------------------------------------------------------------------------------------#

    label eaten:

    if a == 6:

        # PLAY LOUDER FOOTSTEP AUDIO
        i "{cps=25}{i}I keep walking{/i}"

        menu:
            i "{cps=25}{i}The footsteps are becoming a deafening, {a=jump:listening}something is getting closer!{/a}{/i}"
            "----->RUN<-----":
                $ a = 7
                jump eaten

#----------------------------------------------------------------------------------------------------------#

    if a == 7:

        i "{cps=25}{i}I start running{/i}"

        i "{cps=25}{i}Whatever is chasing me is getting faster, {cps=50}the footseps start to speed up, I pick up the pace, {cps=75}I HAVE TO GET OUT OF HERE{/i}" # PUT TIE SHOELACE OPTION AT BEGINNING OF GAME ( TIE SHOELACE IF NOT EDGY)

        i "{cps=80}{i}I run as fast as I can, this thing is chasing me I-I have to run I-"

        menu:    
            i "{cps=25}{i}But then, while running, {a=jump:listen3}I don't hear anything{/a}{/i}"
            "----->Keep Running<-----":
                $ a = 9  

    if a == 9:
        
        i "{cps=25}{i}I trust my instinct and keep running, not even thinking of looking back{/i}"

        i "{cps=25}{i}Eventually...I see a dim light in the distance{/i}"

        i "{cps=25}{i}I-Freedom! I can finally get out of here, I can-{/i}"

        scene bg blacksquare
        with Dissolve(0.5)

        "{b}[i] reaches the end of the tunnel{/b}"

        i "{cps=25}{i}...{/i}"

        i "{cps=25}{i}...I-I give up{i}" 

        i "{cps=25}{i}I'm done{/i}"

        i "{cps=25}{i}I{/i}"

        i "{cps=25}{i}I went in a circle{/i}"

        jump choicesNow     

    i "{cps=25}{i}I start hauling fat ass{/i}"

    i "{cps=25}{i}What is chasing me?{/i}"

    i "{cps=70}{i}I'm running as my life depends on it, I can get out of this I can-{/i}"   

    "{cps=50}{b}[i] TRIPS ON HIS SHOELACES{/b}"

    i "{cps=25}{i}Shi-{/i}"   

    "{cps=25}{b}[i] MEETS A PAINFUL DEATH, HE SHOULD'VE TIED HIS SHOES{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    scene main_menu
    with Dissolve(0.5)

    return   

#----------------------------------------------------------------------------------------------------------#

    label listen3:
    
    i "{cps=25}{i}I stop and stay silent{/i}"

    i "{cps=25}{i}...{/i}"

    i "{cps=25}{i}All I can hear is the sound of my own heartbeat head.{/i}"

    i "{cps=25}{i}It's loud, and it's the only thing I can h-{/i}"

    # ADD SOME JUMPSCARE OR DEATH IDK

    scene bg credits
    with Dissolve(0.5)

    "{b}END{/b}"

    "{b}Made for a college class at Washington State University{/b}"

    scene bg musiccredits
    with Dissolve(0.5)

    "{b}Special thanks to Snow Strippers for giving us permission to use their song!{/b}"

    scene main_menu
    with Dissolve(0.5)

    return 

#----------------------------------------------------------------------------------------------------------#

    label observe: # Make this section something that the player can click on in the text beforehand to unlock this dialogue

    i "{cps=25}{i}They were handcuffed with their hands behind their back, their legs connected together with a chain and collar{/i}"

    i "{cps=25}{i}They were slender in build, it appeared to be the figure of a woman{/i}"

    i "{cps=25}{i}...Why does this person feel so familiar...?{/i}"    

    jump returnFromObserve

    #------------------------------------------------------#
    #   IDEAS (FOR AFTER BASE GAME IS DONE):               #
    #   - File manipulation                                #
    #   - Imagemap                                         #
    #   - Date/Time system                                 #
    #   - Choices being remembered by characters           #
    
    #   - Sound effects                                    #
    #   - Gf sacrifice ALL OUT                             #
    #   - Maybe add rythm game to dance scene              #
    #   - Maybe add a candy-crush kind of game             #
    #   - JUMPSCARES                                       #
    #   - ADD CREDITS FOR MUSIC, MUSIC USED SO FAR:        #
    #     "THROW MYSELF" - SNOW STRIPPERS                  #
    #     "01 GHOSTS I" - NINE INCH NAILS                  #
    #   - Break fourth wall by changing desktop background # 
    #------------------------------------------------------#


#---------GIRLFRIEND CHARACTER DIES-------------------#
    
