default hill_first_visit = True

label hill_dialogue:
    $ location_count = "Hill"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 129>audio/ambience_ravenhill.ogg"):
            $ playSound("<loop 129>audio/ambience_ravenhill.ogg")
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if hill_first_visit and not M_mia.get_state() == S_mia_find_harold:
        scene expression gTimer.image("hill{}_b")
        show player 32 with dissolve
        player_name "Wow! What a view!"
        show player 14 at Position(xpos = 444)
        player_name "( Perfect place to bring a girl on a date... )"
        show player 4 at Position(xpos = 450)
        player_name "( ...If I only had a car! )"
        hide player with dissolve
        $ hill_first_visit = False

    elif M_mia.get_state() == S_mia_find_harold:
        scene expression gTimer.image("hill{}")
        show harold_car_02 at Position (xpos=575,ypos=550)
        show player 31 with dissolve
        player_name "..."
        show player 32
        player_name "I see a police car."
        player_name "Could it be {b}Harold{/b}?"
        hide player with dissolve
    $ callScreen(location_count)

label hill_tree:
    scene expression gTimer.image("location_lair_hill_tree{}")
    if scroll not in inventory.items:
        show expression gTimer.image("objects/object_scroll_01{}.png") at Position(xalign = 0.45, yalign = 0.65)
        player_name "What's this? Some kind of old scroll?"
        player_name "I wonder how long it's been hidden in there."
        call screen hill_tree
        show popup_item_scroll1 at truecenter with dissolve
        $ inventory.items.append(scroll)
        pause
        hide popup_item_scroll1 with dissolve
    else:

        pause
    $ callScreen(location_count)

label harolds_car_dialogue:
    scene hill_c
    show harold 28 at right
    show player 10 at left
    with dissolve
    player_name "{b}Harold{/b}?!"
    show player 11
    show harold 19
    harold "Hey... What are you {b}*Hic*{/b} doing here... Shouldn't you be in bed?"
    show harold 18
    show player 12
    player_name "Ehh... It's noon, sir."
    show player 11
    show harold 20
    harold "Oh, right...that is correct."
    show harold 19
    harold "Nevermind, then..."
    show harold 18
    show player 10
    player_name "Are you alright, sir?"
    show player 5
    show harold 19
    harold "I think I'll {b}*Hic*{/b} survive..."
    harold "...My wife seems to be doing fine {b}*Hic*{/b} without me... So why shouldn't I?!"
    show harold 20
    harold "I can take care of myself {b}*Hic*{/b}... I don't need anyone's help..."
    show harold 19
    harold "Wait... What were you asking me again???"
    show harold 18
    show player 11
    player_name "?!?"
    show player 12
    player_name "Well, {b}Mia{/b} and {b}Helen{/b} haven't heard from you in days... They're just worried about you..."
    player_name "...And I said I'd try and find out if you're okay."
    player_name "Even your collegues at the station are worried."
    show player 10
    player_name "I think a lot of people in your life DO care about you!"
    show player 5
    show harold 19
    harold "They are?!"
    harold "I {b}*Hic*{/b}, err... Wait, how did you find me?!"
    show harold 18
    show player 12
    player_name "I asked around at your office..."
    player_name "...And I saw an old picture of you and {b}Helen{/b} on your desk."
    player_name "Back when you two used to spend time here, at Raven Hill."
    show player 5
    show harold 27
    harold "..."
    show harold 28
    harold "*Sigh*"
    show harold 20
    harold "I feel like things were so much {b}*Hic*{/b}...simpler, back in the day..."
    harold "I was happier...and felt like myself, not pretending to be someone I'm not, you know?"
    harold "I don't even recognize myself anymore..."
    show harold 18
    show player 10
    player_name "Why can't you change back?"
    show player 5
    show harold 19
    harold "What {b}*Hic*{/b}... Do you mean?"
    show harold 18
    show player 10
    player_name "You stopped being yourself... Maybe that's the problem!"
    show player 5
    show harold 28
    harold "..."
    show harold 20
    harold "Maybe you're right..."
    show harold 19
    harold "...But {b}Helen{/b} is not the way she used to be, either."
    show harold 18
    show player 14
    player_name "I think she can change, too!"
    player_name "Give her a chance..."
    show player 13
    show harold 19
    harold "I have to say, you did some great detective work finding me..."
    harold "...And I appreciate you looking out for my family."
    show harold 18
    show player 10
    player_name "I just want you guys to be happy again."
    show player 5
    show harold 27
    harold "..."
    show harold 20
    harold "I should {b}*Hic*{/b} head back to the station and sober up..."
    harold "...Then I'll call the house."
    show harold 19
    harold "See ya later, kiddo!"
    show harold 18
    show player 36 with dissolve
    player_name "Take care, {b}Harold{/b}!"
    show player 13
    hide harold
    with dissolve
    pause
    show player 12
    player_name "Well, that was...interesting."
    player_name "I should tell {b}Mia{/b} I found him and he's okay..."
    hide player with dissolve
    $ M_mia.trigger(T_harold_found)
    $ callScreen(location_count)