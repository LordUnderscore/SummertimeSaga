default current_camshow = 1

label MC_computer:
    if gTimer.is_night():
        scene bedroom_night
        show player 24 at left
        player_name "( I'm so tired right now, I better go to bed... )"
        hide player 17 at left
        $ callScreen(location_count)
    else:
        call screen MC_computer

label MC_pass_check:
    if MC_pass.lower().strip() == "cookies":
        scene expression gTimer.image("backgrounds/computer_player_01{}.jpg")
        $ MC_comp_locked = False
        call screen MC_computer
    else:
        scene expression gTimer.image("backgrounds/computer_player_01{}.jpg")
        show sis_wrong_pass at Position(xpos=570, ypos= 448) with dissolve
        $ renpy.pause()
        hide sis_wrong_pass with dissolve
        call screen MC_computer

label egay_search_dialogue:
    if erik.started(erik_orcette):
        scene player_computer_bg
        show player_computer_egay_search
        player_name "( Hmm... I guess I should just type in the name of the item Erik wanted. )"
        player_name "( What was it again? )"
        hide player_computer_egay_search
        hide player_computer_bg
    show screen MC_computer
    call screen egay("Search")

label egay_purchased_dialogue:
    scene player_computer_bg
    show player_computer_egay_purchased
    player_name "( Looks like I should get the package in the mailbox on {b}Tuesday{/b}. )"
    hide player_computer_egay_purchased
    hide player_computer_bg
    show screen MC_computer
    call screen egay("Purchased")

label egay_search:
    if erik.started(erik_orcette):
        if egay_search.lower() == "orcette":
            show screen MC_computer
            call screen egay("Found")
    show screen MC_computer
    call screen egay("Fail")

