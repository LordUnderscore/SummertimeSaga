screen kitchen:
    if mom_revealing:
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
        action Hide("kitchen"), Jump("dining_room_dialogue")

    if not gTimer.is_dark():
        if is_here("mom"):
            if sister.started(sis_breakfast):
                imagebutton:
                    focus_mask True
                    pos (mom_x,mom_y)
                    idle mom_idle
                    hover mom_hover
                    action Hide("kitchen"), Jump("sis_breakfast_force_mom")

            elif mom_count == 4 and mom_vacuuming and mom_helped == 1:
                imagebutton:
                    focus_mask True
                    pos (722,196)
                    idle "images/objects/character_mom_05.png"
                    hover "images/objects/character_mom_05b.png"
                    action Hide("kitchen"), Jump("dishes_dialogue")

            elif mom_count != 6:
                imagebutton:
                    focus_mask True
                    pos (mom_x, mom_y)
                    idle mom_idle
                    hover mom_hover
                    action Hide("kitchen"), Jump("mom_button_dialogue")

            else:
                $ raise Exception("imagebutton needed!")

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