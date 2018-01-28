default teach_lounge_first_visit = True

label teach_lounge_dialogue:
    $ location_count = "Teacher's Lounge"
    if teach_lounge_first_visit:
        $ teach_lounge_first_visit = False
        scene school_lounge_b with fade
        show player 14 with dissolve
        player_name "This must be the teachers lounge."
        player_name "Their private little getaway from my classmates."
        hide player with dissolve
    $ callScreen(location_count)