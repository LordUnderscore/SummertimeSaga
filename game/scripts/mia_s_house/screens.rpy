screen mias_house:
    if not gTimer.is_dark():
        add "backgrounds/location_mia.jpg"
        imagebutton:
            idle "objects/object_door_24.png"
            hover "objects/object_door_24b.png"
            action If(
                gTimer.is_weekend() and gTimer.is_morning(),
                [Hide("mias_house"), Jump("closed_mia")],
                If(
                    gTimer.is_morning(),
                    If(
                        homework_count >= 1,
                        [Hide("mias_house"), Function(playSound), Jump("mias_entrance")],
                        [Hide("mias_house"), Jump("closed_mia")]
                    ),
                    If(
                        gTimer.is_afternoon(),
                        If(
                            homework_count >= 1,
                            [Hide("mias_house"), Function(playSound), Jump("mias_entrance")],
                            [Hide("mias_house"), Jump("closed_mia")]
                        ),
                        If(
                            gTimer.is_evening(),
                            If(
                                homework_count >= 1 and mias_house_kicked == 2,
                                [Hide("mias_house"), Jump("mias_house_sneak")],
                                [Hide("mias_house"), Jump("night_closed_mia")]
                            ),
                            [Hide("mias_house"), Jump("night_closed_mia")]
                        )
                    )
                )
            )
            xpos 571
            ypos 442
        if gTimer.is_weekend() and homework_count == 0:
            imagebutton:
                idle "objects/character_mia_02.png"
                hover "objects/character_mia_02b.png"
                action Hide("mias_house"), Jump("mia_button_dialogue_house")
                xpos 270
                ypos 480

        elif not gTimer.is_weekend() and not gTimer.is_morning() and homework_count == 0:
            imagebutton:
                idle "objects/character_mia_02.png"
                hover "objects/character_mia_02b.png"
                action Hide("mias_house"), Jump("mia_button_dialogue_house")
                xpos 270
                ypos 480

        imagebutton:
            if mia_mail != []:
                idle "objects/object_mailbox_mia01.png"
                hover "objects/object_mailbox_mia01b.png"
            else:
                idle "objects/object_mailbox_mia02.png"
                hover "objects/object_mailbox_mia02b.png"
            action [Hide("mias_house"), Show("mia_mailbox")]
            xpos 830
            if mia_mail != []:
                ypos 480
            else:
                ypos 500
    else:
        add "backgrounds/location_mia_night.jpg"
        imagebutton:
            idle "objects/object_door_24_night.png"
            hover "objects/object_door_24b_night.png"
            action If(
                gTimer.is_morning() and not gTimer.is_weekend(),
                [Hide("mias_house"), Jump("closed_mia")],
                If(
                    gTimer.is_morning(),
                    If(
                        homework_count >= 1,
                        [Hide("mias_house"), Function(playSound), Jump("mias_entrance")],
                        [Hide("mias_house"), Jump("closed_mia")]
                    ),
                    If(
                        gTimer.is_afternoon(),
                        If(
                            homework_count >= 1,
                            [Hide("mias_house"), Function(playSound), Jump("mias_entrance")],
                            [Hide("mias_house"), Jump("closed_mia")]
                        ),
                        If(
                            gTimer.is_evening(),
                            If(
                                homework_count >= 1 and mias_house_kicked == 2,
                                [Hide("mias_house"), Jump("mias_house_sneak")],
                                [Hide("mias_house"), Jump("night_closed_mia")]
                            ),
                            [Hide("mias_house"), Jump("night_closed_mia")]
                        )
                    )
                )
            )
            xpos 571
            ypos 442

        imagebutton:
            if mia_mail != []:
                idle "objects/object_mailbox_mia01_night.png"
                hover "objects/object_mailbox_mia01b_night.png"
            else:
                idle "objects/object_mailbox_mia02_night.png"
                hover "objects/object_mailbox_mia02b_night.png"
            action [Hide("mias_house"), Show("mia_mailbox")]
            xpos 830
            if mia_mail != []:
                ypos 480
            else:
                ypos 500

screen mias_house_entrance:
    if not gTimer.is_dark():
        add "backgrounds/location_mia_house.jpg"

        imagebutton:
            idle "objects/character_mia_01.png"
            hover "objects/character_mia_01b.png"
            action Hide("mias_house_entrance"), Jump("mia_button_dilaogue_indoors")
            xpos 280
            ypos 330
    else:
        add "backgrounds/location_mia_house_night.jpg"

        imagebutton:
            idle "objects/object_door_33.png"
            hover "objects/object_door_33b.png"
            action Hide("mias_house_entrance"), Function(playSound), Jump("mias_bedroom_screen")
            xpos 638
            ypos 104

    imagebutton:
        idle "boxes/auto_option_08.png"
        hover "boxes/auto_option_08b.png"
        action Hide("mias_house_entrance"), Jump("mias_house_dialogue")
        xpos 350
        ypos 700

screen mias_bedroom:
    add "backgrounds/location_mia_bedroom.jpg"
    imagebutton:
        idle "objects/character_mia_01.png"
        hover "objects/character_mia_01b.png"
        action Hide("mias_bedroom"), Jump("mia_button_dialogue_bedroom")
        xpos 300
        ypos 300

    imagebutton:
        idle "boxes/door11_option_01.png"
        hover "boxes/door11_option_01b.png"
        action Hide("mias_bedroom"), Jump("mias_entrance")
        xpos 350
        ypos 700

screen mia_mailbox:


    if not gTimer.is_dark():
        add "backgrounds/mailbox_mia_day.jpg"
    else:
        add "backgrounds/mailbox_mia_night.jpg"

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("mia_mailbox"), Jump("mias_house")]
    if m_pizza_pamphlet in mia_mail:
        imagebutton:
            idle gTimer.image("objects/object_mailbox_item02{}.png")
            hover gTimer.image("objects/object_mailbox_item02b{}.png")
            action [Hide("mia_mailbox"), Jump("mia_mailbox")]
            xpos 240
            ypos 480
    elif m_newspaper in mia_mail:
        imagebutton:
            idle gTimer.image("objects/object_mailbox_item05{}.png")
            hover gTimer.image("objects/object_mailbox_item05b{}.png")
            action [Hide("mia_mailbox"), Jump("mia_mailbox")]
            xpos 250
            ypos 575