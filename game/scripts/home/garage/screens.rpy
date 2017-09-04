screen garage:
    add gTimer.image("backgrounds/location_home_garage{}.jpg")

    imagebutton:
        focus_mask True
        pos (380,356)
        idle gTimer.image("objects/object_car_01{}.png")
        hover gTimer.image("objects/object_car_01b{}.png")
        action Hide("garage"), Jump("car_dialogue")

    imagebutton:
        focus_mask True
        pos (43,486)
        idle gTimer.image("objects/object_mower_01{}.png")
        hover gTimer.image("objects/object_mower_01b{}.png")
        action Hide("garage"), Jump("lawnmower_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover "boxes/auto_option_08b.png"
        action Hide("garage"), Jump("home_front")

    if not shovel_taken:
        imagebutton:
            focus_mask True
            pos (30,250)
            idle gTimer.image("objects/object_shovel_01{}.png")
            hover gTimer.image("objects/object_shovel_01b{}.png")
            action Function(inventory.get_item, item= shovel), SetVariable("shovel_taken", True), Hide("garage"), Jump("shovel")

    if not stool_taken:
        imagebutton:
            focus_mask True
            pos (257,250)
            idle gTimer.image("objects/object_stool_01{}.png")
            hover gTimer.image("objects/object_stool_01b{}.png")
            action Function(inventory.get_item, item= stool), SetVariable("stool_taken", True), Hide("garage"), Jump("stool")

screen car_engine:
    add gTimer.image("backgrounds/location_home_garage_car{}.jpg")

    imagebutton:
        focus_mask True
        pos (110,97)
        idle gTimer.image("objects/object_engine_01{}.png")
        hover gTimer.image("objects/object_engine_01b{}.png")
        action Hide("car_engine"), Jump("engine_broken_dialogue")