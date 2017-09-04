screen dianes_shed:
    add gTimer.image("backgrounds/location_shed01{}.jpg")

    if aunt_had_sex and gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (670,280)
            idle "objects/character_diane_04.png"
            hover "objects/character_diane_04b.png"
            action Hide("dianes_shed"), Jump("aunt_dialogue_button_night")

    if milk_carton not in inventory.items and quest09 in quest_list and quest09 not in completed_quests and not quest09_3:
        imagebutton:
            focus_mask True
            pos (650,500)
            idle "objects/object_milk_01.png"
            hover "objects/object_milk_01b.png"
            action Function(inventory.get_item, item = milk_carton), Show("milk_popup", transition = dissolve), SetVariable("ui_lock_count", 0)

    if pump not in inventory.items and quest08 not in completed_quests:
        imagebutton:
            focus_mask True
            pos (80,308)
            idle "objects/item_pump1.png"
            hover "objects/item_pump1b.png"
            action SetVariable("pump_quest_active", False), Function(inventory.get_item, item = pump), Show("pump_popup", transition = dissolve)

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_07.png"
        hover "boxes/auto_option_07b.png"
        action Hide("dianes_shed"), SetVariable("in_garden", True), Jump("garden_dialogue")

screen pump_popup:
    imagebutton:
        idle "boxes/popup_item_pump.png"
        action Hide("pump_popup")

screen milk_popup:
    imagebutton:
        idle "boxes/popup_item_milk.png"
        action Hide("milk_popup")

screen shed_sex_options:
    if shed_sex_action == 0:
        imagebutton:
            pos (175,700)
            idle "buttons/diane_stage01_06.png"
            hover "buttons/diane_stage01_06b.png"
            action SetVariable("shed_sex_action", 1), Jump("shed_ride")

        imagebutton:
            pos (375,700)
            idle "buttons/judith_stage02_01.png"
            hover "buttons/judith_stage02_01b.png"
            action Jump("shed_sex_loop")

        imagebutton:
            pos (575,700)
            idle "buttons/diane_stage01_02.png"
            hover "buttons/diane_stage01_02b.png"
            action Jump("shed_sex_cum_in")

    else:
        if shed_sex_action == 1:
            imagebutton:
                pos (250,700)
                idle "buttons/judith_stage02_01.png"
                hover "buttons/judith_stage02_01b.png"
                action Jump("shed_ride_loop")

            imagebutton:
                pos (450,700)
                idle "buttons/diane_stage01_07.png"
                hover "buttons/diane_stage01_07b.png"
                action SetVariable("shed_sex_action", 2), Jump("shed_fuck")

        elif shed_sex_action == 2:
            imagebutton:
                pos (250,700)
                idle "buttons/judith_stage02_01.png"
                hover "buttons/judith_stage02_01b.png"
                action Jump("shed_fuck_loop")

            imagebutton:
                pos (450,700)
                idle "buttons/diane_stage01_08.png"
                hover "buttons/diane_stage01_08b.png"
                action SetVariable("shed_sex_action", 3), Jump("shed_milk")

        elif shed_sex_action == 3:
            imagebutton:
                pos (250,700)
                idle "buttons/judith_stage02_01.png"
                hover "buttons/judith_stage02_01b.png"
                action Jump("shed_milk")

            imagebutton:
                pos (450,700)
                idle "buttons/diane_stage01_09.png"
                hover "buttons/diane_stage01_09b.png"
                action SetVariable("shed_sex_action", 0), SetVariable("shed_sex_angle", 0), Jump("shed_sex_loop")

screen shed_sex_visuals:
    if shed_cow_outfit == True:
        if shed_sex_angle == 0:
            if cow_outfit == 0:
                add "characters/aunt/char_aunt_sex_39.png" pos 299,106

            else:
                add "characters/aunt/char_aunt_sex_41.png" pos 300,105

        else:
            if cow_outfit == 0:
                add "characters/aunt/char_aunt_sex_51.png" pos 193,0

            else:
                add "characters/aunt/char_aunt_sex_53.png" pos 210,0

    if shed_xray_toggle == True:
        if xray == 0:
            if shed_sex_angle == 0:
                add "characters/player/char_player_sex_42.png" pos 530,320

            else:
                add "characters/player/char_player_sex_46.png" pos 350,270

        else:
            if shed_sex_angle == 0:
                add "characters/player/char_player_sex_43.png" pos 521,295
                if shed_cum == True:
                    add "characters/player/char_player_sex_44.png" pos 558,383

            else:
                add "characters/player/char_player_sex_47.png" pos 385,290
                if shed_cum == True:
                    add "characters/player/char_player_sex_48.png" pos 443,320

screen shed_sex_buttons:
    if shed_sex_action == 0:
        imagebutton:
            pos (250,700)
            idle "buttons/diane_stage01_05.png"
            hover "buttons/diane_stage01_05b.png"
            action If(shed_cow_outfit, SetVariable("shed_cow_outfit", False), SetVariable("shed_cow_outfit", True))

        imagebutton:
            pos (450,700)
            idle "buttons/diane_stage01_04.png"
            hover "buttons/diane_stage01_04b.png"
            action If(shed_sex_angle == 0, SetVariable("shed_sex_angle", 1), SetVariable("shed_sex_angle", 0)), Return

        imagebutton:
            pos (940,600)
            if shed_xray_toggle:
                idle "buttons/anim_03.png"
                hover "buttons/anim_03b.png"
            else:
                idle "buttons/anim_04.png"
                hover "buttons/anim_04b.png"
            action If(shed_xray_toggle, SetVariable("shed_xray_toggle", False), SetVariable("shed_xray_toggle", True))

    imagebutton:
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover "buttons/anim_02b.png"
        else:
            idle "buttons/anim_01.png"
            hover "buttons/anim_01b.png"
        action If(anim_toggle, SetVariable("anim_toggle", False), SetVariable("anim_toggle", True)), Return