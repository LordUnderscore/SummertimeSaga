screen mias_bedroom:
    add gTimer.image("backgrounds/location_mia_bedroom{}.jpg")

    if is_here("mia"):
        imagebutton:
            focus_mask True
            pos (300,300)
            idle "objects/character_mia_01c.png"
            hover "objects/character_mia_01d.png"
            action Hide("mias_bedroom"), Jump("mia_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("mias_bedroom"), Jump("mias_upstairs")

screen mia_bedroom_sex_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump("mia_bedroom_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover "buttons/diane_stage01_03b.png"
        action Jump("mia_bedroom_sex_cum_outside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("mia_bedroom_sex_cum_inside")
        xpos 550
        ypos 700

    if M_mia.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Jump("mia_bedroom_slower_sex")
            xpos 250
            ypos 735

    if M_mia.get('sex speed') > .076 and M_mia.is_set('vaginal sex') or M_mia.get('sex speed') > .126 and M_mia.get('butt speed') == 1 or M_mia.get('sex speed') > .076 and M_mia.get('butt speed') > 1:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Jump("mia_bedroom_faster_sex")
            xpos 450
            ypos 735