# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gen = Character("General")
define ply = Character("Taiwan Andrew")
define earthguy = Character("Michael")
define alien = Character("Two Kids In A Trench Coat")
define nar = Character("Narrator")

# The game starts here.

label start:

    nar "Long ago in the depths of space..."
    nar "The year is 2092, and Earth is expanding its logistics across the solar system"
    nar "Mars was the primary victim of this expansion, with heavy farming of the planet"
    nar "The people who work and live there are all prisoners of Earth"
    nar "After the completion of Project Mars, the prisoners were set free to work in Mars"
    nar "However, Earth extracted every resource in the planet leaving it poulluted and on the brink of collapse"
    nar "This forced the new inhabitants to revolt and form a new society"
    nar "At the peak of the revolution a group called The Martian Action Front (MAF) seized Earth controlled police stations, millitary bases, and communications"
    nar "A man, a strong man named Taiwan Andrew took lead of the revolution and brough independence to the planet."

    gen "Dear Leader, you have recieved a message from your mother"
    gen "Would you like to answer"

    menu:
        "yes":
            ply "Yeah Answer It"
            jump momConvoYes
        "no":
            ply "Im busy right now"
            jump momConvoNO

label home:
    "Youre home"

label momConvoYes:
    "No Service Can Not Complete"
    ply "Damn, well anyway"
    jump part1

label momConvoNO:
    gen "She insists"
    ply "NO I CAN NOT, MY LANES ARE FEEDING, I WANT THREE WINNING LANES NOT A CALL FROM MOM"
    gen "Okay i will tell her youre busy"
    jump part1

label part1:

    gen "Now that we have freed ourselves we need to think of important issues"
    gen "The people complain of poor working conditions and the Anarchists scream for factory autonomy"
    gen "What shall we tackle first"

    menu:
        "Better working conditions, control of factories to government":
            jump workGov

        "Better working conditions, control of factories to the people":
            jump workGov

        "Send this to comittee for revision (Do nothing)":
            jump workGov
label workGov:
    scene BG workerscry
    nar "Income decrease, popularity decreases"
    nar "Child Labor Introduced"
    gen "The people seem to be happier, but keeping factory control made them angry"
    jump home

label workPeo:
    pass    
label comittee:
    pass