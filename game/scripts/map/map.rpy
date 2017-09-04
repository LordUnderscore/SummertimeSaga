label map_dialogue:
    $ location_count = "Town Map"
    if gTimer.gameDay() > 1:
        $ tick_skip_active = True
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

        if June.started(june_mc_help):
            scene outside_school_b
            show player 10
            with dissolve
            player_name "I should probably tell {b}Erik{/b} that it's not going to work out with {b}June{/b}..."
            player_name "... and that I might spend time with her."
            player_name "He's going to be upset."
            hide player
            $ june_mc_help.finish()

        elif June.started(june_erik_help):
            scene outside_school_b
            show player 17
            with dissolve
            player_name "I should tell {b}Erik{/b} the good news!"
            player_name "He's going to be so excited about this!"
            show player 14
            player_name "{b}June{/b} seems like the perfect kind of girl for him!"
            hide player
            $ june_erik_help.finish()

        elif erik.in_progress(erik_intro):
            scene event01
            show erik 4 at right with dissolve
            eri "Hey, {b}[firstname]{/b}!"
            show player 10 at left with dissolve
            show erik 1 at right
            player_name "Oh... Hey..."
            show erik 4 at right
            eri "How was your first day back at school?"
            show player 37 at left
            show erik 1 at right
            player_name "Ugh... I don't even want to talk about it."
            show erik 5 at right
            eri "I see..."
            show player 5 at left
            eri "What are you up to now?"
            show erik 1 at right
            show player 26 at left
            player_name "Well, I told my mom that I would visit my {b}Aunt Diane{/b}."
            player_name "She has a small {b}job{/b} for me, to make some money, so..."
            show erik 3 at right
            show player 13 at left
            eri "Man... I wish I had a job..."
            show erik 4 at right
            eri "A job where I could just sit at my computer playing games, all day, heh..."
            show erik 1 at right
            show player 14 at left
            player_name "Oh! Speaking of computer... I think mine is {b}broken{/b}?"
            show player 35 at left
            player_name "I think I need to replace some parts in it, or something..."
            show player 12 at left
            player_name "You know any good store where I could buy some?"
            show erik 4 at right
            show player 1 at left
            eri "Hmmm... I usually shop for parts at {b}CONSUM-R{/b} in the {b}Mall{/b}."
            eri "They have good prices and sell a variety of things."
            show erik 1 at right
            show player 14 at left
            player_name "Alright then, I'll check it out!"
            show erik 7 at right
            show player 36 at left
            eri "See you later!"
            hide erik 7 at right with dissolve
            hide player 36 at left with dissolve

            show unlock15 at truecenter with dissolve
            $ loc_aunt_unlocked = True
            $ renpy.pause()
            hide unlock15 with dissolve

            show unlock16 at truecenter with dissolve
            $ loc_mall_unlocked = True
            $ renpy.pause()
            hide unlock16 with dissolve

            show unlock48 at truecenter with dissolve
            $ loc_beach_unlocked = True
            $ renpy.pause()
            hide unlock48 with dissolve

            show unlock47 at truecenter with dissolve
            $ loc_tattoo_unlocked = True
            $ renpy.pause()
            hide unlock47 with dissolve

            show unlock46 at truecenter with dissolve
            $ loc_treehouse_unlocked = True
            $ renpy.pause()
            hide unlock46 with dissolve

            show unlock49 at truecenter with dissolve
            $ loc_hill_unlocked = True
            $ renpy.pause()
            hide unlock49 with dissolve

            if quest05 not in completed_quests:
                $ quest_list.append(quest05)
            $ erik.complete_events(erik_intro)
            $ event_outside_school_count = 0
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label night_sleep_map:
    scene townmap_night
    player_name "I can't go there at night!"
    $ callScreen("Town Map")

label sleep_locked:
    scene expression gTimer.image("townmap{}")
    player_name "I can't sleep right now."
    $ callScreen("Town Map")

label weekend_locked:
    scene townmap
    player_name "No need to go there, it's closed on weekends."
    $ callScreen("Town Map")