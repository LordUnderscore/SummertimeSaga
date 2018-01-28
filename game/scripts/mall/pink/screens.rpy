screen pink:
    add "backgrounds/location_pink.jpg"

    imagebutton:
        focus_mask True
        idle "objects/object_toy_01.png"
        hover "objects/object_toy_01b.png"
        action Show("popup_buttplug")
        pos 89,167

    imagebutton:
        focus_mask True
        idle "objects/object_toy_02.png"
        hover "objects/object_toy_02b.png"
        action Show("popup_drilldo")
        pos 209,246

    imagebutton:
        idle "objects/object_toy_03.png"
        hover "objects/object_toy_03b.png"
        action Show("pink_ui")
        pos 11,422

    imagebutton:
        focus_mask True
        idle "objects/object_toy_04.png"
        hover "objects/object_toy_04b.png"
        action Show("popup_electroclit")
        pos 162,517

    imagebutton:
        focus_mask True
        idle "objects/object_toy_05.png"
        hover "objects/object_toy_05b.png"
        action Show("popup_strapon")
        pos 301,422

    imagebutton:
        focus_mask True
        idle "objects/object_toy_06.png"
        hover "objects/object_toy_06b.png"
        action Show("popup_badmonster")
        pos 315,306

    imagebutton:
        focus_mask True
        idle "objects/object_toy_07.png"
        hover "objects/object_toy_07b.png"
        action Show("popup_darthmoan")
        pos 284,182

    imagebutton:
        focus_mask True
        idle "objects/object_toy_08.png"
        hover "objects/object_toy_08b.png"
        action Show("popup_sybian")
        pos 334,532

    imagebutton:
        focus_mask True
        idle "objects/object_toy_09.png"
        hover "objects/object_toy_09b.png"
        action Show("popup_fleshtube")
        pos 439,486

    imagebutton:
        focus_mask True
        idle "objects/object_toy_10.png"
        hover "objects/object_toy_10b.png"
        action Show("popup_doomdong")
        pos 477,309

    imagebutton:
        focus_mask True
        idle "objects/object_toy_11.png"
        hover "objects/object_toy_11b.png"
        action Show("popup_ultravibrato")
        pos 530, 231

    imagebutton:
        focus_mask True
        idle "objects/object_toy_12.png"
        hover "objects/object_toy_12b.png"
        action Show("popup_sexdoll")
        pos 551,371

    imagebutton:
        focus_mask True
        idle "objects/object_toy_13.png"
        hover "objects/object_toy_13b.png"
        action Show("popup_whip")
        pos 292,491

    imagebutton:
        focus_mask True
        idle "objects/object_toy_14.png"
        hover "objects/object_toy_14b.png"
        action Show("popup_handcuffs")
        pos 147,468

    imagebutton:
        focus_mask True
        idle "objects/character_ivy_01.png"
        hover "objects/character_ivy_01b.png"
        action Hide("pink"), Jump("ivy_button_dialogue")
        pos 910,350

    imagebutton:
        idle "boxes/auto_option_10.png"
        hover "boxes/auto_option_10b.png"
        action Hide("pink"), Jump("mall_dialogue")
        pos 350, 700

screen popup_buttplug:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_buttplug")]
    add "boxes/pink_item_01.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [
            Function(inventory.buy_item, buttplug),
            If(
                inventory.money < 100,
                Show("popup_fail01"),
                If(buttplug in inventory.items,
                   Show("popup_fail02"),
                   Show("popup_buttplug")
                )
            ),
            Hide("popup_buttplug")
        ]
        xpos 410
        ypos 421

screen popup_drilldo:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_drilldo")]
    add "boxes/pink_item_02.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_400.png"
        hover "buttons/shop_button_400b.png"
        action [
            Function(inventory.buy_item, drilldo),
            If(
                inventory.money < 400,
                Show("popup_fail01"),
                If(drilldo in inventory.items,
                   Show("popup_fail02"),
                   Show("popup_drilldo")
                )
            ),
            Hide("popup_drilldo")
        ]
        xpos 410
        ypos 421

