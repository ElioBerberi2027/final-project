label homeMenu:
    show officebk
    call screen homeMenuScreen
    init python:
        import random
        def rollD():
            return random.randint(1,20)

        def endOdds():
            roll = rollD()
            if roll == 1:
                renpy.jump('endGame')
            else:
                renpy.jump(partsLst[partNum])
    $ endOdds()
    
default total_cookies = 0

screen homeMenuScreen:
    grid 1 3:
        xalign .5
        yalign .5
        frame:
            textbutton "Next Event" action [SetVariable("partNum", partNum + 1), Return(value=None)]
            xysize(400,250)
            xpadding 100 ypadding 100
        frame:
            textbutton "Games" action Call("miniGameMenu")
            xysize(400,250)
            xpadding 125 ypadding 100
        frame:
            textbutton "I'm done being dictator!" action Quit()
            xysize(400,250)
            xpadding 50 ypadding 50
    image "phone.png" zoom 0.3 xalign 0.5 yalign 0.5


label miniGameMenu:
    call screen miniGames
    screen miniGames:
        grid 1 3:
            xalign .5
            yalign .5
            frame:
                textbutton "Memoria" action Jump("memoria_game")
                xysize(400,250)
                xpadding 125 ypadding 100
            frame:
                textbutton "simpleBattle" action Jump("battle_game_1")
                xysize(400,250)
                xpadding 100 ypadding 100
            frame:
                textbutton "Back" action Jump("homeMenu")
                xysize(400,250)
                xpadding 150 ypadding 75
        image "phone.png" zoom 0.3 xalign 0.5 yalign 0.5
        hbox:
            xalign 0.3 yalign 0.5
            frame:
                text "Total Cookies: [total_cookies]" size 24


