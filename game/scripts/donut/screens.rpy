screen donut_shop:
    add gTimer.image("backgrounds/location_donut{}.jpg")

    imagebutton:
        focus_mask True
        pos (591,443)
        idle gTimer.image("objects/object_door_91{}.png")
        hover gTimer.image("objects/object_door_91b{}.png")
        action Hide("donut_shop"), If(gTimer.is_dark(), Jump("donut_locked"), [Function(playSound), Jump("donut_interior_dialogue")])

screen donut_shop_interior:
    add "backgrounds/location_donut_inside.jpg"

    imagebutton:
        focus_mask True
        pos (660,325)
        idle "objects/character_beth_01.png"
        hover "objects/character_beth_01b.png"
        action Hide("donut_shop_interior"), Jump("beth_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("donut_shop_interior"), Jump("donut_shop_dialogue")

screen donut_minigame:
    add "backgrounds/location_donut_minigame.jpg"

    default topping_name = ""
    default topping_xpos = 0
    default glaze_name = ""
    default glaze_xpos = 0

    imagebutton:
        focus_mask True
        pos (65,151)
        idle "buttons/donut_01.png"
        hover "buttons/donut_01b.png"
        action SetScreenVariable("topping_name", "chocolate chips"), SetScreenVariable("topping_xpos", 59)

    imagebutton:
        focus_mask True
        pos (295,151)
        idle "buttons/donut_02.png"
        hover "buttons/donut_02b.png"
        action SetScreenVariable("topping_name", "sprinkles"), SetScreenVariable("topping_xpos", 289)

    imagebutton:
        focus_mask True
        pos (524,151)
        idle "buttons/donut_03.png"
        hover "buttons/donut_03b.png"
        action SetScreenVariable("topping_name", "vanilla drizzle"), SetScreenVariable("topping_xpos", 518)

    imagebutton:
        focus_mask True
        pos (755,151)
        idle "buttons/donut_04.png"
        hover "buttons/donut_04b.png"
        action SetScreenVariable("topping_name", "maple drizzle"), SetScreenVariable("topping_xpos", 749)

    if topping_name != "":
        imagebutton:
            focus_mask True
            pos (topping_xpos,145)
            idle "buttons/donut_selection.png"

    imagebutton:
        focus_mask True
        pos (65,430)
        idle "buttons/donut_05.png"
        hover "buttons/donut_05b.png"
        action SetScreenVariable("glaze_name", "strawberry glazed"), SetScreenVariable("glaze_xpos", 59)

    imagebutton:
        focus_mask True
        pos (295,430)
        idle "buttons/donut_06.png"
        hover "buttons/donut_06b.png"
        action SetScreenVariable("glaze_name", "chocolate glazed"), SetScreenVariable("glaze_xpos", 289)

    imagebutton:
        focus_mask True
        pos (524,430)
        idle "buttons/donut_07.png"
        hover "buttons/donut_07b.png"
        action SetScreenVariable("glaze_name", "blueberry glazed"), SetScreenVariable("glaze_xpos", 518)

    imagebutton:
        focus_mask True
        pos (755,430)
        idle "buttons/donut_08.png"
        hover "buttons/donut_08b.png"
        action SetScreenVariable("glaze_name", "vanilla glazed"), SetScreenVariable("glaze_xpos", 749)

    if glaze_name != "":
        imagebutton:
            focus_mask True
            pos (glaze_xpos,424)
            idle "buttons/donut_selection.png"

    if topping_name != "" and glaze_name != "":
        imagebutton:
            focus_mask True
            pos (409,676)
            idle "buttons/shop_button_50.png"
            hover "buttons/shop_button_50b.png"
            action Hide("donut_minigame"), If(topping_name == harold_topping and glaze_name == harold_glaze, Function(inventory.buy_item, item = donuts_correct), Function(inventory.buy_item, item = donuts_fail)), Jump("donut_buy_dialogue")