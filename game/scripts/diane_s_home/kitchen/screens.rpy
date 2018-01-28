screen dianes_kitchen:
    add "backgrounds/location_diane_kitchen_empty.jpg"

    if aunt_drink_offered:
        imagebutton:
            focus_mask True
            pos (370,408)
            idle "objects/object_drinks_01.png"
            hover "objects/object_drinks_01b.png"
            action Hide("dianes_kitchen"), Jump("kitchen_drink")

    if (not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)) and (not aunt.known(aunt_drunken_splur) or aunt.over(aunt_drunken_splur)):
        if aunt_count >= 8:
            imagebutton:
                focus_mask True
                pos (345,219)
                idle "objects/character_diane_02.png"
                hover "objects/character_diane_02b.png"
                action Hide("dianes_kitchen"), Jump("aunt_button_dialogue")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (0,260)
            idle "objects/object_door_66.png"
            hover "objects/object_door_66b.png"
            action If(
                not aunt.known(aunt_mouse_attack),
                [Hide("dianes_kitchen"), Jump("dianelobby_locked")],
                [Hide("dianes_kitchen"), Function(playSound), Jump("dianelobby_dialogue")]
            )

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_07.png"
        hover "boxes/auto_option_07b.png"
        action If(
            aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack),
            [Hide("dianes_kitchen"), Jump("mouse_attack")],
            [Hide("dianes_kitchen"), SetVariable("in_garden", True), Jump("garden_dialogue")]
        )

screen aunt_sex_xray:
    if xray_toggle == True:
        if xray == 0:
            add "characters/player/char_player_sex_06.png" pos 550,418

        else:
            if condom_on == True:
                add "characters/player/char_player_sex_09.png" pos 562,399

            else:
                add "characters/player/char_player_sex_07.png" pos 562,399

screen aunt_sex_xray_buttons:
    imagebutton:
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover "buttons/anim_02b.png"
        else:
            idle "buttons/anim_01.png"
            hover "buttons/anim_01b.png"
        action If(anim_toggle, SetVariable("anim_toggle", False), SetVariable("anim_toggle", True)), Return

    imagebutton:
        pos (940,600)
        if xray_toggle:
            idle "buttons/anim_03.png"
            hover "buttons/anim_03b.png"
        else:
            idle "buttons/anim_04.png"
            hover "buttons/anim_04b.png"
        action If(xray_toggle, SetVariable("xray_toggle", False), SetVariable("xray_toggle", True))

screen aunt_sex_options:
    imagebutton:
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action If(not aunt_had_sex, Jump ("aunt_sex_loop"), If(condom_on, Jump ("aunt_sex_loop_3"), Jump("aunt_sex_loop_2")))

    imagebutton:
        pos (350,700)
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("aunt_sex_cum_in")

    imagebutton:
        pos (550,700)
        idle "buttons/diane_stage01_03.png"
        hover "buttons/diane_stage01_03b.png"
        action Jump("aunt_sex_cum_out")

    if M_aunt.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("aunt_kitchen_slower_sex")
            xpos 250
            ypos 735

    if M_aunt.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("aunt_kitchen_faster_sex")
            xpos 450
            ypos 735