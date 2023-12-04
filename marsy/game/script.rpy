# The script of the game goes in this file.

# here im declaring all background images as image (name) = filename
# you can declare these by writing scene (var name)
image officebk = "BG office.png"
image ssbk = "BG solarsystem.png"
image earthbk = "BG earth.png"
image marsbk = "BG marsinvaded.png"
image roomdatdaybk = "BG roomatday.jpg"
image roomatnightbk = "BG roomatnight.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gen = Character("General")
define ply = Character("Taiwan Andrew")
define earthguy = Character("Michael")
define alien = Character("Two Kids In A Trench Coat")
define nar = Character("Narrator")

# The game starts here.

label start:
    camera:
        perspective True
        
    scene ssbk
    nar "Long ago in the depths of space..."
    nar "The year is 2092, and Earth is expanding its logistics across the solar system"
    nar "Mars was the primary victim of this expansion, with heavy farming of the planet"
    scene earthbk
    nar "The people who work and live there are all prisoners of Earth"
    nar "After the completion of Project Mars, the prisoners were set free to work in Mars"
    nar "However, Earth extracted every resource in the planet leaving it poulluted and on the brink of collapse"
    nar "This forced the new inhabitants to revolt and form a new society"
    scene marsbk
    nar "At the peak of the revolution a group called The Martian Action Front (MAF) seized Earth controlled police stations, millitary bases, and communications"
    nar "A man, a strong man named Taiwan Andrew took lead of the revolution and brough independence to the planet."


    scene officebk

    gen "Dear Leader, you have recieved a message from your mother"
    gen "Would you like to answer?"

    menu:
        "Yes":
            ply "Yeah answer it"
            jump momConvoYes
        "No":
            ply "Im busy right now"
            jump momConvoNO

label office:
    show officebk
    nar "Youre In Your Office"
    gen "The people have rested but theres still a lot to do"
    ply "Yeah there is, dont worry we will figure everything out and make Mars a better home for us"
    gen "Next we should probably try to figure out what to do when Earth Decides to be a problem"
    ply "Yes that would be a good idea but what shall we do?"
    gen "Well i have thought about it and the best course of action would either to be to invest in our defense or a deterrent"
    ply "Deterent?"
    gen "Yes"
    ply "Like what?"
    gen "Well during my time as a general for the United States we were researching a new kind of bomb"
    ply "What bomb?"
    gen "We called it the planet destroyed, a cobalt bomb"
    ply "Why cobalt?"
    gen "Well if you add cobalt inside of a nuclear bomb..."
    gen "It will definitely destroy all life in a planet"
    ply "Hmm..."
    menu defenseDecision:
        "Planet Defense":
            ply "Its too dangerous, we should invest in defending our planet of threats" # we need to make 2 new labels and add these dialogues into each.
            pass
        "Build the bomb": 
            ply "Lets build the bomb, if we cant live free, no one shall"
            pass

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
            jump workPeo

        "Send this to comittee for revision (Do nothing)":
            jump comittee

label workGov:
    scene BG workerscry
    nar "Income decrease, popularity decreases"
    nar "Child Labor Introduced"
    gen "The people seem to be happier, but keeping factory control made them angry"
    call homeMenu

label workPeo:
    nar "The People are happy, you made the right choice" 
    pass

label comittee:
    nar "It has been almost 3 months since they asked and nothing has been done"
    nar "The people are very angry"
    nar "A revult happened"
    gen "You have somehow managed to start a coup this early on"
    gen "Not much i can do to help"
    ply "Oh... Theres nothing we can do"
    jump EndGame


label EndGame:
    scene BG YouDied
    nar "You have lost the game, your father is disapointed in you, he was really relying on you for the 401k"
    return