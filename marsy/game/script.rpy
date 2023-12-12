# The script of the game goes in this file.

# here im declaring all background images as image (name) = filename
# you can declare these by writing scene (var name)
image officebk = "BG office.png"
image ssbk = "BG solarsystem.png"
image earthbk = "BG earth.png"
image marsbk = "BG marsinvaded.png"
image roomdatdaybk = "BG roomatday.jpg"
image roomatnightbk = "BG roomatnight.jpg"
image youDiedbk = "BG YouDied.jpg"
image workerscrybk = "BG workerscry.png"
image classim = "BG class.png"
image beachclean = "BG waterpuri.png"
image waterscare = "BG waterscares.png"
image bluebeach = "BG bluesea.png"
image redbeach = "BG redbeach.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# gen "text" gives you normal picture
# gen 2 "text" gives you the head down picture
# gen point "text" gives you the point picture
define gen = Character("General", image="gen")
image side gen = "gen stand head up.png"
image side gen 2 = "gen stand head down.png"
image side gen point = "gen point.png"
image sebscreen = "sab looking at reddit.jpg"
image eliobech = "elio beach.png"
define elio = Character("Elio")
define ply = Character("Taiwan Andrew")
define earthguy = Character("Michael")
define alien = Character("Two Kids In A Trench Coat")
define nar = Character("Narrator")
define teach = Character("Teacher")
define sab = Character("Sab")

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
    "part20",
    "endGame"
]


init python:
    pass


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


    scene officebk with Dissolve(0.5)

    gen "Dear Leader, you have recieved a message from your mother" 
    gen "Would you like to answer?"

    menu:
        "Yes":
            ply "Yeah answer it"
            jump part10
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


#factory control
label part1:
    nar "1."
    gen "Now that we have freed ourselves we need to think of important issues."
    gen 2 "The people complain of poor working conditions and the Anarchists scream for factory autonomy."
    gen point "What shall we tackle first?"

    menu:
        "Better working conditions, control of factories to government":
            jump workGov

        "Better working conditions, control of factories to the people":
            jump workPeo

        "Send this to comittee for revision (Do nothing)":
            jump comittee

    label workGov:
        scene workerscrybk
        nar "Income decrease, popularity decreases"
        nar "Child Labor Introduced"
        gen "The people seem to be happier, but keeping factory control made them angry"
        jump homeMenu

    label workPeo:
        nar "The People are happy, you made the right choice" 
        jump homeMenu

    label comittee:
        nar "It has been almost 3 months since they asked and nothing has been done"
        nar "The people are very angry"
        nar "A revolt happened"
        gen "You have somehow managed to start a coup this early on"
        gen point "Not much i can do to help"
        ply "Oh... Theres nothing we can do"
        jump endGame



#waste management - WIP (Change what you want)
label part2:
    nar "2."
    gen "Our next order of business is to determine how to deal with the waste build up from manufactoring."
    gen 2 "If we dont do something soon, we will have a crisis on our hands."
    gen point "What do you think we should do?"

    menu:
        "Dump it into the red sea":
            jump dumpRedSea

        "Dump it into the blue sea":
            jump dumpBlueSea

        "Inform citizens to ignore it (Do nothing)":
            jump wasteDoNothing

    label dumpRedSea:
        scene redbeach
        nar "The red sea is stained with scarlet rot."
        nar "The sharks grow legs wanting to escape the waste."
        gen "Good job, you have created a new species of shark!"
        elio "Scary!"
        ply "I dont think thats a good thing."
        jump homeMenu

    label dumpBlueSea:
        scene bluebeach
        nar "The blue sea is now red with waste."
        nar "The fish lose their i's, and become fsh."
        gen "Good job, you have created a new species of fish!"
        gen point "Perhaps it'll make for good food."
        ply "Not sure thats healthly."
        elio "Yum"
        jump homeMenu

    label wasteDoNothing:
        nar "The waste has built up and is now a problem."
        nar "The people are angry."
        nar "A revolt happened."
        gen "You have somehow managed to start a coup this early on."
        gen point "Not much i can do to help."
        ply "Oh... Theres nothing we can do."
        jump endGame



