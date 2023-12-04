label homeMenu:
    show officebk
    call screen homeMenu
    nar "text test" 
    return


screen homeMenu:
    grid 1 3:
        xalign .5
        yalign .5
        frame:
            textbutton "Next Event" action NullAction()
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


