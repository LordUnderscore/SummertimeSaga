default tattoo_interior_first_visit = True

label tattoo_parlor_dialogue:
    $ location_count = "Tattoo Parlor"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label tattoo_parlor_interior_dialogue:
    $ location_count = "Tattoo Parlor Interior"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if tattoo_interior_first_visit:
        $ tattoo_interior_first_visit = False
        scene tattoo_indoor_b
        show player 13 with dissolve
        player_name "( I've never been in a tattoo shop before. )"
        show player 34
        player_name "( Maybe I should get a tattoo one day... )"
        hide player with dissolve

    if M_mia.get_state() == S_mia_get_tattoo and is_here("mia"):
        scene tattoo_indoor_b
        show mia 7f at Position (xpos=400)
        show player 13 at left
        show grace 2 at right
        with dissolve
        grace "Hey guys!"
        show grace 1
        show player 14
        player_name "Hey."
        show player 13
        show mia 10f
        mia "Hi!"
        show mia 7f
        show grace 4
        grace "Welcome to {b}Sugar Tats{/b}."
        show grace 2
        grace "Have a look around the shop for cool tats..."
        grace "...And come see me if you have any questions!"
        hide grace with dissolve
        pause(.25)
        hide mia
        show mia 12 right
        with dissolve
        mia "She seems busy, maybe we should come back another time?"
        show mia 8
        show player 12
        player_name "Oh, come on."
        show player 10
        player_name "You're going to stop now?!"
        show player 5
        show mia 12
        mia "*Sigh*"
        mia "You're right."
        mia "I said I would, so let's do it!"
        hide mia with dissolve
        show player 17
        player_name "That's the spirit!"
        hide player with dissolve
        $ M_mia.trigger(T_mia_visit_tattoo_parlor)
    $ callScreen(location_count)

