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