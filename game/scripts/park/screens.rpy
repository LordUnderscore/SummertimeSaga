screen park:
    add gTimer.image("backgrounds/location_park{}.jpg")

    if is_here("anna"):
        imagebutton:
            focus_mask True
            pos (710,400)
            idle "objects/character_anna_01.png"
            hover "objects/character_anna_01b.png"
            action Hide("park"), Jump("anna_button_dialogue")

    if gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (724,407)
            idle "objects/object_bench_03_night.png"
            hover "objects/object_bench_03b_night.png"
            action Show("bench03_options")

    if erik.known(erik_father_treasure) or M_mia.get_state() == S_mia_stolen_goods:
        imagebutton:
            focus_mask True
            pos (261,291)
            idle gTimer.image("objects/object_tree_01{}.png")
            hover gTimer.image("objects/object_tree_01b{}.png")
            action Hide("park"), Jump("park_bushes_dialogue")

    imagebutton:
        focus_mask True
        pos (104,464)
        idle gTimer.image("objects/object_bench_02{}.png")
        hover gTimer.image("objects/object_bench_02b{}.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (318,377)
        idle gTimer.image("objects/object_fountain_01{}.png")
        hover gTimer.image("objects/object_fountain_01b{}.png")
        action Hide("park"), Jump("fountain_dialogue")

screen bench03_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bench03_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/bench03_option_01.png"
        hover "boxes/bench03_option_01b.png"
        action If(
            not gTimer.is_evening(),
            [Hide("park"), Hide("bench03_options"), Jump("park_night_closed")],
            [Hide("park"), Hide("bench03_options"), Jump("park_dialogue01")]
        )

screen park_fountain:
    if weird_coin not in inventory.items:
        imagebutton:
            focus_mask True
            align (0.44,0.81)
            if not gTimer.is_dark():
                idle "private/objects/object_coin_01.png"
                hover "private/objects/object_coin_01b.png"
            else:
                idle LiveComposite((35,37), (0,0), "private/objects/object_coin_01_night.png", (10,-10), PulseImage(LiveCrop((0,0,30,30), "map/map_sparkle01_alpha.png"), "map/map_sparkle03.png", delay1 = 5, delay2 = 0.2))
                hover "private/objects/object_coin_01b_night.png"
            action Hide("park_fountain"), Jump("coin_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("park_fountain"), Jump("park_dialogue")