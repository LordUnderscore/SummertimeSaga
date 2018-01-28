default park_count_night = 0
default anna_done = False

label park_dialogue:
    $ location_count = "Park"
    if gTimer.is_dark():
        if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
            $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")

    if not gTimer.is_dark():
        if getPlayingSound("<loop 1>audio/ambience_park.ogg"):
            $ playSound("<loop 1>audio/ambience_park.ogg")
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if gTimer.is_dark() and park_count_night == 0:
        scene park_night
        show player 34 with dissolve
        player_name "..."
        show player 35
        player_name "( I can hear distant voices... )"
        show player 14
        player_name "( Maybe I should go check it out! )"
        hide player 14 with dissolve
        $ park_count_night = 1
    $ callScreen(location_count)

label anna_button_dialogue:
    scene location_park_closeup
    if not Anna.known(anna_missing_pup):
        show player 11 at left with dissolve
        show anna 5 at right with dissolve
        anna "Hey {b}[firstname]{/b}, have you seen a {b}small dog{/b} without a leash??"
        show anna 4
        show player 10
        player_name "I don't think so..."
        show anna 5
        show player 11
        anna "I think I lost him."
        anna "I was running along the trail by the {b}forest{/b}, and when I looked back, he was gone!!"
        show anna 4
        show player 10
        player_name "Have you looked along the trail?"
        show anna 5
        show player 11
        anna "Of course! I looked everywhere!"
        anna "But I can't cover the trail and the {b}forest{/b} all by myself..."
        show anna 4
        show player 10
        player_name "What does he look like?"
        show player 11
        show anna 6 at Position(xpos=1002)
        anna "Oh, right. He's a {b}pug{/b}, about this big!"
        show anna 5 at right
        anna "His name is {b}Awesomo{/b}."
        anna "He's a bit overweight, so he couldn't have gone far."
        anna "Please! Will you help me find him?"
        show anna 4
        menu:
            "Yes":
                show anna 4
                show player 14
                player_name "Sure. I'll look for him."
                player_name "Is there anything I should know about him?"
                player_name "Something that'll help me find him?"
                show player 1
                show anna 5
                anna "Well... He really loves to eat {b}cookies{/b}."
                anna "If you have some, I'm sure he'll smell them and come out..."
                show anna 11
                show player 14
                player_name "Okay! I'll come see you if I find him!"
                show anna 12
                show player 1
                anna "Thank you so much!"
                $ Anna.add_event(anna_missing_pup)
                show unlock42 at truecenter with dissolve
                $ loc_forest_unlocked = True
                pause
                hide unlock42 with dissolve
            "No":

                show anna 4
                show player 10
                player_name "I'd love to help, but I have some things I need to attend to..."
                show player 11
                show anna 5
                anna "Oh, sorry to bother you..."

    elif Anna.started(anna_missing_pup) and dog in inventory.items:
        scene location_park_closeup
        show player 247 at left with dissolve
        show anna 4 at right with dissolve
        player_name "Guess who I found?"
        show anna 5 with vpunch
        anna "!!!"
        show anna 12
        anna "{b}Awesomo{/b}!!!"
        show player 1
        show anna 9
        with dissolve
        anna "Where did you find him?!"
        show anna 8
        show player 14
        player_name "He was in the forest nearby, just off the trail..."
        player_name "And you were right! A few cookies did the trick."
        show anna 10
        show player 1
        anna "Thank you {b}so{/b} much!"
        show anna 9
        anna "I'll be sure to repay you somehow."
        show anna 7
        anna "I should get him home now. He's probably getting hungry after all this."
        show anna 10
        anna "See you around!"
        $ inventory.items.remove(dog)
        $ anna_missing_pup.finish()
    else:

        show player 11 at left with dissolve
        show anna 5 at right with dissolve
        anna "Have you found him??"
        show anna 4
        show player 10
        player_name "Not yet..."
        player_name "Could you describe him to me again? And where could I find him?"
        show player 11
        show anna 6 at Position(xpos=1002)
        anna "He's about this big and he's a {b}pug{/b}!"
        show anna 5 at right
        anna "He should be somewhere near the trail by the {b}forest{/b}..."
        anna "...And he loves {b}cookies{/b}!"
        anna "Maybe you could use some {b}cookies{/b} to lure him out."
        show anna 11
        show player 14
        player_name "Okay! I'll go look for him!"
    hide player
    hide anna
    with dissolve
    $ callScreen(location_count)

