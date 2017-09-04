screen orc_battle:
    if renpy.variant("pc"):
        key "K_SPACE" action [Hide("orc_battle"), Function(orcHit)]

    else:
        imagebutton idle "backgrounds/menu_ground.png" action [Hide("orc_battle"), Function(orcHit)]