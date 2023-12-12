define r = Character('Red Hood', color="#CD0000")
define w = Character('Wolf', color="#B5B5B5")

screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Red Hood" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value red_hood_hp
                    range red_hood_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
                text "[red_hood_hp] / [red_hood_max_hp]" size 16
                
                
    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Wolf" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value wolf_hp
                    range wolf_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
                text "[wolf_hp] / [wolf_max_hp]" size 16
                
    text "Red Hood vs. Wolf" xalign 0.5 yalign 0.05 size 30
                
# The game starts here.
label battle_game_1:
    #### Some variables that describes the game state.
    $ wolf_max_hp = 30
    $ red_hood_max_hp = 50
    $ wolf_hp = wolf_max_hp
    $ red_hood_hp = red_hood_max_hp
    init python:
        import random
        def rollD6Cookies():
            return random.randint(1, 6)
    $ starting_cookies = rollD6Cookies()
    $ cookies_left = starting_cookies * 2
    
    scene black
    
    "BATTLE START!"

    jump battle_1_loop


label battle_1_loop:
    
    #### Let's show the game screen.
    #
    show screen simple_stats_screen
    
    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    while (wolf_hp > 0) and (red_hood_hp > 0):
        show girl with Dissolve(0.3)
        menu:
            "Atack!":
                $ wolf_hp -= 2
                r "K-y-aaa!!!11 (damage dealt - 2hp)"

            "Throw a cookie (got [cookies_left] cookies left)" if cookies_left > 0:
                $ wolf_hp -= 5
                $ cookies_left -= 1
                r "YEETUS DELETUS (damage dealt - 5hp)"
                
            "Eat cookie (got [cookies_left] cookies left)" if cookies_left > 0:
                $ red_hood_hp = min(red_hood_hp+5, red_hood_max_hp)
                $ cookies_left -= 1
                r "Mmm, tasty... (restore 5hp)"
        
        $ wolf_damage = renpy.random.randint(1, 6)
        
        $ red_hood_hp -= wolf_damage
        
        hide girl with Dissolve(0.3)
        
        show wolf with Dissolve(0.3)
        w "RrrrrRRrrrr! {i}*wolf bites you*{/i} (damage dealt - [wolf_damage]hp)" 
        hide wolf with Dissolve(0.3)
    #
    ####        
        
    hide screen simple_stats_screen
    
    if wolf_hp <= 0:
        if red_hood_hp <= 0:
            "Double KO"
            
        else:
            r "VICTORY!"
            r "Finally, I've got to my grandmother's house!"
            
    else:
        w "Om-nom-nom-nom {i}*wolf ate you all up*{/i} (along with the basket, of course...)"
    
    jump battle_1_ending
        
label battle_1_ending:
    $ total_cookies = total_cookies + cookies_left
    "You've got [cookies_left] cookies!"
    jump homeMenu