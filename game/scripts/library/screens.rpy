screen library:
    add "backgrounds/location_library.jpg"

    imagebutton:
        focus_mask True
        pos (513,354)
        idle "objects/object_shelf_03.png"
        hover "objects/object_shelf_03b.png"
        action Hide("library"), Show("library_bookshelf")

    imagebutton:
        focus_mask True
        pos (104,378)
        idle "objects/object_desk_05.png"
        hover "objects/object_desk_05b.png"
        action Show("desk05_options")

    imagebutton:
        focus_mask True
        pos (636,349)
        idle "objects/object_door_29.png"
        hover "objects/object_door_29b.png"
        action If(
            backroom_blocked_count == 0,
            [Hide("library"), Jump("backroom_blocked_dialogue")],
            [Hide("library"), Jump("backroom_dialogue")]
        )

    imagebutton:
        focus_mask True
        pos (803,324)
        idle "objects/object_door_55.png"
        hover "objects/object_door_55b.png"
        action If(
            backroom_blocked_count == 0,
            [Hide("library"), Jump("backroom_blocked_dialogue")],
            [Hide("library"), Jump("meeting_room_dialogue")]
        )

screen library_bookshelf:
    add "backgrounds/location_library_shelf.jpg"

    if quest06 in completed_quests and textbook1 not in inventory.items:
        imagebutton:
            focus_mask True
            pos (742,416)
            idle "buttons/book_01.png"
            hover "buttons/book_01b.png"
            action Function(inventory.get_item, item = textbook1)

    if aunt.completed(aunt_breeding_guide) and breeding_guide not in inventory.items and not aunt.known(aunt_breeding_bull):
        imagebutton:
            focus_mask True
            pos (234,110)
            idle "buttons/book_02.png"
            hover "buttons/book_02b.png"
            action Hide("library_bookshelf"), Jump("breeding_guide")

    if mrsj.started(mrsj_sex_ed) and kamasutra not in inventory.items:
        imagebutton:
            focus_mask True
            pos (406,440)
            idle "buttons/book_03.png"
            hover "buttons/book_03b.png"
            action Hide("library_bookshelf"), Jump("kamasutra")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_04.png"
        hover "boxes/auto_option_04b.png"
        action Hide("library_bookshelf"), Jump("library_dialogue")

screen desk05_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("desk05_options")]

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk05_option_01.png"
        hover "boxes/desk05_option_01b.png"
        action Hide("desk05_options"), Hide("library"), Jump("library_desk_dialogue")