screen shower:
    $ location_count = "Shower"
    add gTimer.image("backgrounds/location_shower_02{}.jpg")

    if M_mom.get_state() == S_mom_fetch_towel and towel not in inventory.items:
        imagebutton:
            focus_mask True
            pos (657,370)
            idle "objects/object_towel_01.png"
            hover "objects/object_towel_01b.png"
            action Function(inventory.get_item, item = towel), Show("popup", Image = "boxes/popup_item_towel1.png")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_01.png"
        hover "boxes/auto_option_01b.png"
        action Hide("shower"), Jump("hallway_dialogue")

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
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Hide("shower_mom_sex_options"), Jump("mom_shower_sex_loop")

    imagebutton:
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Hide("shower_mom_sex_options"), Jump("mom_shower_sex_cum")

    if anim_toggle:
        if M_mom.get("sex speed") < .4:
            imagebutton:
                pos (250,735)
                idle "buttons/speed_02.png"
                hover "buttons/speed_02b.png"
                action Hide("shower_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get('sex speed') + 0.1), Jump("mom_shower_sex_loop_screen_skip")

        if M_mom.get("sex speed") > .21:
            imagebutton:
                pos (450,735)
                idle "buttons/speed_01.png"
                hover "buttons/speed_01b.png"
                action Hide("shower_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get('sex speed') - 0.1), Jump("mom_shower_sex_loop_screen_skip")

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