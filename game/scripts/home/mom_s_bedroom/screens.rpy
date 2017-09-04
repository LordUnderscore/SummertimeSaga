screen moms_bedroom:
    if not gTimer.is_dark():
        add "backgrounds/location_mombedroom.jpg"

        if mom_count >= 11 and m6_note_seen and mom_basement_sex or mom_count >= 11 and not m6_note_seen:
            imagebutton:
                focus_mask True
                pos (550,400)
                idle "objects/character_mom_03.png"
                hover "objects/character_mom_03b.png"
                action Hide("moms_bedroom"), Jump("mom_dialogue_button_room")

        elif learn_kissing and m6_note_seen and mom_basement_sex or learn_kissing and not m6_note_seen:
            imagebutton:
                focus_mask True
                pos (435,435)
                idle "objects/object_bed_03.png"
                hover "objects/object_bed_03b.png"
                action Show("bed03_options")

        if m6_note_seen and not fetched_laundry:
            imagebutton:
                focus_mask True
                pos (247,517)
                idle "objects/object_laundry_01.png"
                hover "objects/object_laundry_01b.png"
                action Hide("moms_bedroom"), Jump("mom_room_laundry")

        imagebutton:
            focus_mask True
            pos (0,459)
            idle "objects/object_desk_07.png"
            hover "objects/object_desk_07b.png"
            action Show("desk07_options")

    else:
        add "backgrounds/location_mombedroom_night.jpg"

        imagebutton:
            focus_mask True
            pos (435,435)
            idle "objects/object_bed_03_night.png"
            hover "objects/object_bed_03b_night.png"
            action Show("bed03_options")

        imagebutton:
            focus_mask True
            pos (0,459)
            idle "objects/object_desk_07_night.png"
            hover "objects/object_desk_07b_night.png"
            action Show("desk07_options")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_12.png"
        hover "boxes/auto_option_12b.png"
        action Hide("moms_bedroom"), Jump("home_livingroom_dialogue")

screen moms_drawer:
    add "backgrounds/location_momdrawer.jpg"

    imagebutton:
        focus_mask True
        pos (-4,283)
        idle "objects/object_panties_02.png"
        hover "objects/object_panties_02b.png"
        action Hide("moms_drawer"), Jump("mom_drawer_continue")

screen bed03_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bed03_options")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (350,600)
            idle "boxes/bed03_option_01.png"
            hover "boxes/bed03_option_01b.png"
            action Hide("bed03_options"), Hide("moms_bedroom"), Jump("mom_bed")

    else:
        imagebutton:
            focus_mask True
            pos (350,600)
            idle "boxes/bed03_option_02.png"
            hover "boxes/bed03_option_02b.png"
            action Hide("bed03_options"), Hide("moms_bedroom"), Jump("mom_bed")

screen desk07_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk07_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk07_option_01.png"
        hover "boxes/desk07_option_01b.png"
        action Hide("desk07_options"), Hide("moms_bedroom"), Jump("mom_drawer")

screen mom_sex_options:
    if mom_sex_position == "missionary":
        imagebutton:
            pos (50,700)
            idle "buttons/judith_stage02_01.png"
            hover "buttons/judith_stage02_01b.png"
            action Jump("missionary_loop")

        imagebutton:
            pos (250,700)
            idle "buttons/diane_stage01_02.png"
            hover "buttons/diane_stage01_02b.png"
            action Jump("mom_missionary_cum")

        imagebutton:
            pos (450,700)
            idle "buttons/diane_stage01_03.png"
            hover "buttons/diane_stage01_03b.png"
            action Jump("mom_missionary_cum_outside")

        imagebutton:
            pos (650,700)
            idle "buttons/mom_stage01_07.png"
            hover "buttons/mom_stage01_07b.png"
            action SetVariable("mom_sex_position", "cowgirl"), Jump("cowgirl_loop")

    elif mom_sex_position == "cowgirl":
        imagebutton:
            pos (-30,700)
            idle "buttons/judith_stage02_01.png"
            hover "buttons/judith_stage02_01b.png"
            action Jump("cowgirl_loop")

        imagebutton:
            pos (170,700)
            idle "buttons/judith_stage01_03.png"
            hover "buttons/judith_stage01_03b.png"
            action SetVariable("xray", False), Jump("suck_tits")

        imagebutton:
            pos (370,700)
            idle "buttons/diane_stage01_02.png"
            hover "buttons/diane_stage01_02b.png"
            action Jump("mom_cowgirl_cum")

        imagebutton:
            pos (570,700)
            idle "buttons/diane_stage01_03.png"
            hover "buttons/diane_stage01_03b.png"
            action Jump("mom_cowgirl_cum_outside")

        imagebutton:
            pos (770,700)
            idle "buttons/mom_stage01_08.png"
            hover "buttons/mom_stage01_08b.png"
            action SetVariable("mom_sex_position", "missionary"), Jump("missionary_loop")

screen xray_scr:
    imagebutton:
        focus_mask True
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover "buttons/anim_03b.png"
        else:
            idle "buttons/anim_04.png"
            hover "buttons/anim_04b.png"
        action If(xray, SetVariable("xray", False), SetVariable("xray", True))

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