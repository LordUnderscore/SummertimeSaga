screen home_front:
    add gTimer.image("backgrounds/location_home_front{}.jpg")

    imagebutton:
        if player_mail != [] or (erik.completed(erik_orcette) and orcette not in inventory.items and not erik.known(erik_orcette_2) and orcette_mail_lock):
            pos (880,480)
            idle gTimer.image("objects/object_mailbox_home01{}.png")
            hover gTimer.image("objects/object_mailbox_home01b{}.png")
        else:
            pos (880,500)
            idle gTimer.image("objects/object_mailbox_home02{}.png")
            hover gTimer.image("objects/object_mailbox_home02b{}.png")
        action Hide("home_front"), Jump("player_mailbox")

    imagebutton:
        focus_mask True
        pos (557,454)
        idle gTimer.image("objects/object_door_34{}.png")
        hover gTimer.image("objects/object_door_34b{}.png")
        action Hide("home_front"), Function(playSound), Play("audio", sfxDoor()), Jump("home_entrance")

    imagebutton:
        focus_mask True
        pos (172,403)
        idle gTimer.image("objects/object_door_36{}.png")
        hover gTimer.image("objects/object_door_36b{}.png")

        action If(
            player.known(lawn_mowed) and not player.over(lawn_mowed),
            [Hide("home_front"), Jump("lawn_mower_dirty")],
            [Hide("home_front"), Jump("home_garage")]
            )

screen mailbox:
    if gTimer.is_dark():
        add "backgrounds/mailbox_player_night.jpg"
    else:
        add "backgrounds/mailbox_player_day.jpg"

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("mailbox"), Jump("home_front")

    if erik.completed(erik_orcette) and orcette not in inventory.items and not erik.known(erik_orcette_2) and orcette_mail_lock:
        imagebutton:
            focus_mask True
            pos (300,345)
            idle gTimer.image("objects/object_mailbox_item04{}.png")
            hover gTimer.image("objects/object_mailbox_item04b{}.png")
            action Hide("mailbox"), Jump("player_mailbox_dialogue")

    elif m_pizza_pamphlet in player_mail:
        imagebutton:
            focus_mask True
            pos (240,480)
            idle gTimer.image("objects/object_mailbox_item02{}.png")
            hover gTimer.image("objects/object_mailbox_item02b{}.png")
            action Hide("mailbox"), Jump("player_mailbox_dialogue")

    elif m_newspaper in player_mail:
        imagebutton:
            focus_mask True
            pos (250,575)
            idle gTimer.image("objects/object_mailbox_item05{}.png")
            hover gTimer.image("objects/object_mailbox_item05b{}.png")
            action Hide("mailbox"), Jump("player_mailbox_dialogue")