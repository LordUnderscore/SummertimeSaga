screen treehouse:
    add gTimer.image("backgrounds/location_treehouse{}.jpg")

    imagebutton:
        focus_mask True
        pos (309,71)
        idle gTimer.image("objects/object_treehouse_01{}.png")
        hover gTimer.image("objects/object_treehouse_01b{}.png")
        action Hide("treehouse"), Jump("treehouse_closeup_dialogue")

screen treehouse_closeup:
    add gTimer.image("backgrounds/location_treehouse_closeup{}.jpg")

    imagebutton:
        focus_mask True
        pos (502,39)
        idle gTimer.image("objects/object_door_83{}.png")
        hover gTimer.image("objects/object_door_83b{}.png")
        action Hide("treehouse_closeup"), Jump("treehouse_interior_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("treehouse_closeup"), Jump("treehouse_dialogue")

screen treehouse_interior:
    add gTimer.image("backgrounds/location_treehouse_inside{}.jpg")

    imagebutton:
        focus_mask True
        pos (467,661)
        idle gTimer.image("objects/object_door_84{}.png")
        hover gTimer.image("objects/object_door_84b{}.png")
        action Hide("treehouse_interior"), Jump("treehouse_closeup_dialogue")

    imagebutton:
        focus_mask True
        pos (20,676)
        idle gTimer.image("objects/object_box_03{}.png")
        hover gTimer.image("objects/object_box_03b{}.png")
        action Hide("treehouse_interior"), Hide("ui"), Show("treehouse_box")

screen treehouse_box:
    add "backgrounds/location_treehouse_box.jpg"

    if lure01 not in inventory.items:
        imagebutton:
            focus_mask True
            pos (450,390)
            idle "objects/object_lure_01.png"
            hover "objects/object_lure_01b.png"
            action Hide("treehouse_box"), Jump("lure_02")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("treehouse_box"), Jump("treehouse_interior_dialogue")