label webcam_dialogue:
    scene expression gTimer.image("MC_computer{}_b")
    if not connected:
        scene player_computer_bg
        show player_computer_webscreen
        player_name "( Weird. It says I can connect my computer to the {b}webcam{/b}, but it seems I can't do it from here. )"
        hide player_computer_webscreen
        hide player_computer_bg
        call screen MC_computer

    elif (not shower.occupied("sis", False) and gTimer.is_morning()):
        if sister.started(sis_webcam01):
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(ypos = 746)
            sis "Hey guuuys!"
            sis "Are you ready for some hot camming?"
            sis "I've been looking forward to getting wet all day!"
            sis "Oh! Don't forget to subscribe to watch the next part of the show..."
            sis "Because this beauty right here needs money!"
            show sissex 8 with fastdissolve
            sis "Now, for my special subscribers..."
            sis "... I have this brand new toy I wanted to try!"
            show sissex 7 with fastdissolve
            pause
            show sissex 10 with fastdissolve
            pause
            show sissex 9
            sis "The {b}Electro Clit{/b}!"
            sis "It's a little vibrating friend ... for my clit!"
            show sissex 11
            sis "I've always wanted one of these!"
            show sissex 21 at Position(xpos = 543, ypos = 767) with dissolve
            sis "Let's give it a try, boys..."
            show sissex 22 with fastdissolve
            sis "Woah! This thing is fast..."
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow01_loop:
                $ current_camshow = 1
                show sissex 22 at Position(xpos = 543, ypos = 767)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 22
                    hide screen camshow_buttons
                    show sissex 23_24_25_22 at Position(xpos = 543, ypos = 767)
                    pause 8
                    hide sissex 23_24_25_22
                    show sissex 22 at Position(xpos = 543, ypos = 767)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 23
                        pause
                        show sissex 24
                        pause
                        show sissex 25
                        pause
                        show sissex 22
                        pause
                        $ animcounter += 1
                    show sissex 23
                    pause
                    show sissex 24
                    pause
                    show sissex 25
                    pause
                    show sissex 22
                call screen camshow_options

            label sis_camshow01_finish:
                show sissex 25b
                sis "Ahhh!!!" with vpunch
                sis "{b}*panting*{/b}"
                sis "That was awesome!"
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "Woah..."
                player_name "( My sister's a camgirl?! )"
                show player 310
                player_name "( I'm not sure how to feel about this. )"
                player_name "( It's so weird seeing her like that... )"
                show player 312
                player_name "Man, I know I shouldn't find this hot, but..."
                show player 310
                player_name "( I think that's enough for now. )"
                hide player
                $ sis_webcam01.finish()
                if not sister.known(sis_telescope01):
                    $ sister.add_event(sis_telescope01)
                $ gTimer.tick()
                $ callScreen(location_count)

        elif sister.started(sis_webcam02):
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(ypos = 746)
            sis "Hey guuuys!"
            sis "Are you ready for some hot camming?"
            sis "I've been looking forward to getting wet all day!"
            sis "Oh! Don't forget to subscribe to watch the next part of the show..."
            sis "Because this beauty right here needs money!"
            show sissex 8 with fastdissolve
            sis "Now, for my special subscribers..."
            sis "... I have this shiny new toy I wanted to try. "
            show sissex 7 with fastdissolve
            pause
            show sissex 13 with fastdissolve
            pause
            show sissex 12
            sis "The {b}Ultra Vibrator 2000{/b}!"
            sis "It's a dildo! Nice and ribbed too..."
            sis "Now, since you kept asking to see some insertion with my toys..."
            sis "... I figured I'd give you all a little treat!"
            sis "Here we go, boys!"
            show sissex 26 at Position(ypos = 770) with dissolve
            sis "This thing looks like the perfect size for me."
            sis "Let's put it to the test..."
            show sissex 27 with fastdissolve
            pause
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow02_loop:
                $ current_camshow = 2
                show sissex 31 at Position(xpos = 512, ypos = 770)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 31
                    hide screen camshow_buttons
                    show sissex 28_29_30_31 at Position(ypos = 770)
                    pause 8
                    hide sissex 28_29_30_31
                    show sissex 31 at Position(ypos = 770)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 28
                        pause
                        show sissex 29
                        pause
                        show sissex 30
                        pause
                        show sissex 31
                        pause
                        $ animcounter += 1
                    show sissex 28
                    pause
                    show sissex 29
                    pause
                    show sissex 30
                    pause
                    show sissex 31
                call screen camshow_options

            label sis_camshow02_finish:
                show sissex 28b
                sis "Oh my... I'm almost there..."
                show sissex 29b
                sis "I'm... Cumming!!"
                show sissex 32
                sis "Ahh!!!" with vpunch
                show sissex 33 with dissolve
                sis "I... I've never had this happen before..."
                sis "What a mess..."
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "( So that's what squirting looks like. )"
                show player 310
                player_name "There was so much! She even hit the camera!"
                player_name "( I had no idea {b}[sis_name]{/b} could do that... )"
                hide player
                $ sis_webcam02.finish()
                if not sister.known(sis_telescope02):
                    $ sister.add_event(sis_telescope02)
                $ gTimer.tick()
                $ callScreen(location_count)

        elif sister.started(sis_webcam03):
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(xpos = 534, ypos = 746)
            sis "Hey guuuys!"
            sis "Are you ready for some hot camming?"
            sis "I've been looking forward to getting wet all day!"
            sis "Oh! And don't forget to subscribe to watch the next part of the show..."
            sis "Because this beauty right here needs money!"
            show sissex 8 with fastdissolve
            sis "Now, for my special subscribers..."
            sis "I have this double pleasure toy I wanted to try. "
            show sissex 7 with fastdissolve
            pause
            show sissex 19 at Position(xpos = 577) with fastdissolve
            pause
            show sissex 18 with fastdissolve
            sis "The {b}Dual Sybian{/b}!"
            show sissex 20
            sis "I've been reading complaints online that I'm scared to do anal..."
            sis "So here's proof that I am NOT scared to try it!"
            sis "In fact, why stop at one hole?"
            sis "For my fans, I'm gonna do double penetration!"
            show sissex 18
            sis "Let me hop on top of this bull and get my anal cherry popped..."
            show sissex 34 at Position(xpos = 344, ypos = 727) with dissolve
            pause
            show sissex 35 at Position(xpos = 473, ypos = 582) with fastdissolve
            sis "... Oh god! That's a strange feeling."
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow03_loop:
                $ current_camshow = 3
                show sissex 35 at Position(xpos = 473, ypos = 582)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 35
                    hide screen camshow_buttons
                    show sissex 36_37_38_35 at Position(xpos = 473, ypos = 582)
                    pause 8
                    hide sissex 36_37_38_35
                    show sissex 35 at Position(xpos = 473, ypos = 582)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 36 at Position(xpos = 465)
                        pause
                        show sissex 37 at Position(xpos = 518)
                        pause
                        show sissex 38 at Position(xpos = 524)
                        pause
                        show sissex 35 at Position(xpos = 473)
                        pause
                        $ animcounter += 1
                    show sissex 36 at Position(xpos = 465)
                    pause
                    show sissex 37 at Position(xpos = 518)
                    pause
                    show sissex 38 at Position(xpos = 524)
                    pause
                    show sissex 35 at Position(xpos = 473)
                call screen camshow_options

            label sis_camshow03_finish:
                show sissex 39 at Position(xpos = 568)
                sis "Ahhh!!!" with hpunch
                sis "{b}*panting*{/b}"
                sis "I've never cum this hard before..."
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "Wow..."
                player_name "( She really loves riding that thing. )"
                show player 310
                player_name "( I wonder what else she's willing to do on camera... )"
                hide player
                $ sis_webcam03.finish()
                if not sister.known(sis_telescope03):
                    $ sister.add_event(sis_telescope03)
                $ gTimer.tick()
                $ callScreen(location_count)

        elif sister.over(sis_webcam04):
            $ sis_lastwebcam_show_seen = True
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(xpos = 534, ypos = 746)
            sis "Hey guuuys!"
            sis "Are you ready for some hot camming?"
            sis "I've been looking forward to getting wet all day!"
            sis "Oh! And don't forget to subscribe to watch the next part of the show..."
            sis "Because this beauty right here needs money!"
            show sissex 8 with fastdissolve
            sis "Now, for my special subscribers..."
            sis "... I have this scary new toy I wanted to try. "
            show sissex 7 with fastdissolve
            pause
            show sissex 16 with fastdissolve
            pause
            show sissex 15
            sis "This right here is..."
            sis "THE {b}Bad Monster{/b}!"
            show sissex 17
            sis "Everyone's been talking about this special toy..."
            sis "... and some of you dared me to let it ravage my pussy."
            show sissex 15
            sis "I finally managed to get my hands on one!"
            show sissex 17
            sis "Now get your wallets ready, because I'm about to tame this monster!"
            show sissex 40 at Position(xpos = 427)
            sis "This one needs a LOT of lube..."
            show sissex 41 at Position(xpos = 423)
            sis "... oh GOD!"
            sis "It's so big!"
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow04_loop:
                $ current_camshow = 4
                show sissex 41 at Position(xpos = 423, ypos = 746)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 41
                    hide screen camshow_buttons
                    show sissex 42_43_44_41 at Position(xpos = 423, ypos = 746)
                    pause 8
                    hide sissex 42_43_44_41
                    show sissex 41 at Position(xpos = 423, ypos = 746)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 42 at Position(xpos = 425)
                        pause
                        show sissex 43 at Position(xpos = 426)
                        pause
                        show sissex 44 at Position(xpos = 425)
                        pause
                        show sissex 41 at Position(xpos = 423)
                        pause
                        $ animcounter += 1
                    show sissex 42 at Position(xpos = 425)
                    pause
                    show sissex 43 at Position(xpos = 426)
                    pause
                    show sissex 44 at Position(xpos = 425)
                    pause
                    show sissex 41 at Position(xpos = 423)
                    pause
                call screen camshow_options

            label sis_camshow04_finish:
                show sissex 43 at Position(xpos = 426)
                sis "Ahhh!!!" with vpunch
                show sissex 45 at Position(xpos = 428) with fastdissolve
                sis "What a GOOD monster..."
                sis "... my pussy will be sore for days!"
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "( I thought that thing was just for show. )"
                player_name "( Apparently it's possible to fit it in there! )"
                player_name "She did it so easily too..."
                player_name "( I hope she doesn't get in trouble for doing this sort of thing on camera. )"
                hide player
                $ gTimer.tick()
                $ callScreen(location_count)
        else:

            scene player_computer_bg
            show player_computer_webscreen
            player_name "( Theres nothing displaying at the moment. )"
            hide player_computer_webscreen
            hide player_computer_bg
            show screen MC_computer
            call screen MC_webcam
    else:
        scene player_computer_bg
        show player_computer_webscreen
        player_name "( Theres nothing displaying at the moment. )"
        hide player_computer_webscreen
        hide player_computer_bg
        show screen MC_computer
        call screen MC_webcam