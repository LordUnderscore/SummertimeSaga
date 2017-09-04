screen pool:
    if not gTimer.is_dark():
        add "backgrounds/location_pool.jpg"
        imagebutton:
            focus_mask True
            idle "objects/object_diving_01.png"
            hover "objects/object_diving_01b.png"
            action Show("diving_options")
            xpos 129
            ypos 382

        imagebutton:
            focus_mask True
            idle "objects/object_door_25.png"
            hover "objects/object_door_25b.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    almost_drowned,
                    [Hide("pool"), Jump("medic_dialogue")],
                    [Hide("pool"), Jump("poolrules03_dialogue")]
                )
            )
            xpos 706
            ypos 375

        imagebutton:
            focus_mask True
            idle "objects/object_door_26.png"
            hover "objects/object_door_26b.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    swimsuit in inventory.items,
                    [Hide("pool"), Jump("changing01_dialogue")],
                    [Hide("pool"), Jump("locked_door26_dialogue")]
                )
            )
            xpos 774
            ypos 367

        imagebutton:
            focus_mask True
            idle "objects/object_door_27.png"
            hover "objects/object_door_27b.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    swimsuit in inventory.items,
                    [Hide("pool"), Jump("changing01_dialogue")],
                    [Hide("pool"), Jump("locked_door26_dialogue")]
                )
            )
            xpos 849
            ypos 358

        imagebutton:
            focus_mask True
            idle "objects/object_door_28.png"
            hover "objects/object_door_28b.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    swimsuit in inventory.items,
                    [Hide("pool"), Jump("changing01_dialogue")],
                    [Hide("pool"), Jump("locked_door26_dialogue")]
                )
            )
            xpos 932
            ypos 348

        imagebutton:
            focus_mask True
            idle "objects/character_ronda_01.png"
            hover "objects/character_ronda_01b.png"
            action Hide("pool"), Jump("ronda_button_dialogue")
            xpos 630
            ypos 386

        imagebutton:
            focus_mask True
            idle "objects/character_cassie_01.png"
            hover "objects/character_cassie_01b.png"
            action Hide("pool"), Jump("cassie_button_dialogue")
            xpos 489
            ypos 307
    else:
        add "backgrounds/location_pool_night.jpg"
        imagebutton:
            focus_mask True
            idle "objects/object_diving_01_night.png"
            hover "objects/object_diving_01b_night.png"
            action Show("diving_options")
            xpos 129
            ypos 382

        imagebutton:
            focus_mask True
            idle "objects/object_door_25_night.png"
            hover "objects/object_door_25b_night.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    almost_drowned,
                    [Hide("pool"), Jump("medic_dialogue")],
                    [Hide("pool"), Jump("poolrules03_dialogue")]
                )
            )
            xpos 706
            ypos 375

        imagebutton:
            focus_mask True
            idle "objects/object_door_26_night.png"
            hover "objects/object_door_26b_night.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    swimsuit in inventory.items,
                    [Hide("pool"), Jump("changing01_dialogue")],
                    [Hide("pool"), Jump("locked_door26_dialogue")]
                )
            )
            xpos 774
            ypos 367

        imagebutton:
            focus_mask True
            idle "objects/object_door_27_night.png"
            hover "objects/object_door_27b_night.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    swimsuit in inventory.items,
                    [Hide("pool"), Jump("changing01_dialogue")],
                    [Hide("pool"), Jump("locked_door26_dialogue")]
                )
            )
            xpos 849
            ypos 358

        imagebutton:
            focus_mask True
            idle "objects/object_door_28_night.png"
            hover "objects/object_door_28b_night.png"
            action If(
                gTimer.is_dark(),
                [Hide("pool"), Jump("pool_dialogue")],
                If(
                    swimsuit in inventory.items,
                    [Hide("pool"), Jump("changing01_dialogue")],
                    [Hide("pool"), Jump("locked_door26_dialogue")]
                )
            )
            xpos 932
            ypos 348

screen diving_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("diving_options")]
    if poolrules_count == 0:
        imagebutton:
            idle "boxes/diving_option_01.png"
            hover "boxes/diving_option_01b.png"
            action If(
                gTimer.is_dark(),
                [Hide("diving_options"),Hide ("pool"), Jump ("pool_dialogue")],
                [Hide ("diving_options"),Hide ("pool"), Jump ("poolrules01_dialogue")]
            )
            xpos 350
            ypos 600
    elif poolrules_count == 1:
        imagebutton:
            idle "boxes/diving_option_01.png"
            hover "boxes/diving_option_01b.png"
            action If(
                gTimer.is_dark(),
                [Hide("diving_options"),Hide ("pool"), Jump ("pool_dialogue")],
                [Hide ("diving_options"),Hide ("pool"), Jump ("poolrules02_dialogue")]
            )
            xpos 350
            ypos 600
    elif poolrules_count == 2:
        imagebutton:
            idle "boxes/diving_option_01.png"
            hover "boxes/diving_option_01b.png"
            action If(
                gTimer.is_dark(),
                [Hide("diving_options"),Hide ("pool"), Jump ("pool_dialogue")],
                [Hide ("diving_options"),Hide ("pool"), Jump ("pool_cutscene01")]
            )
            xpos 350
            ypos 600
    else:
        imagebutton:
            idle "boxes/diving_option_01.png"
            hover "boxes/diving_option_01b.png"
            action If(
                gTimer.is_dark(),
                [Hide("diving_options"),Hide ("pool"), Jump ("pool_dialogue")],
                If(
                    first_swim,
                    [Hide ("diving_options"),Hide ("pool"), Jump ("pool_cutscene01")],
                    [Hide ("diving_options"),Hide ("pool"), Jump ("pool_cutscene02")]
                )
            )
            xpos 350
            ypos 600

screen gloryhole_stage01:
    add "backgrounds/location_changeroom03b.jpg"
    imagebutton:
        idle "buttons/gloryhole_stage01_01.png"
        hover "buttons/gloryhole_stage01_01b.png"
        action Hide ("gloryhole_stage01"), Jump("gloryhole_medic_bj")
        xpos 180
        ypos 700

    imagebutton:
        idle "buttons/gloryhole_stage01_02.png"
        hover "buttons/gloryhole_stage01_02b.png"
        action Hide ("gloryhole_stage01"), Jump("gloryhole_medic_fuck_fail")
        xpos 380
        ypos 700

    imagebutton:
        idle "buttons/gloryhole_stage01_03.png"
        hover "buttons/gloryhole_stage01_03b.png"
        action Hide ("gloryhole_stage01"), Jump("gloryhole_medic_fuckraw_fail")
        xpos 580
        ypos 700

screen gloryhole_stage02:
    add "backgrounds/location_changeroom03b.jpg"
    imagebutton:
        idle "buttons/gloryhole_stage02_01.png"
        hover "buttons/gloryhole_stage02_01b.png"
        action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_bj")
        xpos 90
        ypos 700

    imagebutton:
        idle "buttons/gloryhole_stage02_02.png"
        hover "buttons/gloryhole_stage02_02b.png"
        action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_bjtitsfinal")
        xpos 290
        ypos 700

    imagebutton:
        idle "buttons/gloryhole_stage02_03.png"
        hover "buttons/gloryhole_stage02_03b.png"
        action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_bjfacefinal")
        xpos 490
        ypos 700

    imagebutton:
        idle "buttons/gloryhole_stage02_04.png"
        hover "buttons/gloryhole_stage02_04b.png"
        action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_swallow_fail")
        xpos 690
        ypos 700