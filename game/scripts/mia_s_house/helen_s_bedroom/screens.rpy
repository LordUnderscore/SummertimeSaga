screen helens_bedroom:
    if M_helen.get_state() == S_helen_master_servant_fun:
        add "backgrounds/location_mia_house_helen_closed.jpg"

    else:
        add gTimer.image("backgrounds/location_mia_house_helen{}.jpg")

    if M_mia.get_state() == S_mia_midnight_help:
        imagebutton:
            focus_mask True
            pos (864,436)
            idle "objects/object_statue_01.png"
            hover "objects/object_statue_01b.png"
            action Hide("helens_bedroom"), Jump("helens_mary_statue")

    if is_here("helen"):
        imagebutton:
            focus_mask True
            if not M_mia.is_set('helen button change'):
                pos (170,400)
                if M_helen.get_state() in [S_helen_master_servant_fun, S_helen_end]:
                    idle "objects/character_helen_02.png"
                    hover "objects/character_helen_02b.png"

                else:
                    idle gTimer.image("objects/character_helen_01{}.png")
                    hover gTimer.image("objects/character_helen_01b{}.png")

            else:
                pos (340,470)
                idle gTimer.image("objects/character_helen_03{}.png")
                hover gTimer.image("objects/character_helen_03b{}.png")
            action Hide("helens_bedroom"), Jump("helen_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("helens_bedroom"), Jump("mias_upstairs")

screen helen_bedroom_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("helen_bedroom_sex_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("helen_bedroom_sex_cum")
        xpos 450
        ypos 700

    if M_helen.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("helen_bedroom_slower_sex")
            xpos 250
            ypos 735

    if M_helen.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("helen_bedroom_faster_sex")
            xpos 450
            ypos 735