label helens_locked_room:
    $ location_count = "Helen's Locked Room"
    if M_mia.get_state() == S_mia_locked_room:
        scene mia_house_locked_n
        show object_bed_11 at Position (xpos=527,ypos=765)
        show player 23 at left with dissolve
        player_name "{b}MIA{/b}!"
        player_name "You're tied up?!"
        show player 10
        player_name "Hold on, let me help you..."
        hide player with dissolve
    $ callScreen(location_count)

label mia_tied_up:
    scene mia_house_cs01
    with fade
    show text "{b}Mia{/b} seemed to be tied up on a bed, in a locked room.\nThere was no time to process what I was seeing...\n...I had to do something!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide school_art_cs01
    with dissolve

    scene mia_house_locked_c
    show player 5 at left
    show mia 40f at right
    with dissolve
    pause
    show mia 41f with dissolve
    pause
    show mia 42f at Position (xoffset=-15) with dissolve
    mia "Ow..."
    show mia 43f at Position (xpos=500) with dissolve
    mia "{b}[firstname]{/b}!!!"
    show mia 44f
    show player 10
    player_name "{b}Mia{/b}! What is going on?!"
    player_name "I got your text message on my phone and-"
    show player 11
    show mia 43f
    mia "We have to go, quick!"
    show mia 44f
    show player 12
    player_name "Wait {b}Mia{/b}, what's going on?"
    show player 11
    show mia 43f
    mia "My mom is becoming {b}INSANE{/b}!!"
    mia "She's been locking me up in here..."
    mia "...Forcing me to read the bible and pray, all day..."
    show player 22
    mia "...TIED TO THIS BED!!!"
    show mia 44f
    show player 23
    player_name "What?! That's crazy!"
    show player 11
    show mia 43f
    mia "There's no time to talk about it now."
    mia "We need to leave!!!"
    show mia 44f
    show player 10
    player_name "Now?!"
    show player 11
    show mia 46f
    mia "YES!"
    show mia 45f
    show player 10
    player_name "Wait but, where?!"
    show player 5
    show mia 46f
    mia "I don't care, I can't stay here any-"
    hide player
    show player 22 at left
    show mia 45 at Position (xpos=420)
    show helen 6 at right
    with dissolve
    player_name "!!!"
    show helen 7 with dissolve
    helen "How {b}DARE{/b} you come back here...{b}IN MY HOUSE{/b}!"
    show helen 8
    show player 24
    show mia 47 at Position (xpos=465) with dissolve
    mia "{b}Mom{/b}! {b}STOP{/b}!!!"
    show mia 48
    show helen 7
    helen "I won't let this evildoer take you away from me..."
    show helen 10 at Position (xpos=950) with dissolve
    helen "...{b}THIS{/b} is the only thing that matters..."
    show player 22
    helen "...It will {b}SAVE YOU{/b}!!!"
    show helen 11
    pause.5
    show helen 8 at Position (xpos=750)
    show harold 12 at right
    with dissolve
    harold "{b}Helen{/b}, what's with all the screaming?!"
    show harold 14
    show helen 7b
    helen "Go back downstairs, {b}Harold{/b}."
    show helen 8b
    show harold 13
    show player 11
    harold "No, wait a minute {b}Helen{/b}!"
    harold "This is too much, this has gone too far!!"
    show harold 14
    show helen 7b
    show player 22
    helen "{b}SILENCE{/b}!"
    helen "I've had enough of your lousy parenting..."
    helen "...You were {b}NEVER{/b} able to control our daughter!"
    show helen 8
    show player 11
    hide mia
    show mia 46 at Position (xpos=425) with dissolve
    mia "{b}Dad{/b}!"
    show helen 8b
    hide mia
    show harold 15
    with dissolve
    mia "Please make it stop!"
    harold "..."
    show helen 7b
    helen "She needs to stay here."
    show helen 8b
    show harold 17
    harold "No."
    show harold 16
    helen "..."
    show harold 17
    harold "This is enough!"
    pause
    show player 22
    harold "And you!"
    show harold 16
    show helen 8
    player_name "???"
    show harold 17
    harold "You shouldn't be here."
    harold "Go home and let me deal with this!"
    show harold 16
    show player 10
    player_name "Yes, sorry, I'll... I'm on my way out."
    hide player with dissolve
    show helen 7b
    helen "We're going to have a talk, {b}Harold{/b}."
    show helen 8b
    show harold 17
    harold "I don't think so, {b}Helen{/b}."
    harold "There's nothing left to discuss here."
    harold "{b}Mia{/b} is going to her room and we deal with this tomorrow!"
    hide harold
    hide helen
    scene black
    with fade
    pause

    scene miahouse_night
    show player 12 with dissolve
    player_name "{b}Helen{/b} is out of her {b}MIND{/b}!!"
    player_name "I didn't think it was that bad with {b}Mia's{/b} parents..."
    player_name "...To the point of tying her up?! That's crazy!"
    show player 24
    player_name "{b}*Sigh*{/b}"
    player_name "I feel bad for {b}Mia{/b}..."
    hide player with dissolve
    $ gTimer.tick(4)
    $ M_mia.trigger(T_mia_rescue)
    $ location_count = "Mia's House"
    $ callScreen(location_count)