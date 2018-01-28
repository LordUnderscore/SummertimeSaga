default bissette_office_first_visit = True

label bissette_office_dialogue:
    $ location_count = "Mrs Bissette's Office"
    if bissette_office_first_visit:
        $ bissette_office_first_visit = False
        scene school_office1_b with fade
        show player 10 with dissolve
        player_name "{b}Mrs. Bisette's{/b} office looks so...French!"
        show player 14
        player_name "Maybe one day we can go on a field trip with her..."
        hide player with dissolve
    $ callScreen(location_count)