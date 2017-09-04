label hospital_storage_room_dialogue:
    if hospital_access_card not in inventory.items:
        scene hospital_lock
        player_name "Damn, it's locked!"
        player_name "It looks like I need an {b}access card{/b} to unlock this door..."
        if not Roz.known(roz_storage):
            $ Roz.add_event(roz_storage)
        $ callScreen(location_count)
    $ location_count = "Hospital Storage Room"
    $ roz_storage.finish()
    $ callScreen(location_count)

label hospital_storage_cabinet_dialogue:
    $ location_count = "Hospital Storage Cabinet"
    if mrsj.started(mrsj_sex_ed) and birth_control_pills not in inventory.items:
        scene hospital_cabinet_filled
        player_name "Hmm..."
        player_name "There's quite a few kinds of pills here."
        player_name "Maybe that green box?"
    $ callScreen(location_count, False)