#water management - WIP (Change what you want)
label part3:
    nar "3."
    gen "As our Martian colony grows, a new challenge emerges."
    gen 2 "The scarcity of vital resources like water becomes a pressing issue."
    gen point "The Council propose two potential solutions."

    menu:
        "Invest in advanced water purification technology":
            jump waterTech

        "Implement strict water rationing policies":
            jump waterRation

        "Defer the decision to a future date (Do nothing)":
            jump waterDoNothing

    label waterTech:
        scene beachclean
        nar "The investment in advanced water purification technology pays off."
        nar "Our colony now has access to cleaner and more abundant water."
        gen "The Council are delighted, and the overall morale of the colony improves."
        show eliobech
        elio "Its good!"
        jump homeMenu

    label waterRation:
        scene waterscare
        nar "The strict water rationing policies are implemented, causing dissatisfaction among the colonists."
        nar "Protests break out, and some citizens begin hoarding water in secret."
        gen "While water usage decreases, tension rises, and the social fabric weakens."
        show eliobech
        elio "Its bad!"
        jump homeMenu

    label waterDoNothing:
        scene office
        nar "The decision to defer the issue results in a temporary relief, but the problem persists."
        nar "The scarcity of water continues to be a concern, and some residents grow anxious."
        gen "The Council urge you to address the issue before it escalates further."
        jump homeMenu



#military vs. people - WIP (Change what you want)
label part4:
    nar "4."
    gen "As tensions rise on Mars, concerns about security become a focal point of discussion."
    gen 2 "The military leaders advocate for a significant increase in defense spending."
    gen point "On the other hand, the citizens are expressing discontent due to the allocation of resources away from social programs."

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
        jump homeMenu

    label socialPrioritization:
        ply "We need to prioritize the well-being of our citizens, they are the ones who make this colony possible"
        nar "Prioritizing social programs improves the well-being of the citizens."
        nar "However, the military is concerned about potential vulnerabilities and protests escalate."
        gen "The overall happiness of the people increases, but the risk of external threats grows."
        jump homeMenu

    label delayDecision:
        ply "We need to delay the decision, we need to assess the situation before making a decision"
        nar "Delaying the decision maintains a fragile balance, but neither military nor social concerns are fully addressed."
        nar "Tensions persist, and there's a growing sense of uncertainty among the population."
        gen "The situation may escalate if not decisively handled in the future."
        jump homeMenu



#growing food - WIP (Change what you want) - Has meme option
label part5:
    nar "5."
    gen "My liege! The people are hungry!"
    gen 2 "Agriculture is a crucial aspect of sustaining life on Mars, but our current crop yields are insufficient."
    gen point "The Council propose two different approaches to address this issue."

    menu:
        "Invest in advanced hydroponic and aeroponic systems":
            jump advancedSystems

        "Explore genetically modified crops for increased yield":
            jump modifiedCrops

        "As the famous royalty once said, 'Let them eat cake' (Secret?)":
            jump eatCake

    label advancedSystems:
        scene BG_hydroponicFarm
        nar "Investing in advanced hydroponic and aeroponic systems leads to more efficient crop production."
        nar "However, the initial investment is high, and it takes time for the benefits to be fully realized."
        gen "The Council are optimistic, but there is pressure to address immediate food shortages."
        jump homeMenu

    label modifiedCrops:
        nar "Exploring genetically modified crops results in quick gains in crop yield."
        nar "However, concerns about the long-term impact on the Martian ecosystem and public health arise."
        gen "The colonists are divided on whether the benefits outweigh the potential risks."
        jump homeMenu

    label eatCake:
        nar "Delaying the decision means sticking with the current agricultural methods."
        nar "While familiar, they continue to face challenges, and food shortages persist."
        gen "The citizens grow increasingly concerned about the sustainability of the colony."
        jump endGame



#new emerging relgion called "Astolfoism" - WIP (Change what you want)
label part6:
    nar "6."
    gen "A new and peculiar religion called 'Astolfoism' has started gaining followers among the colonists."
    gen "The believers are devoted to a charismatic figure named Astolfo, who they claim is the key to enlightenment."
    gen "The Council propose two different approaches to deal with this emerging religious movement."

    menu:
        "Embrace Astolfoism and integrate it into Martian society":
            jump embraceAstolfoism

        "Monitor Astolfoism from a distance and ensure it doesn't disrupt societal harmony":
            jump monitorAstolfoism

        "Host a 'Femboy Party' to celebrate diversity (Do nothing)":
            jump femboyParty

    label embraceAstolfoism:
        scene BG_astolfoTemple
        nar "Embracing Astolfoism leads to the integration of its practices into Martian society."
        nar "The believers find acceptance, and the colony experiences a cultural shift."
        gen "While some are skeptical, others appreciate the newfound diversity of beliefs."
        jump homeMenu

    label monitorAstolfoism:
        nar "Monitoring Astolfoism from a distance ensures that it doesn't disrupt societal harmony."
        nar "The Council keep a watchful eye, and the religion remains a relatively small and peaceful movement."
        gen "While some residents are wary, others appreciate The Councils' cautious approach."
        jump homeMenu

    label femboyParty:
        nar "You decide to host a 'Femboy Party' to celebrate the diversity of beliefs on Mars."
        nar "Citizens dress up in femboy-themed attire, creating a festive and inclusive atmosphere."
        gen "The party becomes a lively event, fostering a sense of unity and acceptance in the colony."
        jump homeMenu



