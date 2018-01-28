screen basket_ball_court:
    add gTimer.image("backgrounds/location_basketball{}.jpg")

    imagebutton:
        focus_mask True
        pos (523,358)
        idle "objects/object_basketball_01.png"
        hover "objects/object_basketball_01b.png"
        action Show("popup_unfinished")

    if not gTimer.is_dark():
        imagebutton:
            focus_mask True
            pos (729,414)
            idle "objects/character_dexter_01.png"
            hover "objects/character_dexter_01b.png"
            action Hide("basket_ball_court"), Jump("dexter_court_dialogue")