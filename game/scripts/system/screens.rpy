screen say(who, what, side_image=None, two_window=False):
    if not two_window:

        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

screen choice(items):
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for caption, action, chosen in items:

            if action:
                if caption[0:2] == '<>':
                    button:
                        style "menu_choice_button"
                        text caption[2:] style "inactive_menu_choice"

                else:
                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True
    style inactive_menu_choice:
        color "#777777"
        drop_shadow [(1,1)]
        size 16
        text_align 0.5
        xalign 0.5
        yalign 0.5

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.30)
        xmaximum int(config.screen_width * 0.30)

screen input(prompt):
    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

screen name_input:
    add "backgrounds/menu_name.jpg"
    add SnowBlossom(Animation("buttons/leaf01.png", 0.15, "buttons/leaf02.png", 0.15))
    add "backgrounds/menu_name_overlay.png"
    add Input (size=16, color="#5d9aff", default=firstname, changed=name_func, length=12, xpos= 720, ypos = 412)
    key "K_RETURN" action Start()
    imagebutton:
        idle "buttons/menu_name_back01.png"
        hover "buttons/menu_name_back02.png"
        action Hide("name_input"), Show("main_menu")
        xpos 726
        ypos 231
    imagebutton:
        idle "buttons/menu_name_start01.png"
        hover "buttons/menu_name_start02.png"
        action Start()
        xpos 726
        ypos 506

transform credit_scroll:
    xalign 0.0 yalign 0.0
    linear 20.0 yalign 1.0

screen popup(Image):
    zorder 100

    imagebutton idle "backgrounds/menu_ground.png" action NullAction() xalign 0.0 yalign 0.0
    add Image xalign 0.5 yalign 0.5



    timer 2.0 action Hide("popup")

screen route_warning():
    add "backgrounds/blank.jpg"

    add "boxes/popup_warning.png" at truecenter

    imagebutton:
        focus_mask True
        pos (298,378)
        idle "buttons/menu_goback.png"
        hover "buttons/menu_goback2.png"
        action Hide("route_warning"), Function(callScreen, location_count, newContext = True)

    imagebutton:
        focus_mask True
        pos (612,377)
        idle "buttons/menu_continue.png"
        hover "buttons/menu_continue2.png"
        action Return()

screen adult_warning:

    imagebutton:
        focus_mask True
        pos (435,635)
        idle "buttons/menu_yes.png"
        hover "buttons/menu_yes2.png"
        action Return()

    imagebutton:
        focus_mask True
        pos (565,635)
        idle "buttons/menu_no.png"
        hover "buttons/menu_no2.png"
        action Quit(confirm=False)

screen credits:
    add "backgrounds/menu_credits.jpg"

    side "c b r":
        area (31, 235, 962, 358)
        viewport id "pledgers":
            draggable True
            mousewheel True
            has vbox
            $ pledgers = ""
            python:
                import codecs

                if renpy.variant("mobile"):
                    file = renpy.file("pledge_list.txt")
                else:
                    file = codecs.open(sys.path[0] + "/game/pledge_list.txt", encoding = "utf-8")


                for line in file:
                    line = line.replace("\r\n", "")
                    line = line.replace("\n", "")
                    name,colour = line.split(",")
                    pledgers += "{{color=#{0}}}{1}{{/color}}, ".format(colour,name)

                pledgers = pledgers[:-2]

                file.close()
            $ ylength = len(pledgers) / 22
            imagemap:
                ground im.Composite((962, ylength), (0, 0), "backgrounds/menu_ground.png")

                vbox:
                    text "[pledgers]" text_align 0.5 at credit_scroll

    imagebutton:
        pos (50,675)
        idle "buttons/menu_name_back01.png"
        hover "buttons/menu_name_back02.png"
        action If(_return == main_menu, Function(playMusic, "audio/music_title01.ogg"), Function(playMusic)), Return()

screen creditsquick() tag menu:
    add "backgrounds/menu_credits.jpg"
    imagebutton:
        idle "buttons/menu_name_back01.png"
        hover "buttons/menu_name_back02.png"
        action Return()
        xpos 50
        ypos 675

screen main_menu() tag menu:
    window:
        style "mm_root"
    add "backgrounds/menu_menu.jpg"
    add "cloud_animation" xpos 600 ypos 65
    add SnowBlossom(Animation("buttons/leaf01.png", 0.15, "buttons/leaf02.png", 0.15))
    imagemap:

        ground "backgrounds/menu_menu_overlay.png"
        idle "menu_idle"
        hover "menu_hover"

        alpha False

        hotspot ( 730, 232, 175, 48) action [ShowMenu("name_input"), Hide("main_menu")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_01.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 301, 175, 48) action [ShowMenu("load"), Hide ("gui_tooltip")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_02.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 369, 175, 48) action [ShowMenu("preferences")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_03.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 438, 175, 48) action [ShowMenu("credits"), Hide("main_menu"), SetVariable("_return", main_menu), Function(playSound), Function(playMusic, "<loop 241.5>audio/music_credits.ogg")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_04.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 507, 175, 48) action Quit(confirm=True) hovered Show("gui_tooltip", my_picture = "buttons/tooltip_05.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")

