screen pier:
    add gTimer.image("backgrounds/location_pier{}.jpg")

    imagebutton:
        focus_mask True
        pos (602,364)
        if not gTimer.is_dark():
            idle "objects/character_terry_01.png"
            hover "objects/character_terry_01b.png"
        else:
            idle "objects/character_terry_02.png"
            hover "objects/character_terry_02b.png"
        action Hide("pier"), Jump("terry_button_dialogue")

    imagebutton:
        focus_mask True
        pos (184,449)
        idle gTimer.image("objects/object_chair_01{}.png")
        hover gTimer.image("objects/object_chair_01b{}.png")
        action [Hide("pier"),
                If(
                    gTimer.is_dark(),
                    Jump("fishing_night"),
                    If(
                        fishing_rod in inventory.items,
                        Jump("before_fishing"),
                        Jump("no_fish_rod")
                    )
                )
        ]

    imagebutton:
        focus_mask True
        pos (548,469)
        idle gTimer.image("objects/object_board_02{}.png")
        hover gTimer.image("objects/object_board_02b{}.png")
        action Hide("pier"), Jump("pier_board")