label homeMenu:
    show officebk
    call screen homeMenuScreen
    init python:
        import random
        def rollD6():
            return random.randint(1,25)

        def endOdds():
            roll = rollD6()
            if roll == 1:
                renpy.jump('endGame')
            else:
                renpy.jump(partsLst[partNum])
    $ endOdds()
    


screen homeMenuScreen:
    grid 1 3:
        xalign .5
        yalign .5
        frame:
            textbutton "Next Event" action [SetVariable("partNum", partNum + 1), Return(value=None)]
            xysize(400,250)
            xpadding 150 ypadding 125
        frame:
            textbutton "View Stats" action NullAction()
            xysize(400,250)
            xpadding 150 ypadding 100
        frame:
            textbutton "(Something else)" action NullAction()
            xysize(400,250)
            xpadding 150 ypadding 75
    image "phone.png" zoom 0.3 xalign 0.5 yalign 0.5


#Basic stats - WIP (Might not be used. Change what you want)
'''
default ecnomony = 100
default millitary = 100
default citizenHappiness = 100
default population = 100


#Upgrades - WIP (Might not be used. Change what you want)

default childLabor = False

default nukes = False
default guns = False

default propaganda = False
default foodStamps = False
    
default orphanage = False
'''


