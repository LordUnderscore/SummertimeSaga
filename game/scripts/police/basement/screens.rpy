screen police_basement:
    add "backgrounds/location_police_basement.jpg"

    imagebutton:
        focus_mask True
        pos (841,224)
        idle "images/objects/object_door_51.png"
        hover "images/objects/object_door_51b.png"
        action Hide("police_basement"), If(M_mia.get_state() == S_mia_inmate_status, Jump("inmate_transfer_block"), Jump("police_lobby_dialogue"))

    if is_here("yumi"):
        imagebutton:
            focus_mask True
            pos (536,418)
            idle "images/objects/character_yumi_01.png"
            hover "images/objects/character_yumi_01b.png"
            action Hide("police_basement"), Jump("police_yumi_dialogue")

    if erik.over(erik_thief):
        imagebutton:
            focus_mask True
            pos (314,286)
            idle "images/objects/object_cell_03.png"
            hover "images/objects/object_cell_03b.png"
            action Hide("police_basement"), Jump("police_cell_larry_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (314,286)
            idle "images/objects/object_cell_01.png"
            hover "images/objects/object_cell_01b.png"
            action Hide("police_basement"), Jump("police_cell_dialogue")

    imagebutton:
        focus_mask True
        pos (31,237)
        idle "images/objects/object_cell_02.png"
        hover "images/objects/object_cell_02b.png"
        action Hide("police_basement"), Jump("police_cell_dialogue")