label park_dialogue01:
    if eve_park_dialogue == 0:
        scene park_bench
        show player 1 at left with dissolve
        show eve 2 at right with dissolve
        eve "So you decided to show up, huh?"
        show eve 1 at right
        show player 2 at left
        player_name "Well, you said that I should..."
        show eve 6 at right
        show player 11 at left
        eve "Isn't it a bit late for you?"
        eve "Don't you have a curfew, or something?"
        show eve 1 at right
        show player 5 at left
        player_name "..."
        show eve 6 at right
        show player 11 at left
        eve "I'm just kidding!!"
        show eve 1 at right
        show player 17 at left
        player_name "Oh. Haha..."
        show player 1 at left
        show eve 2 at right
        eve "So, what's up?"
        menu:
            "You look good!":
                show player 21 at left
                show eve 1 at right
                player_name "I don't know if I've ever told you, but I really like your hair!"
                show eve 4 at right
                show player 13 at left
                eve "Haha! That's random!"
                show player 29 at left
                player_name "Just saying... The blue really looks good on you."
                show eve 3 at right
                show player 13 at left
                eve "..."
                show eve 4 at right
                eve "Uhh... Thanks?"
                show eve 6 at right
                show player 11 at left
                eve "Hmm... Hey, you should stick around for a bit!"
                eve "The guys are gonna {b}rap battle{/b} soon."
                show eve 1 at right
                show player 2 at left
                player_name "Oh yeah? Like... dissing each other with a mic?"
                show eve 6 at right
                show player 1 at left
                eve "Yeah!"
                show eve 7 at right
                show player 11 at left
                eve "I think you should do it."
                show eve 5 at right
                show player 23 at left with hpunch
                player_name "What?!"
                show eve 6 at right
                show player 5 at left
                eve "Oh come on. You can't be THAT shy?"
                eve "Just have fun with it!"
                show eve 5 at right
                show player 21 at left
                player_name "I guess I could try it..."
                show player 13 at left
                show eve 6 at right
                eve "So? You going to do it?"
                menu:
                    "Let's do it!":
                        show player 21 at left
                        show eve 5 at right
                        player_name "Okay, let's do it!"
                        show player 13 at left
                        show eve 6 at right
                        eve "I knew you had it in you!"
                        show eve 8 at right
                        eve "Here's your mic..."
                        show player 70
                        show eve 5 at right
                        player_name "Oh. Okay. Is it on?"
                        show eve 6 at right
                        eve "Haha! Of course!"
                        show player 71 at left
                        show eve 5 at right
                        player_name "Who am I facing?"
                        show eve 6 at right
                        eve "There's three of them: {b}Chico{/b}, {b}Tyrone{/b} and {b}Chad{/b}! "
                        show eve 5 at right
                        show player 70 at left
                        player_name "Hmmm... Who should I battle?"
                        menu:
                            "Chico":
                                $ rap_opponent = "chico"
                                show player 70 at left
                                player_name "I'll go against {b}Chico{/b} first."
                                hide player 70 at left with dissolve
                                hide eve 5 at right with dissolve
                                jump chico_before_battle
                            "<>[chr_warn]Chad":

                                $ pass
                            "<>[chr_warn]Tyrone":

                                $ pass

                            "Skip Mini-Game (Cheat)" if cheat_mode:
                                $ gTimer.tick()
                                $ pStats.increase("chr")
                                $ eve_park_dialogue = 1
                                show unlock23 at truecenter with dissolve
                                $ renpy.pause()
                                $ callScreen(location_count)
                    "I have to go.":

                        show player 10 at left
                        show eve 1 at right
                        player_name "Actually, I have to go. There's something I have to do."
                        show eve 6 at right
                        show player 13 at left
                        eve "I guess you really do have a curfew..."
                        show eve 1 at right
                        show player 2 at left
                        player_name "Sorry. I'll come by another time to hang out!"
                        show eve 7 at right
                        show player 13 at left
                        eve "Alright then..."
                        hide player 13 at left with dissolve
                        hide eve 7 at right with dissolve
                        $ callScreen(location_count)
            "I should go home.":

                show eve 1 at right
                show player 10 at left
                player_name "Oh crap! I have to go. There's something I have to do."
                show eve 2 at right
                show player 13 at left
                eve "I guess you really do have a curfew..."
                show eve 1 at right
                show player 2 at left
                player_name "Sorry. I'll come by another time to hang out!"
                show eve 7 at right
                show player 13 at left
                eve "Yeah, whatever."
                hide player 13 at left with dissolve
                hide eve 7 at right with dissolve
                $ callScreen(location_count)
        $ eve_park_dialogue = 1
    else:

        scene park_bench
        show player 1 at left with dissolve
        show eve 6 at right with dissolve
        eve "Hey {b}[firstname]{/b}!"
        show eve 5 at right
        show player 14 at left
        player_name "Hey, {b}Eve{/b}!"
        show eve 6 at right
        show player 1 at left
        eve "I'm glad you showed up!"
        show eve 3 at right
        show player 14 at left
        player_name "It's nice seeing you again..."
        show eve 4 at right
        show player 1 at left
        eve "So what's up?"
        menu:
            "Let's rap battle.":
                show player 33 at left
                show eve 5 at right
                player_name "I wanna rap battle again!"
                show eve 6 at right
                show player 1 at left
                eve "Oh yah??"
                show eve 5 at right
                show player 26 at left
                player_name "Yeah! I think I'm getting better."
                show eve 6 at right
                show player 1 at left
                eve "That's cool!"
                show eve 8 at right
                eve "Okay. Here's your mic..."
                show eve 1 at right
                show player 70 at left
                player_name "Hmmm... Who should I battle?"
                menu:
                    "Chico":
                        $ rap_opponent = "chico"
                        show player 71 at left
                        player_name "I'll go against {b}Chico{/b} first."
                        hide eve 1 at right with dissolve
                        jump chico_before_battle

                    "<>[chr_warn]Chad" if pStats.chr()< 4:
                        $ pass

                    "Chad" if pStats.chr() >= 4:
                        $ rap_opponent = "chad"
                        show player 71 at left
                        player_name "I'll go against {b}Chad{/b}."
                        hide eve 1 at right with dissolve
                        jump chad_before_battle

                    "<>[chr_warn]Tyrone" if pStats.chr() < 7:
                        $ pass

                    "Tyrone" if pStats.chr() >= 7:
                        $ rap_opponent = "tyrone"
                        show player 71 at left
                        player_name "I'll go against {b}Tyrone{/b}."
                        hide eve 1 at right with dissolve
                        jump tyrone_before_battle

                    "Skip Mini-Game (Cheat)" if cheat_mode:
                        $ gTimer.tick()
                        $ pStats.increase("chr")
                        show unlock23 at truecenter with dissolve
                        $ renpy.pause()
                        $ callScreen(location_count)
            "I have to go.":

                show player 10 at left
                show eve 1 at right
                player_name "Actually, I have to go. There's something I have to do."
                show player 13 at left
                show eve 6 at right
                eve "But, you just got here..."
                show eve 1 at right
                show player 2 at left
                player_name "Sorry. I'll come by another time to hangout!"
                show eve 7 at right
                show player 13 at left
                eve "Alright then..."
                hide player 13 at left with dissolve
                hide eve 7 at right with dissolve
                $ callScreen(location_count)

