screen mrs_smiths_office:
    add "backgrounds/location_office.jpg"

    if quest09_1 == True:
        add "characters/principal/char_principal_24.png" xpos 49 ypos 310

    else:
        imagebutton:
            focus_mask True
            pos (238,227)
            idle "objects/object_desk_03c.png"
            hover "objects/object_desk_03d.png"
            action Show("desk03_options")

        imagebutton:
            focus_mask True
            pos (350,700)
            idle "boxes/auto_option_01.png"
            hover "boxes/auto_option_01b.png"
            action Hide("mrs_smiths_office"), Jump("third_floor_dialogue")

    imagebutton:
        focus_mask True
        pos (847,387)
        idle "objects/object_desk_04.png"
        hover "objects/object_desk_04b.png"
        action Show("desk04_options")

screen principle_drawer:
    add "backgrounds/location_office_drawer.jpg"

    imagebutton:
        focus_mask True
        pos (110,25)
        idle "objects/object_papers_01.png"
        hover "objects/object_papers_01b.png"
        action Hide("principle_drawer"), Jump("milk_delivery")

screen desk03_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk03_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk03_option_01.png"
        hover "boxes/desk03_option_01b.png"
        action Hide("desk03_options"), Hide("mrs_smiths_office"), Jump("desk03_locked_dialogue")

screen desk04_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk04_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk04_option_01.png"
        hover "boxes/desk04_option_01b.png"
        if quest09_1 == True and quest09 not in completed_quests:
            action Hide("desk04_options"), Hide("mrs_smiths_office"), Jump("principle_drawer")
        else:
            action Hide("desk04_options"), Hide("mrs_smiths_office"), Jump("desk03_locked_dialogue")