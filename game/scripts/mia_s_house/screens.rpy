screen mias_house:
    add gTimer.image("backgrounds/location_mia{}.jpg")

    imagebutton:
        focus_mask True
        pos (571,442)
        idle gTimer.image("objects/object_door_24{}.png")
        hover gTimer.image("objects/object_door_24b{}.png")
        action If(
            gTimer.is_weekend() and gTimer.is_morning(),
            [Hide("mias_house"), Jump("closed_mia")],
            If(
                M_mia.get_state() == S_mia_need_space,
                [Hide("mias_house"), Jump("mia_banned")],
                If(
                    gTimer.is_morning(),
                    [Hide("mias_house"), Jump("closed_mia")],
                    If(
                        gTimer.is_afternoon(),
                        If(
                            not M_mia.is_set('front door locked'),
                            [Hide("mias_house"), Function(playSound), Jump("mias_entrance")],
                            [Hide("mias_house"), Jump("closed_mia")]
                        ),
                        If(
                            gTimer.is_evening(),
                            If(
                                not M_mia.is_set('front door locked'),
                                [Hide("mias_house"), Jump("mias_house_sneak")],
                                [Hide("mias_house"), Jump("night_closed_mia")]
                            ),
                            If(
                                M_mia.get_state() in [S_mia_midnight_help, S_mia_locked_room],
                                [Hide("mias_house"), Jump("mias_house_sneak")],
                                [Hide("mias_house"), Jump("night_closed_mia")]
                            )
                        )
                    )
                )
            )
        )

    if is_here("mia"):
        imagebutton:
            focus_mask True
            pos (270,480)
            idle "objects/character_mia_02.png"
            hover "objects/character_mia_02b.png"
            action Hide("mias_house"), Jump("mia_button_dialogue_house")

    imagebutton:
        focus_mask True
        if mia_mail != []:
            pos (830,480)
            idle gTimer.image("objects/object_mailbox_mia01{}.png")
            hover gTimer.image("objects/object_mailbox_mia01b{}.png")

        else:
            pos (830,500)
            idle gTimer.image("objects/object_mailbox_mia02{}.png")
            hover gTimer.image("objects/object_mailbox_mia02b{}.png")
        action Hide("mias_house"), Show("mia_mailbox")

screen mia_mailbox:
    add gTimer.image("backgrounds/mailbox_mia_day{}.jpg")

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("mia_mailbox"), Jump("mias_house")

    if m_pizza_pamphlet in mia_mail:
        imagebutton:
            focus_mask True
            pos (240,480)
            idle gTimer.image("objects/object_mailbox_item02{}.png")
            hover gTimer.image("objects/object_mailbox_item02b{}.png")
            action Hide("mia_mailbox"), Jump("mia_mailbox")

    elif m_newspaper in mia_mail:
        imagebutton:
            focus_mask True
            pos (250,575)
            idle gTimer.image("objects/object_mailbox_item05{}.png")
            hover gTimer.image("objects/object_mailbox_item05b{}.png")
            action Hide("mia_mailbox"), Jump("mia_mailbox")