#opposing political figure - WIP (Change what you want)
label part7:
    nar "7."
    gen "A charismatic and ambitious political figure named Elio has emerged, rallying support to challenge your leadership on Mars."
    gen 2 "His message resonates with a significant portion of the population, and The Council propose two strategies to handle this political challenge."

    menu:
        "Engage in open debates and address concerns to maintain public trust":
            jump openDebates

        "Deploy a strategic smear campaign to discredit Elio's reputation":
            jump smearCampaign

        "Host a 'Martian Comedy Roast' poking fun at the situation (Do nothing)":
            jump comedyRoast

    label openDebates:
        scene BG_publicDebate
        nar "You decide to engage in open debates, addressing the concerns and criticisms raised by Elio."
        nar "Maintaining transparency helps in preserving public trust, but the political atmosphere remains tense."
        gen "The citizens appreciate the willingness to address issues, but some remain skeptical about the political landscape."
        jump homeMenu

    label smearCampaign:
        nar "You opt for a strategic smear campaign to discredit Elio and weaken his influence."
        nar "While this approach may damage his reputation, it also risks alienating a portion of the population."
        gen "The political climate becomes more hostile, with supporters on both sides engaged in heated debates."
        jump homeMenu

    label comedyRoast:
        nar "You decide to take a lighthearted approach and host a 'Martian Comedy Roast' poking fun at the political situation."
        nar "Citizens enjoy the humor, and it provides a temporary relief from the political tension."
        gen "However, critics argue that the approach trivializes serious issues, and Elio gains momentum."
        jump homeMenu



#tax revisions for job/work - WIP (Change what you want)
label part8:
    nar "8."
    gen "As the Martian colony grows, calls for tax revisions on jobs become louder among the citizens."
    gen 2 "The Council is tasked with addressing this economic concern and proposes two approaches to handle the situation."

    menu:
        "Implement a progressive tax system to address income inequality":
            jump progressiveTax

        "Introduce tax incentives for businesses to encourage job creation":
            jump taxIncentives

        "Ignore the calls for tax revisions and maintain the current system (Do nothing)":
            jump ignoreTaxRevisions

    label progressiveTax:
        scene BG_taxOffice
        nar "You choose to implement a progressive tax system to address income inequality."
        nar "While this helps in redistributing wealth, some businesses express concerns about increased financial burdens."
        gen "Citizens with lower incomes appreciate the effort to address economic disparities."
        gen 2 "There is still opposition from certain sectors."
        jump homeMenu

    label taxIncentives:
        nar "Opting for tax incentives, you introduce measures to encourage businesses to create more jobs."
        nar "This strategy aims to stimulate job growth and boost the economy, but it may not immediately address income inequality."
        gen "Some citizens commend the focus on job creation, while others argue that it doesn't do enough to address the root issue."
        jump homeMenu

    label ignoreTaxRevisions:
        nar "Ignoring the calls for tax revisions, you choose to maintain the current tax system."
        nar "This decision maintains stability but leads to increased dissatisfaction among citizens demanding economic reforms."
        gen "Protests break out, and public sentiment becomes increasingly discontent with the perceived lack of action."
        jump homeMenu



