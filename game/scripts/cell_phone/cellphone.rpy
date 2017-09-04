init python:
    style.button["message"].background = "#0000"
    style.button_text["message"].size = 15

    class Stat:
        def __init__(self, image=""):
            self.image = image

    class PlayerStats(object) :                                      
        def __init__(self):                                
            self._str = 0
            self._int = 0
            self._dex = 0
            self._chr = 0
        
        def increase(self,stat):
            if stat == "str":
                if self._str < 10:
                    self._str += 1
            elif stat == "int":
                if self._int < 10:
                    self._int += 1
            elif stat == "dex":
                if self._dex < 10:
                    self._dex += 1
            elif stat == "chr":
                if self._chr < 10:
                    self._chr += 1
        
        def max_all(self):
            self._str = 10
            self._int = 10
            self._dex = 10
            self._chr = 10
            return True
        
        def str(self):
            return self._str
        def strength(self):
            return self._str
        
        def int(self):
            return self._int
        def intelligence(self):
            return self._int
        
        def dex(self):
            return self._dex
        def dexterity(self):
            return self._dex
        
        def chr(self):
            return self._chr
        def charisma(self):
            return self._chr
        
        def __repr__(self):
            return "STR:{} INT:{} DEX:{} CHR:{}".format(self._str, self._int, self._dex, self._chr)

    class Quest:
        def __init__(self, name, image="", status= False):
            self.name = name
            self.image = image
            self.status = status

    def quest_complete(Quest):
        completed_quests.append(Quest)

    class Message:
        def __init__(self, name, sender = "", content_prev = "", content = "", image="", status=False):
            self.name = name
            self.sender = sender
            self.content_prev = content_prev
            self.content = content
            self.image = image
            self.status = status

    def message_inactive(list):
        for Message in list:
            if Message.status == True:
                Message.status = False

screen cellphone tag cellphone_screen:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("cellphone_screen")]

    imagebutton idle "buttons/cellphone.png" action NullAction() pos 300,80

    if new_message == True:
        add "buttons/cellphone_app_alert.png" pos 560,127

    add "buttons/cellphone_title_apps.png" pos 460,130

    add "buttons/cellphone_app_temp.png" pos 355,280

    imagebutton idle "buttons/cellphone_app01.png" hover "buttons/cellphone_app01b.png" action Show("quest_log") pos 355,180

    imagebutton idle "buttons/cellphone_app02.png" hover "buttons/cellphone_app02b.png" action Show("stat_log") pos 455,180

    imagebutton idle "buttons/cellphone_app03.png" hover "buttons/cellphone_app03b.png" action Show("message_submenu") pos 555,180



screen hint_system tag cellphone_screen:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("cellphone_screen")]

    imagebutton idle "buttons/cellphone.png" action NullAction() pos 300,80

    add "buttons/cellphone_title_text.png" pos 435,130

    imagebutton idle "buttons/cellphone_back01.png" hover "buttons/cellphone_back01.png" action Show("cellphone") pos 344,125

    imagebutton idle "buttons/cellphone_text_judith01.png" action Show("hint_subsystem", Hint = sister) pos 365,165
    imagebutton idle "buttons/cellphone_text_judith01.png" action Show("hint_subsystem", Hint = sister) pos 435,165
    imagebutton idle "buttons/cellphone_text_judith01.png" action Show("hint_subsystem", Hint = sister) pos 505,165
    imagebutton idle "buttons/cellphone_text_judith01.png" action Show("hint_subsystem", Hint = sister) pos 575,165
    imagebutton idle "buttons/cellphone_text_judith01.png" action Show("hint_subsystem", Hint = sister) pos 365,235

screen hint_subsystem(Hint) tag cellphone_screen:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("cellphone_screen")]

    imagebutton idle "buttons/cellphone.png" action NullAction() pos 300,80

    add "buttons/cellphone_title_goals.png" pos 345,130

    imagebutton idle "buttons/cellphone_back01.png" hover "buttons/cellphone_back01.png" action Show("hint_system") pos 344,125

    $ qa = 370
    $ qc = 0
    $ qb = 220
    $ qb = qb + 70*qc
    add "buttons/cellphone_goals_main01.png" pos qa,qb
    text "{b}{color=#00FF00}This is a hint to test out the new hint system ingame!{/color}{/b}" pos qa+35,qb+5 xmaximum 220
    $ qc += 1
    $ qb = 220
    $ qb = qb + 70*qc
    add "buttons/cellphone_goals_main01.png" pos qa,qb
    text "{b}{color=#00FF00}a a a a a a a a a a a a a a a a a a a a a a a a a a a a{/color}{/b}" pos qa+35,qb+5 xmaximum 220


