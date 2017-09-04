default church_first_time = True
default angelica_count = 0

label church_dialogue:
    $ location_count = "Church"
    if getPlayingSound("<loop 3.9>audio/ambience_church.ogg"):
        $ playSound("<loop 3.9>audio/ambience_church.ogg")
    if church_first_time == True:
        scene church_b with None
        show player 11 with dissolve
        player_name "( The church is empty. )"
        player_name "( Looks like I missed Mass. )"
        hide player 11
        $ church_first_time = False
    $ callScreen(location_count)

label angelica_dialogue:
    scene church_c
    show ang 2 at right
    show player 1 at left
    with dissolve
    ang "Are you from this Parish, young man?"
    show ang 1
    show player 14
    player_name "Hi, I was wo-"
    show ang 2
    show player 11
    ang "Are you from this Parish, young man?"
    show ang 1
    show player 14
    player_name "Uhh... Not really."
    show ang 2
    show player 11
    ang "Do you believe in God?"
    show ang 1
    show player 10
    player_name "Well..."
    show ang 2
    show player 11
    ang "I'm sorry."
    ang "I can only help those who share the faith of our lord!"
    $ angelica_count = 1
    hide player
    hide ang
    hide church_c
    $ callScreen(location_count)

label confessional_left:
    scene church_confession
    show player 283 at Position(xpos=280)
    with dissolve
    player_name "Bless me father, for I have sinned."
    show player 278
    player_name "..."
    show player 284
    player_name "......"
    show player 280
    player_name "Father?"
    player_name "There's no one here?"
    show player 10
    player_name "( I guess there's no priest around at this time... )"
    hide player
    hide church_confession
    $ callScreen(location_count)

label confessional_right:
    scene church_confession
    show player 43f at Position(xpos=760)
    with dissolve
    player_name "( Cool! )"
    player_name "( I've never been on this side of the confessional. )"
    show player 4f
    player_name "Hmm..."
    show player 14f
    player_name "( Looks the same as the other side, actually. )"
    player_name "( I should get out of here... )"
    hide player
    hide church_confession
    $ callScreen(location_count)