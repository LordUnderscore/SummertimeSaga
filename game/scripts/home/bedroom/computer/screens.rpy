screen MC_computer:
    if MC_comp_locked:
        add gTimer.image("backgrounds/computer_player_01{}.jpg")
        add Input (size = 20, color = "#5d9aff", default = "", changed = MC_comp, length = 12, xpos = 425, ypos = 422)
        key "K_RETURN" action Jump("MC_pass_check")

        imagebutton:
            focus_mask True
            pos (780,405)
            idle "buttons/enter_03.png"
            hover "buttons/enter_03b.png"
            action Jump("MC_pass_check")

        imagebutton:
            focus_mask True
            pos (109,576)
            idle "buttons/computer_button_01.png"
            hover "buttons/computer_button_01b.png"
            action Hide("MC_computer"), Jump("bedroom_dialogue")
    else:
        add gTimer.image("backgrounds/computer_player_02{}.jpg")

        imagebutton:
            focus_mask True
            pos (105,603)
            idle "buttons/computer_button_02.png"
            hover "buttons/computer_button_02b.png"
            action Hide("MC_computer"), Jump("bedroom_dialogue")

        imagebutton:
            focus_mask True
            pos (105,140)
            idle "buttons/computer_icon_01.png"
            hover "buttons/computer_icon_01b.png"
            action Show("MC_recycle")

        imagebutton:
            focus_mask True
            pos (105,250)
            idle "buttons/computer_icon_02.png"
            hover "buttons/computer_icon_02b.png"
            action Show("MC_family")

        imagebutton:
            focus_mask True
            pos (105,360)
            idle "buttons/computer_icon_03.png"
            hover "buttons/computer_icon_03b.png"
            action Show("summertime_mc")

        imagebutton:
            focus_mask True
            pos (105,470)
            idle "buttons/computer_icon_04.png"
            hover "buttons/computer_icon_04b.png"
            action If(
                not connected,
                [Hide("MC_computer"), Jump("webcam_dialogue")],
                [Show("MC_webcam")]
            )

        imagebutton:
            focus_mask True
            pos (215,140)
            idle "buttons/computer_icon_13.png"
            hover "buttons/computer_icon_13b.png"
            if homework in inventory.items:
                if textbook1 in inventory.items:
                    action Hide("MC_computer"), Jump("bedroom_study01")
                else:
                    action Hide("MC_computer"), Jump("textbook_missing_dialogue")
            elif homework2 in inventory.items:
                if textbook2 in inventory.items:
                    action Hide("MC_computer"), Jump("bedroom_study01")
                else:
                    action Hide("MC_computer"), Jump("textbook_missing_dialogue")
            elif homework_count == 2:
                action Show("popup_unfinished")

        imagebutton:
            focus_mask True
            pos (215,250)
            idle "buttons/computer_icon_14.png"
            hover "buttons/computer_icon_14b.png"
            action Hide("MC_computer"), Jump("Maze")

        imagebutton:
            focus_mask True
            pos (215,360)
            idle "buttons/computer_icon_23.png"
            hover "buttons/computer_icon_23b.png"
            action Hide("MC_computer"), Jump("egay_search_dialogue")

screen summertime_mc:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    imagebutton:
        focus_mask True
        pos (270,150)
        idle "buttons/computer_window_07.png"
        action Hide("summertime_mc"), Show("summertime_error_mc")

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("summertime_mc")

screen summertime_error_mc:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "buttons/computer_window_08.png" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("summertime_error_mc")

screen egay(state):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    if state == "Search":
        add "buttons/computer_window_12.png" pos 270,150

        add Input (size = 20, color = "#5d9aff", default = "", changed = egay_search_string, length = 10, xpos = 575, ypos = 281)
        key "K_RETURN" action Hide("egay"), Hide("MC_computer"), Jump("egay_search")

    elif state == "Fail":
        add "buttons/computer_window_13.png" pos 270,150

        add Input (size = 20, color = "#5d9aff", default = "", changed = egay_search_string, length = 10, xpos = 575, ypos = 281)
        key "K_RETURN" action Hide("egay"), Hide("MC_computer"), Jump("egay_search")

    elif state == "Found":
        imagemap:
            ground "buttons/computer_window_14.png" at Position(xpos = 270, ypos = 150)
            hotspot (206,397,192,41) background "buttons/computer_window_14.png" action If(inventory.money >= 300,
                [SetField(inventory, "money", inventory.money - 300), Function(erik_orcette.finish),
                  Hide("MC_computer"), Jump("egay_purchased_dialogue")],
                [Show("popup", Image = "boxes/popup_shopping_fail01.png")]
            )

    elif state == "Purchased":
        add "buttons/computer_window_15.png" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("egay")

