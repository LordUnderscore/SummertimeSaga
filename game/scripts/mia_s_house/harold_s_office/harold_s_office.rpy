label harolds_office:
    $ location_count = "Harold's House Office"
    if M_mia.get_state() == S_mia_midnight_help:
        scene mia_house_office_n_b
        player_name "{b}Mia's{/b} not here... And I don't see any keys."
    $ callScreen(location_count)