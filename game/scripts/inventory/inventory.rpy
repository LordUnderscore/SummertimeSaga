init -200 python:
    import math
    class Item:
        def __init__(self, name, cost, image = "", description = "", h_image = "", closeup = ""):
            self.name = name
            self.cost = cost
            self.image = image
            self.description = description
            self.h_image = h_image
            self.closeup = closeup

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
    text description pos 205, 525

screen item_name(Item):
    $ name = Item.name
    text name pos 205, 500

screen inventory_item_preview(Item):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("inventory_item_preview")

    imagebutton idle Item.closeup action NullAction() focus_mask True at truecenter

screen backpack:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("backpack"), Play("audio", "audio/sfx_backpack_close.ogg")]

    imagebutton idle "buttons/backpack.png" action [Hide("backpack"), Play("audio", "audio/sfx_backpack_close.ogg")] focus_mask True

    $ inv_items = inventory.items
    $ a = 0
    $ b = 0
    $ c = 0
    $ c2 = 0
    $ c3 = 0
    side "c b r":
        area (193, 97, 654, 389)
        viewport id "backpack_vp":
            draggable True
            mousewheel True
            has vbox
            imagemap:
                ground im.Composite((654, 1166), (0, -1), "buttons/backpack_preloop.png", (0, 389), im.Crop("buttons/backpack_loop.png", (0, 1, 654, 389)), (0, 778), im.Crop("buttons/backpack_loop.png", (0, 1, 654, 389)))
                vbox:
                    for Item in inv_items:
                        $ c2 = math.trunc(c / 5)
                        if c3 == 5:
                            $ c3 = 0
                        $ a = 7
                        $ b = 3 - (c3 * 125) - (c2 * 495)
                        $ a += c3 * 130
                        imagebutton idle Item.image hover Item.h_image xpos a ypos b action [If(Item.closeup == "", NullAction(), Show("inventory_item_preview", Item = Item)), Hide("item_desc"), Hide("item_name"), Play("audio", "audio/sfx_backpack_select2.ogg")] hovered [Show(("item_name"), Item = Item), Show(("item_desc"), Item = Item)] unhovered [Hide("item_desc"), Hide("item_name")]
                        $ c += 1
                        $ c3 += 1