screen quest_log tag cellphone_screen:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("cellphone_screen")]

    imagebutton idle "buttons/cellphone.png" action NullAction() pos 300,80

    add "buttons/cellphone_title_goals.png" pos 345,130

    imagebutton idle "buttons/cellphone_back01.png" hover "buttons/cellphone_back01.png" action Show("cellphone") pos 344,125

    imagebutton idle "buttons/cellphone_goals_button01.png" hover "buttons/cellphone_goals_button01b.png" action SetVariable("show_quest", "main") pos 378,530

    imagebutton idle "buttons/cellphone_goals_button02.png" hover "buttons/cellphone_goals_button02b.png" action SetVariable("show_quest", "side") pos 508,530

    if show_quest == "main":
        add "buttons/cellphone_goals_main01.png" pos 370,220
        add "buttons/cellphone_goals_main02.png" pos 370,260
        add "buttons/cellphone_goals_main03.png" pos 370,300

    elif show_quest == "side":
        $ qa = 370
        $ qc = 0
        for Quest in quest_list:
            if Quest not in completed_quests:
                $ qb = 220
                $ qb = qb + 40*qc
                $ qpic = Quest.image
                add qpic pos qa,qb
                $ qc += 1

screen stat_log tag cellphone_screen:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("cellphone_screen")]

    imagebutton idle "buttons/cellphone.png" action NullAction() pos 300,80

    add "buttons/cellphone_title_stats.png" pos 345,130

    add "buttons/cellphone_stats_tab.png" pos 357,355

    imagebutton idle "buttons/cellphone_back01.png" hover "buttons/cellphone_back01.png" action Show("cellphone") pos 344,125

    $ a = 436

    for count in range(0, pStats.str()):
        $ x = a + count*19
        add "buttons/cellphone_bar01.png" xpos x ypos 366

    for count in range(0, pStats.dex()):
        $ x = a + count*19
        add "buttons/cellphone_bar02.png" xpos x ypos 424

    for count in range(0, pStats.chr()):
        $ x = a + count*19
        add "buttons/cellphone_bar03.png" xpos x ypos 482

    for count in range(0, pStats.int()):
        $ x = a + count*19
        add "buttons/cellphone_bar04.png" xpos x ypos 540

screen message_submenu tag cellphone_screen:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("cellphone_screen"), Function(message_inactive, list=message_list), SetVariable("new_message", False)]

    imagebutton idle "buttons/cellphone.png" action NullAction() pos 300,80

    add "buttons/cellphone_title_text.png" pos 435,130

    imagebutton idle "buttons/cellphone_back01.png" hover "buttons/cellphone_back01.png" action Show("cellphone") pos 344,125

    add "buttons/cellphone_text_tabs.png" pos 355,220
    add "buttons/cellphone_text_tabs.png" pos 355,270
    add "buttons/cellphone_text_tabs.png" pos 355,320
    add "buttons/cellphone_text_tabs.png" pos 355,370
    add "buttons/cellphone_text_tabs.png" pos 355,420

    $ mc = 0
    for Message in message_list:
        $ ma = 355
        $ mb = 226
        $ mb = mb + 50*mc
        textbutton "[Message.sender] - [Message.content_prev]" style style.button["message"] action Show("message", Message = Message) pos ma,mb
        $ mc += 1

screen message(Message) tag cellphone_screen:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide ("cellphone_screen"), SetVariable("new_message", False)]

    imagebutton idle "buttons/cellphone.png" action NullAction() pos 300,80

    add "buttons/cellphone_title_text.png" pos 435,130

    imagebutton idle "buttons/cellphone_back01.png" hover "buttons/cellphone_back01.png" action Show("cellphone") pos 344,125

    add "buttons/cellphone_text_bg.png" pos 343, 165
    add Message.image pos 365,165

    text "{color=#f00}[Message.sender]{/color} is texting you..." color "#000" size 16 pos 445,195
    text "[Message.content]" color "#000" size 18 pos 374,260