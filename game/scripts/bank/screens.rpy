screen bank:
    add "backgrounds/location_bank.jpg"

    imagebutton:
        focus_mask True
        pos (89,339)
        idle "objects/object_atm_01.png"
        hover "objects/object_atm_01b.png"
        action Show("atm01_options")

    imagebutton:
        focus_mask True
        pos (755,460)
        idle "objects/object_desk_06.png"
        hover "objects/object_desk_06b.png"
        action Show("desk06_options")

screen atm01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("atm01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/atm01_option_01.png"
        hover "boxes/atm01_option_01b.png"
        action Hide("atm01_options"), Hide("bank"), Show("atm")

screen desk06_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk06_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk06_option_01.png"
        hover "boxes/desk06_option_01b.png"
        action Hide("bank"), Hide("desk06_options"), Jump("bank__tellerdialogue")

screen atm:
    add "backgrounds/atm01.jpg"

    $ money = '{:20,}'.format(inventory.savings)
    text "[money] / 25,000" xalign 1.0 pos 575,560 size 30

    imagebutton:
        focus_mask True
        pos (335,224)
        idle "buttons/atm_button_01.png"
        hover "buttons/atm_button_01b.png"
        action Function(deposit_money, d_money = 100)

    imagebutton:
        focus_mask True
        pos (492,224)
        idle "buttons/atm_button_02.png"
        hover "buttons/atm_button_02b.png"
        action Function(deposit_money, d_money = 200)

    imagebutton:
        focus_mask True
        pos (650,224)
        idle "buttons/atm_button_03.png"
        hover "buttons/atm_button_03b.png"
        action Function(deposit_money, d_money = 500)

    imagebutton:
        focus_mask True
        pos (335,280)
        idle "buttons/atm_button_04.png"
        hover "buttons/atm_button_04b.png"
        action Function(deposit_money, d_money = 1000)

    imagebutton:
        focus_mask True
        pos (492,280)
        idle "buttons/atm_button_05.png"
        hover "buttons/atm_button_05b.png"
        action Function(deposit_money, d_money = 5000)

    imagebutton:
        focus_mask True
        pos (650,280)
        idle "buttons/atm_button_06.png"
        hover "buttons/atm_button_06b.png"
        action Function(deposit_money, d_money = 10000)

    imagebutton:
        focus_mask True
        pos (335,372)
        idle "buttons/atm_button_01.png"
        hover "buttons/atm_button_01b.png"
        action Function(withdraw_money, d_money = 100)

    imagebutton:
        focus_mask True
        pos (492,372)
        idle "buttons/atm_button_02.png"
        hover "buttons/atm_button_02b.png"
        action Function(withdraw_money, d_money = 200)

    imagebutton:
        focus_mask True
        pos (650,372)
        idle "buttons/atm_button_03.png"
        hover "buttons/atm_button_03b.png"
        action Function(withdraw_money, d_money = 500)

    imagebutton:
        focus_mask True
        pos (335,428)
        idle "buttons/atm_button_04.png"
        hover "buttons/atm_button_04b.png"
        action Function(withdraw_money, d_money = 1000)

    imagebutton:
        focus_mask True
        pos (492,428)
        idle "buttons/atm_button_05.png"
        hover "buttons/atm_button_05b.png"
        action Function(withdraw_money, d_money = 5000)

    imagebutton:
        focus_mask True
        pos (650,428)
        idle "buttons/atm_button_06.png"
        hover "buttons/atm_button_06b.png"
        action Function(withdraw_money, d_money = 10000)

    imagebutton:
        idle "buttons/atm_button_07.png"
        hover "buttons/atm_button_07b.png"
        action Hide("atm"), Jump("bank_dialogue")
        pos 680,513