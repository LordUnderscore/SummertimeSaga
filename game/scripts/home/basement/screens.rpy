screen basement:
    add gTimer.image("backgrounds/location_home_basement{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,308)
        idle gTimer.image("objects/object_stairs_03{}.png")
        hover gTimer.image("objects/object_stairs_03b{}.png")
        action Hide("basement"), Jump("home_livingroom_dialogue")

    if M_mom.get_state() == S_mom_close_valve:
        imagebutton:
            focus_mask True
            pos (394,512)
            idle gTimer.image("objects/object_pipe_01{}.png")
            hover gTimer.image("objects/object_pipe_01b{}.png")
            action Hide("basement"), Jump("broken_pipe")

    if is_here("mom"):
        imagebutton:
            focus_mask True
            pos (486,320)
            idle "images/objects/character_mom_06.png"
            hover "images/objects/character_mom_06b.png"
            action Hide("basement"), If(
                                        M_mom.get_state() == S_mom_laundry_help and M_mom.is_set('chores'),
                                        Jump("laundry_dialogue"),
                                        Jump("mom_button_dialogue"),
                                     )

screen basement_mom_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("basement_mom_sex_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("basement_mom_sex_cum")
        xpos 450
        ypos 700

    if M_mom.get('sex speed') < .176:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("basement_mom_slower_sex")
            xpos 250
            ypos 735

    if M_mom.get('sex speed') > .075:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("basement_mom_faster_sex")
            xpos 450
            ypos 735