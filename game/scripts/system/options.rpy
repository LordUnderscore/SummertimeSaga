init -1 python hide:


    config.developer = False
    config.rollback_enabled = False
    config.screen_width = 1024
    config.screen_height = 768
    config.framerate = 60
    config.window_title = u"SummertimeSaga"

    theme.roundrect(
        widget = "#8833ce",
        widget_hover = "#cd249b",
        widget_text = "#000000",
        widget_selected = "#b6d754",
        disabled = "#57cdff",
        disabled_text = "#717be5",
        label = "#000000",
        frame = "#04b4ff",
        mm_root = "backgrounds/menu_menu.jpg",
        gm_root = "backgrounds/menu_quit.jpg",
        rounded_window = False,
    )

    style.window.background = Frame("boxes/dialogue_chatbox.png", 12, 12)
    style.window.left_margin = 0
    style.window.right_margin = 0
    style.window.top_margin = 0
    style.window.bottom_margin = 0
    style.window.left_padding = 80
    style.window.right_padding = 80
    style.window.top_padding = 20
    style.window.bottom_padding = 20
    style.window.yminimum = 122
    style.default.size = 15
    style.default.drop_shadow = [(1, 1)]
    config.has_sound = True
    config.has_music = True
    config.has_voice = False
    config.main_menu_music = "audio/music_title01.ogg"
    config.help = "README.html"
    config.enter_transition = None
    config.exit_transition = None
    config.intra_transition = None
    config.main_game_transition = None
    config.game_main_transition = None
    config.end_splash_transition = None
    config.end_game_transition = None
    config.after_load_transition = None
    config.window_show_transition = None
    config.window_hide_transition = None
    config.adv_nvl_transition = dissolve
    config.nvl_adv_transition = dissolve
    config.enter_yesno_transition = None
    config.exit_yesno_transition = None
    config.enter_replay_transition = None
    config.exit_replay_transition = None
    config.say_attribute_transition = None

python early:
    config.name = "SummertimeSaga"
    config.version = "0.14.30"
    config.save_directory = str(config.name) + "-" + str(config.version)

init -1 python hide:
    config.default_fullscreen = False
    config.default_text_cps = 0
    config.default_afm_time = 10
    style.menu_choice_button.background = Frame("buttons/dialogue_choice1.png",28,9)
    style.menu_choice_button.hover_background = Frame("buttons/dialogue_choice1b.png",28,9)
    style.menu_choice_button.yminimum = 30
    style.menu_choice_button.xminimum = 500
    style.menu_choice.color = "#ffffff"
    style.menu_choice.size = 16
    style.menu_choice.drop_shadow = [(1, 1)]

init python:
    build.archive("audio", "all")
    build.archive("images", "all")
    build.archive("scripts", "all")
    build.archive("secret", "all")
    build.directory_name = str(config.name) + "-" + str(config.version)
    build.executable_name = config.name
    build.include_update = False
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/secret/**.**', 'secret')
    build.classify('game/**.ogg', 'audio')
    build.classify('game/**.rpy', None)
    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/scripts/**.txt', 'scripts')
    build.documentation('*.html')
    build.documentation('*.txt')