label chico_before_battle:
    if chico_battle_count == 0:
        scene park_bench
        show douche 1 at right with dissolve
        show player 77 at left with dissolve
        player_name "Hey guys!"
        hide douche 1 at right
        show douche 2 at right
        show chico 3
        hide player 77
        show player 77 at left
        with dissolve
        chi "Who the fuck're you?!"
        show player 74 at left
        show chico 1
        show player 71 at left
        player_name "Oh, hi! I'm {b}[firstname]{/b}!"
        player_name "And I'm guessing you're... {b}Chico{/b}?"
        show chico 2
        show player 74 at left
        chi "You don't know me, foo!"
        show chico 1
        show player 71 at left
        player_name "Well, {b}Eve{/b} just told me your name so-"
        show chico 3 with hpunch
        show player 74 at left
        chi "{b}YO{/b}! Shut the {b}fuck{/b}, {b}UP{/b}!"
        show player 75 at left
        show chico 1
        player_name "..."
        show chico 4
        show player 74 at left
        chi "I'm going first, now {b}step up{/b}!"
        hide player 74
        hide chico 4
        hide douche
        with dissolve
        $ chico_battle_count = 1
        jump rapbattle_listing
    else:

        scene park_bench
        show douche 1 at right with dissolve
        show player 77 at left with dissolve
        player_name "Hey guys!"
        hide douche 1 at right
        show douche 2 at right with dissolve
        show chico 3
        hide player
        show player 74 at left
        with dissolve
        chi "You back for some more? You lil'punk!"
        show chico 1
        show player 71 at left
        player_name "Hey {b}Chico{/b}!"
        player_name "Yah, let's do it!"
        show chico 4
        show player 74 at left
        chi "I'm going first. Now {b}step up{/b}!"
        hide player 74 at left with dissolve
        hide chico 4 with dissolve
        jump rapbattle_listing

