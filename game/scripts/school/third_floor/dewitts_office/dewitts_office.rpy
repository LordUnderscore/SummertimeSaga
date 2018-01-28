default dewitt_office_first_visit = True

label dewitt_office_dialogue:
    $ location_count = "Mrs Dewitt's Office"
    if dewitt_office_first_visit:
        $ dewitt_office_first_visit = False
        scene school_office2_b with fade
        show player 14 with dissolve
        player_name "Wow... {b}Ms. Dewitt's{/b} office has a sweet setup!"
        player_name "Looks like she brings students for private recordings..."
        player_name "...And she has a couch to hang out!!"
        hide player with dissolve
    $ callScreen(location_count)