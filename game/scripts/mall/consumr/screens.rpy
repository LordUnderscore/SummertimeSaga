screen consumr:
    add "backgrounds/location_consumr.jpg"

    imagebutton:
        focus_mask True
        pos (174,281)
        idle "objects/object_shop_01.png"
        hover "objects/object_shop_01b.png"
        action Show("popup_parts")

    imagebutton:
        focus_mask True
        pos (454,584)
        idle "objects/object_shop_03.png"
        hover "objects/object_shop_03b.png"
        action Show("popup_swimsuit")

    imagebutton:
        focus_mask True
        pos (88,261)
        idle "objects/object_shop_02.png"
        hover "objects/object_shop_02b.png"
        action Show("popup_webcam")

    imagebutton:
        focus_mask True
        pos (820,524)
        idle "objects/object_shop_05.png"
        hover "objects/object_shop_05b.png"
        action Show("popup_bike")

    imagebutton:
        focus_mask True
        pos (60,606)
        idle "objects/object_shop_06.png"
        hover "objects/object_shop_06b.png"
        action Show("popup_milkjug")

    imagebutton:
        focus_mask True
        pos (170,620)
        idle "objects/object_shop_07.png"
        hover "objects/object_shop_07b.png"
        action Show("popup_exterminator")

    imagebutton:
        focus_mask True
        pos (230,618)
        idle "objects/object_shop_08.png"
        hover "objects/object_shop_08b.png"
        action Show("popup_eradicator")

    imagebutton:
        focus_mask True
        pos (290,616)
        idle "objects/object_shop_09.png"
        hover "objects/object_shop_09b.png"
        action Show("popup_annihilator")

    imagebutton:
        focus_mask True
        pos (350,608)
        idle "objects/object_shop_10.png"
        hover "objects/object_shop_10b.png"
        action Show("popup_gas_can")

    imagebutton:
        focus_mask True
        pos (536,515)
        idle "objects/object_shop_11.png"
        hover "objects/object_shop_11b.png"
        action Show("popup_wrench")

    imagebutton:
        focus_mask True
        pos (380,388)
        idle "objects/object_shop_12.png"
        hover "objects/object_shop_12b.png"
        action Show("popup_cat_food")

    imagebutton:
        focus_mask True
        pos (700,400)
        idle "objects/character_vero_01.png"
        hover "objects/character_vero_01b.png"
        action Hide("consumr"), Jump("veronica_dialogue_button")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_03.png"
        hover "boxes/auto_option_03b.png"
        action Hide("consumr"), Jump("mall_dialogue")

screen popup_parts:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_parts")

    add "boxes/shop_item_parts01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_200.png"
        hover "buttons/shop_button_200b.png"
        action [Function(inventory.buy_item, parts), If(inventory.money < 200, Show("popup_fail01"), If(parts in inventory.items, Show("popup_fail02"), Show("popup_parts"))), Function(quest_complete, quest05), Hide("popup_parts")]

screen popup_swimsuit:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_swimsuit")

    add "boxes/shop_item_swimsuit01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [Function(inventory.buy_item, swimsuit), If(inventory.money < 100, Show("popup_fail01"), If(swimsuit in inventory.items, Show("popup_fail02"), [Function(quest_complete, quest03), Show("popup_swimsuit")])), Hide("popup_swimsuit")]

screen popup_webcam:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_webcam")

    add "boxes/shop_item_camera01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_300.png"
        hover "buttons/shop_button_300b.png"
        action [Function(inventory.buy_item, supersaga_webcam), If(inventory.money < 300, Show("popup_fail01"), If(supersaga_webcam in inventory.items, Show("popup_fail02"), Show("popup_webcam"))), Hide("popup_webcam")]

screen popup_bike:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_bike")

    add "boxes/shop_item_bike01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_500.png"
        hover "buttons/shop_button_500b.png"
        action [Function(inventory.buy_item, bike), If(inventory.money < 500, Show("popup_fail01"), If(bike in inventory.items, Show("popup_fail02"), Show("popup_bike"))), Hide("popup_bike")]

screen popup_milkjug:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide ("popup_milkjug")

    add "boxes/shop_item_jug01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_300.png"
        hover "buttons/shop_button_300b.png"
        action [Function(inventory.buy_item, milkjug), If(inventory.money < 300, Show("popup_fail01"), If(milkjug in inventory.items, Show("popup_fail02"), Show("popup_milkjug"))), Hide("popup_milkjug")]

screen popup_exterminator:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_exterminator")

    add "boxes/shop_item_spray01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [Function(inventory.buy_item, exterminator), If(inventory.money < 100, Show("popup_fail01"), If(exterminator in inventory.items, Show("popup_fail02"), Show("popup_exterminator"))), Hide("popup_exterminator")]

screen popup_eradicator:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_eradicator")

    add "boxes/shop_item_spray02.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [Function(inventory.buy_item, eradicator), If(inventory.money < 100, Show("popup_fail01"), If(eradicator in inventory.items, Show("popup_fail02"), Show("popup_eradicator"))), Hide("popup_eradicator")]

screen popup_annihilator:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_annihilator")

    add "boxes/shop_item_spray03.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [Function(inventory.buy_item, annihilator), If(inventory.money < 100, Show("popup_fail01"), If(annihilator in inventory.items, Show("popup_fail02"), Show("popup_annihilator"))), Hide("popup_annihilator")]

screen popup_gas_can:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_gas_can")

    add "boxes/shop_item_gas01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [Function(inventory.buy_item, gas_can), If(inventory.money < 100, Show("popup_fail01"), If(gas_can in inventory.items, Show("popup_fail02"), Show("popup_gas_can"))), Hide("popup_gas_can")]

screen popup_wrench:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_wrench")

    add "boxes/shop_item_wrench01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_50.png"
        hover "buttons/shop_button_50b.png"
        action [Function(inventory.buy_item, wrench), If(inventory.money < 50, Show("popup_fail01"), If(wrench in inventory.items, Show("popup_fail02"), Show("popup_wrench"))), Hide("popup_wrench")]

screen popup_cat_food:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_cat_food")

    add "boxes/shop_item_catfood01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [Function(inventory.buy_item, cat_food), If(inventory.money < 100, Show("popup_fail01"), If(cat_food in inventory.items, Show("popup_fail02"), Show("popup_cat_food"))), Hide("popup_cat_food")]

screen popup_fail01:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_fail01")

    add "boxes/popup_shopping_fail01.png"

screen popup_fail02:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_fail02")

    add "boxes/popup_shopping_fail02.png"