init -2:
    style mm_button:
        size_group "mm"

screen navigation() tag menu:
    imagemap:
        ground "backgrounds/menu_quickmenu.jpg"
        idle "backgrounds/menu_quickmenu.jpg"
        hover "backgrounds/menu_quickmenu2.jpg"
        hotspot ( 430, 139, 167, 40) action Return()
        hotspot ( 430, 256, 167, 40) action MainMenu()
        hotspot ( 430, 317, 167, 40) action ShowMenu("save")
        hotspot ( 430, 379, 167, 40) action ShowMenu("load")
        hotspot ( 430, 440, 167, 40) action ShowMenu("preferences")
        hotspot ( 430, 503, 167, 40) action ShowMenu("credits"), Function(playSound), Function(playMusic, "<loop 241.5>audio/music_credits.ogg")
        hotspot ( 430, 564, 167, 40) action Quit()

    key "K_ESCAPE" action Return()

screen file_picker():
    frame:
        style "file_picker_frame"

        has vbox

        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"


            for i in range(1, columns * rows + 1):


                button:
                    action FileAction(i)
                    xfill True

                    has hbox


                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

screen preferences() tag menu:
    imagemap:
        ground "backgrounds/menu_settings.jpg"
        idle "backgrounds/menu_settings.jpg"
        hover "backgrounds/menu_settings2.jpg"
        hotspot ( 430, 80, 167, 40) action Return()
        hotspot ( 404, 210, 167, 33) action Preference("display", "window")
        hotspot ( 404, 260, 167, 33) action Preference("display", "fullscreen")
        hotspot ( 404, 360, 167, 33) action Preference("skip", "all")
        hotspot ( 404, 410, 167, 33) action Preference("skip", "seen")

        bar value Preference("text speed") at Position (xpos= 404, ypos = 505, xmaximum = 220, ymaximum = 70)
        bar value Preference("music volume") at Position (xpos= 404, ypos = 580, xmaximum = 220, ymaximum = 70)
        bar value Preference("sound volume") at Position (xpos= 404, ypos = 650, xmaximum = 220, ymaximum = 70)

    if _preferences.fullscreen == True:
        add "buttons/checkbox.png" pos 603,269
    else:
        add "buttons/checkbox.png" pos 603,219

    if _preferences.skip_unseen == True:
        add "buttons/checkbox.png" pos 603,369
    else:
        add "buttons/checkbox.png" pos 603,419

screen quick_preferences tag menu:
    imagemap:
        ground "backgrounds/menu_settings.jpg"
        idle "backgrounds/menu_settings.jpg"
        hover "backgrounds/menu_settings2.jpg"
        hotspot (430, 139, 167, 40) action Return()
        hotspot (404, 270, 167, 33) action Preference("display", "window")
        hotspot (404, 320, 167, 33) action Preference("display", "fullscreen")

        bar value Preference("text speed") at Position (xpos= 404, ypos = 415, xmaximum = 220, ymaximum = 70)
        bar value Preference("music volume") at Position (xpos= 404, ypos = 502, xmaximum = 220, ymaximum = 70)
        bar value Preference("sound volume") at Position (xpos= 404, ypos = 575, xmaximum = 220, ymaximum = 70)

    if _preferences.fullscreen == True:
        add "buttons/checkbox.png" pos 603,328
    else:
        add "buttons/checkbox.png" pos 603,278

screen save() tag menu:
    imagemap:
        ground "backgrounds/menu_saving01.jpg"
        idle "backgrounds/menu_saving01.jpg"
        hover "backgrounds/menu_saving02.jpg"
        alpha False
        hotspot (288, 206, 40, 40) clicked FilePage(1)
        hotspot (347, 206, 40, 40) clicked FilePage(2)
        hotspot (406, 206, 40, 40) clicked FilePage(3)
        hotspot (464, 207, 40, 40) clicked FilePage(4)
        hotspot (523, 206, 40, 40) clicked FilePage(5)
        hotspot (581, 207, 40, 40) clicked FilePage(6)
        hotspot (640, 208, 40, 40) clicked FilePage(7)
        hotspot (699, 207, 40, 40) clicked FilePage(8)
        hotspot (134, 206, 94, 41) clicked FilePagePrevious()
        hotspot (799, 207, 95, 40) clicked FilePageNext()

        hotspot (134, 276, 227, 170) clicked FileSave(1):
            use load_save_slot(number=1)
        hotspot (401, 276, 227, 170) clicked FileSave(2):
            use load_save_slot(number=2)
        hotspot (669, 276, 227, 170) clicked FileSave(3):
            use load_save_slot(number=3)
        hotspot (134, 468, 227, 170) clicked FileSave(4):
            use load_save_slot(number=4)
        hotspot (401, 468, 227, 170) clicked FileSave(5):
            use load_save_slot(number=5)
        hotspot (669, 468, 227, 170) clicked FileSave(6):
            use load_save_slot(number=6)

        hotspot (427, 136, 174, 48) action Return()

