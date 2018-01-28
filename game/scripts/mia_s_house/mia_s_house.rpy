default mia_mail = []

label mias_house_dialogue:
    $ location_count = "Mia's House"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if gTimer.is_morning() and not gTimer.is_weekend():
        scene miahouse
        show player 12 with dissolve
        player_name "( There's no one here... )"
        show player 35
        player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
        hide player 35 with dissolve

    elif M_mia.get_state() == S_mia_concerning_visit and gTimer.is_afternoon():
        scene expression gTimer.image("miahouse{}")
        show harold 21 at right
        show player 10 at left
        with dissolve
        player_name "{b}Harold{/b}! Is {b}Mia{/b}-"
        show player 11
        player_name "..."
        show harold 23
        harold "Hey..."
        show harold 22
        show player 12
        player_name "Are you okay?"
        show player 11
        show harold 23
        harold "I've been better."
        show harold 22
        show player 10
        player_name "Where are you going?"
        show player 5
        show harold 23
        harold "I'm...not quite sure at the moment."
        show harold 22
        show player 10
        player_name "Huh?"
        show player 12
        player_name "So, what's with the box?"
        show player 11
        show harold 23
        harold "I'm moving out, {b}[firstname]{/b}..."
        show harold 22
        show player 22
        player_name "!!!"
        show harold 23
        harold "...I'm sorry you had to see us at our worst."
        show harold 21
        harold "See you around, kiddo."
        hide harold with dissolve
        show player 10
        player_name "Woah!"
        player_name "I better check on {b}Mia{/b} and see if she's okay..."
        hide player with dissolve
        $ ui_lock_count = 1
        $ M_mia.trigger(T_harold_leaves)

    elif gTimer.is_evening() and M_mia.is_set('front door locked'):
        scene miahouse_night
        show player 2 with dissolve
        player_name "( {b}Mia{/b} is probably asleep... I should come back tomorrow. )"
        hide player 2 with dissolve
        hide miahouse_night
    $ callScreen(location_count)

label mia_button_dialogue_house:
    if M_mia.get_state() == S_mia_do_homework:
        scene location_mia_closeup
        show player 14 at left with dissolve
        show mia 1 at right with dissolve
        player_name "Hey {b}Mia{/b}!"
        show mia 4 at right
        show player 1 at left
        mia "Hey {b}[firstname]{/b}!"
        mia "What're you doing here?"
        show mia 1 at right
        show player 29 at left
        player_name "Umm... I wanted to ask you something!"
        menu:
            "About that homework.":
                show player 21 at left
                player_name "Do you still need help studying for the exams?"
                show mia 3 at right
                show player 13 at left
                mia "Of course! I've been looking for {b}someone to study with{/b}..."
                show mia 6 at right
                show player 11 at left
                mia "...But have you caugh up with class yet?"
                show mia 2 at right
                show player 10 at left
                player_name "Oh! Right! {b}Mrs. Bissette{/b} assigned me some homework to catch up..."
                show mia 6 at right
                show player 13 at left
                mia "You probably should finish that, first!"
                show mia 4 at right
                mia "Then you can come over to my house... and we'll study in my room!"
                show mia 1 at right
                show player 14 at left
                player_name "Ye... yeah?"
                show mia 3 at right
                show player 1 at left
                mia "Sure! It'll be fun!"
                show mia 1 at right
                show player 17 at left
                player_name "Alright... I'll let you know when I'm done with them!"
                show mia 4 at right
                show player 1 at left
                mia "See you soon!"
                hide mia 4 at right with dissolve
                show player 5 with dissolve
                player_name "( I should try and finish my {b}french homework{/b}, so I can study with {b}Mia{/b}. )"
                show player 4 with dissolve
                pause
                player_name "( I wonder why she picked me to help her study. )"
                player_name "( She usually studies with {b}Judith{/b} and she's really good in french... )"
                player_name "( ...I'm not sure how I could help her. )"
                show player 13 with dissolve
                player_name "( At least we'll get to hang out, and she's really cute... )"
                hide player with dissolve
            "I forgot...":

                show mia 1 at right
                show player 4 at left
                player_name "Hmm... Yeah, but I forgot!"
                show mia 3 at right
                show player 11 at left
                mia "Haha! You're funny~"
                show mia 1 at right
                show player 17 at left
                player_name "Sorry! I can't remember what I wanted to say!"
                show player 14 at left
                player_name "I should get going."
                show mia 4 at right
                show player 1 at left
                mia "Have a good night!"
                hide player 1 at left with dissolve
                hide mia 4 at right with dissolve
    $ callScreen(location_count)

label night_closed_mia:
    scene miahouse_night
    show player 2 with dissolve
    player_name "( {b}Mia{/b} is probably asleep... I should come back tomorrow. )"
    hide player 2 with dissolve
    $ callScreen(location_count)

label mia_banned:
    scene expression gTimer.image("miahouse{}")
    show player 12 with dissolve
    player_name "I should leave {b}Mia{/b} and her family alone for now..."
    hide player with dissolve
    $ callScreen(location_count)

label closed_mia:
    scene miahouse
    show player 12 with dissolve
    if gTimer.is_morning() and not gTimer.is_weekend():
        player_name "( There's no one here... )"
        show player 35
        player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
    else:
        player_name "( {b}Mia{/b} is outside, I shouldn't go in there. )"
    $ callScreen(location_count)

label mia_mailbox:
    scene expression gTimer.image("mia_mailbox{}")
    if m_pizza_pamphlet in mia_mail:
        player_name "( This is probably junk mail. )"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( Tony's Pizza. I haven't been there in a while. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        if not loc_pizza_unlocked:
            show expression "boxes/popup_pizza.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_pizza.png" with dissolve
            $ loc_pizza_unlocked = True
        call screen mia_mailbox
    elif m_newspaper in mia_mail:
        player_name "( Local news. This should be interesting... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( The theif is still out on the loose? You would've thought they would've caught him by now. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_newspaper.png" with dissolve
        call screen mia_mailbox
    else:
        call screen mia_mailbox

label mias_house:
    $ location_count = "Mia's House"
    $ callScreen(location_count)