screen popup_darthmoan:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_darthmoan")]
    add "boxes/pink_item_03.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_300.png"
        hover "buttons/shop_button_300b.png"
        action [
            Function(inventory.buy_item, darthmoan),
            If(
                inventory.money < 300,
                Show("popup_fail01"),
                    If(
                        darthmoan in inventory.items,
                        Show("popup_fail02"),
                        Show("popup_darthmoan")
                    )
            ),
            Hide("popup_darthmoan")
        ]
        xpos 410
        ypos 421

screen popup_badmonster:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_badmonster")]
    add "boxes/pink_item_04.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover "buttons/shop_button_500b.png"
        action [
            Function(inventory.buy_item, badmonster),
            If(
                inventory.money < 500,
                Show("popup_fail01"),
                If(
                    badmonster in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_badmonster")
                )
            ),
            Hide("popup_badmonster")
        ]
        xpos 410
        ypos 421

screen popup_sybian:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_sybian")]
    add "boxes/pink_item_05.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover "buttons/shop_button_500b.png"
        action [
            Function(inventory.buy_item, sybian),
            If(
                inventory.money < 500,
                Show("popup_fail01"),
                If(
                    sybian in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_sybian")
                )
            ),
            Hide("popup_sybian")
        ]
        xpos 410
        ypos 421

screen popup_strapon:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_strapon")]
    add "boxes/pink_item_06.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover "buttons/shop_button_500b.png"
        action [
            Function(inventory.buy_item, strapon),
            If(
                inventory.money < 500,
                Show("popup_fail01"),
                If(
                    strapon in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_strapon")
                )
            ),
            Hide("popup_strapon")
        ]
        xpos 410
        ypos 421

screen popup_fleshtube:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_fleshtube")]
    add "boxes/pink_item_07.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [
            Function(inventory.buy_item, fleshtube),
            If(
                inventory.money < 100,
                Show("popup_fail01"),
                If(
                    fleshtube in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_fleshtube")
                )
            ),
            Hide("popup_fleshtube")
        ]
        xpos 410
        ypos 421

screen popup_electroclit:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_electroclit")]
    add "boxes/pink_item_08.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_100.png"
        hover "buttons/shop_button_100b.png"
        action [
            Function(inventory.buy_item, electroclit),
            If(
                inventory.money < 100,
                Show("popup_fail01"),
                If(
                    electroclit in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_electroclit")
                )
            ),
            Hide("popup_electroclit")
        ]
        xpos 410
        ypos 421

screen popup_ultravibrato:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_ultravibrato")]
    add "boxes/pink_item_09.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_200.png"
        hover "buttons/shop_button_200b.png"
        action [
            Function(inventory.buy_item, ultravibrato),
            If(
                inventory.money < 200,
                Show("popup_fail01"),
                If(
                    ultravibrato in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_ultravibrato")
                )
            ),
            Hide("popup_ultravibrato")
        ]
        xpos 410
        ypos 421

screen popup_doomdong:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_doomdong")]
    add "boxes/pink_item_10.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_300.png"
        hover "buttons/shop_button_300b.png"
        action [
            Function(inventory.buy_item, doomdong),
            If(
                inventory.money < 300,
                Show("popup_fail01"),
                If(
                    doomdong in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_doomdong")
                )
            ),
            Hide("popup_doomdong")
        ]
        xpos 410
        ypos 421

screen popup_sexdoll:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_sexdoll")]
    add "boxes/pink_item_12.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_800.png"
        hover "buttons/shop_button_800b.png"
        action [
            Function(inventory.buy_item, sexdoll),
            If(inventory.money < 800,
               Show("popup_fail01"),
               If(
                    sexdoll in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_sexdoll")
               )
            ),
            Hide("popup_sexdoll")
        ]
        xpos 410
        ypos 421

