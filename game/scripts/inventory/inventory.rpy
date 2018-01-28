init -200 python:
    import math
    class Item:
        def __init__(self, name, cost, image = "", description = "", h_image = "", closeup = "", dialogue = ""):
            self.name = name
            self.cost = cost
            self.image = image
            self.description = description
            self.h_image = h_image
            self.closeup = closeup
            self.dialogue = dialogue

    class Inventory (object) :                                      
        def __init__(self, money = 20, savings = 0):                                
            self.items = []
            self.money = money
            self.savings = savings
        
        def get_item (self, item):
            if item not in self.items:
                self.items.append(item)
        
        def buy_item (self, item):
            if item not in self.items and self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost
                renpy.play("audio/sfx_coins2.ogg")
        
        def remove_item (self, item):
            if item in self.items:
                self.items.remove(item)
        
        def trade_item (self, item, item_2):
            if item in self.items:
                self.items.remove(item)
                self.items.append(item_2)
        
        def spend_money (self, value):
            self.money -= value
            renpy.play("audio/sfx_coins2.ogg")

    def deposit_money(d_money):
        if inventory.money >= d_money and (inventory.savings + d_money) <= 25000:
            inventory.savings += d_money
            inventory.money -= d_money

    def withdraw_money(d_money):
        if inventory.savings >= d_money:
            inventory.savings -= d_money
            inventory.money += d_money

screen item_desc(Item):
    $ description = Item.description
    text description pos 205, 555

screen item_name(Item):
    $ name = Item.name
    text name pos 205, 530

screen inventory_item_preview(Item):
    imagebutton:
        idle "backgrounds/backpack_closeup.jpg"
        action Hide("inventory_item_preview")

    imagebutton idle Item.closeup action NullAction() focus_mask True at Position(xalign = 0.5, yalign = 1.0)

screen backpack:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("backpack"), Hide("item_name"), Hide("item_desc"), Play("audio", "audio/sfx_backpack_close.ogg")]

    imagebutton idle "buttons/backpack.png" xalign 0.5 yalign 1.0 action [Hide("backpack"), Play("audio", "audio/sfx_backpack_close.ogg")] focus_mask True

    imagebutton idle "buttons/backpack_preloop.png" xpos 190 ypos 134 action NullAction() focus_mask True

    default backback_page = 1
    default items_per_page = 15
    default current_item = 0
    default start_item = 0
    default total_items = len(inventory.items)
    default Inv = inventory.items

    for current_item in xrange(start_item, (backback_page * items_per_page)):
        if current_item < total_items:
            $ start_xpos = 191
            $ start_ypos = 134
            $ row_ypos = math.trunc(current_item / 5)
            $ row_xpos = current_item - (row_ypos * 5)
            $ row_ypos -= math.trunc(start_item / 5)
            $ start_xpos += 130 * row_xpos
            $ start_ypos += 130 * row_ypos

            vbox:
                area (start_xpos,start_ypos,130,130)
                imagebutton:
                    idle Inv[current_item].image
                    hover Inv[current_item].h_image
                    xalign 0.5
                    yalign 0.5
                    action [If(Inv[current_item].closeup == "",
                                NullAction(),
                                Show("inventory_item_preview", Item = Inv[current_item])
                            ),
                            If(Inv[current_item].dialogue == "",
                                NullAction(),
                                Function(renpy.call_in_new_context, Inv[current_item].dialogue, item = Inv[current_item])
                            ),
                            
                            Play("audio", "audio/sfx_backpack_select2.ogg")
                           ] hovered [Show(("item_name"), Item = Inv[current_item]),
                                      Show(("item_desc"), Item = Inv[current_item])
                                     ] unhovered [Hide("item_desc"), Hide("item_name")]

    if backback_page > 1:
        imagebutton:
            focus_mask True
            pos (43,261)
            idle "buttons/backpack_left.png"
            action SetScreenVariable("backback_page", backback_page - 1), SetScreenVariable("start_item", start_item - 15)

    if current_item + 1 < total_items:
        imagebutton:
            focus_mask True
            pos (874,264)
            idle "buttons/backpack_right.png"
            action SetScreenVariable("backback_page", backback_page + 1), SetScreenVariable("start_item", start_item + 15)