screen shower:
    $ location_count = "Shower"
    add gTimer.image("backgrounds/location_shower_02{}.jpg")

    imagebutton:
        idle "boxes/auto_option_01.png"
        hover "boxes/auto_option_01b.png"
        action Hide("shower"), Jump("hallway_dialogue")
        xpos 350
        ypos 600

screen shower_sex_buttons:
    imagebutton:
        focus_mask True
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover "buttons/anim_03b.png"
        else:
            idle "buttons/anim_04.png"
            hover "buttons/anim_04b.png"
        action If(
            xray,
            SetVariable("xray", False),
            SetVariable("xray", True)
        )

    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover "buttons/anim_02b.png"
        else:
            idle "buttons/anim_01.png"
            hover "buttons/anim_01b.png"
        action [
            If(
                anim_toggle,
                SetVariable("anim_toggle", False),
                SetVariable("anim_toggle", True)
            ),
            Return
        ]

screen shower_mom_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("mom_shower_sex_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("mom_shower_sex_cum")
        xpos 450
        ypos 700

    if M_mom.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("mom_shower_slower_sex")
            xpos 250
            ypos 735

    if M_mom.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("mom_shower_faster_sex")
            xpos 450
            ypos 735

screen sis_shower_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("sis_shower_sex_loop")
        xpos 250
        ypos 700

    if pStats.str() < 7:
        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_02.png"
            hover "buttons/diane_stage01_02b.png"
            action Jump("sis_shower_sex_cum_1")
            xpos 450
            ypos 700

    if pStats.str() >= 7:
        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_02.png"
            hover "buttons/diane_stage01_02b.png"
            action Jump("sis_shower_sex_cum_2")
            xpos 450
            ypos 700

    if M_sis.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("sis_shower_slower_sex")
            xpos 250
            ypos 735

    if M_sis.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("sis_shower_faster_sex")
            xpos 450
            ypos 735