screen library_backroom:
    if quest06 not in completed_quests:
        add "backgrounds/location_library_backroom01.jpg"
    else:
        add "backgrounds/location_library_backroom01_hd_cam.jpg"

    imagebutton:
        focus_mask True
        pos (300,700)
        idle "boxes/auto_option_04.png"
        hover "boxes/auto_option_04b.png"
        action Hide("library_backroom"), Jump("library_dialogue")

screen backroom_couple_sex01:
    $ backroom_count = 1

    imagebutton:
        pos (350,700)
        idle "buttons/backroom_stage01_01.png"
        hover "buttons/backroom_stage01_01b.png"
        action Hide("backroom_couple_sex01"), Jump("backroom_couple_finish01")