screen popup_whip:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_whip")]
    add "boxes/pink_item_13.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover "buttons/shop_button_500b.png"
        action [
            Function(inventory.buy_item, whip),
            If(inventory.money < 500,
               Show("popup_fail01"),
               If(
                    whip in inventory.items,
                    Show("popup_fail02"),
                    Show("popup_whip")
               )
            ),
            Hide("popup_whip")
        ]
        xpos 410
        ypos 421

screen popup_handcuffs:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_handcuffs")]
    add "boxes/pink_item_14.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_50.png"
        hover "buttons/shop_button_50b.png"
        action [Function(inventory.buy_item, handcuffs), If(inventory.money < 50, Show("popup_fail01"), If(handcuffs in inventory.items, Show("popup_fail02"), Show("popup_handcuffs"))), Hide("popup_handcuffs")]
        xpos 410
        ypos 421

screen popup_fail01:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_fail01")]
    add "boxes/popup_shopping_fail01.png"

screen popup_fail02:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_fail02")]
    add "boxes/popup_shopping_fail02.png"

screen pamphlet:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("pamphlet"), Show("pink")]
    imagebutton:
        idle "buttons/massage_01.png"
        hover "buttons/massage_01b.png"
        action If(
            inventory.money >= 100,
            [
                Function(inventory.spend_money, 100),
                Function(gTimer.tick),
                Jump("ivy_paizuri")
            ], Jump("ivy_no_money")
        )
        pos 180,30
    imagebutton:
        idle "buttons/massage_02.png"
        hover "buttons/massage_02b.png"
        action If(
            inventory.money >= 200,
            [
                Function(inventory.spend_money, 200),
                Function(gTimer.tick),
                Jump ("ivy_blowjob")
            ],
            Jump("ivy_no_money")
        )
        pos 176,203
    imagebutton:
        idle "buttons/massage_03.png"
        hover "buttons/massage_03b.png"
        action If(
            inventory.money >= 400,
            [
                Function(inventory.spend_money, 400),
                Function(gTimer.tick),
                Jump ("ivy_reverse_cowgirl")
            ],
            Jump("ivy_no_money")
        )
        pos 177,363
    imagebutton:
        idle "buttons/massage_04.png"
        hover "buttons/massage_04b.png"
        action If(
            inventory.money >= 600,
            [
                Function(inventory.spend_money, 600),
                Function(gTimer.tick),
                Jump ("ivy_cowgirl")
            ],
            Jump("ivy_no_money")
        )
        pos 183,545

screen ivy_paizuri_options:
    imagebutton:
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump ("ivy_paizuri_stage1")
        xpos 300
        ypos 700
    imagebutton:
        idle "buttons/ivy_stage01_01.png"
        hover "buttons/ivy_stage01_01b.png"
        action SetVariable("ivy_sex_speed", ivy_sex_speed-0.25), Jump ("ivy_paizuri_stage1")
        xpos 500
        ypos 700

screen ivy_blowjob_options:
    imagebutton:
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump ("ivy_blowjob_stage1")
        xpos 300
        ypos 700
    imagebutton:
        idle "buttons/ivy_stage01_01.png"
        hover "buttons/ivy_stage01_01b.png"
        action SetVariable("ivy_sex_speed", ivy_sex_speed-0.25), Jump ("ivy_blowjob_stage1")
        xpos 500
        ypos 700

screen ivy_rcowgirl_options:
    imagebutton:
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump ("ivy_rcgirl_stage1")
        xpos 200
        ypos 700
    imagebutton:
        idle "buttons/ivy_stage01_01.png"
        hover "buttons/ivy_stage01_01b.png"
        action SetVariable("ivy_sex_speed", ivy_sex_speed-0.25), Jump ("ivy_rcgirl_stage1")
        xpos 400
        ypos 700
    imagebutton:
        idle "buttons/ivy_stage01_02.png"
        hover "buttons/ivy_stage01_02b.png"
        action Jump ("ivy_slap_ass")
        xpos 600
        ypos 700

