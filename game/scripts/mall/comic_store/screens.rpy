screen comic_store:
    add "backgrounds/location_comic.jpg"

    imagebutton:
        focus_mask True
        pos (675,318)
        idle "objects/character_tatiana_01.png"
        hover "objects/character_tatiana_01b.png"
        action Hide("comic_store"), Jump("tatiana_dialogue")

    imagebutton:
        focus_mask True
        pos (9,333)
        idle "objects/object_bookshelf_01.png"
        hover "objects/object_bookshelf_01b.png"
        action Show("comic_ui", interface = "Video Games")

    imagebutton:
        focus_mask True
        pos (159,355)
        idle "objects/object_comicstand_01.png"
        hover "objects/object_comicstand_01b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (564,175)
        idle "objects/object_costumes_01.png"
        hover "objects/object_costumes_01b.png"
        action Show("comic_ui", interface = "Cosplay")

    imagebutton:
        focus_mask True
        pos (328,392)
        idle "objects/object_figurines_01.png"
        hover "objects/object_figurines_01b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (905,409)
        idle "objects/object_posters_01.png"
        hover "objects/object_posters_01b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (297,509)
        idle "objects/object_shelf_01.png"
        hover "objects/object_shelf_01b.png"
        action Show("comic_ui", interface = "Collectible")

    imagebutton:
        focus_mask True
        pos (583,500)
        idle "objects/object_shelf_02.png"
        hover "objects/object_shelf_02b.png"
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (440,293)
        idle "objects/object_vr_01.png"
        hover "objects/object_vr_01b.png"
        action Show("popup_virtualsaga")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_10.png"
        hover "boxes/auto_option_10b.png"
        action Hide("comic_store"), Jump("mall_dialogue")

screen popup_virtualsaga:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_virtualsaga")]

    add "boxes/pink_item_11.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_600.png"
        hover "buttons/shop_button_600b.png"
        action [
            Function(inventory.buy_item, virtualsaga),
            If(
                inventory.money < 600,
                Show("popup_fail01"),
                If(
                    virtualsaga in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_virtualsaga")
                )
            ),
            Hide("popup_virtualsaga")
        ]

screen comic_item_info(Item):
    text "{color=#8995AD}[Item.category]:{/color}\n\n{color=#5E6C8F}[Item.name]{/color}" pos 130, 93
    imagebutton idle ["buttons/shop_button_" + str(Item.price) + ".png"] hover ["buttons/shop_button_" + str(Item.price) + "b.png"] action If(inventory.money < Item.price, Show("popup_fail01"), If(Item.item in inventory.items, Show("popup_fail02"), [Function(inventory.buy_item, Item.item), Show("popup", Image = Item.popup)])) pos 685, 93

screen comic_item_preview(Item):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("comic_item_preview")

    imagebutton idle "buttons/comic_ui_02.png" action Hide("comic_item_preview") focus_mask True at truecenter

    imagebutton idle Item.image action NullAction() focus_mask True at truecenter

screen comic_ui(interface):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("comic_item_info"), Hide("comic_ui")]

    imagebutton idle "buttons/comic_ui_01.png" action NullAction() focus_mask True at truecenter

    $ items = []

    for Item in comicstore.items:
        if Item.category == interface and Item.purchased == False:
            $ items += [Item]

    $ a = 0
    $ b = 0
    $ c = 0
    $ c2 = 0
    $ c3 = 0
    for Item in items:
        $ c2 = math.trunc(c / 6)
        if c3 == 6:
            $ c3 = 0
        $ a = 123
        $ b = 163 + (c2 * 133)
        $ a += c3 * 130
        imagebutton idle Item.idle hover Item.hover xpos a ypos b action [Show("comic_item_info", Item = Item), If(Item.image == "", NullAction(), Show("comic_item_preview", Item = Item))]
        $ c += 1
        $ c3 += 1