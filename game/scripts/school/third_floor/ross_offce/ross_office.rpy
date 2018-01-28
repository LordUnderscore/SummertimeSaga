default ross_office_first_visit = True

label ross_office_dialogue:
    $ location_count = "Mrs Ross' Office"
    if ross_office_first_visit:
        $ ross_office_first_visit = False
        scene school_office3_b with fade
        show player 11 with dissolve
        player_name "*Sniff*"
        show player 12
        player_name "What's that smell?"
        player_name "It's like...incense...and herbs..."
        player_name "{b}Ms. Ross{/b} must be spending a lot of time in here."
        hide player with dissolve
    $ callScreen(location_count)