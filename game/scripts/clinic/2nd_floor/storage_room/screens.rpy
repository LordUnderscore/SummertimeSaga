screen hospital_storage_room:
    add "backgrounds/location_hospital_storage.jpg"

    imagebutton:
        focus_mask True
        pos (247,282)
        idle "objects/object_door_80.png"
        hover "objects/object_door_80b.png"
        action Hide("hospital_storage_room"), Jump("hospital_storage_cabinet_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("hospital_storage_room"), Jump("hospital_second_floor_dialogue")

screen hospital_storage_cabinet:
    add "backgrounds/location_hospital_cabinet.jpg"

    imagebutton:
        focus_mask True
        pos (98,173)
        idle "objects/object_pharmacy_01.png"
        hover "objects/object_pharmacy_01b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (486,207)
        idle "objects/object_pharmacy_02.png"
        hover "objects/object_pharmacy_02b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (770,226)
        idle "objects/object_pharmacy_03.png"
        hover "objects/object_pharmacy_03b.png"
        action Show("popup_unfinished")

    if birth_control_pills not in inventory.items:
        imagebutton:
            focus_mask True
            pos (148,469)
            idle "objects/object_pharmacy_04.png"
            hover "objects/object_pharmacy_04b.png"
            action Function(inventory.get_item, item = birth_control_pills), Show("popup", Image = "boxes/popup_item_pills1.png")

    imagebutton:
        focus_mask True
        pos (331,502)
        idle "objects/object_pharmacy_05.png"
        hover "objects/object_pharmacy_05b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (596,466)
        idle "objects/object_pharmacy_06.png"
        hover "objects/object_pharmacy_06b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (732,457)
        idle "objects/object_pharmacy_07.png"
        hover "objects/object_pharmacy_07b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("hospital_storage_room"), Jump("hospital_storage_room_dialogue")

screen roz_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("roz_sex_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("roz_sex_cum")
        xpos 450
        ypos 700

    if M_roz.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("roz_slower_sex")
            xpos 250
            ypos 735

    if M_roz.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("roz_faster_sex")
            xpos 450
            ypos 735