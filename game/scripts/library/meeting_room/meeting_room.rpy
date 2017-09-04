label meeting_room_dialogue:
    $ location_count = "Library Meeting Room"
    $ callScreen(location_count)

label meeting_room_table_dialogue:
    scene library_meeting_c with None
    show xtra 19 zorder 2 at Position(xpos = 597, ypos = 675)
    show popup_unfinished zorder 3 at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    $ callScreen(location_count)