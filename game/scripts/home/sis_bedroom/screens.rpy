screen sybianscr:
    modal True

    if sybian_stage == 0:
        imagebutton:
            pos (50,320)
            idle "images/buttons/sybian_04.png"
            hover "images/buttons/sybian_04b.png"
            action Hide("sybianscr"), SetVariable("sybian_stage", 1), SetVariable("sis_sybian_speed", sis_sybian_speed - 0.25), Jump("sybian_stage1")

    if sybian_stage == 1:
        imagebutton:
            pos (50,320)
            idle "images/buttons/sybian_01.png"
            hover "images/buttons/sybian_01b.png"
            action Hide("sybianscr"), SetVariable("sybian_stage", 2), SetVariable("sis_sybian_speed", sis_sybian_speed - 0.25), Jump("sybian_stage2")

    if sybian_stage == 2:
        imagebutton:
            pos (50,320)
            idle "images/buttons/sybian_02.png"
            hover "images/buttons/sybian_02b.png"
            action Hide("sybianscr"), SetVariable("sybian_stage", 3), SetVariable("sis_sybian_speed", sis_sybian_speed - 0.25), Jump("sybian_stage3")

screen diary_next:
    imagebutton:
        idle "objects/object_diary_button01.png"
        hover "objects/object_diary_button01b.png"
        action Return()
        xpos 900
        ypos 330

screen sis_bedroom:
    add gTimer.image("backgrounds/location_sisbedroom{}.jpg")


    imagebutton:
        focus_mask True
        pos (30,327)
        idle gTimer.image("objects/object_desk_02{}.png")
        hover gTimer.image("objects/object_desk_02b{}.png")
        action Show("desk02_options")


    imagebutton:
        focus_mask True
        pos (865,483)
        idle gTimer.image("objects/object_bedtable_01{}.png")
        hover gTimer.image("objects/object_bedtable_01b{}.png")
        action Show("bedtable01_options")


    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_01.png"
        hover "boxes/auto_option_01b.png"
        action Hide("sis_bedroom"), Jump("hallway_dialogue")


    if not condom_taken:
        imagebutton:
            focus_mask True
            pos (465,590)

            idle "objects/object_condom_01.png"
            hover "objects/object_condom_01b.png"
            action Function(inventory.get_item, item = condom), SetVariable("condom_taken", True), Hide("sis_bedroom"), Jump("condom")


    if is_here("sis") and gTimer.is_dark():


        imagebutton:
            focus_mask True
            pos (362,416)
            idle "objects/object_bed_02_night.png"
            hover "objects/object_bed_02b_night.png"
            action Show("sisbed_options")

    elif is_here("sis"):
        if sister.over(sis_final):
            $ img_i = "objects/character_sister_03.png"
            $ img_h = "objects/character_sister_03b.png"
            $ img_x = 580
            $ img_y = 420

        elif sis_bedroom_count == 2:
            $ img_i = "objects/character_sister_01.png"
            $ img_h = "objects/character_sister_01b.png"
            $ img_x = 660
            $ img_y = 320

        else:
            $ img_i = "objects/character_sister_02.png"
            $ img_h = "objects/character_sister_02b.png"
            $ img_x = 600
            $ img_y = 400

        imagebutton:
            focus_mask True
            pos (img_x, img_y)
            idle img_i
            hover img_h
            action Hide("sis_bedroom"), Jump("sis_button_dialogue")


    else:
        if sis_diary_unlocked:
            imagebutton:
                focus_mask True
                pos (610,520)

                idle "objects/object_diary_item01.png"
                hover "objects/object_diary_item01b.png"
                action Hide("sis_bedroom"), Jump("diary_dialogue")

screen sisbed_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("sisbed_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/bed02_option_01.png"
        hover "boxes/bed02_option_01b.png"
        action Hide("sisbed_options"), Hide("sis_bedroom"), Jump("sneak_in_sis_bed")

screen desk02_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk02_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk02_option_01.png"
        hover "boxes/desk02_option_01b.png"
        action If(
            not gTimer.is_dark(),
            [Hide("desk02_options"), Hide("sis_bedroom"), Jump("siscomp_day")],
            [Hide("desk02_options"), Hide("sis_bedroom"), Jump("sis_computer")]
        )

screen bedtable01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk04_options")

    if bedtable01_count == 0:
        imagebutton:
            focus_mask True
            pos (350,600)
            idle "boxes/bedtable01_option_01.png"
            hover "boxes/bedtable01_option_01b.png"
            action If(
                not gTimer.is_dark(),
                [Hide("bedtable01_options"), Hide("sis_bedroom"), Jump("bedside01_dialogue")],
                [Hide("bedtable01_options"), Hide("sis_bedroom"), Jump("bedtable_night")]
            )

    else:
        imagebutton:
            focus_mask True
            pos (350,600)
            idle "boxes/bedtable01_option_01.png"
            hover "boxes/bedtable01_option_01b.png"
            action If(
                not gTimer.is_dark(),
                [Hide("bedtable01_options"), Hide("sis_bedroom"), Jump("bedside01_dialogue2")],
                [Hide("bedtable01_options"), Hide("sis_bedroom"), Jump("bedtable_night")]
            )

screen bedside01:
    add "backgrounds/location_sistable.jpg"
    imagebutton:
        idle "objects/object_panties_01.png"
        hover "objects/object_panties_01b.png"
        action Hide("bedside01"), Jump ("sis_bedroom_dialogue")
        xpos 382
        ypos 302

screen sis_cheerleader_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        if sis_cheerleader_sex2_menu:
            action Jump("sis_cheerleader_fuck_looprep2")
        else:
            action Jump("sis_cheerleader_fuck_looprep")
        if not sis_cheerleader_sex2_menu:
            xpos 150
            ypos 700
        else:
            xpos 250
            ypos 700


    if not sis_cheerleader_sex2_menu:
        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_03.png"
            hover "buttons/diane_stage01_03b.png"
            action Jump("sis_cheerleader_fuck_cum_outside")
            xpos 350
            ypos 700

    if sis_cheerleader_sex2_menu:
        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_02.png"
            hover "buttons/diane_stage01_02b.png"
            if sis_final_cum == "Outside":
                action Jump("sis_cheerleader_fuck_cum_inside_unhappy")
            elif sis_final_cum == "Inside" and sister.completed(sis_final2):
                action Jump("sis_cheerleader_fuck_cum_inside_happy")
            xpos 450
            ypos 700

    if pStats.str() < 7 and not sis_cheerleader_sex2_menu:
        imagebutton:
            focus_mask True
            idle "buttons/sis_break_01.png"
            hover "buttons/sis_break_01b.png"
            action Jump("sis_cheerleader_break_free_fail")
            xpos 550
            ypos 700

    if pStats.str() >= 7 and not sis_cheerleader_sex2_menu:
        imagebutton:
            focus_mask True
            idle "buttons/sis_break_01.png"
            hover "buttons/sis_break_01b.png"
            action Jump("sis_cheerleader_break_free_pass")
            xpos 550
            ypos 700

    if M_sis.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("sis_cheerleader_slower_sex")
            xpos 250
            ypos 735

    if M_sis.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("sis_cheerleader_faster_sex")
            xpos 450
            ypos 735