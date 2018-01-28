screen park_bushes:
    add gTimer.image("backgrounds/location_park_bushes{}.jpg")

    if not M_mia.is_set('stolen goods recovered'):
        imagebutton:
            focus_mask True
            pos (32,508)
            idle gTimer.image("objects/object_bag_02{}.png")
            hover gTimer.image("objects/object_bag_02b{}.png")
            action Hide("park_bushes"), Jump("park_bushes_bag_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("park_bushes"), Jump("park_dialogue")

screen park_bushes_bag:
    add "backgrounds/location_park_bag.jpg"

    if treasure_key not in inventory.items:
        imagebutton:
            focus_mask True
            pos (540,280)
            idle "objects/object_key_02.png"
            hover "objects/object_key_02b.png"
            action Function(inventory.get_item, item = treasure_key), Show("popup", Image = "boxes/popup_item_key1.png")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("park_bushes_bag"), If(treasure_key in inventory.items, [Function(inventory.get_item, item = stolen_goods), Show("popup", Image = "boxes/popup_item_goods.png"), Function(M_mia.trigger, T_harold_found_goods)], NullAction()), Jump("park_bushes_dialogue")