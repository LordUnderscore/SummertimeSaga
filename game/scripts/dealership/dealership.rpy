default dealership_first_time_visit = True
default plates = ["incezt", "dtfmom", "assman", "peni5", "viber8r", "yes269", "xesttub", "2grl1cp"]

label dealership_dialogue:
    $ location_count = "Dealership"
    $ callScreen(location_count)

label josephine_button_dialogue:
    scene location_dealership_indoor_closeup with None
    show joe 1 at Position(xpos=0.5474,ypos=0.7630)
    show xtra3 at right
    show player 108f at left
    with dissolve
    if dealership_first_time_visit == True:
        player_name "Good morning."
        show player 109f
        pause
        pause
        show player 108f
        player_name "Hello?"
        show player 109f
        pause
        Josephine "Sigh..."
        pause
        show sato 2 behind xtra3 at Position(xpos=.7630,ypos=0.7299) with dissolve
        show player 11
        Mr. Sato "{b}Josephine{/b}!"
        show sato 1
        show joe 3 at Position(xpos=0.4976,ypos=1.0000)
        Josephine "What?!"
        show joe 2
        show sato 2
        Mr. Sato "Can't you see that we have a {b}customer{/b} waiting?!"
        show sato 1
        Josephine "{b}*Sigh*{/b}"
        show sato 4
        Mr. Sato "Sorry, Sir. My {b}daughter{/b} is still learning proper work ethics."
        show sato 2
        Mr. Sato "Now, {b}Josephine{/b}! Please, put down your phone and help this young man."
        Mr. Sato "Remember: Put the customer first!"
        hide sato
        show joe 3 at Position(xpos=0.8294,ypos=1.0000)
        with dissolve
        Josephine "Ugh..."
        show joe 5
        Josephine "I hate him so much."
        Josephine "He's always on my case..."
        show joe 4
        show player 10
        player_name "You work for your {b}Dad{/b}?"
        show player 11
        show joe 5
        Josephine "I never wanted to work here. He just makes me work here to keep an eye on me."
        Josephine "I wish he'd just let me be, already!"
        show joe 4
        pause
        show joe 5
        Josephine "Anyway..."
        $ dealership_first_time_visit = False
    Josephine "What do you want again?"
    show joe 4 at Position(xpos=0.8294,ypos=1.0000)
    menu dealership_options:
        "Buy a vehicle.":
            show popup_unfinished at truecenter with dissolve
            $ renpy.pause()
            hide popup_unfinished with dissolve
            jump dealership_options

        "Make an insurance claim" if quest16 in quest_list and quest16_1 == False:
            show player 14
            player_name "Um... I was hoping to talk to someone about an insurance claim."
            show player 11
            show joe 5
            Josephine "What was the registered license plate?"
            show joe 4
            show player 4
            label platemenu:
                player_name "What was {b}Mom's{/b} vanity plate again?"
                $ selected_plates = []
                $ counter = 0
                while (counter < 4):
                    $ random_plate = renpy.random.choice(plates)
                    while (random_plate in selected_plates):
                        $ random_plate = renpy.random.choice(plates)
                    $ selected_plates += [random_plate]
                    $ counter += 1
                menu:
                    "INCEZT" if "incezt" in selected_plates:
                        jump wrong_plate

                    "DTFM0M" if "dtfmom" in selected_plates:
                        show player 11
                        show joe 6
                        Josephine "That one is in the system."
                        show joe 5
                        Josephine "Still live at 240 Cookie Street?"
                        show joe 4
                        show player 17
                        player_name "Yep!"
                        show player 11
                        show joe 5
                        Josephine "Okay... What can I help you with..."
                        show joe 4
                        show player 10
                        player_name "Well I wanted to report a claim; my mom's car is broken."
                        show player 11
                        show joe 6
                        Josephine "One sec..."
                        pause
                        Josephine "..."
                        pause
                        show joe 5
                        Josephine "Umm... yeah... I just noticed, but your insurance policy has been canceled because of lack of payments."
                        show joe 4
                        show player 23
                        player_name "What!?"
                        show player 22
                        show joe 6
                        Josephine "I see an outstanding balance of {b}$4,000{/b}."
                        Josephine "Your deductible is set at {b}$5,000{/b}."
                        show joe 4
                        show player 23
                        player_name "!!!" with hpunch
                        show joe 5
                        Josephine "So... you're looking at least {b}$9,000{/b} before we'll cover anything."
                        Josephine "Is the damage pretty major?"
                        show joe 4
                        show player 22
                        player_name "Uh... Yeah..."
                        show joe 5
                        Josephine "Oh. If it wasn't, I'd suggest just fixing it yourself."
                        show joe 4
                        pause
                        show player 10
                        player_name "Damn..."
                        show player 24
                        jump fix_car

                    "ASSMAN" if "assman" in selected_plates:
                        show player 11
                        show joe 5
                        Josephine "You are definitely not the {b}ASSMAN{/b}. The local proctologist has that license."
                        show joe 4
                        show player 26
                        player_name "Oh. Yeah..."
                        show player 4
                        jump platemenu

                    "I♥PEN15" if "peni5" in selected_plates:
                        jump wrong_plate

                    "VIBE R8R" if "viber8r" in selected_plates:
                        jump wrong_plate

                    "YES 269" if "yes269" in selected_plates:
                        jump wrong_plate

                    "XESTTUB" if "xesttub" in selected_plates:
                        jump wrong_plate

                    "2GRL 1CP" if "2grl1cp" in selected_plates:
                        jump wrong_plate
                    "None of these.":

                        jump platemenu
        "Nothing":
            $ callScreen(location_count)

