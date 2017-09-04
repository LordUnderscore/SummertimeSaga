screen gym:
    add gTimer.image("backgrounds/location_training{}.jpg")

    if erik.completed(erik_favor_2):
        imagebutton:
            focus_mask True
            pos (136,378)
            idle "objects/object_bench_01c.png"
            hover "objects/object_bench_01d.png"
            action Show("bench01_options")
    else:
        imagebutton:
            focus_mask True
            pos (136,458)
            idle "objects/object_bench_01.png"
            hover "objects/object_bench_01b.png"
            action Show("bench01_options")

    imagebutton:
        pos (32,380)
        focus_mask True
        idle "images/objects/character_cedric_01.png"
        hover "images/objects/character_cedric_01b.png"
        action Hide("gym"), Jump("cedric_dialogue")

    imagebutton:
        focus_mask True
        pos (414,383)
        idle "objects/object_door_10.png"
        hover "objects/object_door_10b.png"
        action Hide("gym"), Jump("yoga_room")

    imagebutton:
        focus_mask True
        pos (498,0)
        idle "objects/object_bag_01.png"
        hover "objects/object_bag_01b.png"
        action Show("bag01_options")

screen bag01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bag01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/training_option_02.png"
        hover "boxes/training_option_02b.png"
        action If(
            gTimer.is_dark() or training_done,
            [Hide("bag01_options"), Hide("gym"), Jump("tired_training_dialogue")],
            [Hide("bag01_options"), Hide("gym"), Jump("training01_payment_dialogue")]
        )

screen bench01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bench01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/training_option_01.png"
        hover "boxes/training_option_01b.png"
        action If(
            gTimer.is_dark(),
            [Hide("bench01_options"), Hide("gym"), Jump("tired_training_dialogue")],
            If(
                erik.completed(erik_favor_2),
                [Hide("bench01_options"), Hide("gym"), Jump("weightlifting_dialogue")],
                [Hide("bench01_options"), Hide("gym"), Jump("cant_solo_lift")]
            )
        )