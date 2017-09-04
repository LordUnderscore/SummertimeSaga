label movie_theatre_dialogue:
    if movie_theatre_count == 0:
        scene movie_lobby
        show player 14 with dissolve
        player_name "Cool!"
        show player 14
        player_name "( New movies just came out! )"
        show player 17
        player_name "( Hmm... Maybe I could bring someone on a date here... )"
        hide player 17 with dissolve
        $ movie_theatre_count = 1
    scene movie_lobby
    show movie_desk zorder 2
    show player 1f zorder 3 at right
    show bub 2 zorder 1 at Position(ypos=570, xpos=440)
    bub "Hi!"
    bub "Going on a date, huh?"
    show bub 1
    show player 14f
    player_name "Uhh... Yeah?"
    show bub 2
    show player 1f
    bub "Niiiice!"
    bub "Is there a particular movie you'd like to watch?"
    hide bub
    hide player
    hide movie_desk
    scene movie_options
    call screen movieoptions

label after_movie_pick_dialogue:
    scene movie_lobby
    show movie_desk zorder 2
    show player 1f zorder 3 at right
    show bub 2 zorder 1 at Position(ypos=570, xpos=420) with dissolve
    bub "Good pick!"
    show bub 3 at Position (xpos=470)
    bub "Here's your ticket."
    show bub 1 at Position (xpos=420)
    show player 14f
    player_name "Thanks."
    show player 1f
    show bub 2
    bub "Just don't make a mess on the seats."
    bub "I hate cleaning that stuff off!"
    show bub 1
    show player 11f
    player_name "..."
    show bub 2
    bub "Enjoy!"
    jump watch_movie

label watch_movie:
    scene movie with fade
    show popup_unfinished at truecenter with dissolve
    $ renpy.pause()
    hide popup_unfinished with dissolve
    hide movie
    jump mall_dialogue