screen load() tag menu:
    imagemap:
        ground "backgrounds/menu_loading01.jpg"
        idle "backgrounds/menu_loading01.jpg"
        hover "backgrounds/menu_loading02.jpg"
        alpha False
        hotspot (288, 206, 40, 40) clicked FilePage(1)
        hotspot (347, 206, 40, 40) clicked FilePage(2)
        hotspot (406, 206, 40, 40) clicked FilePage(3)
        hotspot (464, 207, 40, 40) clicked FilePage(4)
        hotspot (523, 206, 40, 40) clicked FilePage(5)
        hotspot (581, 207, 40, 40) clicked FilePage(6)
        hotspot (640, 208, 40, 40) clicked FilePage(7)
        hotspot (699, 207, 40, 40) clicked FilePage(8)
        hotspot (134, 206, 94, 41) clicked FilePagePrevious()
        hotspot (799, 207, 95, 40) clicked FilePageNext()

        hotspot (134, 276, 227, 170) clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (401, 276, 227, 170) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (669, 276, 227, 170) clicked FileLoad(3):
            use load_save_slot(number=3)
        hotspot (134, 468, 227, 170) clicked FileLoad(4):
            use load_save_slot(number=4)
        hotspot (401, 468, 227, 170) clicked FileLoad(5):
            use load_save_slot(number=5)
        hotspot (669, 468, 227, 170) clicked FileLoad(6):
            use load_save_slot(number=6)

        hotspot (427, 136, 174, 48) action Return()

screen load_save_slot:
    $ file_text = "% 2s. %s\n%s" % (
                        FileSlotName(number, 6),
                        FileTime(number),
                        FileSaveName(number))

    add FileScreenshot(number)
    text file_text
    if FileLoadable(number):
        imagebutton idle "buttons/delete_button_01.png" hover "buttons/delete_button_01b.png" action FileDelete(number)
    key "save_delete" action FileDelete(number)

init -2 python:
    config.thumbnail_width = 223
    config.thumbnail_height = 165    

screen yesno_prompt(message, yes_action, no_action):
    modal True

    window:
        style "gm_root"

    if message == layout.DELETE_SAVE or message == layout.OVERWRITE_SAVE:
        add "backgrounds/menu_confirm.jpg"

    imagemap:
        ground "menu_ground"
        idle "menu_quit_idle"
        hover "menu_quit_hover"

        alpha False


        hotspot ( 312, 463, 175, 48) action yes_action
        hotspot ( 530, 463, 175, 48) action no_action

    if message == layout.QUIT or message == layout.MAIN_MENU:
        text "{a=http://www.patreon.com/summertimesaga}http://www.patreon.com/summertimesaga{/a}" at Position (xpos= 360, ypos = 640)


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen quick_menu():
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Return()
        textbutton _("Hide") action HideInterface()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button is default:

        background None
        xpadding 5

    style quick_button_text is default:

        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

screen popup_unfinished:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_unfinished")

    key "K_SPACE" action Hide("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.5)
        idle "boxes/popup_unfinished.png"
        action Hide("popup_unfinished")

screen button(Image, Label):
    imagebutton:
        align (0.5,0.97)
        idle str(Image) + ".png"
        hover str(Image) + "b.png"
        action Hide("button"), Jump(Label)

screen sex_anim_buttons:
    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover "buttons/anim_02b.png"
        else:
            idle "buttons/anim_01.png"
            hover "buttons/anim_01b.png"
        action [
            If(
                anim_toggle,
                SetVariable("anim_toggle", False),
                SetVariable("anim_toggle", True)
            ),
            Return
        ]

screen sex_xray_anim_buttons:
    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover "buttons/anim_02b.png"
        else:
            idle "buttons/anim_01.png"
            hover "buttons/anim_01b.png"
        action [
            If(
                anim_toggle,
                SetVariable("anim_toggle", False),
                SetVariable("anim_toggle", True)
            ),
            Return
        ]

    imagebutton:
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover "buttons/anim_03b.png"
        else:
            idle "buttons/anim_04.png"
            hover "buttons/anim_04b.png"
        action [
            If(
                xray, 
                SetVariable("xray", False), 
                SetVariable("xray", True)
            )
        ]

screen popup_savegame:

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action MainMenu(False)
    imagebutton:
        idle "boxes/popup_save.png"
        action MainMenu(False)
        xpos 218
        ypos 214

label bad_savegame:
    call screen popup_savegame

screen escape_key:
    key "K_ESCAPE" action ShowMenu("navigation")