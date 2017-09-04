screen pizzeria_exterior:
    add gTimer.image("backgrounds/location_pizza_outside{}.jpg")

    imagebutton:
        focus_mask True
        pos (353,465)
        idle gTimer.image("objects/object_door_37{}.png")
        hover gTimer.image("objects/object_door_37b{}.png")
        if not gTimer.is_dark():
            action Hide("pizzeria_exterior"), Jump("pizza_interior_dialogue")
        else:
            action Hide("pizzeria_exterior"), Jump("pizza_closed")

screen pizzeria_interior:
    add "backgrounds/location_pizza.jpg"

    if pizza_count == 1:
        imagebutton:
            focus_mask True
            pos (163,256)
            idle "objects/character_tony_01.png"
            hover "objects/character_tony_01b.png"
            action Hide("pizzeria_interior"), Jump("tony_dialogue")

    if deliver_pizzas == True:
        imagebutton:
            focus_mask True
            pos (380,400)
            idle "objects/object_pizza_01.png"
            hover "objects/object_pizza_01b.png"
            action Hide("pizzeria_interior"), Jump("pizza_minigame")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover "boxes/auto_option_08b.png"
        action Hide("pizzeria_interior"), Jump("pizza_exterior_dialogue")