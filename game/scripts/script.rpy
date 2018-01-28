init python:
    import datetime

    config.keymap["game_menu"].remove("K_ESCAPE")
    config.debug_sound = True
    renpy.music.register_channel("music2", "music", True)
    renpy.music.register_channel("music3", "music", True)
    renpy.music.register_channel("sound2", "sfx", True)
    renpy.music.register_channel("sound3", "sfx", True)

label splashscreen:
    $ gTimer = DayTimer()
    scene black

    show splash_logo with dissolve
    $ renpy.pause(1)

    scene black with dissolve
    $ renpy.pause(1, hard=True)

    scene splash
    show expression "buttons/menu_yes.png" at Position(xpos=491, ypos=685)
    show expression "buttons/menu_no.png" at Position(xpos=621, ypos=684)
    with dissolve

    $ callScreen("Adult Warning", False, False)













    scene black with dissolve
    $ renpy.pause(1, hard=True)

    return

init python:
    savegame_version_required = config.version
    def check_savegame():
        try:
            savegame_version
        except NameError:
            renpy.jump('bad_savegame');
        else:
            if savegame_version != savegame_version_required:
                renpy.jump('bad_savegame');

    config.after_load_callbacks = [check_savegame]


init python:
    location_count = "Bedroom"

init python:
    timer_range = 0
    timer_jump = 0
    if "K_LCTRL" in config.keymap["fast_skip"]:
        config.keymap['fast_skip'].remove("K_LCTRL")
    if "K_LCTRL" not in config.keymap["skip"]:
        config.keymap['skip'].append("K_LCTRL")
    class Good:
        def __init__(self, price, status, passive, image="", passive_pic = ""):
            self.price = price
            self.status = status
            self.passive = passive
            self.image = image
            self.passive_pic = passive_pic
        
        def change_passive(self):
            self.passive = True

    def good_reset():
        for Good in item_list:
            Good.passive = False

    def rotten_good_reset():
        for Good in rotten_list:
            Good.passive = False

    def upgrade_garden():
        for Good in item_list:
            if Good in bad_list:
                Good.price += 5
        item_list.append(earwig01)
        bad_list.append(earwig01)
        earwig01.price += 15
        earwig01.passive_pic = "objects/minigame01_number08.png"
        rat.passive_pic = "objects/minigame01_number08.png"
        pumpkin.passive_pic = "objects/minigame01_number03.png"
        tomato.passive_pic = "objects/minigame01_number03.png"
        bug.passive_pic = "objects/minigame01_number03.png"
        weed.passive_pic = "objects/minigame01_number07.png"
        spider.passive_pic = "objects/minigame01_number07.png"
        grapes.passive_pic = "objects/minigame01_number03.png"

    def Sleep():
        global aunt_dialogue_advance
        global aunt_count
        if aunt_dialogue_advance == True:
            aunt_dialogue_advance = False
            aunt_count += 1
        
        global sis_dialogue_advance
        global sis_bedroom_count
        if sis_dialogue_advance and sis_bedroom_count < 2:
            sis_dialogue_advance = False
            sis_bedroom_count += 1
        
        global diary_scene
        diary_scene = False
        
        global left_hall_dialogue_advancement
        global left_hall_dialogue_count
        if left_hall_dialogue_advancement:
            left_hall_dialogue_advancement = False
            left_hall_dialogue_count += 1
        
        global pizza_dialogue_advance
        global pizza_count
        if pizza_dialogue_advance:
            pizza_dialogue_advance = False
            pizza_count += 1
        
        global player_mail
        if renpy.random.randint(0,4) != 0:
            player_mail = [renpy.random.choice(player_mailbox_items)]
        
        global erik_mail
        if renpy.random.randint(0,4) != 0:
            erik_mail = [renpy.random.choice(erik_mailbox_items)]
        
        global mia_mail
        if renpy.random.randint(0,4) != 0:
            mia_mail = [renpy.random.choice(mia_mailbox_items)]
        
        global gTimer
        global erik_drunk
        global judith_daylock
        global training_done
        global masturbated_tv
        global moms_panties_taken
        global roxxy_shower_lock
        global mrsj_filled
        global erik_funky
        gTimer.sleep()
        erik_drunk = False
        judith_daylock = False
        training_done = False
        masturbated_tv = False
        moms_panties_taken = False
        roxxy_shower_lock = False
        mrsj_filled = False
        erik_funky = False
        
        global orcette_mail_lock
        if gTimer.dayOfWeek() == "Tue" and erik.completed(erik_orcette):
            orcette_mail_lock = True
        
        global random_message
        random_message = renpy.random.randint(0,9)
        
        global judith_sex_sequence_unlocked
        global m_judith01
        global message_list
        global new_message
        if judith_sex_sequence_unlocked and m_judith01 not in message_list:
            if random_message == 9:
                message_list.append(m_judith01)
                new_message = True
        
        global erik_telescope_random
        global erikmom_telescope_random
        global mia_telescope_random
        erik_telescope_random = renpy.random.randint(0,1)
        erikmom_telescope_random = renpy.random.randint(0,2)
        mia_telescope_random = renpy.random.randint(0,1)
        
        global tick_skip_active
        tick_skip_active = True
        
        global rump_n_cunt
        if not gTimer.is_weekend():
            rump_n_cunt = randomizer()
        else:
            rump_n_cunt = 0
        
        global Machine
        for event in store.my_events:
            event.complete_events()
        Machine.trigger(T_all_sleep)
        
        global location_count
        global M_player
        if location_count == "Bedroom":
            M_player.set("just wokeup", True)
        
        global M_mom
        M_mom.set("room sneak", False)
        M_mom.set("movie night", False)
        M_mom.set("location random", choice_randomizer([("bedroom", 1), ("kitchen", 3), ("basement", 3)]))
        M_mom.set("time random", choice_randomizer([(gTimer.is_morning, 1), (gTimer.is_afternoon, 2)]))
        
        global shower
        shower.randomize()


    class ShowerClass:
        _name = ""
        
        def occupied(self, name = "", morning_check = True):
            if name == "":
                if name == self._name:
                    return True
                else:
                    return where_is(self._name) != "Shower"
            elif morning_check:
                return where_is(name) == "Shower" and gTimer.is_morning()
            else:
                return where_is(name) == "Shower"
        
        def check(self, name, morning_check = True):
            if morning_check:
                return self._name == name and gTimer.is_morning()
            else:
                return self._name == name
        
        def unoccupy(self):
            self._name = ""
        
        def randomize(self):
            self._name = choice_randomizer([("mom", 2), ("sis", 3), ("", 1)])

    class DayTimer:
        _tod = 1
        _dow = 0
        _game_day = 0
        weekdays = (
            'Mon',
            'Tue',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun',
            )
        weekdays_long = (
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
            )
        
        def is_morning(self):
            return self._tod == 1
        
        def is_afternoon(self):
            return self._tod == 2
        
        def is_evening(self):
            return self._tod == 3
        
        def is_night(self):
            return self._tod == 4
        
        def is_dark(self):
            return self._tod >= 3
        
        def image(self, name, layer = "master"):
            import re
            if not re.search('\{}', name):
                name = name + '{}'
            if self.is_dark():
                name = name.replace("_day", "")
                if self.is_evening(): 
                    tmp = name.format("_evening") 
                    if renpy.can_show(tmp, layer): 
                        return tmp 
                    if renpy.loadable(tmp): 
                        return tmp 
                tmp = name.format("_night")
                if renpy.can_show(tmp, layer):
                    return tmp
                if renpy.loadable(tmp):
                    return tmp
                return name.format("_n")
            else:
                return name.format("")
        
        def is_weekend(self):
            return self._dow == 5 or self._dow ==6
        
        def dayOfWeek(self,full=False):
            if full:
                return self.weekdays_long[self._dow]
            else:
                return self.weekdays[self._dow]
        
        def gameDay(self):
            return self._game_day
        
        def tick(self,tod=None):
            if tod:
                self._tod = tod
            elif self._tod < 4:
                self._tod += 1
            tele_rand()
        
        def sleep(self):
            self._tod = 1
            self._dow = (self._dow +1) % 7
            self._game_day += 1
        
        def __repr__(self):
            if self._tod == 1:
                tod = "morning"
            elif self._tod == 2:
                tod = "afternoon"
            elif self._tod == 3:
                tod = "evening"
            else:
                tod = "night"
            return self.dayOfWeek(True)+" "+tod+" day "+str(self._game_day)

    def where_is(name):
        loc_logic = {
            "mom": [
                "Entrance", ["M_mom.get_state() == S_mom_debt_collectors",
                             "M_mom.get_state() == S_mom_vacuum_help and M_mom.is_set('chores') and not gTimer.is_dark()",
                             "M_mom.get_state() == S_mom_movie_night and gTimer.is_evening()",
                            ],
                "Home Front", "M_mom.get_state() == S_mom_mrsj_visit",
                "Living Room", "M_mom.get_state() == S_mom_romance_movie",
                "Cupid", "M_mom.get_state() in [S_mom_choose_gift, S_mom_show_necklace]",
                "Cupid Dressroom", "M_mom.get_state() == S_mom_dressing_room",
                "Backyard", "M_mom.get_state() == S_mom_fetch_towel",
                "Mom's Bedroom", ["gTimer.is_dark()",
                                  
                                  "M_mom.get_state() == S_mom_spy",
                                  "M_mom.get('sex available') and M_mom.get('location random') == 'bedroom' and M_mom.get('time random')()",
                                  ],
                "Basement", ["gTimer.is_afternoon()",
                             "M_mom.get_state() == S_mom_wash_clothes",
                             "M_mom.get_state() in [S_mom_laundry_help, S_mom_lotion_adventure] and not gTimer.is_dark()",
                             "M_mom.get_state() == S_mom_fetch_laundry",
                            ],
                "Shower", ["shower.check('mom') and M_mom.is_set('shower random')",
                           "shower.check('mom') and M_mom.get_state() in [S_mom_shower_peek, S_mom_shower_peek_after, S_mom_shower_walk_in]"
                          ],
                "Kitchen", ["gTimer.is_morning()",
                            "M_mom.get_state() == S_mom_debt_call",
                           ],
                None, "True",
                ],
            "sis": [
                None, ["sis_bedroom_count == 0",
                       "diary_scene and sis_dialogue_advance and sis_diary_unlocked and not gTimer.is_dark()"],
                "Dining Room", ["gTimer.is_morning() and sister.started(sis_breakfast)",
                                "gTimer.is_morning() and not shower.check('sis', False) and sister.over(sis_telescope01) and not sister.over(sis_breakfast)",
                                ],
                None, ["M_mom.get_state() in [S_mom_sis_check, S_mom_close_valve, S_mom_pipe_check]",
                       "M_mom.get_state() == S_mom_fix_pipe and not gTimer.is_dark()",
                      ],
                "Shower", "shower.check('sis')",
                "Sis' Bedroom", "True",
                ],
            "erik": [
                "Erik's Basement Backroom", "mrsj_afterpoker_fun",
                "Erik's Basement", ["erik.over(erik_intro) and not erik.known(erik_card_hunt)",
                                    "erik.over(erik_crown_card) and not erik.known(erik_orcette)",
                                    "erik.completed(erik_bullying_3) and not erik.known(erik_vr)",
                                    "gTimer.is_dark() and poker_bot02 != ''",
                                    ],
                "Mrs Johnson's Room", ["mrsj.over(mrsj_yoga_help_2) and not erik.over(erik_breastfeeding_2)",
                                       "erik.in_progress(erik_sex_ed)",
                                       "gTimer.is_dark() and mrsj.over(mrsj_sex_ed)",
                                       ],
                "Erik's Room", ["erik.known(erik_card_hunt) and (not gTimer.is_morning() or gTimer.is_weekend())",
                                "erik.known(erik_bullying) and not erik.known(erik_bullying_2)",
                                "erik.over(erik_path_split) and erik.started(erik_sex_ed)",
                                "mrsj.started(mrsj_sex_ed)",
                                ],
                "Computer Lab", "erik.completed(erik_gf_2) and gTimer.is_morning()",
                "Cafeteria", "gTimer.is_morning()",
                None, "True",
                ],
            "mrsj": [
                "Erik's Basement Backroom", "mrsj_afterpoker_fun",
                "Erik's Basement", "gTimer.is_dark() and poker_bot02 == 'erik_mom'",
                "Mrs Johnson's Room", ["gTimer.is_dark() and erik.over(erik_breastfeeding)",
                                       "mrsj.over(mrsj_yoga_help_2) and not erik.over(erik_breastfeeding_2)",
                                       "mrsj.over(erik_breastfeeding_2) and not erik.over(erik_thief_2)",
                                       "erik.over(erik_path_split) and erik.known(erik_sex_ed) and not mrsj.completed(mrsj_sex_ed)",
                                       ],
                "Erik's House Entrance", ["gTimer.is_morning()",
                                          "erik.over(erik_vr) and not mrsj.completed(mrsj_yoga_help)",
                                          ],
                "Yoga Room", "gTimer.is_afternoon()",
                None, "True",
                ],
            "june": [
                "Erik's Room", "gTimer.is_afternoon() and erik.completed(erik_gf_2)",
                "Bedroom", "gTimer.is_evening() and June.known(june_mc_help_2) and june_hang_out",
                "Computer Lab", "gTimer.is_morning() or gTimer.is_afternoon()",
                None, "True",
                ],
            "anna": [
                "Yoga Room", "gTimer.is_evening() and mrsj.known(mrsj_yoga_help)",
                "Park", "Anna.over(anna_intro) and not gTimer.is_dark() and not Anna.completed(anna_missing_pup)",
                None, "True",
                ],
            "roz": [
                "Hospital", "not Roz.started(roz_trick)",
                None, "True",
                ],
            "crystal": [
                "Trailer Interior", "not gTimer.is_dark()",
                None, "True",
                ],
            "grace": [
                "Tattoo Parlor Interior", "not gTimer.is_dark()",
                None, "True",
                ],
            "angelica": [
                "Angelica's Room", "gTimer.is_dark()",
                "Church", "not (gTimer.is_weekend() and gTimer.is_morning())",
                None, "True",
                ],
            "mia": [
                None, "M_mia.get_state() in [S_mia_unexpected_visit, S_mia_helen_outfit_request] and not gTimer.is_morning()",
                "Tattoo Parlor Interior", "M_mia.get_state() in [S_mia_get_tattoo, S_mia_buy_tattoo] and gTimer.dayOfWeek() == 'Sat'",
                "Church", "gTimer.is_morning() and gTimer.is_weekend()",
                "Science Classroom", "gTimer.is_morning()",
                "Helen's Locked Room", "M_mia.get_state() in [S_mia_midnight_help, S_mia_locked_room] and gTimer.is_dark()",
                "Mia's Bedroom", "gTimer.is_dark()",
                "Mia's House", "M_mia.get_state() == S_mia_do_homework",
                "Mia's House Entrance", "gTimer.is_afternoon()",
                None, "True",
                ],
            "helen": [
                "Angelica's Room", ["gTimer.is_dark() and M_mia.get_state() in [S_mia_angelicas_order, S_mia_angelicas_whip]",
                                    "gTimer.is_dark() and M_mia.is_set('helen angelica training 2')",
                                    ],
                "Church Confessional Left", "M_mia.get_state() == S_mia_priest_act",
                "Church", "gTimer.is_morning() and gTimer.is_weekend()",
                "Mia's House Entrance", "gTimer.is_morning()",
                "Helen's Bedroom", ["gTimer.is_afternoon()",
                                    "gTimer.is_dark() and M_mia.is_set('harold left')",
                                    "M_mia.get_state() in [S_mia_unexpected_visit, S_mia_helen_outfit_request]"],
                "Mia's Living Room", "gTimer.is_dark()",
                None, "True",
                ],
            "harold": [
                None, "M_mia.get_state() == S_mia_harold_yumi_out",
                "Hill", "M_mia.get_state() in [S_mia_urgent_help, S_mia_clues, S_mia_search_desk, S_mia_find_harold, S_mia_harold_found_news, S_mia_angelicas_patience]",
                "Church", "gTimer.is_morning() and gTimer.is_weekend() and not M_mia.is_set('harold left')",
                "Police Office", "not gTimer.is_dark()",
                "Mia's Living Room", "gTimer.is_dark() and not M_mia.is_set('harold left')",
                None, "True",
                ],
            "yumi": [
                None, "M_mia.get_state() == S_mia_harold_yumi_out",
                "Police Basement Cell", "M_mia.get_state() in [S_mia_inmate_status, S_mia_harold_backup, S_mia_harold_to_the_rescue]",
                "Police Basement", "gTimer.is_morning() or gTimer.is_afternoon()",
                None, "True",
                ],
            "earl": [
                None, "M_mia.get_state() in [S_mia_inmate_status, S_mia_harold_backup, S_mia_harold_to_the_rescue]",
                "Police Office", "True",
                ],
            "dexter": [
                "Basket Ball Court", "not gTimer.is_dark()",
                None, "True",
                ],
            "terry": [
                None, "M_terry.get_state() == S_terry_drunk",
                "Pier", "True",
                ],
            "aqua": [
                "Lair", "M_aqua.is_set('altar pass') and M_aqua.is_set('treasure pass') and M_aqua.is_set('squid pass') and M_aqua.is_set('maze pass')",
                None, "True",
                ],
            }
        default = None
        for m in machines:
            if m._name == name:
                default = m.where()
                if m.forced():
                    return default
        logic_list = loc_logic[name]
        for idx in xrange(0,len(logic_list),2):
            loc = logic_list[idx]
            logic_tests = logic_list[idx+1]
            
            
            if isinstance(logic_tests,basestring):
                logic_tests = [logic_tests,]
            for logic in logic_tests:
                if eval(logic):
                    return loc
        return default

    def is_here(name):
        return where_is(name) == location_count

    def lock_ui():
        global ui_lock
        ui_lock = True


    def unlock_ui():
        global ui_lock
        ui_lock = False


    def ui_locked():
        global ui_lock
        return ui_lock

    def callScreen(name, ui = True, clear = True, newContext = False):
        renpy.hide_screen("ui")
        if clear:
            clearImages()
        if gTimer.is_night() and name in ["Lair"]:
            name = "Town Map"
            ui = True
        name = name.lower()
        name = name.replace("'", "")
        name = name.replace(" ", "_")
        
        if newContext:
            renpy.call("newScreen", screen = name, user = ui, images = clear)
        elif ui:
            renpy.show_screen(name)
            renpy.call_screen("ui")
        else:
            renpy.call_screen(name)

    def hideScreen(name):
        name = name.lower()
        name = name.replace("'", "")
        name = name.replace(" ", "_")
        renpy.hide_screen("ui")
        renpy.hide_screen(name)

    def clearImages():
        for VisibleImage in renpy.get_showing_tags():
            renpy.hide(VisibleImage)

    def playSound(name = "", fade = 0.7, loop = True, multi = False):
        if name == "":
            renpy.music.stop("sound", fadeout = fade)
            renpy.music.stop("sound2", fadeout = fade)
            renpy.music.stop("sound3", fadeout = fade)
        elif renpy.sound.get_playing("sound") == name or renpy.sound.get_playing("sound2") == name or renpy.sound.get_playing("sound3") == name:
            return True
        elif not renpy.music.is_playing("sound") and renpy.sound.get_playing("sound") != name:
            if multi == False:
                renpy.music.stop("sound2", fadeout = fade)
                renpy.music.stop("sound3", fadeout = fade)
            renpy.music.play(name, "sound", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("sound2") and renpy.sound.get_playing("sound2") != name:
            if multi == False:
                renpy.music.stop("sound", fadeout = fade)
                renpy.music.stop("sound3", fadeout = fade)
            renpy.music.play(name, "sound2", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("sound3") and renpy.sound.get_playing("sound3") != name:
            if multi == False:
                renpy.music.stop("sound", fadeout = fade)
                renpy.music.stop("sound2", fadeout = fade)
            renpy.music.play(name, "sound3", loop = loop, fadein = fade)

    def getPlayingSound(name):
        if renpy.sound.get_playing("sound") == name or renpy.sound.get_playing("sound2") == name or renpy.sound.get_playing("sound3") == name:
            return False
        return True

    def playMusic(name = "", fade = 0.7, loop = True, multi = False):
        if name == "":
            renpy.music.stop("music", fadeout = fade)
            renpy.music.stop("music2", fadeout = fade)
            renpy.music.stop("music3", fadeout = fade)
        elif renpy.music.get_playing("music") == name or renpy.music.get_playing("music2") == name or renpy.music.get_playing("music3") == name:
            return True
        elif not renpy.music.is_playing("music") and renpy.music.get_playing("music") != name:
            if multi == False:
                renpy.music.stop("music2", fadeout = fade)
                renpy.music.stop("music3", fadeout = fade)
            renpy.music.play(name, "music", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("music2") and renpy.music.get_playing("music2") != name:
            if multi == False:
                renpy.music.stop("music", fadeout = fade)
                renpy.music.stop("music3", fadeout = fade)
            renpy.music.play(name, "music2", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("music3") and renpy.music.get_playing("music3") != name:
            if multi == False:
                renpy.music.stop("music", fadeout = fade)
                renpy.music.stop("music2", fadeout = fade)
            renpy.music.play(name, "music3", loop = loop, fadein = fade)

    def getPlayingMusic(name):
        if renpy.music.get_playing("music") == name or renpy.music.get_playing("music2") == name or renpy.music.get_playing("music3") == name:
            return False
        return True

    def randomizer(name = "", start = 0, end = 99):
        import re
        rand = renpy.random.randint(start, end)
        if name == "":
            return rand
        if not re.search('\{}', name):
            name = name + '{}'
        tmp = name.format(rand)
        return tmp

    def choice_randomizer(list):
        import random
        r = random.uniform(0, sum([v[1] for v in list]))
        s = 0.0
        for k, w in list:
            s += w
            if r < s:
                return k
        return k

    def sfxDoor(locked = False):
        if not locked:
            tmp = randomizer("audio/sfx_door1_{}.ogg", 1, 2)
        else:
            tmp = randomizer("audio/sfx_door1_lock{}.ogg", 1, 2)
        return tmp

















define chr_warn = "{color=#b61c1c}{b}[CHR]: {/b}{/color}"
define str_warn = "{color=#b61c1c}{b}[STR]: {/b}{/color}"
define dex_warn = "{color=#b61c1c}{b}[DEX]: {/b}{/color}"
define int_warn = "{color=#b61c1c}{b}[INT]: {/b}{/color}"
define chr_pass = "{color=#00ff00}{b}[CHR]: {/b}{/color}"
define str_pass = "{color=#00ff00}{b}[STR]: {/b}{/color}"
define dex_pass = "{color=#00ff00}{b}[DEX]: {/b}{/color}"
define int_pass = "{color=#00ff00}{b}[INT]: {/b}{/color}"
define fastdissolve = Dissolve(.2)

define mom = Character("[mom_char_name]", color="#b96dff")
define sis = Character("[sis_char_name]", color="#ff6df0")
define eri = Character("Erik", color="#56aaff")
define rox = Character("Roxxy", color="#c8ffc8")
define mia = Character("Mia", color="#c499ff")
define erimom = Character("Mrs. Johnson", color="#c8ffc8")
define mon = Character("Monster Girl", color="#c8ffc8")
define dex = Character("Dexter", color="#c8ffc8")
define ron = Character("Ronda", color="#c8ffc8")
define bri = Character("Coach Bridget", color="#c8ffc8")
define smi = Character("Principal Smith", color="#c8ffc8")
define bis = Character("Mrs. Bissette", color="#c8ffc8")
define eve = Character("Eve", color="#c8ffc8")
define dia = Character("Aunt Diane", color="#c8ffc8")
define mas = Character("Master Somrak", color="#c8ffc8")
define ton = Character("Tony", color="#c8ffc8")
define cam = Character("Camilla", color="#c8ffc8")
define igo = Character("Igor", color="#c8ffc8")
define hen = Character("Henchman", color="#c8ffc8")
define lar = Character("Larry", color="#c8ffc8")
define sus = Character("Susan", color="#c8ffc8")
define gin = Character("Nurse Ginger", color="#c8ffc8")
define jud = Character("Judith", color="#c8ffc8")
define ann = Character("Annie", color="#c8ffc8")
define cas = Character("Cassie", color="#c8ffc8")
define jan = Character("Jane", color="#c8ffc8")
define kev = Character("Kevin", color="#c8ffc8")
define liu = Character("Banker", color="#c8ffc8")
define martinez = Character("Martinez", color="#c8ffc8")
define lopez = Character("Lopez", color="#c8ffc8")
define ross = Character("Ms. Ross", color="#c8ffc8")
define dewitt = Character("Ms. Dewitt", color="#c8ffc8")
define okita = Character("Ms. Okita", color="#c8ffc8")
define june = Character("June", color="#a771b6")
define beth = Character("Beth", color="#ce6b6a")
define sara = Character("Sara")
define aqua = Character("Aqua")
define ced = Character("Cedric")
define chi = Character("Chico")
define helen = Character("Helen")
define harold = Character("Harold")
define ivy = Character("Ivy")
define vero = Character("Veronica")
define awesomo = Character("Dog")
define rump = Character("Mayor Rump")
define tony = Character("Tony")
define maria = Character("Maria")
define tonymaria = Character ("Tony and Maria")
define Mr.Sato = Character("Mr. Sato")
define Josephine = Character ("Josephine")
define henchman2 = Character ("Henchmen")
define chad = Character("Chad")
define tyrone = Character("Tyrone")
define Terry = Character("Terry")
define poker_sayer02 = Character("Bot")
define anna = Character("Anna")
define bub = Character("Mr. Bubbles")
define ang = Character("Sister Angelica")
define ear = Character("Earl")
define yum = Character("Yumi")
define tati = Character("Tatiana")
define iwanka = Character("Iwanka")
define becca = Character("Becca")
define missy = Character("Missy")
define micoe = Character("Micoe")
define thief = Character("Thief")
define larry = Character("Larry")
define crys = Character("Crystal")
define grace = Character("Grace")
define roz = Character("Roz")
define guard = Character("Guard")
define jaing = Character("Jiang")
define Kass = Character("Kass")
define cat = Character("Cat")

define player_name = Character('[firstname]', color="#6f96f1")

define flash = Fade(.25, 0.0, .75, color="#fff")

init python:
    firstname = ""
    sis_pass = ""
    sis_name = "Sis"
    sis_char_name = "Jenny"
    MC_pass = ""
    mom_name = "Mom"
    mom_char_name = "Debbie"
    cat_name = ""
    pink_user = ""
    pink_pass = ""
    egay_search = ""

    def name_func(newstring):
        store.firstname = newstring

    def sis_comp(newstring):
        store.sis_pass = newstring

    def sister_name(newstring):
        store.sis_char_name = newstring

    def MC_comp(newstring):
        store.MC_pass = newstring

    def mother_name(newstring):
        store.mom_char_name = newstring

    def stray_cat_name(newstring):
        store.cat_name = newstring

    def pink_channel_user(newstring):
        store.pink_user = newstring

    def pink_channel_pass(newstring):
        store.pink_pass = newstring

    def egay_search_string(newstring):
        store.egay_search = newstring


init python:
    cheat_mode = False
    cheat_pass = False
    event_wait_till = 999999
    rump_n_cunt = 0
    anim_toggle = False
    tick_skip_active = False
    ui_lock = True
    hallway_count= 0
    mia_count = 0
    sis_shower_count = 0
    mom_count = 0
    map_status_count = 0
    school_count = 0
    gym_count = 0
    classroom_count = 0
    closed_valve = 0
    training_done = False
    masturbated_tv = False
    sis_lastwebcam_show_seen = False
    sis_watch_tv_tonight = False
    june_hang_out = False
    mrsj_filled = False
    erik_funky = False

    kitchen_count = 0
    training_count = 0
    classroom_door_count = 0
    courtyard_door_count = 0
    left_hall_dialogue_count = 0
    left_hall_dialogue_advancement = False
    left_hall_count = 0
    locker_room_count = 0
    shower_door_count = 0
    stairs_count = 0
    stairs_dialogue_count = 0
    office_count = 0
    desk03_count = 0
    desk04_count = 0
    wearing_jersey_count = 1
    bed_locked = 0
    sis_bedroom_count = 0
    sis_door_locked_count = 0
    bedtable01_count = 0
    event_outside_school_count = 0
    mall_count = 0
    mia_house_count = 0
    park_count = 0
    erik_door_count = 0
    library_count = 0
    pool_count = 0
    poolrules_count = 0
    bank_count = 0
    computer_count = 0
    changing_count = 0
    backroom_count = 0
    lockershowers_count = 0
    library_desk_count = 0
    almost_drowned = False
    first_swim = True
    medic_dialogue_count = 0
    cafeteria_count = 0
    backroom_blocked_count = 0
    backroom_count = 0
    class_study_count = 0
    bank_teller_count = 0
    more_account_info = 0
    bankteller_chat = 0
    library_subscription = False
    mrsj_afterpoker_fun = False

    wearing_swimsuit = False
    changing_girls = ["girl1", "girl2", "girl3", "girl4", "girl5", "girl6"]
    used_changing_girls = []
    eve_park_dialogue = 0
    chico_battle_count = 0
    erik_game_given = False
    comp_locked = True
    kevin_replaced = False
    found_cafe_replacement = False
    erik_favor = False
    homework_handed = False
    roxxy_copied1 = False
    asked_for_lollipop = False
    in_sis_room = False

    erik_basement_seen = False

    sexspeed = .15   

    sis_panties_trade = False
    in_erik_house = False
    pink_count = 0
    movie_theatre_count = 0
    girl_lockerroom_unlocked = False
    judith_sex_sequence_unlocked = False
    judith_daylock = False
    judith_sobbing = False
    new_message = False
    first_time_changing = True
    banned_from_pool = False
    sis_dialogue_advance = False
    sis_diary_unlocked = False
    look_for_panties = False
    connected = False
    homework_count = 0
    janice_thankyou = False
    webcam_quest = False
    webcam_erik_help = False
    webcam_planted = False
    homework_done = False
    judith_in_toilet = False
    mia_house_kicked = 0
    ronda_after_swimming = False
    gloryhole_done = 0

    erik_helped_with_camera = False

    diary_scene = False

    newspaper_thief = False
    bad_garden_count = 0

    quest09_1 = False
    quest09_2 = False
    quest09_3 = False
    quest14_1 = False
    quest14_2 = False
    quest16_1 = False
    quest17_1 = False

    doorbell_rang = False
    dinner_quest = False

    MC_comp_locked = True
    mom_phone_event01 = False

    poker_bot02 = ""

    henchmen_count = 0
    magic_numbers = [6, 16, 26, 36, 46, 56, 66, 76, 86, 96]

    rap_opponent = ""

    sis_cheerleader_sex2_menu = False

    xray = False
    cum = False
    animcounter = 0

    roxxy_shower_lock = False
    orcette_mail_lock = False
    yoga_fail_retry = False
    drawn_tattoo = ""

label start:
    $ shower = ShowerClass()
    $ gTimer = DayTimer()
    call INIT_FSM
    python:
        machines = []
        for m in Machine.get_instances():
            machines.append(m)
        events = []
        for e in Event_Queue.get_instances():
            events.append(e)
        store.my_events = events

    if firstname.strip() == "":
        $ firstname = "Anon"
    show screen escape_key

    init python:
        random_girl = 0

    python:
        gTimer = DayTimer()
        sister = Event_Queue()
        player = Event_Queue()
        mother = Event_Queue()
        aunt = Event_Queue()
        roxxy = Event_Queue()
        crystal = Event_Queue()
        erik = Event_Queue()
        mrsj = Event_Queue()
        June = Event_Queue()
        Anna = Event_Queue()
        Grace = Event_Queue()
        Roz = Event_Queue()
        loc_school_unlocked = False
        loc_aunt_unlocked = False
        loc_mia_unlocked = False
        loc_gym_unlocked = False
        loc_library_unlocked = False
        loc_park_unlocked = False
        loc_pool_unlocked = False
        loc_mall_unlocked = False
        loc_bank_unlocked = False
        loc_pizza_unlocked = False
        loc_dealership_unlocked = False
        loc_pier_unlocked = False
        loc_forest_unlocked = False
        loc_church_unlocked = False
        loc_police_unlocked = False
        loc_beach_unlocked = False
        loc_hill_unlocked = False
        loc_clinic_unlocked = False
        loc_trailer_unlocked = False
        loc_tattoo_unlocked = False
        loc_treehouse_unlocked = False
        loc_donuts_unlocked = False
        loc_court_unlocked = False
        loc_lair_unlocked = False
        loc_warehouse_unlocked = False
        savegame_version = config.version

    python:
        earnings = 0
        valid_pos = [(116,111), (280,111), (442,111), (603,111), (767,111), (116,272), (280,272), (442,272), (603,272), (767,272), (116,439), (280,439), (442,439), (603,439), (767,439)]
        rat = Good(20, False, False, image="objects/minigame01_bad04.png", passive_pic = "objects/minigame01_number07.png")
        carrot = Good(5, True, False, image="objects/minigame01_good03.png", passive_pic = "objects/minigame01_number04.png")
        carrot_rotten = Good(10, False, False, image="objects/minigame01_good03b.png", passive_pic = "objects/minigame01_number02.png")
        eggplant = Good(10, True, False, image="objects/minigame01_good01.png", passive_pic = "objects/minigame01_number05.png")
        eggplant_rotten = Good(10, False, False, image="objects/minigame01_good01b.png", passive_pic = "objects/minigame01_number02.png")
        pickle = Good(15, True, False, image="objects/minigame01_good02.png", passive_pic = "objects/minigame01_number06.png")
        pickle_rotten = Good(10, False, False, image="objects/minigame01_good02b.png", passive_pic = "objects/minigame01_number02.png")
        pumpkin = Good(10, False, False, image="objects/minigame01_bad05.png", passive_pic = "objects/minigame01_number02.png")
        pumpkin_rotten = Good(10, False, False, image="objects/minigame01_bad05b.png", passive_pic = "objects/minigame01_number02.png")
        tomato = Good(10, False, False, image = "objects/minigame01_bad03.png", passive_pic = "objects/minigame01_number02.png")
        tomato_rotten = Good(10, False, False, image = "objects/minigame01_bad03b.png", passive_pic = "objects/minigame01_number02.png")
        bug = Good(10, False, False, image = "objects/minigame01_bad02.png", passive_pic = "objects/minigame01_number02.png")
        weed = Good(15, False, False, image = "objects/minigame01_bad01.png", passive_pic = "objects/minigame01_number03.png")
        spider = Good(15, False, False, image = "objects/minigame01_bad07.png", passive_pic = "objects/minigame01_number03.png")
        corn = Good(5, True, False, image = "objects/minigame01_good04.png", passive_pic = "objects/minigame01_number04.png")
        corn_rotten = Good(10, False, False, image = "objects/minigame01_good04b.png", passive_pic = "objects/minigame01_number02.png")
        grapes = Good(10, False, False, image = "objects/minigame01_bad06.png", passive_pic = "objects/minigame01_number02.png")
        grapes_rotten = Good(10, False, False, image = "objects/minigame01_bad06b.png", passive_pic = "objects/minigame01_number02.png")
        earwig01 = Good(10, False, False, image = "objects/minigame01_bad08.png", passive_pic = "objects/minigame01_number02.png")
        earwig02 = Good(10, False, False, image = "objects/minigame01_bad08.png", passive_pic = "objects/minigame01_number02.png")
        earwig03 = Good(10, False, False, image = "objects/minigame01_bad08.png", passive_pic = "objects/minigame01_number02.png")
        item_list = [rat, carrot, eggplant, pickle, pumpkin, tomato, bug, weed, spider, grapes, corn]
        t_list = []
        bad_list = [rat, pumpkin, tomato, bug, weed, spider, grapes]
        rotten_list = [carrot_rotten, eggplant_rotten, pickle_rotten, pumpkin_rotten, tomato_rotten, grapes_rotten, corn_rotten]
        rotten_t_list = [carrot_rotten, eggplant_rotten, pickle_rotten, pumpkin_rotten, tomato_rotten, grapes_rotten, corn_rotten, earwig01, earwig02, earwig03]

    python:
        m_up = Arrow(image = "buttons/attack_02.png", passive = "buttons/attack_02b.png")
        m_down = Arrow(image = "buttons/attack_04.png", passive = "buttons/attack_04b.png")
        m_left = Arrow(image = "buttons/attack_01.png", passive = "buttons/attack_01b.png")
        m_right = Arrow(image = "buttons/attack_03.png", passive = "buttons/attack_03b.png")
        K_a = Key(image = "buttons/attack_05.png", passive = "buttons/attack_05b.png")
        K_s = Key(image = "buttons/attack_06.png", passive = "buttons/attack_06b.png")
        K_d = Key(image = "buttons/attack_07.png", passive = "buttons/attack_07b.png")
        K_f = Key(image = "buttons/attack_08.png", passive = "buttons/attack_08b.png")
        arrow_list = [m_up, m_down, m_left, m_right]
        keyboard_list = [K_a, K_s, K_d, K_f]
        task_list = []
        arrow_index = 0
        movedpiece = 0
        piecelist = [[0,0],[-60,580],[830,580],[830,580],[830,580],[-60,580],
                     [830,580],[-60,580],[830,580],[-60,580],[830,580],[-60,580],
                     [830,580],[-60,580],[-60,580],[-60,580],[830,580],[830,580],
                     [-60,580],[-60,580],[830,580],[830,580],[-60,580]]

    python:
        pStats = PlayerStats()

    python:
        inventory = Inventory()
        homework = Item("{b}Homework:{/b}", 0, image = "objects/item_homework1.png", description = "Use your desk at home to complete your homework and improve your grades!", h_image = "objects/item_homework1b.png")
        panties = Item("{b}Panties:{/b}", 100, image = "objects/item_panties1.png", description = "Your Sister's used panties.", h_image = "objects/item_panties1b.png")
        parts = Item("{b}Computer Parts:{/b}", 200, image = "objects/item_parts1.png", description = "New computer parts for sweet graphics.", h_image = "objects/item_parts1b.png")
        swimsuit = Item("{b}Swimsuit:{/b}", 100, image = "objects/item_swimsuit1.png", description = "A slick speedo for swimming.", h_image = "objects/item_swimsuit1b.png")
        homework1 = Item("{b}Completed Homework:{/b}", 0, image = "objects/item_homework1c.png", description = "A completed homework. It needs to return to your teacher.", h_image = "objects/item_homework1d.png")
        homework2 = Item("New Homework", 0, image = "objects/item_homework2.png", description = "Use your desk at home to complete your new homework and improve your grades!", h_image = "objects/item_homework2b.png")
        homework3 = Item("New Homework", 0, image = "objects/item_homework3.png", description = "Use your desk at home to complete your new homework and improve your grades!", h_image = "objects/item_homework3b.png")
        textbook1 = Item("{b}French Grammar Volume 1:{/b}", 400, image = "objects/item_volume1.png", description = "The latest textbook edition on how to speak French! En Francais!", h_image = "objects/item_volume1b.png")
        textbook2 = Item("{b}French Grammar Volume 2:{/b}", 400, image = "objects/item_volume2.png", description = "The latest textbook edition on how to speak French! En Francais!", h_image = "objects/item_volume2b.png")
        textbook3 = Item("{b}French Grammar Volume 3:{/b}", 400, image = "objects/item_volume3.png", description = "The latest textbook edition on how to speak French! En Francais!", h_image = "objects/item_volume3b.png")
        breeding_guide = Item("{b}Lactation and Me:{/b}", 0, image = "objects/item_book1.png", description = "A very \"in-depth\" guide on how to breed like a {b}Bull{/b}!", h_image = "objects/item_book1b.png")
        supersaga_webcam = Item("{b}Supersaga Digital Webcam:{/b}", 300, image = "objects/item_cam1.png", description = "The next gen webcam with high definition!", h_image = "objects/item_cam1b.png")
        bike = Item("{b}Delivery Road Bike:{/b}", 500, image = "objects/item_bike1.png", description = "The perfect way to start delivering pizza!", h_image = "objects/item_bike1b.png")
        pump = Item("Breast Pump", 0, image = "objects/item_pump2.png", description = "A cone-shaped pump meant to collect breast milk.", h_image = "objects/item_pump2b.png")
        milkjug = Item("{b}Milk Jug:{/b}", 300, image = "objects/item_jug1.png", description = "A thermal milk jug. Keep your fresh milk nice and cool!", h_image = "objects/item_jug1b.png")
        exterminator = Item("{b}Bug Exterminator:{/b}", 100, image = "objects/item_spray1.png", description = "Nothing can survive the exterminator!", h_image = "objects/item_spray1b.png")
        eradicator = Item("{b}Bug Eradicator:{/b}", 100, image = "objects/item_spray2.png", description = "Nothing can survive the eradicator!", h_image = "objects/item_spray2b.png")
        annihilator = Item("{b}Bug Annihilator:{/b}", 100, image = "objects/item_spray3.png", description = "Nothing can survive the annihilator!", h_image = "objects/item_spray3b.png")
        milk_carton = Item("{b}Fresh Milk Cartons:{/b}", 0, image = "objects/item_milk1.png", description = "A delivery of fresh milk cartons!", h_image = "objects/item_milk1b.png")
        package = Item("{b}Pink package:{/b}", 0, image = "objects/item_package1.png", description = "A purchased item from Pink.", h_image = "objects/item_package1b.png")
        gas_can = Item("{b}Gas Tank:{/b}", 100, image = "objects/item_gas1.png", description = "A safe container for flammable fluids containing gasoline.", h_image = "objects/item_gas1b.png")
        wrench = Item("{b}Wrench:{/b}", 50, image = "objects/item_wrench1.png", description = "A metal tool used to provide grip and tighten bolts.", h_image = "objects/item_wrench1b.png")
        seatrout = Item("{b}Seatrout:{/b}", 100, image = "objects/item_fish1.png", description = "A fresh fish! A bit smelly...", h_image = "objects/item_fish1b.png")
        snapper = Item("{b}Snapper:{/b}", 100, image = "objects/item_fish2.png", description = "A fresh fish! A bit smelly...", h_image = "objects/item_fish2b.png")
        mackerel = Item("{b}Mackerel:{/b}", 100, image = "objects/item_fish3.png", description = "A fresh fish! A bit smelly...", h_image = "objects/item_fish3b.png")
        cookies = Item("{b}Cookie box:{/b}", 0, image = "objects/item_cookies1.png", description = "A box of cookie. Everybody loves cookies.", h_image = "objects/item_cookies1b.png")
        condom = Item("{b}Pink package:{/b}", 0, image = "objects/item_condom1.png", description = "An extra, extra, extra large Hungdom condom.", h_image = "objects/item_condom1b.png")
        attic_key = Item("{b}Small key:{/b}", 0, image = "objects/item_key1.png", description = "A small key.", h_image = "objects/item_key1b.png")
        shovel = Item("{b}Shovel:{/b}", 0, image = "objects/item_shovel1.png", description = "A used metal shovel.", h_image = "objects/item_shovel1b.png")
        stool = Item("{b}Stool:{/b}", 0, image = "objects/item_stool1.png", description = "A small stool.", h_image = "objects/item_stool1b.png")
        fishing_rod = Item("{b}Fishing Rod:{/b}", 0, image = "objects/item_rod1.png", description = "An old fishing rod.", h_image = "objects/item_rod1b.png")
        ring = Item("{b}Diamong ring:{/b}", 0, image = "objects/item_ring1.png", description = "A tiny ring with a large stone fixed to it.", h_image = "objects/item_ring1b.png")
        cheerleader_outfit = Item("{b}Cheerleader Outfit:{/b}", 0, image = "objects/item_outfit1.png", description = "It's the cheerleader outfit that [sis_name] used to wear during college.", h_image = "objects/item_outfit1b.png")
        dog = Item("{b}Awesomo:{/b}", 0, image = "objects/item_dog1.png", description = "A small pug.", h_image = "objects/item_dog1.png")
        worm = Item("{b}Worm:{/b}", 0, image = "objects/item_bait1.png", description = "A fresh worm.", h_image = "objects/item_bait1b.png")
        buttplug = Item("{b}Buttplug:{/b}", 100, image = "objects/item_sex1.png", description = "A cone shaped dildo for anal insertion that glows in the dark.", h_image = "objects/item_sex1b.png")
        drilldo = Item("{b}The Drilldo:{/b}", 400, image = "objects/item_sex2.png", description = "A power drill dildo.", h_image = "objects/item_sex2b.png")
        darthmoan = Item("{b}DarthMoan:{/b}", 300, image = "objects/item_sex3.png", description = "A double bladed dildo, for double the fun!.", h_image = "objects/item_sex3b.png")
        badmonster = Item("{b}Bad Monster:{/b}", 500, image = "objects/item_sex4.png", description = "A very bad monster dildo.", h_image = "objects/item_sex4b.png")
        sybian = Item("{b}Dual Sybian:{/b}", 500, image = "objects/item_sex5.png", description = "A double dildo mounted sybian.", h_image = "objects/item_sex5b.png")
        milkslave = Item("{b}The Milk Slave:{/b}", 1000, image = "objects/item_sex6.png", description = "Full body cow outfit with a buttplug tail.", h_image = "objects/item_sex6b.png")
        fleshtube = Item("{b}The Flesh Tube:{/b}", 100, image = "objects/item_sex7.png", description = "A strange tube with soft rubber lining.", h_image = "objects/item_sex7b.png")
        electroclit = Item("{b}Electro Clit:{/b}", 100, image = "objects/item_sex8.png", description = "A battery powered vibrating clit stimulator.", h_image = "objects/item_sex8b.png")
        ultravibrato = Item("{b}UltraVibrator 2000:{/b}", 200, image = "objects/item_sex9.png", description = "A battery powered vibrating dildo with ribbed lining.", h_image = "objects/item_sex9b.png")
        doomdong = Item("{b}The Doom Dong:{/b}", 300, image = "objects/item_sex10.png", description = "A very large, black, dildo.", h_image = "objects/item_sex10b.png")
        virtualsaga = Item("{b}Virtual Saga X:{/b}", 600, image = "objects/item_vr1.png", description = "A virtual reality headset.", h_image = "objects/item_vr1b.png")
        sexdoll = Item("{b}Sex Doll:{/b}", 800, image = "objects/item_sex12.png", description = "A stange sex doll of a man, with a moustache.", h_image = "objects/item_sex12b.png")
        lingerie = Item("{b}Pink Lingerie:{/b}", 400, image = "objects/item_sex13.png", description = "A sexy women's undergarment.", h_image = "objects/item_sex13b.png")
        handcuffs = Item("{b}Handcuffs:{/b}", 50, image = "objects/item_sex14.png", description = "Sturdy metal handcuffs.", h_image = "objects/item_sex14b.png")
        strapon = Item("{b}Strapon:{/b}", 500, image = "objects/item_sex15.png", description = "A rubber dick fit to be wielded by a warrior.", h_image = "objects/item_sex15b.png")
        strapon_drawing = Item("{b}Drawing:{/b}", 0, image = "objects/item_note1.png", description = "A drawing from Angelica of the final item she requires.", h_image = "objects/item_note1b.png")
        whip = Item("{b}Whip:{/b}", 500, image = "objects/item_sex16.png", description = "A whip to punish sinners.", h_image = "objects/item_sex16b.png")
        aviators = Item("{b}Aviators:{/b}", 0, image = "objects/item_glasses1.png", description = "A sweet pair of badass aviators.", h_image = "objects/item_glasses1b.png", closeup = "objects/closeup_note01.png")
        lure01 = Item("{b}Lure:{/b}", 0, image = "objects/item_bait2.png", description = "This lure looks very familiar.", h_image = "objects/item_bait2b.png")
        card03 = Item("{b}Trading Card - Orcette - The Whoremonger:{/b}", 0, image = "objects/item_card3.png", description = "The Fappening card for Orcette - The Whoremonger.", h_image = "objects/item_card3b.png", closeup = "objects/closeup_card03.png")
        card04 = Item("{b}Trading Card - Dillon:{/b}", 0, image = "objects/item_card5.png", description = "The Fappening card for Dillon.", h_image = "objects/item_card5b.png", closeup = "objects/closeup_card04.png")
        eriks_cards = Item("{b}Erik's Fappening Trading Cards:{/b}", 0, image = "objects/item_box1.png", description = "This box contains the Fappening cards that Erik lost.", h_image = "objects/item_box1b.png")
        orcette = Item("{b}Orcette:{/b}", 0, image = "objects/item_orcette1.png", description = "ZUG! ZUG! It's an Orcette.", h_image = "objects/item_orcette1b.png")
        instructions1 = Item("{b}Yoga Instructions:{/b}", 0, image = "objects/item_instructions1.png", description = "Is this really how Yoga works ?", h_image = "objects/item_instructions1b.png", closeup = "objects/closeup_instructions_01.png")
        kamasutra = Item("{b}Kama Sutra:{/b}", 0, image = "objects/item_book2.png", description = "A book about the art of sex.", h_image = "objects/item_book2b.png")
        birth_control_pills = Item("{b}Birth Control Pills:{/b}", 0, image = "objects/item_pills1.png", description = "We don't want you knocking up the entire town now do we.", h_image = "objects/item_pills1b.png")
        hospital_access_card = Item("{b}Hospital Storage card:{/b}", 0, image = "objects/item_card4.png", description = "The access card for the Hospital Storage room.", h_image = "objects/item_card4b.png")
        stolen_goods = Item("{b}Stolen Goods:{/b}", 0, image = "objects/item_goods1.png", description = "The goods that were stolen by a recent serial thief.", h_image = "objects/item_goods1b.png")
        donuts_fail = Item("{b}DOH-nuts:{/b}", 50, image = "objects/item_donut1.png", description = "Some delicious tasting holes of the finest caliber.", h_image = "objects/item_donut1b.png")
        donuts_correct = Item("{b}DOH-nuts:{/b}", 50, image = "objects/item_donut1.png", description = "Some delicious tasting holes of the finest caliber.", h_image = "objects/item_donut1b.png")
        pearl_necklace = Item("{b}Pearl Necklace:{/b}", 50, image = "objects/item_necklace3.png", description = "A pearl necklace fit for a beauty.", h_image = "objects/item_necklace3b.png")
        towel = Item("{b}Towel:{/b}", 0, image = "objects/item_towel1.png", description = "It's a towel.", h_image = "objects/item_towel1b.png")
        lotion = Item("{b}Lotion:{/b}", 0, image = "objects/item_lotion1.png", description = "It's lotion used for \"massages\"!", h_image = "objects/item_lotion1b.png")
        cat_food = Item("{b}Cat Food:{/b}", 100, image = "objects/item_catfood1.png", description = "It's a special brand of food for cats, the best type of animal in the world!", h_image = "objects/item_catfood1b.png")
        tattoo_butterfly = Item("{b}Tattoo Drawing:{/b}", 0, image = "objects/item_tattoo_drawing1.png", description = "Your drawing of a butterlfy tattoo.", h_image = "objects/item_tattoo_drawing1b.png")
        tattoo_dolphin = Item("{b}Tattoo Drawing:{/b}", 0, image = "objects/item_tattoo_drawing2.png", description = "Your drawing of a dolphin tattoo.", h_image = "objects/item_tattoo_drawing2b.png")
        tattoo_stars = Item("{b}Tattoo Drawing:{/b}", 0, image = "objects/item_tattoo_drawing3.png", description = "Your drawing of a tattoo of stars.", h_image = "objects/item_tattoo_drawing3b.png")
        tattoo_flowers = Item("{b}Tattoo Drawing:{/b}", 0, image = "objects/item_tattoo_drawing4.png", description = "Your drawing of a tattoo of flowers.", h_image = "objects/item_tattoo_drawing4b.png")
        tattoo_skull = Item("{b}Tattoo Drawing:{/b}", 0, image = "objects/item_tattoo_drawing5.png", description = "Your drawing of a skull tattoo.", h_image = "objects/item_tattoo_drawing5b.png")
        tattoo_cookie = Item("{b}Tattoo Drawing:{/b}", 0, image = "objects/item_tattoo_drawing6.png", description = "Your drawing of a cookie tattoo.", h_image = "objects/item_tattoo_drawing6b.png")
        tattoo_choices = {"tattoo_butterfly": tattoo_butterfly, "tattoo_dolphin": tattoo_dolphin, "tattoo_stars": tattoo_stars, "tattoo_flowers": tattoo_flowers, "tattoo_skull": tattoo_skull, "tattoo_cookie": tattoo_cookie}

        key03 = Item("{b}Helen's Secret Key{/b}", 0, image = "objects/item_key3.png", description = "The key secretely hidden by the statue of Mary", h_image = "objects/item_key3b.png")

        obituary_records = Item("{b}Obituary Records{/b}", 0, image = "objects/item_records1.png", description = "The obituary records that contains the name of the boatsmith.", h_image = "objects/item_records1b.png", closeup = "objects/closeup_records_01.png", dialogue = "obituary_records")
        scroll = Item("{b}Scroll{/b}", 0, image = "private/objects/item_scroll1.png", description = "A mysterious scroll you found hidden in a tree on Raven Hill.", h_image = "private/objects/item_scroll1b.png", closeup = "private/objects/closeup_scroll_01.png", dialogue = "scroll")
        treasure_key = Item("{b}Mystery key:{/b}", 0, image = "objects/item_key2.png", description = "A mysterious key.", h_image = "objects/item_key2b.png")
        weird_coin = Item("{b}Weird Coin{/b}", 0, image = "private/objects/item_coin1.png", description = "A coin with weird engravings that you found in the park fountain.", h_image = "private/objects/item_coin1b.png", closeup = "private/objects/closeup_coin_01.png", dialogue = "weird_coin")
        old_book = Item("{b}Old Book{/b}", 0, image = "private/objects/item_book3.png", description = "An old book that looks like it can decipher something from the library.", h_image = "private/objects/item_book3b.png", closeup = "private/objects/closeup_book_03.png", dialogue = "old_book")
        treasure_map = Item("{b}Treasure Map{/b}", 0, image = "private/objects/item_map1.png", description = "A treasure map that you acquired after solving difficult puzzle.", h_image = "private/objects/item_map1b.png", closeup = "private/objects/closeup_map_01.png", dialogue = "treasure_map")
        golden_compass = Item("{b}Golden Compass{/b}", 0, image = "private/objects/item_compass1.png", description = "The golden compass that is said to lead you to your greatest desire.", h_image = "private/objects/item_compass1b.png", closeup = "private/objects/closeup_compass_01.png", dialogue = "golden_compass")
        special_lure = Item("{b}Special Lure{/b}", 0, image = "objects/item_bait4.png", description = "A lure said to be able to catch anything and everything.", h_image = "objects/item_bait4b.png")
        tigger = Item("{b}Demon Spawn Tigger{/b}", 0, image = "objects/item_tigger1.png", description = "Once a man's swarn enemy, but no longer will anymore piggy's go to the market.", h_image = "objects/item_tigger1b.png", closeup = "objects/closeup_tigger_01.png", dialogue = "tigger")
        mushroom = Item("{b}Mushroom{/b}", 0, image = "objects/item_mushroom1.png", description = "Shrooms for days bois.", h_image = "objects/item_mushroom1b.png")

        game = Item("{b}Sea Dogs SAGA{/b}", 100, image = Transform("game_1"), description = "The latest video game sensation from DarkCookie!", h_image = Transform("game_1b"))
        game02 = Item("{b}World of Orcette{/b}", 100, image = Transform("game_2"), description = "The latest video game sensation from DarkCookie!", h_image = Transform("game_2b"))
        card01 = Item("{b}Trading Card - The Flying Cock Goblin:{/b}", 50, image = "objects/item_card1.png", description = "The Fappening card for The Flying Cock Goblin.", h_image = "objects/item_card1b.png", closeup = "objects/closeup_card01.png")
        card02 = Item("{b}Trading Card - Cock Crown of Thorns:{/b}", 50, image = Transform("card_2"), description = "The Fappening card for Cock Crown of Thorns.", h_image = Transform("card_2b"), closeup = "objects/closeup_card02.png")
        orcette_cosplay = Item("{b}Orcette Queen Garments:{/b}", 300, image = Transform("cosplay_1"), description = "The outfit befit for an Orcette Queen made from the battle scarred skin of her enemies.", h_image = Transform("cosplay_1b"))

        sea_dogs_saga = ComicItem(game, "PC Game - Sea Dogs Saga", "", "boxes/popup_item_game.png", Transform("game_1"), Transform("game_1b"), 100, "Video Games", False)
        world_of_orcette = ComicItem(game02, "PC Game - World of Orcette", "", "boxes/popup_item_game2.png", Transform("game_2"), Transform("game_2b"), 100, "Video Games", False)
        orcette_outfit = ComicItem(orcette_cosplay, "Cosplay Outfit - Orcette Queen", "", "boxes/popup_cosplay.png", Transform("cosplay_1"), Transform("cosplay_1b"), 300, "Cosplay", False)
        cock_goblin = ComicItem(card01, "Trading Card - The Flying Cock Goblin", "objects/closeup_card01.png", "boxes/popup_item_card1.png", "objects/item_card1.png", "objects/item_card1b.png", 50, "Collectible", False)
        cock_crown = ComicItem(card02, "Trading Card - Cock Crown of Thorns", "objects/closeup_card02.png", "boxes/popup_item_card2.png", Transform("card_2"), Transform("card_2b"), 50, "Collectible", False)

        comicstore = ComicStore()
        comicstore.items = [cock_goblin, sea_dogs_saga, world_of_orcette, cock_crown, orcette_outfit]

        red_corset = Item("{b}Lingerie - Red Corset:{/b}", 300, image = Transform("sex_17"), description = "A nice sexy lingerie set in a dashing blood red colour.", h_image = Transform("sex_17b"))
        cow_outfit = Item("{b}Lingerie - Cow Outfit:{/b}", 300, image = Transform("sex_6"), description = "A black and white spotted bikini accompanied with bell, tail plug and ear headband.", h_image = Transform("sex_6b"))

        red_corset_lingerie = PinkItem(red_corset, "Red Corset", "", "boxes/pink_item_15.png", Transform("sex_17"), Transform("sex_17b"), 300, "Lingerie", False)
        cow_outfit_lingerie = PinkItem(cow_outfit, "Cow Outfit", "", "boxes/pink_item_16.png", Transform("sex_6"), Transform("sex_6b"), 300, "Lingerie", False)

        pinkstore = PinkStore()
        pinkstore.items = [cow_outfit_lingerie]

        m_magazine = Item("Mrs. Johnson's magazine", 0, image = "objects/object_mailbox_item01.png", description = "", h_image = "objects/object_mailbox_item01b.png")
        m_erik_package = Item("Erik's package", 0, image = "objects/object_mailbox_item04.png", description="", h_image = "objects/object_mailbox_item04b.png")
        m_dad_letter = Item("Dad's letter", 0, image = "objects/object_mailbox_item03.png", description = "", h_image = "objects/object_mailbox_item03b.png")
        m_pizza_pamphlet = Item("Pizza pamphlet", 0, image = "objects/object_mailbox_item02.png", description = "", h_image = "objects/object_mailbox_item02b.png")
        m_newspaper = Item("Newspaper", 0, image = "objects/object_mailbox_item05.png", description = "", h_image = "objects/object_mailbox_item05b.png")
        player_mailbox_items = [m_pizza_pamphlet, m_newspaper]
        erik_mailbox_items = [m_erik_package, m_dad_letter, m_magazine, m_pizza_pamphlet, m_newspaper]
        mia_mailbox_items = [m_pizza_pamphlet, m_newspaper]

    python:
        bait = ""

    python:
        encounters = []
        player_pos_x = 427
        player_pos_y = 615
        unpassable = [(427,431),(335,615),(335,523),(335,431),(519,431),(519,615),(427,707),(611,615),(703,615),(795,615),(887,615),(887,523),
        (887,431), (887,339), (887,247), (795,247), (795,155), (703,63), (611,63), (519,63), (427,155), (427,63), (335,63), (243,63), (151,63),
        (59,63), (59,155), (59,247), (59,339), (59,431), (59,523), (59,615), (151,615), (243, 615), (243,523), (243, 431), (243,339), (243,247),
        (427,247), (611,431), (611,339), (611,247), (703,431)]
        gelly = Mob(image = "images/objects/minigame03_monster02.png")
        skeleton = Mob(image = "images/objects/minigame03_monster01.png")
        firespirit = Mob(image = "images/objects/minigame03_monster03.png")
        mob_list = [gelly, skeleton, firespirit]
        encounter_chance = 99
        mob_pos_x = 0
        mob_pos_y = 0

    $ day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    $ time_count = 5
    $ harold_toppings = ['chocolate chips', 'sprinkles', 'vanilla drizzle', 'maple drizzle']
    $ harold_glazes = ['chocolate glazed', 'strawberry glazed', 'blueberry glazed', 'vanilla glazed']
    $ harold_glaze = renpy.random.choice(harold_glazes)
    $ harold_topping = renpy.random.choice(harold_toppings)

    python:
        quest01 = Quest("Homework", image = "buttons/cellphone_goals_side01.png", status = False)
        quest02 = Quest("Training", image = "buttons/cellphone_goals_side02.png", status = False)
        quest03 = Quest("Swimsuit", image = "buttons/cellphone_goals_side03.png", status = False)
        quest04 = Quest("Cafe_Replacement", image = "buttons/cellphone_goals_side04.png", status = False)
        quest05 = Quest("Comp_Parts", image = "buttons/cellphone_goals_side05.png", status = False)
        quest06 = Quest("Webcam", image = "buttons/cellphone_goals_side06.png", status = False)
        quest07 = Quest("Panties", image = "buttons/cellphone_goals_side07.png", status = False)
        quest08 = Quest("Milk Pump", image = "buttons/cellphone_goals_side09.png", status = False)
        quest09 = Quest("Milk Delivery", image = "buttons/cellphone_goals_side10.png", status = False)
        quest10 = Quest("Bug Infestation", image = "buttons/cellphone_goals_side08.png", status = False)
        quest11 = Quest("Hidden Camera", image = "buttons/cellphone_goals_side12.png", status = False)
        quest12 = Quest("Milkjug", image = "buttons/cellphone_goals_side11.png", status = False)
        quest13 = Quest("Cow Costume", image = "buttons/cellphone_goals_side13.png", status = False)
        quest14 = Quest("Mowing Lawn", image = "buttons/cellphone_goals_side14.png", status = False)
        quest15 = Quest("Find player for Poker", image = "buttons/cellphone_goals_side19.png", status = False)
        quest16 = Quest("Check the Car", image = "buttons/cellphone_goals_side18.png", status = False)
        quest17 = Quest("Fix the pipe", image = "buttons/cellphone_goals_side15.png", status = False)
        quest18 = Quest("Buy fish", image = "buttons/cellphone_goals_side16.png", status = False)
        quest19 = Quest("Look for dog", image = "buttons/cellphone_goals_side20.png", status = False)
        quest20 = Quest("Find a shovel", image = "buttons/cellphone_goals_side20.png", status = False)
        quest21 = Quest("Wheelbarrow", image = "buttons/cellphone_goals_side22.png", status = False)
        quest_list = []
        completed_quests = []
        quest01_status = quest01.status
        quest02_status = quest02.status
        quest03_status = quest03.status
        quest04_status = quest04.status
        quest05_status = quest05.status
        quest06_status = quest06.status
        quest07_status = quest07.status
        quest08_status = quest08.status

        m_judith01 = Message("Judith01", sender = "Judith", content_prev = "I'm in the washroom...", content = "I'm in the washroom...\nIf you want to meet me...", image = "buttons/cellphone_text_judith01.png", status = False)
        m_mia01 = Message("Mia01", sender = "Mia", content_prev = "HELP!", content = "HELP!", image = "buttons/cellphone_text_mia01.png", status = False)
        m_mia02 = Message("Mia02", sender = "Mia", content_prev = "We can't find {b}my dad{/b}...", content = "We can't find {b}my dad{/b}...\nCan you come help us please?", image = "buttons/cellphone_text_mia01.png", status = False)
        message_list = []

    screen cheat_option:
        add "backgrounds/menu_cheats.jpg"
        imagebutton:
            focus_mask True
            idle "buttons/menu_cheats_01.png"
            hover "buttons/menu_cheats_01b.png"
            action Jump("define_events")
            xpos 230
            ypos 240

        imagebutton:
            focus_mask True
            idle "buttons/menu_cheats_02.png"
            hover "buttons/menu_cheats_02b.png"
            action Jump("cheat_intro")
            xpos 610
            ypos 240

    call screen cheat_option

    label cheat_intro:
        $ cheat_mode = True
        $ inventory.money = 999999
        jump define_events

    label intro:
        python:
            events = []
            for e in Event_Queue.get_instances():
                events.append(e)
            store.my_events = events

        $ erik_telescope_random = renpy.random.randint(0,1)
        $ erikmom_telescope_random = renpy.random.randint(0,1)
        $ mia_telescope_random = renpy.random.randint(0,1)
        $ backyard_telescope_random = renpy.random.randint (0,3)
        $ helen_telescope_random = renpy.random.randint(0,1)
        stop music fadeout 2
        scene black
        with Pause(0.5)
        play music "<loop 79>audio/music_sad.ogg" loop fadein 1.0
        $ playSound("<loop 5 to 179>audio/ambience_rain1.ogg")

        show intro_01 with dissolve
        show text "March 3rd, on a rainy afternoon.\nAll my relatives are here, mourning the loss of my father.\nHe died from a work related accident at the age of 40. Leaving behind my mom, my sister, and I..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)
        $ playSound("<loop 3 to 94>audio/ambience_rain2.ogg", multi = True)

        show intro_02 with dissolve
        show text "Circumstances surrounding his death have been found {i}suspicious{/i} by the police.\nThey were at our house for an entire week asking questions, but they said nothing was {i}conclusive{/i}.\nHopefully things get sorted out and we can get some {i}justice{/i}..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)
        $ playSound("<loop 5 to 181>audio/ambience_rain3.ogg")

        show intro_03 with dissolve
        show text "The night of the funeral, I overheard a conversation between [mom_name] and Aunt Diane. \nShe said it's been a tough year for us, and that Dad had owed a {i}lot of money{/i} to some bad people. \nNow that he was gone, she didn't know what to do.\nShe started sobbing..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)
        stop music fadeout 2
        $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg")

        show intro_04 with dissolve
        show text "Our family was a wreck. \n{b}Dad's{/b} passing was unexpected and really hit us all pretty hard as a family. \n{b}[mom_name]{/b} even got me excused from school for a month, as we tried to sort everything out. \n...but I can't grieve forever. Tomorrow is a new day, and I have to look after Mom and my Sister." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        show text "There are {i}3 things{/i} I have to take care of before the end of the summer.\n1) - {b}I have to save enough money for college.{/b}\n2) - {b}I have to find out what really happened to Dad.{/b}\n3) - {b}I have to find a date for prom.{/b} " at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve
        hide intro_01
        hide intro_02
        hide intro_03
        hide intro_04 with dissolve
        $ playSound()

        scene black with dissolve
        with Pause(0.5)
        jump bedroom_dialogue

label newScreen(screen, user, images):
    $ callScreen(screen, user, images)