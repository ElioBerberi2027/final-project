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
    nar "Mars was terriformed into a lush paradcie planet"
    nar "Earth being crowed with prisoners sends ten million prisoners to mars"
    scene earthbk
    nar "After the completion of Project Mars, the prisoners were set free to work in Mars"
    nar "However, Earth burdened the new coloney with debt demanding the extraction of rare earth metals vital for earth's economy"
    nar "Earth's extraction forced the inhabitants to revolt and form a new society"
    scene marsbk
    nar "At the peak of the revolution a group called The Martian Action Front (MAF) seized Earth controlled police stations, millitary bases, and communications"
    nar "a populist named Taiwan Andrew took lead of the revolution and brough independence to the planet."


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
        ply "fine no problem"
        gen "Opps, sorry, the cell cell servis is terrible out here"
        jump part1


#WIP - No use rn
label office:
    show officebk
    nar "Back In Your Office-feeling good"
    gen "we have secured our population but we need to develope a stratagy to before the countryies of earth recover their logictical network"
    ply "what do you sugest?"
    gen "Well i have thought about it and the best course of action would either to be to invest in our defense or a deterrent"
    ply "Deterent?"
    gen "Yes"
    ply "Like what?"
    gen "Well if we develop a culuster bomb we can send shrapnal spinning around the earth, securing our control over the solarstem"
    ply "unethical but I understand"
    ply "Hmm... we are still dependent on earth for some rare mars resources"
    gen "Yes, the decison is yours but we may only have one shot to expolite their weakness"
    menu defenseDecision:
        "Planet Defense":
            ply "Its too dangerous if Earth intellegence finds out our revolution my be over before it begins" # we need to make 2 new labels and add these dialogues into each.
            pass
        "Build the bomb": 
            ply "Lets build the bomb, fortune favors the bold"
            pass



#factory control
label part1:

    gen "1. Now that we have freed ourselves we need to think of important issues"
    gen "The people complain of poor working conditions and subersive Anarchists demand factory autonomy"
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
        nar "in an effort to increase producttivity the planning commity has introduced Child Labor"
        gen "The people are angry with you"
        call homeMenu

    label workPeo:
        nar "The People are happy, you think you made the right choice" 
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
        how to deal with the bacteria waste build up from manufactoring."
    gen "If we dont do something soon, we will have a ecological crisis on our hands."
    gen "the people are used to having earthlike bioshpear"
    gen "What do you think we should do?"

    menu:
        "Dump it into the red sea":
            jump dumpRedSea

        "Dump it into the blue sea":
            jump dumpBlueSea

        "Do nothing":
            jump wasteDoNothing

    label dumpRedSea:
        nar "The red sea is stained with scarlet fome, the bateriea is alterning the dna of the fish"
        nar "gold fish are made of gold"
        nar "The sharks grow legs, and take over"
        gen "We're being overrun by land sharks"
        gen "Not much we can do to help."
        ply "I sugest the coastal population sell their homes"
        call homeMenu

    label dumpBlueSea:
        nar "The blue sea is now red with waste"
        nar "The people are depressed nostalga for earth incraces"
        ply "Oh... Theres nothing we can do now."
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
    gen "water has beecome more polutend by no falt of the govenmet's insustrealiation chamian." 
    gen "The scientists and buracrats propose two potential solutions."

    menu:
        "Invest in advanced water purification technology(approved by scientists)":
            jump waterTech

        "Implement strict water rationing policies (approved by buracrats)":
            jump waterRation

        "Do nothing ":
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
        gen "however the govenment maintains control of the walter supply. loctical officers become wealthy from corruption "
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
    nar "You have lost the game, the people spit on your grave"
    return