screen mrs_johnsons_room:
    add gTimer.image("backgrounds/location_erik_house_upstairs{}.jpg")

    imagebutton:
        focus_mask True
        pos (696,498)
        idle gTimer.image("objects/object_ball_01{}.png")
        hover gTimer.image("objects/object_ball_01b{}.png")
        action Hide("mrs_johnsons_room"), Jump("mrsj_ball")

    if is_here("mrsj"):
        if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
            imagebutton:
                focus_mask True
                pos (826,300)
                idle "objects/character_erikmom_03.png"
                hover "objects/character_erikmom_03b.png"
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        elif gTimer.is_dark() and erik.over(erik_gf):
            imagebutton:
                focus_mask True
                pos (250,420)
                idle "objects/character_erikmom_04.png"
                hover "objects/character_erikmom_04b.png"
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (0,410)
                idle gTimer.image("objects/object_bed_04_day{}.png")
                hover gTimer.image("objects/object_bed_04b_day{}.png")
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("mrs_johnsons_room"), Jump("erik_indoors")

screen erimom_private_pos1_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("mrsj_private_yoga_pos1_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/johnson_01.png"
        hover "buttons/johnson_01b.png"
        action Jump("erimom_private_pos1_switch")
        xpos 450
        ypos 700

    if M_erimom.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("erimom_private_pos1_slower_sex")
            xpos 250
            ypos 735

    if M_erimom.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("erimom_private_pos1_faster_sex")
            xpos 450
            ypos 735

screen erimom_private_pos2_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("mrsj_private_yoga_pos2_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("erimom_private_pos2_cum")
        xpos 450
        ypos 700

    if M_erimom.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("erimom_private_pos2_slower_sex")
            xpos 250
            ypos 735

    if M_erimom.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("erimom_private_pos2_faster_sex")
            xpos 450
            ypos 735

screen mrsj_3some_pos1_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("mrsj_3some_pos1_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/johnson_01.png"
        hover "buttons/johnson_01b.png"
        action Jump("mrsj_3some_pos1_switch")
        xpos 450
        ypos 700

    if M_erimom.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("mrsj_3some_pos1_slower_sex")
            xpos 250
            ypos 735

    if M_erimom.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("mrsj_3some_pos1_faster_sex")
            xpos 450
            ypos 735

screen mrsj_3some_pos2_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("mrsj_3some_pos2_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("mrsj_3some_pos2_cum")
        xpos 450
        ypos 700

    if M_erimom.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("mrsj_3some_pos2_slower_sex")
            xpos 250
            ypos 735

    if M_erimom.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("mrsj_3some_pos2_faster_sex")
            xpos 450
            ypos 735