screen ivy_cowgirl_options:
    imagebutton:
        idle "buttons/judith_stage02_01.png"
        hover "buttons/judith_stage02_01b.png"
        action Jump ("ivy_cowgirl_stage1")
        xpos 300
        ypos 700
    imagebutton:
        idle "buttons/ivy_stage01_01.png"
        hover "buttons/ivy_stage01_01b.png"
        action SetVariable("ivy_sex_speed", ivy_sex_speed-0.25), Jump ("ivy_cowgirl_stage1")
        xpos 500
        ypos 700

screen ivy_sex_xray:
    if ivy_xray_toggle == True:
        if xray == 0:
            if xray_front == True:
                add "characters/player/char_player_sex_36.png" pos 431,283
            else:
                add "characters/player/char_player_sex_39.png" pos 413, 285
        else:
            if xray_front == True:
                if ivy_cum_inside == True:
                    add "characters/player/char_player_sex_38.png" pos 425,326
                else:
                    add "characters/player/char_player_sex_37.png" pos 425,326
            else:
                if ivy_cum_inside == True:
                    add "characters/player/char_player_sex_41.png" pos 422,349
                else:
                    add "characters/player/char_player_sex_40.png" pos 422,349

screen ivy_sex_xray_button:
    if xray_needed == True:
        imagebutton:
            if ivy_xray_toggle == True:
                idle "buttons/anim_03.png"
                hover "buttons/anim_03b.png"
            else:
                idle "buttons/anim_04.png"
                hover "buttons/anim_04b.png"
            action If(ivy_xray_toggle == True, SetVariable("ivy_xray_toggle", False), SetVariable("ivy_xray_toggle", True))
            xpos 940
            ypos 600

    imagebutton:
        if anim_toggle== True:
            idle "buttons/anim_02.png"
            hover "buttons/anim_02b.png"
        else:
            idle "buttons/anim_01.png"
            hover "buttons/anim_01b.png"
        action If(anim_toggle == True, SetVariable("anim_toggle", False), SetVariable("anim_toggle", True)), Return
        xpos 10
        ypos 600

screen pink_item_info(Item):
    text "{color=#8995AD}[Item.category]:{/color}\n\n{color=#5E6C8F}[Item.name]{/color}" pos 130, 93
    imagebutton idle ["buttons/shop_button_" + str(Item.price) + ".png"] hover ["buttons/shop_button_" + str(Item.price) + "b.png"] action If(inventory.money < Item.price, Show("popup_fail01"), If(Item.item in inventory.items, Show("popup_fail02"), [Function(inventory.buy_item, Item.item), Show("popup", Image = Item.popup)])) pos 685, 93

screen pink_ui:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("pink_item_info"), Hide("pink_ui")]

    imagebutton idle "buttons/pink_ui_01.png" action NullAction() focus_mask True at truecenter

    $ a = 0
    $ b = 0
    $ c = 0
    $ c2 = 0
    $ c3 = 0
    for Item in pinkstore.items:
        $ c2 = math.trunc(c / 6)
        if c3 == 6:
            $ c3 = 0
        $ a = 123
        $ b = 163 + (c2 * 133)
        $ a += c3 * 130
        imagebutton idle Item.idle hover Item.hover xpos a ypos b action Show("pink_item_info", Item = Item)
        $ c += 1
        $ c3 += 1

screen ivy_cowgirl_cum_options:
    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover "buttons/diane_stage01_03b.png"
        action Jump("ivy_cowgirl_cum_outside")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("ivy_cowgirl_cum_inside")
        xpos 450
        ypos 700

screen ivy_rcowgirl_cum_options:
    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover "buttons/diane_stage01_03b.png"
        action Jump("ivy_rcowgirl_cum_outside")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover "buttons/diane_stage01_02b.png"
        action Jump("ivy_rcowgirl_cum_inside")
        xpos 450
        ypos 700