screen eriks_house tag eriks_house:
    add gTimer.image("backgrounds/location_erik_house{}.jpg")

    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    imagebutton:
        focus_mask True
        pos (350,417)
        idle gTimer.image("objects/object_door_18{}.png")
        hover gTimer.image("objects/object_door_18b{}.png")
        action If(
            not erik.over(erik_intro),
            [Hide("eriks_house"), Jump("door18_locked_dialogue")],
            [Hide("eriks_house"),
             If(
                mrsj.known(mrsj_intro),
                If(
                    not gTimer.is_dark(),
                    [Play("audio", sfxDoor()),
                     If(
                        erik.in_progress(erik_gf_stolen),
                        Jump("erik_gf_stolen"),
                        Jump("erik_indoors")
                     )
                    ],
                    If(
                        erik.in_progress(erik_thief),
                        [Jump("erik_thief_block")],
                        [Function(playSound), Play("audio", sfxDoor()),
                         If(
                            erik.in_progress(erik_gf_stolen),
                            Jump("erik_gf_stolen"),
                            Jump("erik_indoors")
                         )
                        ],
                    )
                ),
                Jump("closed_erik")
             )
            ]
        )

    imagebutton:
        focus_mask True
        pos (846,410)
        idle gTimer.image("objects/object_door_67{}.png")
        hover gTimer.image("objects/object_door_67b{}.png")
        action [Hide("eriks_house"), Jump("erik_backyard_dialogue")]

    imagebutton:
        focus_mask True
        if erik_mail != []:
            pos (735,480)
            idle gTimer.image("objects/object_mailbox_erik01{}.png")
            hover gTimer.image("objects/object_mailbox_erik01b{}.png")
        else:
            pos (735,500)
            idle gTimer.image("objects/object_mailbox_erik02{}.png")
            hover gTimer.image("objects/object_mailbox_erik02b{}.png")
        action Hide("eriks_house"), Show("erik_mailbox")

screen erik_mailbox:
    if gTimer.is_dark():
        add "backgrounds/mailbox_erik_night.jpg"
    else:
        add "backgrounds/mailbox_erik_day.jpg"

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("erik_mailbox"), Jump("erik_house")

    if m_magazine in erik_mail:
        imagebutton:
            focus_mask True
            pos (310,455)
            idle gTimer.image("objects/object_mailbox_item01{}.png")
            hover gTimer.image("objects/object_mailbox_item01b{}.png")
            action Hide("erik_mailbox"), Jump("erik_mailbox")

    elif m_dad_letter in erik_mail:
        imagebutton:
            focus_mask True
            pos (510,345)
            idle gTimer.image("objects/object_mailbox_item03{}.png")
            hover gTimer.image("objects/object_mailbox_item03b{}.png")
            action Hide("erik_mailbox"), Jump("erik_mailbox")

    elif m_pizza_pamphlet in erik_mail:
        imagebutton:
            focus_mask True
            pos (240,480)
            idle gTimer.image("objects/object_mailbox_item02{}.png")
            hover gTimer.image("objects/object_mailbox_item02b{}.png")
            action Hide("erik_mailbox"), Jump("erik_mailbox")

    elif m_newspaper in erik_mail:
        imagebutton:
            focus_mask True
            pos (250,575)
            idle gTimer.image("objects/object_mailbox_item05{}.png")
            hover gTimer.image("objects/object_mailbox_item05b{}.png")
            action Hide("erik_mailbox"), Jump("erik_mailbox")