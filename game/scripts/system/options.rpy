init -1 python hide:


    config.developer = False
    config.rollback_enabled = False
    config.screen_width = 1024
    config.screen_height = 768
    config.framerate = 60
    config.window_title = u"SummertimeSaga"
    config.search_prefixes = [ "", "images/", ]

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
    config.version = "0.14.51"
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
    build.directory_name = str(config.name) + "-" + str(config.version)
    build.executable_name = config.name
    build.include_update = False
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/hide/**', None)
    build.classify('game/**.ogg', 'audio')
    build.classify('game/**.rpy', None)
    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/scripts/**.txt', 'scripts')
    build.documentation('*.html')
    build.documentation('*.txt')

init python:
    class Wrapped(object):
        def __init__(self,file_obj,name,pattern=0xdeadbeef):
            self._file = file_obj
            self._name = name
            self._pattern = bytearray(4096)
            self._loc = 0
            seed = pattern
            a = 1103515245
            c = 12345
            m = 2**31-1
            for i in xrange(0,4096,4): 
                seed = (a*seed+c) % m
                self._pattern[i] = seed & 0xff
                self._pattern[i+1] = (seed >>8) & 0xff
                self._pattern[i+2] = (seed >> 16) & 0xff
                self._pattern[i+3] = (seed >> 24) & 0xff
        def read(self,*args,**kwargs):
            ba = bytearray(self._file.read(*args,**kwargs))
            length = len(ba)
            start = self._loc % 4096
            for i in xrange(0,length):
                ba[i] = ba[i] ^ self._pattern[start]
                start += 1
                start = start % 4096
            self._loc += length
            return str(ba)
        def seek(self,offset,whence=0):
            if whence==0:
                self._loc = offset
            elif whence == 1:
                self._loc += offset
            else:
                raise Exception("Unable to seek relative to end of file")
            return self._file.seek(offset,whence)
        def __getattr__(self, attr):
            if attr == 'length' or attr == 'base':
                raise AttributeError
            return getattr(self._file, attr)
    import hashlib
    import os
    def create_extras(name):
        if name[:8] != 'private/':
            raise Exception("Can only create extras from private resources")
        if name[-4] == '.':
            fn=name[8:-4]
            ext=name[-4:]
        else:
            fn=name[8:]
            ext=''
        hashname = hashlib.md5(fn).hexdigest()
        new_fn = os.path.join(config.basedir,'game','images','extras',hashname+ext)
        print "Creating {} from {}".format(new_fn,fn+ext)
        fio = Wrapped(renpy.file('hide/'+fn+ext),fn+ext)
        out = open(new_fn,'wb')
        while True:
            piece = fio.read(4096)
            if not piece:
                break
            out.write(piece)
        out.close()
        fio.close()

    def update_extras(dir_name=None):
        if dir_name is None:
            base_name = os.path.join(config.basedir,'game','hide')
        else:
            base_name = os.path.join(config.basedir,'game','hide',dir_name)
        
        
        for f in os.listdir(base_name):
            if os.path.isfile(os.path.join(base_name,f)):
                create_extras("private/"+dir_name+"/"+f)
            else: 
                if dir_name is None:
                    update_extras(f)
                else:
                    update_extras(dir_name+'/'+f)

    def our_file_loader(name):
        if name[:8] == 'private/':
            if name[-4] == '.':
                fn = name[8:-4]
                ext = name[-4:]
            else:
                fn=name[8:]
                ext=''
            hashname = hashlib.md5(fn).hexdigest()
            new_fn = 'extras/'+hashname+ext
            try:
                rv= Wrapped(renpy.file(new_fn),new_fn)
                return rv
            except IOError:
                if config.developer:
                    return renpy.file('hide/'+fn+ext)
                else:
                    return None
        return None

    config.file_open_callback = our_file_loader