label chad_before_battle:
    show player 1 at left
    show chad 2 at right
    with dissolve
    chad "So you’re the the kid who beat Chico."
    chad "Don’t know why you’re stepping up to me though unless you think you can beat me somehow."
    show chad 1
    show player 2
    player_name "That's exactly what I'm thinking."
    show chad 4
    show player 1
    chad "Check this out! Punk has balls!"
    chad "I’ll play your game, just know you aren’t leaving here the same way you came in."
    jump rapbattle_listing

label tyrone_before_battle:
    show tyrone 2 at right
    show player 1 at left
    with dissolve
    tyrone "Ay who is this fool?"
    show tyrone 1
    show player 2
    player_name "Hey I’m-"
    show player 3
    show tyrone 3
    tyrone "Was I asking you!"
    show player 12
    show tyrone 1
    player_name "No, but I thought-"
    show tyrone 2
    tyrone "You thought wrong!"
    tyrone "Now you tryin’ to get your ass beat, or you here to waste my damn time?"
    show tyrone 4
    show player 12
    player_name "Neither?"
    show player 1
    show tyrone 3
    tyrone "Boi, I only gave you two options, and you’re doing the latter, right now!"
    show tyrone 2
    tyrone "Let me just roast you, and get this over with!"
    jump rapbattle_listing

label eve_after_win:
    scene park_bench
    show player 76 at left
    show eve 4 at right with dissolve
    eve "Wow! That was great!"
    show player 77 at left
    show eve 5 at right
    player_name "Thanks!"
    show eve 7 at right
    show player 76 at left
    eve "Are you sure this was your first time??"
    show eve 5 at right
    show player 71 at left
    player_name "Yeah!"
    show eve 6 at right
    show player 76 at left
    eve "Well, I'm glad you tried it. You should come back again, soon!"
    show eve 5 at right
    show player 77 at left
    player_name "Sure! I think I will!"
    show eve 6 at right
    show player 76 at left
    player_name "I have to go home now! I'll see you next time!"
    show eve 5 at right
    show player 77 at left
    eve "Okay. Good night!"
    hide player 77 at left with dissolve
    hide eve 5 at right with dissolve
    $ eve_park_dialogue = 1
    $ callScreen(location_count)

label eve_after_lose:
    scene park_bench
    show player 71 at left
    show eve 1 at right with dissolve
    player_name "That was pretty bad..."
    show eve 6 at right
    show player 76 at left
    eve "Haha! Yeah..."
    show eve 7 at right
    eve "But it's okay; you'll get better at it."
    show eve 1 at right
    show player 71 at left
    player_name "I don't know if I'm cut out for this..."
    show eve 6 at right
    show player 76 at left
    eve "Don't say that!"
    show eve 7 at right
    eve "The guys will get to know you, so it won't be so bad."
    show eve 1 at right
    show player 71 at left
    player_name "Yeah. Perhaps..."
    show eve 6 at right
    show player 76 at left
    eve "I have to go now, but I think you should come back again next time!"
    show eve 1 at right
    show player 77 at left
    player_name "Alright. Good night!"
    show eve 6 at right
    show player 76 at left
    eve "See ya!"
    hide player 76 at left with dissolve
    hide eve 6 at right with dissolve
    $ eve_park_dialogue = 1
    $ callScreen(location_count)

label fountain_dialogue:
    scene expression gTimer.image("park_fountain{}")
    if weird_coin not in inventory.items:
        show expression gTimer.image("objects/object_coin_01{}.png") at Position(xalign = 0.44, yalign = 0.81)
    player_name "( I can see a lot of coins in there. )"
    $ callScreen("Park Fountain", False, False)

label coin_dialogue:
    show closeup_coin_01 at Position(xalign = 0.5, yalign = 1.0) with dissolve
    player_name "Huh?"
    player_name "That looks like a really old coin."
    player_name "Just look at these odd {b}symbols{/b}!"
    player_name "I should keep it. Maybe it's worth something?"
    show popup_item_coin1 at truecenter with dissolve
    $ inventory.items.append(weird_coin)
    pause
    hide popup_item_coin1 with dissolve
    hide closeup_coin_01 with dissolve
    $ callScreen("Park Fountain", False, False)

label park_night_closed:
    scene park_night
    show player 10 with dissolve
    player_name "( It's getting late. I should go home. )"
    hide player
    hide park_night
    $ callScreen(location_count)