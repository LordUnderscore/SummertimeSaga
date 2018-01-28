screen kitchen:
    if M_mom.is_set("revealing") or (M_mom.is_set("sleep together") and not M_mom.is_set("revealing")):
        $ mom_idle = "objects/character_mom_02.png"
        $ mom_hover = "objects/character_mom_02b.png"
        $ mom_x = 420
        $ mom_y = 276

    else:
        $ mom_idle = "objects/character_mom_01.png"
        $ mom_hover = "objects/character_mom_01b.png"
        $ mom_x = 682
        $ mom_y = 197

    add gTimer.image("backgrounds/location_home_kitchen{}.jpg")

    imagebutton:
        focus_mask True
        pos (41,97)
        idle gTimer.image("objects/object_door_20{}.png")
        hover gTimer.image("objects/object_door_20b{}.png")
        action Hide("kitchen"), If(
                                   M_mom.is_set("fetch lotion"),
                                   Jump("mom_lotion_block"),
                                   Jump("dining_room_dialogue")
        )

    if is_here("mom"):
        if M_mom.get_state() == S_mom_dishes_help and M_mom.is_set('chores'):
            imagebutton:
                focus_mask True
                pos (722,196)
                idle "images/objects/character_mom_05.png"
                hover "images/objects/character_mom_05b.png"
                action Hide("kitchen"), If(
                                           sister.started(sis_breakfast),
                                           Jump("sis_breakfast_force_mom"),
                                           Jump("dishes_dialogue")
                )

        else:
            imagebutton:
                focus_mask True
                pos (mom_x, mom_y)
                idle mom_idle
                hover mom_hover
                action Hide("kitchen"), If(
                                           sister.started(sis_breakfast),
                                           Jump("sis_breakfast_force_mom"),
                                           Jump("mom_button_dialogue")
                )

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_01.png"
        hover "boxes/auto_option_01b.png"
        action If(
            sister.started(sis_breakfast),
            [Hide("kitchen"), Jump("sis_breakfast_force")],
            [Hide("kitchen"), Jump("home_entrance")]
        )

screen mom_name_input:
    add "boxes/popup_name_mom.png" pos 250,250
    add Input (size=24, color="#5d9aff", default="", changed=mother_name, length=12, xpos= 347, ypos = 347)
    key "K_RETURN" action Return
    imagebutton idle "buttons/menu_skip_01.png" hover "buttons/menu_skip_01b.png" action Return pos 362,447

screen mom_kitchen_fuck_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Hide("mom_kitchen_fuck_options"), Jump("mom_kitchen_fuck_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Hide("mom_kitchen_fuck_options"), Jump("mom_kitchen_fuck_cum")

    if M_mom.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover "buttons/speed_02b.png"
            action Hide("mom_kitchen_fuck_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("mom_kitchen_fuck_loop")

    if M_mom.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover "buttons/speed_01b.png"
            action Hide("mom_kitchen_fuck_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.05), Jump("mom_kitchen_fuck_loop")