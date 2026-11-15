# CHARACTERS

define hedge = Character('DAVEN', color="#FFA500")
define worm = Character('WORM', color="#FFA500")
define LEINARD = Character('LEINARD', color="#FFA500")
define star = Character('STAR', color="#FFA500")


default parts = 0


transform big:
    zoom 4.0

# screenssss

screen forest:

    imagebutton:
        xpos 0.5
        ypos 0.5
        idle "worm chalant.png"
        action Jump("worm")

    imagebutton:
        xpos 0.0
        ypos 0.2
        idle "alien.png" at big
        action Jump("alien")
    

    imagebutton:
        xpos 0.6
        ypos 0.4
        idle "ladder.png"
        action Jump("ladder")


        
        




transform zoom_dissolve:
    alpha .0
    linear .5 alpha 1.0
    on hide:
        alpha 1.0 zoom 1.0
        linear .5 alpha .0 


transform bounce:
    yalign 0.6
    linear 0.9 yalign 0.0
    linear 0.7 yalign 0.6

transform bounce2:
    yalign 0.6
    linear 0.9 yalign -2.0

transform bounce3:
    yalign 2.0
    linear 1 yalign -2.0

transform bounce4:
    yalign -2.0
    xalign 0.7
    linear 1 yalign 0.8




# The game starts here.

label start:
    play music "audio/song.mp3"
    scene autumn
    show trampoline:
        zoom 0.7
        xpos 0.1
        ypos 0.4
    "DAVEN was jumping on his trampoline when a TERRIBLE MISFORTUNE befell him... " 

    show hedge normal at bounce:
        xpos 0.35
    pause 1.6
    stop sound
    show hedge normal at bounce:
        xpos 0.35
    pause 1.6
    stop sound
    show hedge normal at bounce2:
        xpos 0.35
    pause 1
    stop sound
    scene space
    show hedge normal at bounce3:
        xpos 0.35
    pause 1
    scene black
    play sound "audio/crash.mp3"
    pause 2.5

    
    scene place with fade


    show hedge normal:
        zoom 2


    hedge "Oh dear... where have I ended up?"
    show worm chalant at zoom_dissolve:
        zoom 3
        xpos 0.4
        ypos -0.2
    worm "OHMYGOD PLEASE DONT EAT ME"
    hedge "I—"
    worm "PLEASE HAVE MERCY"
    hedge "I'm not going to eat you!"
    worm "oh"
    hedge "My trampoline bounced me over here and now idk how to get back ):"
    worm "hmmmm"
    worm "wait wait here me out.... what if you make ANOTHER trampoline to bounce you back???"
    show screw at zoom_dissolve:
        ypos 0.45
        xpos 0.7
        zoom 4
    worm "here's a piece to start you out!"
    $ parts += 1
    hide hedge
    hide worm
    hide screw
  
        
    call screen forest

label alien:
    if parts < 3:
        show alien:
            zoom 7
            xpos 0.3
        LEINARD "gleep glorp"
        $ parts += 1
        show alien smile:
            zoom 7
            xpos 0.3
        "(Leinad the IIrd gave you his parachute)"
        hide alien smile
        call screen forest
    else:
        show alien smile:
            zoom 7
            xpos 0.3
        show steel 
        LEINARD "yoooooooo i have steel for you.... because you steel my heart...."
        $ parts += 1
        hide steel
        hide alien smile
        call screen forest

label worm:
    menu:
        "Eat":
            worm "AGHHHHHHHHH"
            "*you feel really regretful*"
            "really sad ending"
            return
        "how many parts i got":
            worm "You have [parts]/4 parts"
        "I'm ready to go home.":
            if parts < 4:
                worm "home isn't ready for you..."
                call screen forest
            else:
                worm "ok! let's go build the trampoline!"
                jump home
        "nvm":
            call screen forest

label home:
    scene place
    show trampoline:
        zoom 0.7
        xpos 0.1
        ypos 0.4
    worm "well, we finished."
    worm "just one question... do you truly want to leave?"
    menu:
        "Yes":
            worm "Ok. Goodbye, friend!"
            jump bye
        "No":
            worm "huh. I guess you'll just stay here with us then!"
            "New Home Ending!"
            return

label bye:
    play sound "audio/jump.mp3"
    show hedge normal at bounce2:
        xpos 0.35
    pause 1.6
    stop sound
    scene space
    show hedge normal at bounce3:
        xpos 0.35
    pause 1
    scene autumn
    show trampoline
    show hedge normal at bounce4:
        xpos 0.35
    pause 1
    "Bounced Back Ending!"
    return



label ladder:
    "*you found a ladder*"
    $ parts += 1
    hide ladder
    call screen forest


        
