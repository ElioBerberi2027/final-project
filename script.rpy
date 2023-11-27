# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    
    menu:
        "Memoria":
            call memoria_game
        "Simple battle game":
            call battle_game_1
        "none":
            pass

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy


    
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "more text woo"

    # This ends the game.

    return

label finishedMiniGame:
    show eileen happy
    e "You finished the minigame!"
    return