label wrong_plate:
    show player 11
    $ plate_rand = renpy.random.randint(0,1)
    show joe 6
    pause
    show joe 5
    if plate_rand == 0:
        Josephine "I'm not seeing an account that matches that license plate."
    else:
        Josephine "That would be a neat plate, but unfortunately it's not in the system."
    Josephine "Any other license plate you can think of?"
    show joe 4
    show player 4
    jump platemenu

label fix_car:
    player_name "What should I do now?"
    menu:
        "Pay the bill":
            show popup_unfinished at truecenter with dissolve
            $ renpy.pause()
            hide popup_unfinished with dissolve
            jump fix_car
        "Convince her.":

            if pStats.chr() >= 7:
                show player 12
                player_name "Is it possible to make the payments later?"
                show player 10
                player_name "Our family is in a rough spot right now."
                player_name "My mom really needs the car running for work, otherwise we can't really pay off the insurance."
                show player 11
                show joe 5
                Josephine "I don't think I can-"
                show joe 4
                show player 24
                player_name "And my {b}Dad{/b} recently passed away! We're struggling to get back on our feet!"
                show player 25
                player_name "Is there really nothing you can do to help us?"
                pause
                show joe 6
                Josephine "Listen..."
                show joe 5
                Josephine "I'll help you out this {b}ONE{/b} time!"
                show joe 6
                Josephine "My {b}Dad{/b} would never approve of this, so keep it on the down-low."
                show joe 4
                show player 14
                player_name "Of course."
                show player 13
                show joe 5
                Josephine "He'd be super pissed at me, but it wouldn't be the first time!"
                show joe 6
                Josephine "I'll just make your debt disappear and lower your deductible at the same time."
                Josephine "I'll send a truck out to your house to pick up the car. It should be fixed up before you get home!"
                show joe 4
                show player 10
                player_name "Really?"
                Josephine "..."
                show player 14
                player_name "I mean, Thank you very much!"
                show player 13
                show joe 5
                Josephine "You {b}owe{/b} me!"
                show joe 4
                show player 17
                player_name "Of course! Anything!"
                show player 18
                $ quest16_1 = True
            else:

                show player 24
                player_name "[chr_warn]I... Uhm... Could you?"
                show joe 5
                Josephine "Could I... What?"
                show joe 4
                show player 37
                player_name "[chr_warn]Um... Nevermind."
                pause
                show player 24
                player_name "[chr_warn]I'm sorry I bothered you."
                show joe 5
                Josephine "Well, I hope you get your car fixed."
                show joe 4
                show player 25
                player_name "Yeah, thanks..."
                show player 24
                player_name "( Come on {b}[firstname]{/b}! All you had to do was ask for some help. )"
                player_name "{b}*Sigh*{/b}"
                player_name "( I'm way too nervous... )"
        "Give up":
            show player 10
            player_name "I should probably talk to my mom about this."
            show player 2
            player_name "Thanks!"
            show player 1
            show joe 5
            Josephine "Sure, whatever."
    $ callScreen(location_count)