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


# Nagivate through different parts of the story
# partNum starts @ 1 b/c start label is 0, partNum = 1 is part1, and etc.
default partNum = 1
default partsLst = [
    "start", 
    "part1", 
    "part2", 
    "part3", 
    "part4", 
    "part5", 
    "part6",
    "part7",
    "part8",
    "part9",
    "part10",
    "part11",
    "part12",
    "part13",
    "part14",
    "part15",
    "part16",
    "part17",
    "part18",
    "part19",
    "part20"
]


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


    label momConvoYes:
        "No Service Can Not Complete"
        ply "Damn, well anyway"
        jump part1

    label momConvoNO:
        gen "She insists"
        ply "NO I CAN NOT, MY LANES ARE FEEDING, I WANT THREE WINNING LANES NOT A CALL FROM MOM"
        gen "Okay i will tell her youre busy"
        jump part1


#WIP - No use rn
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



#factory control
label part1:

    gen "1. Now that we have freed ourselves we need to think of important issues"
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
        call homeMenu

    label comittee:
        nar "It has been almost 3 months since they asked and nothing has been done"
        nar "The people are very angry"
        nar "A revolt happened"
        gen "You have somehow managed to start a coup this early on"
        gen "Not much i can do to help"
        ply "Oh... Theres nothing we can do"
        jump endGame



#waste management - WIP (Change what you want)
label part2:
    
    gen "2. Our next order of business is to determine 
        how to deal with the waste build up from manufactoring."
    gen "If we dont do something soon, we will have a crisis on our hands."
    gen "What do you think we should do?"

    menu:
        "Dump it into the red sea":
            jump dumpRedSea

        "Dump it into the blue sea":
            jump dumpBlueSea

        "Do nothing":
            jump wasteDoNothing

    label dumpRedSea:
        nar "The red sea is stained with scarlet rot"
        nar "The sharks grow legs, and take over"
        gen "We're being overrun by land sharks"
        gen "Not much I can do to help."
        ply "Oh... Theres nothing we can do."
        call homeMenu

    label dumpBlueSea:
        nar "The blue sea is now red with waste"
        nar "The people are angry."
        nar "A revolt happened."
        gen "You have somehow managed to start a coup this early on."
        gen "Not much I can do to help."
        ply "Oh... Theres nothing we can do."
        call homeMenu

    label wasteDoNothing:
        nar "The waste has built up and is now a problem."
        nar "The people are angry."
        nar "A revolt happened."
        gen "You have somehow managed to start a coup this early on."
        gen "Not much i can do to help."
        ply "Oh... Theres nothing we can do."
        jump endGame



#water management - WIP (Change what you want)
label part3:
    gen "3. As our Martian colony grows, a new challenge emerges."
    gen "The scarcity of vital resources like water becomes a pressing issue."
    gen "The scientists propose two potential solutions."

    menu:
        "Invest in advanced water purification technology":
            jump waterTech

        "Implement strict water rationing policies":
            jump waterRation

        "Do nothing":
            jump waterDoNothing

    label waterTech:
        scene BG_waterPurification
        nar "The investment in advanced water purification technology pays off."
        nar "Our colony now has access to cleaner and more abundant water."
        gen "The scientists are delighted, and the overall morale of the colony improves."
        call homeMenu

    label waterRation:
        nar "The strict water rationing policies are implemented, causing dissatisfaction among the colonists."
        nar "Protests break out, and some citizens begin hoarding water in secret."
        gen "While water usage decreases, tension rises, and the social fabric weakens."
        call homeMenu

    label waterDoNothing:
        nar "The decision to defer the issue results in a temporary relief, but the problem persists."
        nar "The scarcity of water continues to be a concern, and some residents grow anxious."
        gen "The scientists urge you to address the issue before it escalates further."
        jump homeMenu



#military vs. people - WIP (Change what you want)
label part4:
    gen "4. As tensions rise on Mars, concerns about security become a focal point of discussion."
    gen "The military leaders advocate for a significant increase in defense spending."
    gen "On the other hand, the citizens are expressing discontent due to the allocation of resources away from social programs."

    menu:
        "Invest heavily in military and security measures":
            jump militaryInvestment

        "Prioritize social programs and citizens' well-being":
            jump socialPrioritization

        "Delay the decision and assess the situation later (Do nothing)":
            jump delayDecision

    label militaryInvestment:
        scene BG_militaryBase
        ply "We need to invest in our military, we need to be able to defend ourselves"
        nar "The military investment strengthens our defense capabilities, but at a cost."
        nar "Citizens experience a decrease in public services, and some express dissatisfaction."
        gen "The sense of security increases, but at the expense of the overall happiness of the people."
        call homeMenu

    label socialPrioritization:
        ply "We need to prioritize the well-being of our citizens, they are the ones who make this colony possible"
        nar "Prioritizing social programs improves the well-being of the citizens."
        nar "However, the military is concerned about potential vulnerabilities and protests escalate."
        gen "The overall happiness of the people increases, but the risk of external threats grows."
        call homeMenu

    label delayDecision:
        ply "We need to delay the decision, we need to assess the situation before making a decision"
        nar "Delaying the decision maintains a fragile balance, but neither military nor social concerns are fully addressed."
        nar "Tensions persist, and there's a growing sense of uncertainty among the population."
        gen "The situation may escalate if not decisively handled in the future."
        call homeMenu



label endGame:
    scene BG YouDied
    nar "You have lost the game, your father is disapointed in you, he was really relying on you for the 401k"
    return