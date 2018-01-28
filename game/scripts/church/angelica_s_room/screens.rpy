screen angelicas_room:
    add gTimer.image("backgrounds/location_church_nun{}.jpg")

    if M_mia.get_state() == S_mia_church_plan and gTimer.is_weekend() and gTimer.is_morning():
        imagebutton:
            focus_mask True
            pos (52,205)
            idle "objects/object_robe_01.png"
            hover "objects/object_robe_01b.png"
            action Hide("angelicas_room"), Jump("priest_outfit")

    if is_here("angelica") and is_here("helen"):
        imagebutton:
            focus_mask True
            pos (225,270)
            if M_mia.get_state() in [S_mia_angelicas_order, S_mia_angelicas_whip]:
                idle "objects/character_angelica_05.png"
                hover "objects/character_angelica_05b.png"

            else:
                idle "objects/character_angelica_04.png"
                hover "objects/character_angelica_04b.png"
            action Hide("angelicas_room"), Jump("angelicas_room_dialogue")

    elif is_here("angelica"):
        imagebutton:
            focus_mask True
            pos (225,270)
            idle "objects/character_angelica_02.png"
            hover "objects/character_angelica_02b.png"
            action Hide("angelicas_room"), Jump("angelicas_room_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/door11_option_01.png"
        hover "boxes/door11_option_01b.png"
        action Hide("angelicas_room"), Jump("church_stairs_dialogue")

screen helen_ang_chamber_ang_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("helen_ang_churchsex_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("helen_ang_chamber_ang_sex_cum")
        xpos 450
        ypos 700

    if M_helen.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("helen_ang_chamber_ang_slower_sex")
            xpos 250
            ypos 735

    if M_helen.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("helen_ang_chamber_ang_faster_sex")
            xpos 450
            ypos 735

screen helen_ang_chamber_mc_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("helen_mc_churchsex_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("helen_ang_chamber_mc_sex_cum")
        xpos 450
        ypos 700

    if M_helen.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("helen_ang_chamber_mc_slower_sex")
            xpos 250
            ypos 735

    if M_helen.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("helen_ang_chamber_mc_faster_sex")
            xpos 450
            ypos 735