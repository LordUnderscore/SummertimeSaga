init python:
    class PizzaHouse:
        def __init__(self, img = "", ydiff = 0):
            self.img = img
            self.ydiff = ydiff

    def pizza_movement(multiplier):
        global pizza_bg_sky_xpos
        global pizza_bg_road_xpos
        global pizza_bg_forest_xpos
        global pizza_bg_houses_xpos
        global pizza_slice01_xpos
        global pizza_slice02_xpos
        global pizza_slice03_xpos
        
        pizza_bg_sky_xpos -= 0 + (1 * multiplier)
        pizza_bg_road_xpos -= 3 + (1 * multiplier)
        pizza_bg_forest_xpos -= 1 + (1 * multiplier)
        pizza_bg_houses_xpos -= 3 + (1 * multiplier)
        pizza_slice01_xpos -= 3 + (1 * multiplier)
        pizza_slice02_xpos -= 3 + (1 * multiplier)
        pizza_slice03_xpos -= 3 + (1 * multiplier)

    pizza_house_01 = PizzaHouse(img = "buttons/pizza_house_01.png", ydiff = 107)
    pizza_house_02 = PizzaHouse(img = "buttons/pizza_house_02.png", ydiff = 107)
    pizza_house_03 = PizzaHouse(img = "buttons/pizza_house_03.png", ydiff = 33)
    pizza_house_04 = PizzaHouse(img = "buttons/pizza_house_04.png", ydiff = 33)
    pizza_house_05 = PizzaHouse(img = "buttons/pizza_house_05.png", ydiff = 0)
    pizza_house_06 = PizzaHouse(img = "buttons/pizza_house_06.png", ydiff = 0)
    pizza_houses = [pizza_house_01, pizza_house_02, pizza_house_03, pizza_house_04, pizza_house_05, pizza_house_06]
    pizza_positions = [1200, 1800, 2400, 3000, 3600, 4200]

image pizza_minigame_bg_sky:
    HBox(Image("backgrounds/minigame_scroll_03.png", xoffset = -1),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -2),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -3),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -4),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -5),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -6),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -7),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -8),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -9),
        Image("backgrounds/minigame_scroll_03.png", xoffset = -10))

image pizza_minigame_bg_road:
    HBox(Image("backgrounds/minigame_scroll_01.png", xoffset = -1),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -2),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -3),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -4),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -5),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -6),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -7),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -8),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -9),
        Image("backgrounds/minigame_scroll_01.png", xoffset = -10))

image pizza_minigame_bg_forest:
    HBox(Image("backgrounds/minigame_scroll_02.png", xoffset = -1),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -2),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -3),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -4),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -5),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -6),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -7),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -8),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -9),
        Image("backgrounds/minigame_scroll_02.png", xoffset = -10))

image pizza_minigame_bg_houses:
    HBox(Image(pizza_houses[0].img, xoffset = 1200, yoffset = pizza_houses[0].ydiff),
        Image(pizza_houses[1].img, xoffset = 1800, yoffset = pizza_houses[1].ydiff),
        Image(pizza_houses[2].img, xoffset = 2400, yoffset = pizza_houses[2].ydiff),
        Image(pizza_houses[3].img, xoffset = 3000, yoffset = pizza_houses[3].ydiff),
        Image(pizza_houses[4].img, xoffset = 3600, yoffset = pizza_houses[4].ydiff),
        Image(pizza_houses[5].img, xoffset = 4200, yoffset = pizza_houses[5].ydiff))

screen pizza_minigame:
    add "pizza_minigame_bg_sky" anchor (0,0) pos (pizza_bg_sky_xpos,0)
    add "pizza_minigame_bg_road" anchor (0,0) pos (pizza_bg_road_xpos,531)
    add "pizza_minigame_bg_forest" anchor (0,0) pos (pizza_bg_forest_xpos,369)
    add "pizza_minigame_bg_houses" anchor (0,0) pos (pizza_bg_houses_xpos,140)

    add "buttons/pizza_transport_01.png" anchor (0,0) pos (100,480)

    add "buttons/pizza_01_slice.png" anchor (0,0) pos (pizza_slice01_xpos,0)
    add "buttons/pizza_02_slice.png" anchor (0,0) pos (pizza_slice02_xpos,0)
    add "buttons/pizza_03_slice.png" anchor (0,0) pos (pizza_slice03_xpos,0)

    add "buttons/pizza_instructions.png" anchor (0,0) pos (0,0)

    add "buttons/pizza_01.png" anchor (0,0) pos (650,635)
    if pizza01_delivered == 1:
        add "buttons/pizza_good.png" anchor (0,0) pos (677,661)
    elif pizza01_delivered == 2:
        add "buttons/pizza_bad.png" anchor (0,0) pos (677,662)

    add "buttons/pizza_02.png" anchor (0,0) pos (775,635)
    if pizza02_delivered == 1:
        add "buttons/pizza_good.png" anchor (0,0) pos (802,661)
    elif pizza02_delivered == 2:
        add "buttons/pizza_bad.png" anchor (0,0) pos (802,662)

    add "buttons/pizza_03.png" anchor (0,0) pos (900,635)
    if pizza03_delivered == 1:
        add "buttons/pizza_good.png" anchor (0,0) pos (927,661)
    elif pizza03_delivered == 2:
        add "buttons/pizza_bad.png" anchor (0,0) pos (927,662)

    timer 0.01 repeat True action If(time_count > 0, true=[SetVariable("time_count", time_count - 0.01), If(pizza01_delivered == 0 and pizza_slice01_xpos < 0, SetVariable("pizza01_delivered", 2)), If(pizza02_delivered == 0 and pizza_slice02_xpos < 0, SetVariable("pizza02_delivered", 2)), If(pizza03_delivered == 0 and pizza_slice03_xpos < 0, SetVariable("pizza03_delivered", 2)), If(pizza01_delivered != 0 and pizza02_delivered != 0 and pizza03_delivered != 0, [Hide("pizza_minigame_buttons"), Hide("pizza_minigame"), Jump("pizza_delivered")], If(pizza_slice01_xpos > -200 or pizza_slice02_xpos > -200 or pizza_slice03_xpos > -200, [Function(pizza_movement, vehicle_movement)], [Hide("pizza_minigame_buttons"), Hide("pizza_minigame"), Jump("pizza_delivered")]))], false=NullAction())


screen pizza_minigame_buttons:
    if pizza01_delivered == 0 and pizza_slice01_xpos > 0:
        imagebutton idle "buttons/pizza_01.png" hover "buttons/pizza_01b.png" action [If(pizza_slice01_xpos < 277 and pizza_slice01_xpos > 150, SetVariable("pizza01_delivered", 1), SetVariable("pizza01_delivered", 2))] anchor (0,0) pos (650,635) focus_mask True

    if pizza02_delivered == 0 and pizza_slice02_xpos > 0:
        imagebutton idle "buttons/pizza_02.png" hover "buttons/pizza_02b.png" action [If(pizza_slice02_xpos < 277 and pizza_slice02_xpos > 150, SetVariable("pizza02_delivered", 1), SetVariable("pizza02_delivered", 2))] xpos 775 ypos 635 focus_mask True

    if pizza03_delivered == 0 and pizza_slice03_xpos > 0:
        imagebutton idle "buttons/pizza_03.png" hover "buttons/pizza_03b.png" action [If(pizza_slice03_xpos < 277 and pizza_slice03_xpos > 150, SetVariable("pizza03_delivered", 1), SetVariable("pizza03_delivered", 2))] xpos 900 ypos 635 focus_mask True