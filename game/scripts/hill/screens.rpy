screen hill:
    add gTimer.image("backgrounds/location_hill{}.jpg")

    if M_mia.get_state() == S_mia_find_harold:
        imagebutton:
            focus_mask True
            pos (389,398)
            idle "objects/character_harold_02.png"
            hover "objects/character_harold_02b.png"
            action Hide("hill"), Jump("harolds_car_dialogue")

    imagebutton:
        focus_mask True
        pos (18,497)
        if not gTimer.is_dark():
            idle "private/objects/object_treehole_01.png"
            hover "private/objects/object_treehole_01b.png"
        else:
            idle "private/objects/object_treehole_01_night.png"
            hover "private/objects/object_treehole_01b_night.png"
        action Hide("hill"), Jump("hill_tree")

screen hill_tree:
    imagebutton:
        focus_mask True
        align (0.45,0.65)
        if not gTimer.is_dark():
            idle "private/objects/object_scroll_01.png"
            hover "private/objects/object_scroll_01b.png"
        else:
            idle "private/objects/object_scroll_01_night.png"
            hover "private/objects/object_scroll_01b_night.png"
        action Return()