label grace_dialogue:
    scene tattoo_indoor_c
    if M_mia.get_state() == S_mia_buy_tattoo and is_here("mia"):
        scene tattoo_indoor_c
        show mia 7f at Position (xpos=400)
        show player 13 at left
        show grace 2 at right
        show tattoo_desk at right
        with dissolve
        grace "Hey there!"
        grace "Are you here for an appointment?"
    else:

        show player 13 at left
        show grace 2 at right
        show tattoo_desk at right
        with dissolve
        grace "Hey there!"
        grace "Are you here for an appointment?"
    show grace 1
    menu grace_menu_dialogue:
        "Tattoo." if M_mia.get_state() == S_mia_buy_tattoo and is_here("mia"):
            show mia 10f
            mia "I'd like to get a tattoo... Now."
            show mia 7f
            show grace 2
            grace "Now? I see..."
            show grace 3
            grace "Do you have a design in mind?"
            show grace 1
            show mia 30f at Position (xoffset=64) with dissolve
            mia "My friend here drew this for me, and I'd like it done today!"
            show mia 7f
            show grace 5
            with dissolve
            grace "Hmm..."
            show grace 6
            grace "Are you sure you want this done?"
            grace "Tattoos are permanent, so I have to make sure my clients know what they're getting into!"
            show grace 7
            show mia 10f
            mia "I've been thinking about it for a long time and... Yes, I do want it."
            show mia 7f
            show grace 6
            grace "Alright, sweetie. But, it aint cheap!"
            show grace 7
            show player 14
            player_name "How much is it?"
            show player 13
            show grace 5
            grace "For that size... with colors... Around {b}$400{/b}."
            show grace 7
            show player 22
            show mia 12f
            mia "!!!"
            mia "Damn... I think I only have {b}$200{/b}..."
            show mia 8f
            show player 11
            player_name "..."
            show player 10
            player_name "You don't have enough?"
            show player 5
            show mia 12 with dissolve
            mia "No, that's all I was able to save up."
            mia "What do you think I should do?"
            show mia 8
            menu:
                "I'll help you." if inventory.money >= 200:
                    $ inventory.money -= 200
                    show player 14
                    player_name "I'll help you pay for the remaining."
                    show player 13
                    show mia 12
                    mia "Really?!"
                    show mia 7
                    show player 14
                    player_name "Why not."
                    player_name "I've been working lately so I have some money to spend..."
                    show player 17
                    player_name "...And it's for a good cause!"
                    show player 13
                    show mia 10
                    mia "That's really sweet of you..."
                    mia "...And I'll make sure to pay you back!"
                    show mia 7
                    show player 17
                    player_name "It's alright, ha ha."
                    show player 13
                    show grace 6
                    grace "So?"
                    show mia 7f with dissolve
                    grace "Ready to start?"
                    show grace 7
                    show mia 10f
                    mia "I'm ready!"
                    hide player
                    hide mia
                    hide grace
                    hide tattoo_desk
                    with dissolve


                    scene tattoo_cs01
                    show text "It took a while for {b}Grace{/b} to finish the work.\nI was really nervous for {b}Mia{/b}...\n...But, she seemed to be fine the whole time!" at Position (xpos= 512, ypos = 700) with dissolve
                    with dissolve
                    pause
                    hide text
                    hide tattoo_cs01
                    with dissolve


                    scene tattoo_indoor_b
                    show mia 7f at Position (xpos=400)
                    show player 13 at left
                    show grace 2 at right
                    with dissolve
                    grace "All done!"
                    grace "I hope you guys like it."
                    show grace 1
                    show mia 10f
                    mia "It's great! And it didn't hurt as much as I thought..."
                    show mia 7f
                    show grace 2
                    grace "Make sure you leave the bandage on it for at least a few days."
                    show grace 1
                    show mia 10f
                    mia "Okay, thank you!"
                    show mia 7f
                    show grace 2
                    grace "Bye, guys."
                    hide grace with dissolve
                    pause(.25)
                    hide mia
                    show mia 7 right
                    with dissolve
                    show player 14
                    player_name "How does it feel?"
                    show player 13
                    show mia 12
                    mia "The tattoo?"
                    show mia 7
                    show player 14
                    player_name "Yeah."
                    show player 13
                    show mia 12
                    mia "It's fine... It just has this tingling sensation."
                    show mia 10
                    mia "And I'm glad I did it... I can finally say I did something that I wanted."
                    show mia 7
                    show player 10
                    player_name "Are you scared your mom might find out?"
                    show player 5
                    show mia 9
                    mia "Hopefully not, but it's in a well hidden spot, ha ha."
                    show mia 7
                    show player 17
                    player_name "I think it's cool you did it."
                    show player 18
                    show mia 10
                    mia "Thanks, {b}[firstname]{/b}. I'm happy you came with me."
                    show player 13
                    mia "I should get going, though. Before my mom starts getting suspicious..."
                    show mia 7
                    show player 14
                    player_name "Okay, see you at school!"
                    show player 13
                    show mia 10
                    mia "Bye."
                    hide player
                    hide mia
                    with dissolve
                    $ gTimer.tick()
                    $ M_mia.trigger(T_mia_tattoo_done)
                "Come back later.":

                    show player 10
                    player_name "Maybe we should come back later?"
                    show player 5
                    mia "..."
                    show mia 12
                    mia "I suppose we should."
                    show mia 8
                    show player 10
                    player_name "It's okay. We can always come back another time."
                    show player 5
                    show mia 12
                    mia "You're right."
                    show mia 8
                    show player 10
                    player_name "Sorry you couldn't get your tattoo today..."
                    show player 5
                    show mia 12
                    mia "It's fine. I should get home now."
                    show mia 8
                    show player 10
                    player_name "Alright, see you later."
                    hide player
                    hide mia
                    hide grace
                    hide tattoo_desk
                    with dissolve

        "You look familiar." if not Grace.known(grace_intro) and not is_here("mia"):
            show player 10
            player_name "You know... I think..."
            show player 12
            player_name "Uhh."
            show player 34
            show grace 3
            grace "Is everything okay?"
            show grace 1
            show player 30
            player_name "Sorry, but you look... familiar."
            show player 5
            show grace 3
            grace "Huh?"
            show grace 2
            grace "Hmm... Maybe you're thinking of my sister?"
            show grace 1
            show player 12
            player_name "Sister?"
            show player 11
            show grace 3
            grace "My little sister? {b}Eve{/b}?"
            show grace 1
            show player 38 with dissolve
            player_name "Oh! Of course!"
            show player 14 with dissolve
            player_name "I can see the connection, now."
            show player 13
            show grace 4
            grace "Ha ha."
            show grace 2
            grace "Anyway, is there anything I can do for you?"
            $ Grace.add_event(grace_intro)
            $ grace_intro.finish()
            jump grace_menu_dialogue
        "Nothing.":

            show player 14
            player_name "I'm just looking around."
            show player 13
            show grace 2
            grace "Cool! Have a look."
            grace "I do all styles and designs showcased in my shop!"
            grace "Just let me know if you ever think about getting something, and we can make an appointment!"
            show grace 1
            show player 14
            player_name "Okay, thanks!"
            show player 13
            show grace 2
            grace "See ya."
            hide grace
            hide mia
            hide player
            hide tattoo_desk
            with dissolve
    $ callScreen(location_count)