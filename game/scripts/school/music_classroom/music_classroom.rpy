default music_classroom_first_visit = True

label music_classroom_dialogue:
    $ location_count = "Music Classroom"
    if music_classroom_first_visit == True:
        scene music_classroom_c with None
        show dewitt 1 at left
        show player 1f at right
        with dissolve
        show player 2f
        player_name "Hi, {b}Ms. Dewitt{/b}!"
        show dewitt 2
        show player 1f
        dewitt "My goodness!"
        dewitt "I was starting to think you had moved to another school!"
        show dewitt 1
        show player 10f
        player_name "Sorry, {b}Ms. Dewitt{/b}..."
        player_name "I know I'm behind now, but I'll try to catch up."
        show dewitt 2
        show player 5f
        dewitt "Oh, come on, honey. It's fine."
        dewitt "You just have to get back into the rhythm!!"
        show dewitt 3
        show player 11f
        pause
        show dewitt 2
        dewitt "Pick an instrument, and take a seat!"
        dewitt "We'll get you back in the groove!"
        show dewitt 1
        show player 2f
        player_name "Thanks, {b}Ms. Dewitt{/b}..."
        hide dewitt
        hide player
        with dissolve
        $ music_classroom_first_visit = False
    $ callScreen(location_count)

label dewitt_button_dialogue:
    scene music_classroom_c with None
    show dewitt 1 at left
    show player 2f at right
    player_name "Hi, {b}Ms. Dewitt{/b}."
    show dewitt 2
    show player 1f
    dewitt "Hello, {b}[firstname]{/b}!"
    dewitt "Ready to groove with us today?"
    show dewitt 1
    show player 33f
    player_name "Of course!"
    show dewitt 2
    show player 13f
    dewitt "Is there anything you want to talk about?"
    show dewitt 1
    show player 34f
    menu:
        "Not really.":
            show player 10f
            player_name "Not really..."
            player_name "Just hoping I can catch up."
            show dewitt 2
            show player 5f
            dewitt "Oh, honey. You'll be just fiiine!"
            show player 13f
            dewitt "Pick an instrument and take a seat!"
            dewitt "We'll get you back in the groove..."
            show dewitt 1
            show player 14f
            player_name "Thanks, {b}Ms. Dewitt{/b}..."
        "Which instrument?":

            show player 29f
            player_name "I'm just wondering what {b}instrument{/b} I should use..."
            show dewitt 2
            show player 3f
            dewitt "Hmm..."
            dewitt "Well, I know you used the cowbell, before..."
            dewitt "But I really think you should try something more... Delicate, this time."
            show dewitt 1
            show player 12f
            player_name "Oh, yeah?"
            show dewitt 2
            show player 5f
            dewitt "That's right!"
            dewitt "Why don't you try the {b}flute{/b}, for example?"
            show dewitt 1
            show player 4f
            player_name "Hmm..."
            show player 10f
            player_name "I don't know-"
            show dewitt 2
            show player 5f
            dewitt "Just try it, honey!!"
            dewitt "There's nothing to be afraid of!"
            show dewitt 1
            show player 10f
            player_name "I guess so... I do like to draw stuff..."
            show dewitt 2
            show player 11f
            dewitt "I also happen to be excellent at teaching the flute..."
            show dewitt 1
            show player 17f
            player_name "Haha. All right, then."
    hide dewitt
    hide player
    with dissolve
    $ callScreen(location_count)