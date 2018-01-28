default okita_office_first_visit = True

label okita_office_dialogue:
    $ location_count = "Mrs Okita's Office"
    if okita_office_first_visit:
        $ okita_office_first_visit = False
        scene school_office4_b with fade
        show player 14 with dissolve
        player_name "!!!"
        player_name "I didn't think {b}Ms. Okita{/b} would have so many gadgets in here."
        show player 12
        player_name "Hmm..."
        player_name "Those blueprints."
        player_name "Looks like she's working on something..."
        hide player with dissolve
    $ callScreen(location_count)