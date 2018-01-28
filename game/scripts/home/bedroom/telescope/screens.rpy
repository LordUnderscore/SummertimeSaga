screen telescope:
    imagebutton:
        focus_mask True
        align (0.1,0.02)
        if M_player.get("telescope selection") == "Erik":
            idle "buttons/telescope_icon_01.png"
        else:
            idle "buttons/telescope_icon_01c.png"
        if M_player.is_set("telescope active"):
            if M_player.get("telescope selection") != "Erik":
                hover "buttons/telescope_icon_01d.png"
                action Function(M_player.set, "telescope selection", "Erik"), Function(M_player.set, "telescope active", False), Jump("erik_bedroom")



    imagebutton:
        focus_mask True
        align (0.02,0.1)
        if M_player.get("telescope selection") == "Mrs Johnson":
            idle "buttons/telescope_icon_02.png"
        else:
            idle "buttons/telescope_icon_02c.png"
        if M_player.is_set("telescope active"):
            if M_player.get("telescope selection") != "Mrs Johnson":
                hover "buttons/telescope_icon_02d.png"
                action Function(M_player.set, "telescope selection", "Mrs Johnson"), Function(M_player.set, "telescope active", False), Jump("erikmom_bedroom")



    imagebutton:
        focus_mask True
        align (0.9,0.02)
        if M_player.get("telescope selection") == "Mia":
            idle "buttons/telescope_icon_03.png"
        else:
            idle "buttons/telescope_icon_03c.png"
        if M_player.is_set("telescope active"):
            if M_player.get("telescope selection") != "Mia":
                hover "buttons/telescope_icon_03d.png"
                action Function(M_player.set, "telescope selection", "Mia"), Function(M_player.set, "telescope active", False), Jump("mia_bedroom")



    imagebutton:
        focus_mask True
        align (0.98,0.1)
        if M_player.get("telescope selection") == "Helen":
            idle "buttons/telescope_icon_04.png"
        else:
            idle "buttons/telescope_icon_04c.png"
        if M_player.is_set("telescope active"):
            if M_player.get("telescope selection") != "Helen":
                hover "buttons/telescope_icon_04d.png"
                action Function(M_player.set, "telescope selection", "Helen"), Function(M_player.set, "telescope active", False), Jump("helen_room")



    imagebutton:
        focus_mask True
        align (0.02,0.9)
        if M_player.get("telescope selection") == "Erik's Backyard":
            idle "buttons/telescope_icon_05.png"
        else:
            idle "buttons/telescope_icon_05c.png"
        if M_player.is_set("telescope active"):
            if M_player.get("telescope selection") != "Erik's Backyard":
                hover "buttons/telescope_icon_05d.png"
                action Function(M_player.set, "telescope selection", "Erik's Backyard"), Function(M_player.set, "telescope active", False), Jump("backyard")



    if M_player.is_set("telescope active"):
        imagebutton:
            focus_mask True
            align (0.5,0.97)
            idle "boxes/auto_option_generic_01.png"
            hover "boxes/auto_option_generic_01b.png"
            action Hide("telescope"), Jump("bedroom_dialogue")

screen telescope_fake:
    add "backgrounds/menu_ground.png"