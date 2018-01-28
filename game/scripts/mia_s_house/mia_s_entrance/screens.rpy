screen mias_house_entrance:
    if M_mia.is_set('harold left') and gTimer.is_dark():
        add "backgrounds/location_mia_house_without_night.jpg"

    else:
        add gTimer.image("backgrounds/location_mia_house{}.jpg")

    if is_here("mia"):
        imagebutton:
            focus_mask True
            pos (280,330)
            idle "objects/character_mia_01c.png"
            hover "objects/character_mia_01d.png"
            action Hide("mias_house_entrance"), Jump("mia_button_dialogue")

    imagebutton:
        focus_mask True
        pos (531,267)
        idle gTimer.image("objects/object_stairs_05{}.png")
        hover gTimer.image("objects/object_stairs_05b{}.png")
        action Hide("mias_house_entrance"), Jump("mias_upstairs")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_08.png"
        hover "boxes/auto_option_08b.png"
        action Hide("mias_house_entrance"), If(M_mia.get_state() == S_mia_unexpected_visit, Jump("helen_masturbating_block"), Jump("mias_house_dialogue"))