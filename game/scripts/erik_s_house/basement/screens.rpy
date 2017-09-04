screen eriks_basement tag eriks_house:
    add "backgrounds/location_erik_basement01.jpg"

    imagebutton:
        focus_mask True
        pos (37,475)
        idle "objects/object_cabinet_01.png"
        hover "objects/object_cabinet_01b.png"
        action Show("cabinet01_options")

    if is_here("erik") and is_here("mrsj"):
        imagebutton:
            focus_mask True
            pos (393,353)
            idle "objects/object_poker_02.png"
            hover "objects/object_poker_02b.png"
            action Hide("eriks_basement"), Jump("mrsj_poker")

    else:
        imagebutton:
            focus_mask True
            pos (394,505)
            idle "objects/object_poker_01.png"
            hover "objects/object_poker_01b.png"
            action Show("poker01_options")

    imagebutton:
        focus_mask True
        pos (137,308)
        idle "objects/object_stairs_01.png"
        hover "objects/object_stairs_01b.png"
        action If(
            mrsj_afterpoker_fun,
            [Hide("eriks_basement"), Jump("mrsj_afterpoker_fun_block")],
            [Hide("eriks_basement"), Jump("erik_indoors")]
        )

    imagebutton:
        focus_mask True
        pos (879,310)
        idle "objects/object_door_81.png"
        hover "objects/object_door_81b.png"
        action Hide("eriks_basement"), Jump("erik_basement_backroom_dialogue")

    if is_here("erik") and not is_here("mrsj") and not erik_drunk:
        imagebutton:
            focus_mask True
            pos (855,410)
            idle "objects/character_erik_01.png"
            hover "objects/character_erik_01b.png"
            action Hide("eriks_basement"), Jump("erik_button_dialogue")

screen cabinet01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("cabinet01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/cabinet01_option_01.png"
        hover "boxes/cabinet01_option_01b.png"
        action Hide("cabinet01_options"), Hide("eriks_basement"), Jump("cabinet")

screen poker01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("poker01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/poker01_option01.png"
        hover "boxes/poker01_option01b.png"
        action Hide("poker01_options"), Hide("eriks_basement"), Jump("poker_table")

screen eriks_basement_backroom:
    add "backgrounds/location_erik_basement_back.jpg"

    imagebutton:
        focus_mask True
        pos (733,231)
        idle "objects/object_door_82.png"
        hover "objects/object_door_82b.png"
        action Hide("eriks_basement_backroom"), Jump("erik_basement")

    if is_here("erik") and is_here("mrsj"):
        imagebutton:
            focus_mask True
            pos (0,315)
            idle "images/objects/character_erikmom_02.png"
            hover "images/objects/character_erikmom_02b.png"
            action Hide("eriks_basement_backroom"), Jump("mrsj_afterpoker_fun")

    else:
        imagebutton:
            focus_mask True
            pos (0,385)
            idle "objects/object_couch_01.png"
            hover "objects/object_couch_01b.png"
            action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (888,539)
        idle "objects/object_aquarium_01.png"
        hover "objects/object_aquarium_01b.png"
        action Hide("eriks_basement_backroom"), Hide("ui"), Show("backroom_aquarium")

screen backroom_aquarium:
    add "backgrounds/location_erik_basement_aquarium.jpg"

    if erik.started(erik_card_hunt) and eriks_cards not in inventory.items:
        imagebutton:
            focus_mask True
            pos (350,450)
            idle "objects/object_box_02.png"
            hover "objects/object_box_02b.png"
            action Hide("backroom_aquarium"), Jump("backroom_aquarium")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("backroom_aquarium"), Show("eriks_basement_backroom"), Show("ui")