screen MC_recycle:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "buttons/computer_window_03.png" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("MC_recycle")

    imagebutton:
        focus_mask True
        pos (290,210)
        idle "buttons/computer_icon_17.png"
        hover "buttons/computer_icon_17b.png"
        action NullAction()

    imagebutton:
        focus_mask True
        pos (380,213)
        idle "buttons/computer_icon_18.png"
        hover "buttons/computer_icon_18b.png"
        action NullAction()

    imagebutton:
        focus_mask True
        pos (470,199)
        idle "buttons/computer_icon_19.png"
        hover "buttons/computer_icon_19b.png"
        action NullAction()

screen MC_webcam:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "buttons/computer_window_09.png" pos 270,150

    if not connected:
        add "buttons/computer_window_10.png" pos 304,302

    else:
        imagebutton:
            focus_mask True
            pos (370,380)
            idle "buttons/computer_icon_20.png"
            hover "buttons/computer_icon_20b.png"
            action Hide("MC_webcam"), Hide("MC_computer"), Jump("webcam_dialogue")

        imagebutton:
            focus_mask True
            pos (500,380)
            idle "buttons/computer_icon_21.png"
            hover "buttons/computer_icon_21b.png"
            action NullAction()

        imagebutton:
            focus_mask True
            pos (623,380)
            idle "buttons/computer_icon_21.png"
            hover "buttons/computer_icon_21b.png"
            action NullAction()

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("MC_webcam")

screen MC_family:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "buttons/computer_window_01.png" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover "buttons/computer_button_03b.png"
        action Hide("MC_family")

    imagebutton:
        focus_mask True
        pos (290,210)
        idle "buttons/computer_icon_16.png"
        hover "buttons/computer_icon_16b.png"
        action Show("MC_picture", number = 2)

    imagebutton:
        focus_mask True
        pos (390,210)
        idle "buttons/computer_icon_15.png"
        hover "buttons/computer_icon_15b.png"
        action Show("MC_picture", number = 1)

screen MC_picture(number):
    imagebutton idle "backgrounds/menu_ground.png" action Hide("MC_picture")

    if number == 1:
        add "buttons/computer_pic_06.png" pos 220,150

    elif number == 2:
        add "buttons/computer_pic_07.png" pos 220,150

screen camshow_buttons:
    if False:
        imagebutton:
            if shed_xray_toggle:
                idle "buttons/anim_03.png"
                hover "buttons/anim_03b.png"
            else:
                idle "buttons/anim_04.png"
                hover "buttons/anim_04b.png"
            action If(
                xray_toggle,
                SetVariable("xray_toggle", False),
                SetVariable("xray_toggle", True)
            )
            xpos 940
            ypos 600

    imagebutton:
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
        xpos 10
        ypos 600

screen camshow_options:
    if not sister.over(sis_webcam04):
        imagebutton:
            idle "buttons/cam_stage01_01.png"
            hover "buttons/cam_stage01_01b.png"
            action If(
                current_camshow == 1,
                Jump("sis_camshow01_loop"),
                If(
                    current_camshow == 2,
                    Jump("sis_camshow02_loop"),
                    If(
                        current_camshow == 3,
                        Jump("sis_camshow03_loop"),
                        Jump("sis_camshow04_loop")
                    )
                )
            )
            xpos 250
            ypos 700

        imagebutton:
            idle "buttons/cam_stage01_02.png"
            hover "buttons/cam_stage01_02b.png"
            action If(
                current_camshow == 1,
                Jump("sis_camshow01_finish"),
                If(
                    current_camshow == 2,
                    Jump("sis_camshow02_finish"),
                    If(
                        current_camshow == 3,
                        Jump("sis_camshow03_finish"),
                        Jump("sis_camshow04_finish")
                    )
                )
            )
            xpos 450
            ypos 700

    else:
        imagebutton:
            idle "buttons/cam_stage01_01.png"
            hover "buttons/cam_stage01_01b.png"
            action If(
                current_camshow == 1,
                Jump("sis_camshow01_loop"),
                If(
                    current_camshow == 2,
                    Jump("sis_camshow02_loop"),
                    If(
                        current_camshow == 3,
                        Jump("sis_camshow03_loop"),
                        Jump("sis_camshow04_loop")
                    )
                )
            )
            xpos 175
            ypos 700

        imagebutton:
            idle "buttons/cam_stage01_02.png"
            hover "buttons/cam_stage01_02b.png"
            action If(
                current_camshow == 1,
                Jump("sis_camshow01_finish"),
                If(
                    current_camshow == 2,
                    Jump("sis_camshow02_finish"),
                    If(
                        current_camshow == 3,
                        Jump("sis_camshow03_finish"),
                        Jump("sis_camshow04_finish")
                    )
                )
            )
            xpos 375
            ypos 700

        imagebutton:
            idle "buttons/cam_stage01_03.png"
            hover "buttons/cam_stage01_03b.png"
            action If(
                current_camshow == 1,
                Jump("sis_camshow02_loop"),
                If(
                    current_camshow == 2,
                    Jump("sis_camshow03_loop"),
                    If(
                        current_camshow == 3,
                        Jump("sis_camshow04_loop"),
                        Jump("sis_camshow01_loop")
                    )
                )
            )
            xpos 575
            ypos 700