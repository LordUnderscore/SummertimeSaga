screen hospital:
    add gTimer.image("backgrounds/location_hospital_first{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,0)
        if is_here("roz"):
            idle "objects/object_desk_09.png"
            hover "objects/object_desk_09b.png"
            action Hide("hospital"), Jump("roz_dialogue")

        else:
            idle "objects/object_desk_09_empty.png"
            hover "objects/object_desk_09b_empty.png"
            action Hide("hospital"), Show("hospital_front_desk")

    imagebutton:
        focus_mask True
        pos (466,458)
        idle "objects/object_elevator_01.png"
        hover "objects/object_elevator_01b.png"
        action Hide("hospital"), Jump("elevator_dialogue")

screen hospital_front_desk:
    add "backgrounds/location_hospital_desk.jpg"

    imagebutton:
        focus_mask True
        pos (338,183)
        idle "objects/object_box_01.png"
        hover "objects/object_box_01b.png"
        action Hide("hospital_front_desk"), Show("roz_locker")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("hospital_front_desk"), Jump("hospital_dialogue")

screen roz_locker:
    add "backgrounds/location_hospital_box.jpg"

    if hospital_access_card not in inventory.items:
        imagebutton:
            focus_mask True
            pos (580,50)
            idle "objects/object_card_01.png"
            hover "objects/object_card_01b.png"
            action Function(inventory.get_item, item = hospital_access_card), Show("popup", Image = "boxes/popup_item_card4.png")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover "boxes/auto_option_generic_01b.png"
        action Hide("roz_locker"), Show("hospital_front_desk")