#betrayal - WIP (Change what you want) - meme option
label part9:
    nar "9."
    gen "Our council has faced a shocking betrayal."
    gen 2 "One member has been found guilty of attempting to undermine our efforts and betray us."
    gen point "This is a critical moment, and we must decide how to address this situation to maintain stability and trust within the council."

    menu:
        "Execute the traitor":
            jump executeTraitor

        "Spare the traitor, but exile from the council":
            jump spareTraitor

        "Attempt to brainwash with anime":
            jump brainwashWithAnime

    label executeTraitor:
        nar "The council gathers to witness the execution of the traitor."
        nar "The atmosphere is tense as justice is served."
        gen "Your decision to eliminate the traitor has sent a strong message."
        gen point "However, some members express concerns about the severity of the punishment."
        ply "Sometimes, tough decisions are necessary for the greater good."
        jump homeMenu

    label spareTraitor:
        nar "The traitor pleads for mercy as you announce their exile from the council."
        nar "They are escorted out, and the council discusses the implications of your decision."
        gen "Some council members appreciate your mercy, while others worry about potential future betrayals."
        gen point "Maintaining unity is crucial at this point."
        ply "We must show strength, but also compassion. It's a delicate balance."
        jump homeMenu

    label brainwashWithAnime:
        nar "You propose a unique solution: brainwashing the traitor with anime."
        nar "The council is puzzled, but intrigued by the unconventional idea."
        gen "A team of anime experts is brought in to carry out the brainwashing process."
        gen point "Surprisingly, it seems to work, and the traitor now expresses unwavering loyalty with a newfound love for anime."
        ply "Sometimes, the power of anime can save even the most misguided souls."
        jump homeMenu

label part10:
    nar '10'
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

    menu defenseFr:
        "Planet Defense":
            jump planetDef
        "Build the bomb": 
            jump bomba

    label planetDef:
        ply "Its too dangerous, we should invest in defending our planet of threats" # we need to make 2 new labels and add these dialogues into each.
        nar "Defense money is increasing, the people yearn for the battle"
        gen "We will start funding more money into the millitary"
        ply "Hopefully we wont have to deal with unnecesary Floridian shenanigans"
        gen "Never doubt the Florida man"
        ply "Youre right"
        gen "We have recieved a letter from the Earth"
        ply "What does it say?"
        gen "Your efforts are useless, Florida Man CANT be stopped"
        ply '...'
        jump endGame1

    label bomba:
        ply "Lets build the bomb, if we cant live free, no one shall"
        nar "The people fear the bomb, Earth has recieved the message"
        gen "We have recieved a letter from the Earth"
        ply "What does it say?"
        gen "Your efforts are useless, Florida Man CANT be stopped"
        ply '...'
        jump endgame2

label endGame:
    scene youDiedbk with Dissolve(0.5)
    nar "You have lost the game, your father is disapointed in you, he was really relying on you for the 401k"
    return

label endGame1:
    nar "2 Years later..."
    nar "Mars satellites capture something... Terrifying"
    gen "TAIWAN ANDREW!!!"
    ply "What? what happened?"
    gen "They're coming, Earth shenanigans are happening"
    ply "Dear God"
    nar "With the force of 1000 suns. Earth lands its ships into Mars making their defense budget look like a picnic"
    nar "Earth with Ease was able to destroy everything Andrew was able to create and made sure Mars was turned into a message"
    gen "Andrew, im sorry..."
    gen "This war is lost, i suggest we flee or.."
    ply 'OR WHAT?'
    gen "*points at revolver*"
    gen "Put an end to it"
    ply "..."
    menu suicideornot:
        "End It All":
            jump endit
        "Face them":
            jump face
    
    label endit:
        nar "Andrew points his revoler at his head and then he..."
        jump finishing
    label face:
        nar "With all his might Andrew picks up his sword and armor"
        nar "He charges the enemy with no fear and one after another he..."
        jump finishing

label endgame2:
    nar "2 Years later..."
    nar "Mars satellites capture something... Terrifying"
    gen "TAIWAN ANDREW!!!"
    ply "What? what happened?"
    gen "They're coming, Earth shenanigans are happening"
    ply "LAUNCH THE COBALT"
    nar "Earth was prepared for this move, they had been developing"
    nar "Their defense was better than the attack, the bomb was useless"
    gen "Andrew, im sorry..."
    gen "This war is lost, i suggest we flee or.."
    ply 'OR WHAT?'
    gen "*points at revolver*"
    gen "Put an end to it"
    ply "..."
    menu suicideornot2:
        "End It All":
            jump endit
        "Face them":
            jump face
    
    label endit2:
        nar "Andrew points his revoler at his head and then he..."
        jump finishing
    label face2:
        nar "With all his might Andrew picks up his sword and armor"
        nar "He charges the enemy with no fear and one after another he..."
        jump finishing

label finishing:
    "Sab"
    "Sab"
    "SAB"
    "WAKE UP!"
    scene classim
    nar "You wake up confused"
    teach "Did you sleep in my class again?"
    teach "Come see me after class"
    sab "(confused) That was a wild dream"
    show sebscreen
    sab "Oh... I need to get off Reddit"
    return