default dex_first_visit = True

label basket_court_dialogue:
    $ location_count = "Basket Ball Court"
    if M_dex.get_state() == S_dex_start and is_here("dexter"):
        scene basketball_b
        show player 5 at left
        show dexter 3 at right
        with dissolve
        dex "What are you doing here?"
        show dexter 1
        show player 12
        player_name "Why do you care? Maybe I'm just here to practice."
        show player 11
        show dexter 3
        dex "Hah!"
        dex "That's a good one."
        show dexter 1
        show player 25
        player_name "*Sigh*"
        show player 12
        player_name "What do you want, {b}Dexter{/b}?"
        show player 5
        show dexter 6 with dissolve
        dex "Just stay away from my court, understood?"
        hide dexter with dissolve
        show player 24
        player_name "..."
        hide player with dissolve
        $ M_dex.trigger(T_dex_territory)
    $ callScreen(location_count)

label dexter_court_dialogue:
    scene basketball_b
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "Didn't I tell you to stay away?"
    dex "What does a loser like you want anyway?"
    show dexter 1
    menu:
        "Challenge.":
            show player 12
            player_name "I'm here to challenge you, {b}Dexter{/b}."
            show player 5
            show dexter 3
            dex "Ha ha!"
            dex "To what?!"
            show dexter 1
            show player 10
            player_name "To uh..."
            show player 5
            show dexter 3
            dex "You know I'd beat you at anything."
            show dexter 4 with dissolve
            dex "Now fuck off before I decide to beat the shit out of you."
            $ M_dex.trigger(T_dex_challenge)
        "Nothing.":

            show player 10
            player_name "I... uhh... didn't mean to bother you."
            player_name "I need to get to class."
            show player 5
            show dexter 3
            dex "Run along, loser."
    hide dexter
    hide player
    with dissolve
    $ callScreen(location_count)