screen dianes_garden:
    if not gTimer.is_dark():
        add "backgrounds/location_garden.jpg"

        imagebutton:
            focus_mask True
            pos (26,369)
            idle "objects/object_door_08.png"
            hover "objects/object_door_08b.png"
            action If(
                aunt_count == 5 and not aunt_dialogue_advance,
                If(
                    gTimer.is_dark(),
                    [Hide("dianes_garden"), Jump("night_closed_garden")],
                    If(
                        aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur),
                        [Hide("dianes_garden"), Play("audio", sfxDoor()), Jump("kitchen_dialogue")],
                        [Hide("dianes_garden"), Jump("aunt_masturbate")]
                    )
                ),
                If(aunt_count == 5 and aunt_dialogue_advance ,
                   If(
                        gTimer.is_dark(),
                        [Hide("dianes_garden"), Jump("night_closed_garden")],
                        [Hide("dianes_garden"), Jump("after_masturbation")]
                   ),
                   If(
                        gTimer.is_dark(),
                        [Hide("dianes_garden"), Jump("night_closed_garden")],
                        [Hide("dianes_garden"), Play("audio", sfxDoor()), Jump("kitchen_dialogue")]
                   )
                )
            )

        imagebutton:
            focus_mask True
            pos (686,345)
            idle "objects/object_door_09.png"
            hover "objects/object_door_09b.png"
            action If(
                gTimer.is_dark(),
                [Hide("dianes_garden"),
                 If(
                    not gTimer.is_night(),
                    If(
                        shed_unlocked,
                        [Function(playSound), Jump("shed")],
                        Jump("night_closed_garden")
                    ),
                    Jump("night_closed_garden")
                 )
                ],
                [Hide("dianes_garden"),
                 If(
                    shed_unlocked,
                    [Function(playSound), Play("audio", "audio/sfx_door_heavy.ogg"), Jump("shed")],
                    Jump ("locked_shed_dialogue")
                 )
                ]
            )

        if (not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)) and (not aunt.known(aunt_drunken_splur) or aunt.over(aunt_drunken_splur)):
            if quest20 in completed_quests:
                if quest10 in quest_list and quest10 not in completed_quests:
                    $ garden_img_i = "objects/object_garden_01_dead.png"
                    $ garden_img_h = "objects/object_garden_01b_dead.png"
                else:
                    $ garden_img_i = "objects/object_garden_01.png"
                    $ garden_img_h = "objects/object_garden_01b.png"
                imagebutton:
                    focus_mask True
                    pos (36,535)
                    idle garden_img_i
                    hover garden_img_h
                    action Show("garden01_options")

        if (not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)) and (not aunt.known(aunt_drunken_splur) or aunt.over(aunt_drunken_splur)):
            if aunt_count < 8:
                if aunt_count != 5:
                    imagebutton:
                        focus_mask True
                        pos (491,397)
                        if aunt_drink_made:
                            idle "objects/character_diane_03.png"
                            hover "objects/character_diane_03b.png"
                        else:
                            idle "objects/character_diane_01.png"
                            hover "objects/character_diane_01b.png"
                        action Hide("dianes_garden"), Jump("aunt_button_dialogue")

    else:
        add "backgrounds/location_garden_night.jpg"
        imagebutton:
            focus_mask True
            pos (26,369)
            idle "objects/object_door_08_night.png"
            hover "objects/object_door_08b_night.png"
            action If(
                aunt_count == 5 and not aunt_dialogue_advance,
                If(
                    gTimer.is_dark(),
                    [Hide("dianes_garden"), Jump("night_closed_garden")],
                    [Hide("dianes_garden"), Jump("aunt_masturbate")]
                ),
                If(
                    aunt_count == 5 and aunt_dialogue_advance,
                    If(
                        gTimer.is_dark(),
                        [Hide("dianes_garden"), Jump("night_closed_garden")],
                        [Hide("dianes_garden"), Jump("after_masturbation")]
                    ),
                    If(
                        gTimer.is_dark(),
                        [Hide("dianes_garden"), Jump("night_closed_garden")],
                        [Hide("dianes_garden"), Function(playSound), Jump("kitchen_dialogue")]
                    )
                )
            )

        if quest09 in completed_quests and not aunt_shed_scene:
            imagebutton:
                focus_mask True
                pos (686,315)
                idle "objects/object_door_09_night02.png"
                hover "objects/object_door_09_night02b.png"
                action If(
                    gTimer.is_dark(),
                    [Hide("dianes_garden"),
                     If(
                        not gTimer.is_night(),
                        If(
                            shed_unlocked,
                            [Function(playSound), Jump("shed")],
                            Jump("night_closed_garden")
                        ),
                        Jump("night_closed_garden")
                     )
                    ],
                    [Hide("dianes_garden"),
                     If(
                        shed_unlocked,
                        [Function(playSound), Jump("shed")],
                        Jump ("locked_shed_dialogue")
                     )
                    ]
                )

        else:
            imagebutton:
                focus_mask True
                pos (686,345)
                idle "objects/object_door_09_night.png"
                hover "objects/object_door_09b_night.png"
                action If(
                    gTimer.is_dark(),
                    [Hide("dianes_garden"),
                     If(
                        not gTimer.is_night(),
                        If(
                            shed_unlocked,
                            [Function(playSound), Jump("shed")],
                            Jump("night_closed_garden")
                        ),
                        Jump("night_closed_garden")
                     )
                    ],
                    [Hide("dianes_garden"),
                     If(
                        shed_unlocked,
                        [Function(playSound), Jump("shed")],
                        Jump ("locked_shed_dialogue")
                     )
                    ]
                )

        if quest10 in quest_list and quest10 not in completed_quests:
            $ garden_img_i = "objects/object_garden_01_dead_night.png"
            $ garden_img_h = "objects/object_garden_01b_dead_night.png"

        else:
            $ garden_img_i = "objects/object_garden_01_night.png"
            $ garden_img_h = "objects/object_garden_01b_night.png"

        imagebutton:
            focus_mask True
            pos (36,535)
            idle garden_img_i
            hover garden_img_h
            action Show("garden01_options")

    if False:
        imagebutton:
            focus_mask True
            if not gTimer.is_dark():
                pos (928,420)
            else:
                pos (928,418)
            idle gTimer.image("objects/object_crack_02{}.png")
            hover gTimer.image("objects/object_crack_02b{}.png")
            action Show("popup_unfinished")

    else:
        imagebutton:
            focus_mask True
            if not gTimer.is_dark():
                pos (928,420)
            else:
                pos (928,416)
            idle gTimer.image("objects/object_crack_01{}.png")
            hover gTimer.image("objects/object_crack_01b{}.png")
            action Hide("dianes_garden"), Jump("church_graveyard_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("dianes_garden"), Jump("diane_front_yard")

screen garden01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("garden01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/garden_option_01.png"
        hover "boxes/garden_option_01b.png"
        if aunt_drink_offered:
            action Hide("garden01_options"), Hide("dianes_garden"), Jump("drink_offered")

        elif aunt_count == 5 and not aunt_dialogue_advance:
            action Hide("garden01_options"), Hide("dianes_garden"), Jump("before_masturbation")

        elif aunt_count == 5 and aunt_dialogue_advance:
            action Hide("garden01_options"), Hide("dianes_garden"), Jump("after_masturbation")

        else:
            action If(
                gTimer.is_dark(),
                [Hide("garden01_options"), Hide("dianes_garden"), Jump("night_closed_garden")],
                [Hide("garden01_options"), Hide("dianes_garden"), Jump("garden_listing")]
            )