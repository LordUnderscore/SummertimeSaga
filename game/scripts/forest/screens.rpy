screen forest:
    add gTimer.image("backgrounds/location_forest{}.jpg")

    if not gTimer.is_dark():
        if Anna.started(anna_missing_pup):
            if awesomo_lured == True and dog not in inventory.items:
                imagebutton:
                    focus_mask True
                    pos (576,630)
                    idle "images/objects/character_awesomo_02.png"
                    hover "images/objects/character_awesomo_02b.png"
                    action Hide("forest"), Jump("awesomo_dialogue_button")

        if dirt_pile_done == False:
            imagebutton:
                focus_mask True
                pos (184,708)
                idle "images/objects/object_dirt_01.png"
                hover "images/objects/object_dirt_01b.png"
                action Hide("forest"), Jump("dirt_pile")

    imagebutton:
        focus_mask True
        pos (314,594)
        idle gTimer.image("objects/object_rocks_01{}.png")
        hover gTimer.image("objects/object_rocks_01b{}.png")
        action Show("popup_unfinished")

screen forest_worms:
    add "backgrounds/location_forest_dirt3.jpg"

    imagebutton:
        focus_mask True
        pos (313,269)
        idle "objects/object_worms_01.png"
        hover "objects/object_worms_01b.png"
        action Function(inventory.get_item, item = worm), Hide("forest_worms"), Jump("worm_popup")