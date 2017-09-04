screen police_lobby:
    add "backgrounds/location_police_lobby.jpg"

    imagebutton:
        focus_mask True
        pos (151,360)
        idle "images/objects/object_door_49.png"
        hover "images/objects/object_door_49b.png"
        action Hide("police_lobby"), Jump("police_basement_dialogue")

    imagebutton:
        focus_mask True
        pos (586,376)
        idle "images/objects/object_door_50.png"
        hover "images/objects/object_door_50b.png"
        action Hide("police_lobby"), Jump("police_office_dialogue")

    imagebutton:
        focus_mask True
        pos (12,338)
        idle "images/objects/object_board_03.png"
        hover "images/objects/object_board_03b.png"
        action Hide("police_lobby"), Jump("police_board")