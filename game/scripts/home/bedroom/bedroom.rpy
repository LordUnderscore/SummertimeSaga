default MC_computer_broken = True
default cookies_taken = False
default first_mom_visit = False

label bedroom_dialogue:
    $ location_count = "Bedroom"
    if not M_player.is_set("just wokeup"):
        if M_mom.get_state() == S_mom_mrsj_visit and not gTimer.is_dark():
            jump home_front

        elif M_mom.get_state() == S_mom_car_fixed:
            jump home_front

        elif M_mom.get_state() == S_mom_bad_guys_revisit and not gTimer.is_dark():
            jump home_front

        elif M_mom.get_state() == S_mom_diane_visit and gTimer.is_evening():
            jump home_entrance

    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump erik_bullying_3

    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom{}"

    if M_player.get_state() == S_player_start and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        player_name "Ugh... I hate getting up early."
        show player 9
        player_name "( No text messages from {b}Erik{/b}. Maybe he's still sleeping. )"
        player_name "( I'll stop by his house on the way to school. )"
        hide player 9 with dissolve

    elif gTimer.is_morning() and not gTimer.is_weekend() and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        window hide
        pause
        show player 9
        player_name "( I should get ready for school... )"
        hide player with dissolve

    elif gTimer.is_morning() and gTimer.is_weekend() and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        window hide
        pause
        show player 9
        player_name "( What should I do this weekend... )"
        hide player with dissolve

    if gTimer.gameDay() >= event_wait_till and not erik.known(erik_bullying):
        scene black with fade
        mom "Sweetie?"
        pause
        mom "Wake up, Sweetie."
        scene expression gTimer.image(tmp_image) with fade
        show mom 14f at left
        show player 101bf at right
        with dissolve
        player_name "Huh? {b}[mom_name]{/b}? What time is it?"
        show player 100bf
        show mom 13f
        mom "{b}Mrs. Johnson{/b} is at the door asking to see you."
        show mom 14f
        show player 101bf
        player_name "{b}Mrs. Johnson{/b}? For me?"
        show player 100bf
        show mom 13f
        mom "She hasn't said much, but she wanted to talk with you before you headed to school."
        show mom 14f
        show player 101bf
        player_name "Oh. Ok. Let me get dressed and I'll be down soon."
        show player 100bf
        show mom 13f
        mom "Alright..."
        show mom 14f
        pause
        show mom 13f
        mom "Is there anything I need to know about, {b}[firstname]{/b}?"
        show mom 14f
        player_name "..."
        show player 101bf
        player_name "I have no idea why she's here either, {b}[mom_name]{/b}."
        show player 100bf
        mom "..."
        show mom 13f
        mom "Ok, Sweetie."
        hide mom
        hide player
        with dissolve
        $ lock_ui()
        $ erik.add_event(erik_bullying)

    elif M_mia.get_state() == S_mia_tattoo_help and M_mia.is_set('story delay'):
        scene expression gTimer.image(tmp_image)
        show player 35 with dissolve
        player_name "( I have to make something nice for her tattoo idea. )"
        show player 34
        player_name "Hmm..."
        show player 35
        player_name "( Perhaps, I can use one of the {b}easels in art class{/b}! )"
        show player 33
        player_name "( I can use it to come up with a nice design for her. )"
        show player 8 with dissolve
        pause
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 101 with dissolve
        player_name "I should sleep."
        hide player with dissolve
        show unlock53 at truecenter with dissolve
        pause
        hide unlock53 with dissolve
        $ M_mia.trigger(T_mia_tattoo_start)

    elif M_mia.get_state() == S_mia_strip_aftermath and M_mia.is_set('story delay'):
        scene expression gTimer.image(tmp_image)
        show player 24 with dissolve
        player_name "( I can't believe I won't be able to see {b}Mia{/b} anymore. )"
        show player 25
        player_name "( Her parents don't trust me. )"
        show player 35
        player_name "( Perhaps I can make it up to them somehow... )"
        hide player with dissolve
        $ M_mia.trigger(T_mia_grounded)

    elif M_mia.get_state() == S_mia_strip_aftermath:
        scene expression gTimer.image(tmp_image)
        show player 4 with dissolve
        pause
        show player 30 at Position (xoffset=-6) with dissolve
        player_name "( I wonder how {b}Mia{/b} is doing. )"
        show player 12 at Position (xoffset=-6)
        player_name "( It's been a few days, and I haven't heard anything from her... )"
        player_name "( ...Perhaps I should visit her and see how she's doing... )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_urgent_message:
        scene expression gTimer.image(tmp_image)
        show player 12 with dissolve
        player_name "Huh?"
        show player 9 at Position (xoffset=40) with dissolve
        pause
        show player 14 with dissolve
        player_name "( Looks like I got a text message... )"
        hide player with dissolve
        $ lock_ui()
        if m_mia02 not in message_list:
            $ message_list.append(m_mia02)
            $ new_message = True

    elif M_mia.get_state() == S_mia_angelicas_impatience:
        scene expression gTimer.image(tmp_image)
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "( I should get ready for- )"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "There's someone downstairs who's here for you."
        show mom 1f
        show player 30f
        player_name "{b}Erik{/b}?"
        show player 11f
        show mom 2f
        mom "No, Sweetie. It's a lady!"
        mom "She says you two have spoken before..."
        show mom 1f
        show player 10f
        player_name "What?"
        player_name "But who-"
        show player 5f
        show mom 2f
        mom "She's waiting downstairs. Why don't you {b}get dressed and come down{/b}."
        hide mom with dissolve
        show player 12f player_name "A lady?!"
        show player 4f at Position (xoffset=-6) with dissolve
        player_name "Huh..."
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_home_visit:
        scene expression gTimer.image(tmp_image)
        show player 13f at right
        show mom 2f at left
        mom "Sweetie?"
        show mom 1f
        show player 17f
        player_name "Good morning, {b}[mom_name]{/b}."
        show player 13f
        show mom 2f
        mom "Morning."
        mom "That nice lady from the other day is downstairs again."
        show mom 1f
        show player 11f
        player_name "..."
        show player 12f
        player_name "Who?"
        show player 5f
        show mom 3f
        mom "Come on now, sleepyhead. The nun is here again."
        show mom 1f
        show player 22f
        player_name "!!!"
        mom "Hurry up so you can meet her downstairs."
        hide mom with dissolve
        show player 10f
        player_name "What is she going to want now?"
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_final_home_visit:
        scene expression gTimer.image(tmp_image) with fade
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "I should get ready for-"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "That nun is here again..."
        show mom 1f
        show player 30f
        player_name "Again?"
        show player 24f
        pause
        show mom 13f
        mom "I've been meaning to ask..."
        mom "What exactly are you doing for the church?"
        show mom 14f
        show player 11f
        player_name "..."
        show mom 13f
        mom "I mean, I'm surprised to see a nun visiting so much..."
        show mom 14bf
        show player 29f at Position (xoffset=-35) with dissolve
        player_name "Yeah, um... everything is... fine."
        player_name "She's just... got me running errands."
        player_name "( Yeah, heh... heh... )"
        show player 3f at Position (xoffset=-35)
        show mom 14f
        mom "..."
        show mom 13f
        mom "Well, at least you're doing something good for the community..."
        show player 5f with dissolve
        show mom 2f
        mom "I suppose I shouldn't be worried."
        show mom 3f
        mom "What harm could come from you spending time at church?"
        hide mom with dissolve
        show player 11f
        player_name "..."
        show player 37f at Position (xoffset=-41) with dissolve
        player_name "( You have no idea... )"
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_impatience:
        scene expression gTimer.image(tmp_image)
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "I should get ready for-"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "There's someone downstairs who's here for you."
        show mom 1f
        show player 30f
        player_name "{b}Erik{/b}?"
        show player 11f
        show mom 2f
        mom "No, Sweetie. It's a lady!"
        mom "She says you two have spoken before..."
        show mom 1f
        show player 10f
        player_name "What?"
        player_name "But who-"
        show player 5f
        show mom 2f
        mom "She's waiting downstairs. Why don't you {b}get dressed and come down{/b}."
        hide mom with dissolve
        show player 12f player_name "A lady?!"
        show player 4f at Position (xoffset=-6) with dissolve
        player_name "Huh..."
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_home_visit:
        scene expression gTimer.image(tmp_image) with fade
        show player 13f at right
        show mom 2f at left
        mom "Sweetie?"
        show mom 1f
        show player 17f
        player_name "Good morning, {b}[mom_name]{/b}."
        show player 13f
        show mom 2f
        mom "Morning."
        mom "That nice lady from the other day is downstairs again."
        show mom 1f
        show player 11f
        player_name "..."
        show player 12f
        player_name "Who?"
        show player 5f
        show mom 3f
        mom "Come on now, sleepyhead. The nun is here again."
        show mom 1f
        show player 22f
        player_name "!!!"
        mom "Hurry up so you can meet her downstairs."
        hide mom with dissolve
        show player 10f
        player_name "What is she going to want now?"
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_final_home_visit:
        scene expression gTimer.image(tmp_image) with fade
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "I should get ready for-"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "That nun is here again..."
        show mom 1f
        show player 30f
        player_name "Again?"
        show player 24f
        pause
        show mom 13f
        mom "I've been meaning to ask..."
        mom "What exactly are you doing for the church?"
        show mom 14f
        show player 11f
        player_name "..."
        show mom 13f
        mom "I mean, I'm surprised to see a nun visiting so much..."
        show mom 14bf
        show player 29f at Position (xoffset=-27) with dissolve
        player_name "Yeah, um... everything is...fine."
        player_name "She's just...got me running errands."
        player_name "Yeah, heh...heh..."
        show player 3f at Position (xoffset=-35)
        show mom 14f
        mom "..."
        show mom 13f
        mom "Well, at least you're doing something good for the community..."
        show player 5f with dissolve
        show mom 2f
        mom "I suppose I shouldn't be worried."
        show mom 3f
        mom "What harm could come from you spending time at church."
        hide mom with dissolve
        show player 11f
        player_name "..."
        show player 37f at Position (xoffset=-41) with dissolve
        player_name "You have no idea..."
        hide player with dissolve
        $ lock_ui()

    if M_mom.get_state() == S_mom_overheard and gTimer.is_dark():
        scene expression gTimer.image(tmp_image)
        show player 34 with dissolve
        player_name "...{b}*distant voice*{/b}..."
        show player 35
        player_name "( Is that {b}[mom_name]{/b} on the phone? )"
        show player 12
        player_name "( ...She sounds like she's mad... Is she yelling? )"
        show player 10
        player_name "( I should go see if she's okay. )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_check)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_doorbell:
        scene expression gTimer.image(tmp_image)
        show player 12 with dissolve
        player_name "( Doorbell's ringing, someone's at the door. )"
        player_name "( Must be {b}Erik{/b} or something... )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_check_door)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_movie_afterthoughts:
        scene expression gTimer.image(tmp_image)
        show player 5
        player_name "Well that was super awkward!"
        player_name "There is no way she didn't notice..."
        player_name "I mean, she didn't say anything."
        player_name "... but it definintely got uncomfortable."
        show player 11
        player_name "I hope {b}[mom_name]{/b} isn't upset with me..."
        player_name "..."
        show player 24
        player_name "Ugh, I'll worry about it tomorrow. Right now, I need some sleep."
        hide player with dissolve
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.get_state() == S_mom_movie_afterthoughts_two:
        scene location_bedroom_blur_night
        show player 13
        player_name "That was hot!"
        player_name "[mom_name]'s wet pussy was rubbing up against me."
        player_name "... And her nipples tasted so good!"
        show player 5
        player_name "..."
        player_name "She kinda freaked out there at the end though."
        player_name "Maybe I should have apologized more?"
        player_name "..."
        show player 13
        player_name "No sense worrying about it now. I should get some sleep."
        hide player with dissolve
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.get_state() == S_mom_note and gTimer.is_dark():
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 101 with dissolve
        player_name "I should sleep."
        hide player with dissolve

    elif M_mom.get_state() == S_mom_note and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 11
        player_name "!!!"
        show player 10
        player_name "Someone left a {b}note{/b} on my computer screen?"
        hide player with dissolve
        $ M_player.set("just wokeup", False)
        $ lock_ui()

    if not gTimer.is_dark():
        if M_player.is_set("just wokeup"):
            if gTimer.is_morning() and not shower.occupied("sis", False) and (
                    sister.started(sis_webcam01) or
                    sister.started(sis_webcam02) or
                    sister.started(sis_webcam03) or
                    (sister.over(sis_webcam04) and not sis_lastwebcam_show_seen)
                    ):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "Hmm..."
                player_name "( I wonder what my {b}Sister{/b} is doing right now. )"
                show player 1
                player_name "( Maybe I could connect to her {b}webcam{/b} from my computer... )"
                hide player with dissolve

            elif sister.started(sis_telescope01) and (not shower.occupied("sis", False) and gTimer.is_morning()):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( I wonder what {b}Erik{/b} is doing right now. )"
                player_name "( I should use my {b}telescope{/b} and see what he's up to... )"
                hide player with dissolve

            elif sister.started(sis_telescope02) and (not shower.occupied("sis", False) and gTimer.is_morning()):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( I wonder what {b}Mia{/b} is doing right now. )"
                player_name "( I should use my {b}telescope{/b} and see what she's up to... )"
                hide player with dissolve

            elif sister.started(sis_telescope03) and (not shower.occupied("sis", False) and gTimer.is_morning()):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( I wonder what {b}Mrs. Johnson{/b} is doing right now. )"
                player_name "( I should use my {b}telescope{/b} and see what she's up to... )"
                hide player with dissolve

            elif training_count == 1 and training_tier == 2 and sister.over(sis_shower_cuddle01) or training_count == 2 and training_tier == 3 and sister.over(sis_couch02) or training_count == 3 and training_tier == 4 and sister.over(sis_couch03):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( I wonder if {b}Master Somrak{/b} is ready to train me again. )"
                hide player with dissolve

            if M_mom.is_set("chores"):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                if randomizer() < 50:
                    player_name "I wonder if {b}[mom_name]{/b} needs help around the house."
                    player_name "I should go ask her..."
                else:
                    player_name "Wonder if {b}[mom_name]{/b} needs my help with anything else..."
                hide player with dissolve

            elif M_mom.get_state() == S_mom_search_panties:
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( I can't stop thinking about putting that lotion on [mom_name] )"
                player_name "( Her legs are so long and soft.. )"
                player_name "( And she smells so good.. )"
                show player 11
                player_name "( Come to think of it. The lotion was in her panty drawer. )"
                player_name "( I'm dying to go check those panties out... )"
                show player 13
                player_name "( Maybe now is a good time. )"
                hide player with dissolve

            elif M_mom.get_state() == S_mom_kissing_practice:
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "I keep having naughty dreams involving [mom_name]."
                player_name "They are driving me nuts!"
                show player 5
                player_name "..."
                player_name "I should probably {b}talk to her{/b} about it..."
                hide player with dissolve
            $ M_player.set("just wokeup", False)

    elif gTimer.is_evening():
        if sister.started(sis_couch01):
            scene expression gTimer.image(tmp_image)
            show player 10 with dissolve
            player_name "( I hear someone in the hallway... My {b}Sister{/b}'s door? )"
            show player 4
            player_name "( I wonder if she's up to something. )"
            hide player with dissolve

        elif sister.started(sis_couch03):
            scene expression gTimer.image(tmp_image)
            show player 4 with dissolve
            player_name "( I wonder if there's a {b}new porn video{/b} on TV tonight. )"
            show player 26
            player_name "( I should try and check it out while everyone's sleeping... )"
            hide player with dissolve
    $ callScreen(location_count)

label june_bedroom_dialogue:
    $ gTimer.tick()
    $ june_hang_out = False
    if June.in_progress(june_cosplay):
        scene bedroom_sex2
        show player_sitting 2 zorder 1 at right
        show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
        with fastdissolve
        player_name "So, what're we doing?"
        show june_sitting 10
        show player_sitting 5
        june "Is your door locked?"
        show june_sitting 11
        show player_sitting 2
        player_name "Uhh... I think so? Why?"
        show june_sitting 12
        show player_sitting 5
        june "Well, I don't want your parents seeing me while I'm getting dressed up!"
        show june_sitting 11
        show player_sitting 4
        player_name "Oh, you're doing it... right... here?"
        show june_sitting 10
        show player_sitting 5
        june "Of course, silly!"
        june "I might need your help while I put things on..."
        june "And I want your opinion on the whole process!"
        show player_sitting 3
        june "My cosplay has to look just right."
        show june_sitting 11
        show player_sitting 4
        player_name "I see."
        player_name "So... How do we start?"
        show june_sitting 10
        show player_sitting 5
        june "I should probably get undressed first."
        show june_sitting 11
        player_name "..."
        show june_sitting 10
        june "Hold on, let me just get these clothes off..."
        show june_sitting 14 at Position(xoffset=7) with fastdissolve
        pause
        show player_sitting 7
        show june_sitting 15 with fastdissolve
        pause
        show june_sitting 16 at Position(xpos=288) with fastdissolve
        show player_sitting 10 with hpunch
        pause
        show june_sitting 19
        show june_sitting_underwear zorder 2 at Position(xpos=268,ypos=595)
        with fastdissolve
        june "..."
        show june_sitting 20
        june "Ha ha!"
        show player_sitting 5 with fastdissolve
        june "You don't have to hide your eyes, silly!"
        show june_sitting 19
        show player_sitting 4
        player_name "I just... Didn't want-"
        show june_sitting 20
        show player_sitting 5
        june "It's fine, I want you to watch."
        show june_sitting 19
        show player_sitting 4
        player_name "Okay..."
        show june_sitting 20
        show player_sitting 3
        june "I need to remove ALL of my clothes..."
        hide june_sitting_underwear
        show june_sitting 23
        with fastdissolve
        pause
        show june_sitting 24 with fastdissolve
        pause
        show june_sitting 25 at Position(xoffset=40) with fastdissolve
        june "... If we want to make this cosplay right!"
        show june_sitting 19 with fastdissolve
        show player_sitting 4
        player_name "You... You look really good!"
        show june_sitting 22b at Position(xoffset=18)
        show player_sitting 3
        june "Thanks."
        show june_sitting 20
        june "Now, before I put on the actual costume, I need your help with something..."
        show june_sitting 19
        show player_sitting 4
        player_name "How can I help?"
        show player_sitting 11
        show june_sitting 26 at Position(xoffset=24) with fastdissolve
        june "I have to put on body paint... And there's some spots I just can't reach!"
        june "Here, take this and scoop some out with your fingers..."
        show june_sitting 19
        show player_sitting 12
        with fastdissolve
        player_name "Where do I start?"
        show june_sitting 22b at Position(xoffset=18)
        show player_sitting 13 with fastdissolve
        june "Just let your imagination do the work!"
        show black zorder 3 with dissolve
        show june_sitting 29
        show player_sitting 1
        player_name "... Are you sure you want paint down here too?"
        june "Don't be scared, get in there!"
        june "Ooh, that tickles..."
        hide black with dissolve
        june "So?"
        june "How do I look?"
        show june_sitting 28
        show player_sitting 2
        player_name "It's really... convincing!"
        player_name "You really look like an orcette, that's certain..."
        show june_sitting 29
        show player_sitting 5
        june "Do you feel... attracted to my new look?"
        show june_sitting 28
        show player_sitting 4
        player_name "You mean I-"
        show june_sitting 29
        show player_sitting 5
        june "Do you feel horny... looking at me?"
        show june_sitting 28
        show player_sitting 3
        player_name "..."
        show player_sitting 4
        player_name "I think you're very pretty... in green..."
        show june_sitting 29
        show player_sitting 3
        june "Why don't you come closer and kiss me, Chieftain?"
        hide player_sitting
        show june_sitting 31 at center
        with fastdissolve
        pause
        label june_cosplay_sex:
            show junesex 2b
            hide june_sitting
            hide player_sitting
            with fade
            june "I want that big... chieftain cock..."
            june "... deep inside me!"
            show junesex 3b with fastdissolve
            june "Ahh..."
            show junesex 4b with fastdissolve
            june "Yess!"
            june "Bork me, {b}[firstname]{/b}!!"
            $ anim_toggle = False
            $ xray = False
            $ M_june.set('sex speed', .3)

            label june_mcbedroom_cosplay_sex_loop:
                hide screen june_mcbedroom_cosplay_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show junesex 4b_5b_6b_7b_8b
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 3:
                        show junesex 4b
                        pause
                        show junesex 5b
                        pause
                        show junesex 6b
                        pause
                        show junesex 7b
                        pause
                        show junesex 8b
                        pause
                        $ animcounter += 1

            show screen june_mcbedroom_cosplay_sex_options
            pause
            jump june_mcbedroom_cosplay_sex_loop

            label june_mcbedroom_cosplay_sex_cum_inside:
                hide screen june_mcbedroom_cosplay_sex_options
                show junesex 4b_5b_6b_7b_8b
                pause
                show junesex 9b with hpunch
                june "Ahh!!!"
                show white
                pause 0.3
                hide white with dissolve
                pause
                show junesex 14b with fastdissolve
                june "I... that feels so good..."
                june "... your orc seed deep inside me..."
                june "... my chieftain..."
                if June.over(june_cosplay):
                    jump june_aftercum_inside
                else:
                    jump june_aftercum_initial

            label june_mcbedroom_cosplay_sex_cum_outside:
                hide screen june_mcbedroom_cosplay_sex_options
                show junesex 4b_5b_6b_7b_8b
                pause
                show junesex 9b with hpunch
                player_name "Ahh!!!"
                show white
                pause 0.3
                show junesex 10b
                hide white with dissolve
                pause
                show junesex 11b with fastdissolve
                june "..."
                show junesex 12b
                june "So much... cum!"
                june "I was hoping you would hold me down and cum inside..."
                june "... with all that strong orc cum..."
                june "Maybe next time?"
                if June.over(june_cosplay):
                    jump june_aftercum_outside

        label june_aftercum_initial:
        hide junesex
        scene black
        with fade
        scene bedroom_sex2
        show player_sitting 3 zorder 1 at right
        show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
        with fade
        june "That was great!"
        june "It's getting pretty late... I should get home."
        show player_sitting 6
        show june_sitting 11
        player_name "Yeah, my mom is going to get suspicious with all the time we spend in here..."
        show june_sitting 10
        show player_sitting 3
        june "Ha ha."
        june "I think it was time well spent!"
        show june_sitting 11
        show player_sitting 4
        player_name "I had fun too."
        show june_sitting 10
        show player_sitting 3
        june "Maybe we can do this again soon?"
        show june_sitting 11
        show player_sitting 4
        player_name "Sure!"
        show player_sitting 6
        player_name "I'd love to."
        show june_sitting 10
        show player_sitting 3
        june "Okay, I'll see you at school then?"
        show june_sitting 11
        show player_sitting 4
        player_name "Yeah!"
        $ June.complete_events(june_cosplay)
    else:

        scene bedroom_sex2
        if June.over(june_cosplay):
            show june_sitting 3 at Position(xpos=300,ypos=787)
            show player_sitting 1 at right
            with dissolve
            june "Cool room!"
            june "I love your posters and figurines!"
            show june_sitting 4
            show player_sitting 2
            player_name "Ha ha, yeah, they're pretty nice."
            player_name "I've had them since I was a kid."
            player_name "They're sort of... geeky, I guess."
            show june_sitting 3
            show player_sitting 1
            june "I really like them!"
            show june_sitting 4
            show player_sitting 2
            player_name "Thanks."
            show june_sitting 3
            show player_sitting 1
            june "So... What do you wanna do?"
            show june_sitting 4
        else:

            show player_sitting 2 zorder 1 at right
            show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
            with fastdissolve
            player_name "So, what's the plan?"
            show june_sitting 10
            show player_sitting 1
            june "Is your door locked?"
            show player_sitting 2
            show june_sitting 11
            player_name "Yeah. I don't think my mom will be bothering us."
            show june_sitting 10
            june "Cool."
            show player_sitting 1
            show june_sitting 12
            june "It's just that... I really like hanging out in your room..."
            show player_sitting 3
            june "It's so... cozy. I just feel like we can do anything we want, in secret..."
            show player_sitting 4
            show june_sitting 13
            player_name "I like it, too."
            show player_sitting 1
            show june_sitting 10
            june "So, what does my... orc chieftain want from me tonight?"
            show june_sitting 11
        menu:
            "Sex!" if June.over(june_cosplay):
                show player_sitting 2 zorder 1 at right
                show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
                player_name "Do you want to... have sex?"
                show player_sitting 1
                show june_sitting 10
                june "Should I get my costume?"
                show player_sitting 4
                show june_sitting 11
                player_name "Eh, maybe another time?"
                show player_sitting 3
                show june_sitting 12
                june "Okay... I guess we can do it like this."
                show player_sitting 4
                show june_sitting 13
                player_name "You don't mind?"
                show player_sitting 3
                show june_sitting 10
                june "Role playing is really fun, but sure, I'm fine with it..."
                show june_sitting 14 at Position(xoffset=7) with fastdissolve
                pause
                show june_sitting 15 with fastdissolve
                pause
                show june_sitting 16 at Position(xpos=288) with fastdissolve
                pause
                hide june_sitting_underwear
                show june_sitting 23
                with fastdissolve
                pause
                show june_sitting 24 with fastdissolve
                pause
                show june_sitting 25 at Position(xoffset=40) with fastdissolve
                june "Well? What are you waiting for? I'm right here..."
                show june_sitting 30 at center
                hide player_sitting
                with fastdissolve
                pause
                jump june_normal_sex

            "Cosplay sex!" if June.over(june_cosplay):
                show player_sitting 6 at right
                show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
                player_name "I could help you dress up like last time... and be your chieftain?"
                show player_sitting 3
                show june_sitting 10
                june "I was hoping you would suggest that!"
                june "All I've been thinking about is dressing up and becoming your orcette..."
                june "Okay, let put the costume on..."
                show june_sitting 29
                with fade
                june "Why don't you come closer... And kiss me, Chieftain?"
                hide player_sitting
                show june_sitting 31 at center
                with fastdissolve
                pause
                jump june_cosplay_sex
            "Play games.":

                if June.over(june_cosplay):
                    show june_sitting 11 at Position(xpos=300,ypos=787)
                    show player_sitting 2 at right
                    player_name "Do you want to play games again?"
                    show june_sitting 10
                    show player_sitting 1
                    june "Sure, there's still some quests I haven't finished in Orc Bork."
                    show june_sitting 11
                    show player_sitting 6
                    player_name "Let's do it!"
                    show player_sitting 2
                    player_name "Just one thing, could you tell me how to play it again?"
                    show june_sitting 10
                    show player_sitting 1
                    june "Ha ha."
                    june "Sure, come closer so you can see the screen better..."
                    show june_sitting 7 at center
                    hide player_sitting
                    with fastdissolve
                    june "We have to play together and time our attacks."
                    june "When the arrow is in the green bar, press the button!"
                    show june_sitting 8
                    player_name "Oh, okay! Sounds pretty simple."
                    show june_sitting 7
                    june "Let's give it a try!"
                else:

                    show june_sitting 4 at Position(xpos=300,ypos=787)
                    show player_sitting 2 at right
                    player_name "We could try beating that game of yours."
                    show june_sitting 3
                    show player_sitting 1
                    june "Yeah? You really want to?"
                    show june_sitting 4
                    show player_sitting 6
                    player_name "Let's do it!"
                    show player_sitting 2
                    player_name "Just one thing, could you tell me how to play?"
                    show june_sitting 3
                    show player_sitting 1
                    june "Ha ha."
                    june "Well, It's just one of those monster hunting games."
                    june "You go through dungeons, kill monsters, get items..."
                    show player_sitting 5
                    june "... But there's this final boss I've been trying to beat for the longest time!!"
                    show player_sitting 1
                    june "Here, come closer so you can see the screen better..."
                    show june_sitting 8 at center
                    hide player_sitting
                    with fastdissolve
                    player_name "Okay, so how do we beat this boss?"
                    show june_sitting 7
                    june "We have to play together and time our attacks."
                    june "When the arrow is in the green bar, press the button!"
                    show june_sitting 8
                    player_name "Oh, okay! Sounds pretty simple."
                    show june_sitting 7
                    june "Let's give it a try!"
                jump orc_battle_prep
            "I have to sleep.":

                show player_sitting 4 at right
                show june_sitting 6 at Position(xpos=300,ypos=787)
                player_name "Actually, I should really get to bed..."
                show june_sitting 5
                show player_sitting 3
                june "Already?!"
                show june_sitting 6
                show player_sitting 4
                player_name "Yeah... My mom said I need to get to bed earlier."
                player_name "Sorry, {b}June{/b}..."
                show june_sitting 5
                show player_sitting 3
                june "It's alright, I guess."
                june "Maybe we can hang out another time?"
                show june_sitting 6
                show player_sitting 4
                player_name "Sure!"
                show june_sitting 4
                player_name "I'd love to."
                show june_sitting 3
                show player_sitting 3
                june "Okay, see you at school?"
                show june_sitting 4
                show player_sitting 4
                player_name "Yeah!"
                hide june_sitting
                hide player_sitting
                with dissolve
                jump sleeping
    $ callScreen(location_count)

label june_normal_sex:
    show junesex 2
    hide june_sitting
    hide player_sitting
    with fade
    june "I want that big cock of yours..."
    june "... deep inside me!"
    show junesex 3 with fastdissolve
    june "Ahh..."
    show junesex 4 with fastdissolve
    june "Yess!"
    june "Fuck me, {b}[firstname]{/b}!!"
    $ anim_toggle = False
    $ xray = False
    $ M_june.set('sex speed', .3)

    label june_mcbedroom_normal_sex_loop:
        hide screen june_mcbedroom_normal_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            show junesex 4_5_6_7_8
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 3:
                show junesex 4
                pause
                show junesex 5
                pause
                show junesex 6
                pause
                show junesex 7
                pause
                show junesex 8
                pause
                $ animcounter += 1

    show screen june_mcbedroom_normal_sex_options
    pause
    jump june_mcbedroom_normal_sex_loop

    label june_mcbedroom_normal_sex_cum_inside:
        hide screen june_mcbedroom_normal_sex_options
        show junesex 4_5_6_7_8
        pause
        show junesex 9 with hpunch
        june "Ahh!!!"
        show white
        pause 0.3
        hide white with dissolve
        pause
        show junesex 14 with fastdissolve
        june "I... that feels so good..."
        june "... your cum deep inside me..."
        jump june_aftercum_inside

    label june_mcbedroom_normal_sex_cum_outside:
        hide screen june_mcbedroom_normal_sex_options
        show junesex 4_5_6_7_8
        pause
        show junesex 9 with hpunch
        player_name "Ahh!!!"
        show white
        pause 0.3
        show junesex 10
        hide white with dissolve
        pause
        show junesex 11 with fastdissolve
        june "..."
        show junesex 12
        june "So much..."
        june "I was hoping you would hold me down and cum inside..."
        june "... with all that strong cum..."
        june "Maybe next time?"
        jump june_aftercum_outside

label june_aftercum_outside:
    hide junesex
    scene black
    with fade
    scene bedroom_sex2
    show player_sitting 3 zorder 1 at right
    show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
    hide junesex
    with fade
    june "That was great!"
    june "It's getting pretty late... I should get home."
    show player_sitting 6
    show june_sitting 11
    player_name "Yeah, my mom is going to get suspicious with all the time we spend in here..."
    show june_sitting 10
    show player_sitting 3
    june "Ha ha."
    june "I think it was time well spent!"
    show june_sitting 11
    show player_sitting 4
    player_name "I had fun too."
    show june_sitting 10
    show player_sitting 3
    june "Maybe we can do this again soon?"
    show june_sitting 11
    show player_sitting 4
    player_name "Sure!"
    show player_sitting 6
    player_name "I'd love to."
    show june_sitting 10
    show player_sitting 3
    june "Okay, I'll see you at school then?"
    show june_sitting 11
    show player_sitting 4
    player_name "Of course!"
    $ callScreen(location_count)

label june_aftercum_inside:
    hide junesex
    scene black
    with fade
    scene bedroom_sex2
    show player_sitting 3 zorder 1 at right
    show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
    hide junesex
    with fade
    june "That was great!"
    june "It's getting pretty late... I should get home."
    show player_sitting 6
    show june_sitting 11
    player_name "Yeah, my mom is going to get suspicious with all the time we spend in here..."
    show june_sitting 10
    show player_sitting 3
    june "Ha ha."
    june "I think it was time well spent!"
    show june_sitting 11
    show player_sitting 4
    player_name "I had fun too."
    show june_sitting 13
    show player_sitting 4
    player_name "Hey, uh, about doing it inside..."
    show june_sitting 12
    show player_sitting 5
    june "Oh, don't worry about that, I'll just take a pill."
    show june_sitting 11
    show player_sitting 4
    player_name "Does that mean we can do this again soon?"
    show june_sitting 10
    show player_sitting 3
    june "That depends... Do you want to?"
    show player_sitting 6
    show june_sitting 11
    player_name "I'd love to."
    show june_sitting 10
    show player_sitting 3
    june "Okay, I'll see you at school then?"
    show june_sitting 11
    show player_sitting 4
    player_name "Of course!"
    $ callScreen(location_count)

label bedroom_study01:
    if homework not in inventory.items and homework2 not in inventory.items and homework_done == False:
        scene expression gTimer.image(tmp_image)
        show player 1 with dissolve
        player_name "( I don't have any homework. )"
        hide player with dissolve
        $ callScreen(location_count)

    elif homework_done == True:
        scene expression gTimer.image(tmp_image)
        show player 1 with dissolve
        player_name "( I already did my homework. )"
        hide player with dissolve
        $ callScreen(location_count)
    else:



        scene expression gTimer.image("bedroom{}")
        if not gTimer.is_dark():
            scene studybedroom01 with dissolve
            show text "I spent a good part of the day going through my textbook to complete my homework for {b}Mrs. Bissette{/b}." at Position (xpos= 512, ypos = 700) with dissolve
        else:
            scene studybedroom02 with dissolve
            show text "I spent the whole night going through my textbook to complete my homework for {b}Mrs. Bissette{/b}.\nNow I can go sleep..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve
        hide studybedroom01
        hide studybedroom02
        scene black
        with dissolve
        show unlock20 at truecenter with dissolve
        $ renpy.pause()
        hide unlock20 with dissolve
        if homework in inventory.items:
            $ inventory.items.remove(homework)
            $ inventory.items.append(homework1)
        elif homework2 in inventory.items:
            $ inventory.items.remove(homework2)
            $ inventory.items.append(homework1)
        $ homework_done = True
        $ gTimer.tick()
        $ callScreen(location_count)

label mia_midnight_text:
    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom"
    scene expression gTimer.image(tmp_image)
    show player 442 with dissolve
    player_name "{b}Mia{/b}!? Asking...for help?"
    player_name "What is this all about?"
    player_name "Is she in trouble?"
    show player 443
    player_name "..."
    show player 442
    player_name "Maybe I should {b}go see her now{/b}... Just to make sure she's alright."
    hide player with dissolve
    $ unlock_ui()
    $ M_mia.trigger(T_mia_message)
    $ callScreen(location_count)

label mia_urgent_text:
    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom"
    scene expression gTimer.image(tmp_image)
    show player 10 with dissolve
    player_name "She can't find her dad?"
    player_name "I better go see what's going on..."
    hide player with dissolve
    $ unlock_ui()
    $ M_mia.trigger(T_mia_message)
    $ callScreen(location_count)

label textbook_missing_dialogue:
    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom"
    scene expression gTimer.image(tmp_image)
    show player 73 with dissolve
    player_name "( I first need to get the right school {b}textbook{/b} before I can finish my {b}homework{/b}... )"
    player_name "( I can probably find it at the local {b}library{/b}. )"
    hide player with dissolve
    $ callScreen(location_count)

label bed_locked:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I still have something I need to do before I can sleep... )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label bedroom_check_on_mom:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I should really go check on {b}[mom_name]{/b}... )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label sleeping:
    if not gTimer.is_night() and (M_player.is_set("jerk mom") or M_player.is_set("jerk mia")):
        if MC_computer_broken:
            scene expression gTimer.image("backgrounds/location_bedroom_broken{}.jpg")
        else:
            scene expression gTimer.image("backgrounds/location_bedroom{}.jpg")
        menu:
            "Jerk off.":
                menu:
                    "Mom." if M_player.is_set("jerk mom"):
                        $ M_player.set("sex speed", .4)
                        scene expression gTimer.image("backgrounds/location_bedroom_jerk{}.jpg")
                        show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
                        pause
                        show player 496b
                        player_name "... Mom is so beautiful."
                        player_name "I just can't stop thinking about it."
                        player_name "... about her."
                        player_name "Mmm, God, I want her so bad!"
                        show player 496c
                        show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
                        pause
                        show momd 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
                        pause
                        show momd 2
                        mom "Well Hello there..."
                        show momd 1
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        show momd 2
                        mom "Oh gosh... Is that for me?"
                        mom "... It's so big!"
                        show momd 1
                        pause
                        show momd 2
                        mom "... and thick."
                        show momd 3 with dissolve
                        mom "Mmm, are you gonna give it to me?"
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        mom "Give it to me, [firstname]!"
                        $ M_mom.set("sex speed", M_mom.get("sex speed") / 1)
                        show momd 4_5
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        pause
                        show player 496f
                        player_name "OH!"
                        show player 496g with flash
                        player_name "HHHNNNGGGG, HHuuuUUHH!!"
                        show player 496h
                        hide jerkbubble
                        hide momd
                        player_name "Haaaah... Haaaah..."
                        player_name "Uuuhh man, I'm covered..."

                    "Mia." if M_player.is_set("jerk mia"):
                        $ M_player.set("sex speed", .4)
                        scene expression gTimer.image("backgrounds/location_bedroom_jerk{}.jpg")
                        show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
                        pause
                        show player 496b
                        player_name "Mia is so cute!"
                        player_name "I can't wait to see her again..."
                        pause
                        player_name "... That cute body of hers."
                        player_name "Mmm..."
                        show player 496c
                        show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
                        pause
                        show miad 1 zorder 2 at Position(xpos=0.735, ypos=0.8) with dissolve
                        pause
                        show miad 2
                        mom "Hey, [firstname]!"
                        show miad 1
                        pause
                        show miad 2
                        mia "Wow, I've never seen one of those before!"
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        mia "Are they all that big?!"
                        show miad 1
                        pause
                        show miad 2
                        mia "I was really hoping you would be my first, [firstname]."
                        show miad 1
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        pause
                        show miad 2
                        mia "Do you think it will fit?"
                        mia "... In my..."
                        show miad 1
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        pause
                        show miad 2
                        mia "...In my pussy?"
                        show player 496f
                        player_name "OH!"
                        show player 496g with flash
                        player_name "HHHNNNGGGG, HHuuuUUHH!!"
                        show player 496h
                        hide jerkbubble
                        hide miad
                        player_name "Haaaah... Haaaah..."
                        player_name "Uuuhh man, I'm covered..."

                scene black with fade
                $ gTimer.tick()
                $ callScreen(location_count)
            "Sleep.":

                $ pass

    if M_mom.get_state() in [S_mom_movie_night, S_mom_movie_night_two]:
        if MC_computer_broken:
            scene expression gTimer.image("bedroom_broken{}")
        else:
            scene expression gTimer.image("bedroom{}")
        show player 101b with dissolve
        player_name "I think I heard {b}[mom_name]{/b} doing something downstairs."
        hide player with dissolve
        $ gTimer.tick(3)
        $ lock_ui()
        $ callScreen(location_count)

    elif M_mom.get_state() == S_mom_sleepover:
        if MC_computer_broken:
            scene expression gTimer.image("bedroom_broken{}")
        else:
            scene expression gTimer.image("bedroom{}")
        show player 101b with dissolve
        player_name "Maybe I should could sleep next to {b}[mom_name]{/b} tonight."
        player_name "She did say I could go visit her at night if I wanted to..."
        hide player with dissolve
        $ callScreen(location_count)

    elif M_mom.is_set("room sneak"):
        jump mom_sleepover

    if erik.over(erik_breastfeeding_2) and not erik.over(erik_thief) and randomizer() > 66:
        if erik.in_progress(erik_thief):
            $ erik_thief.unfinish()
            $ unlock_ui()
        else:

            if not erik.known(erik_thief):
                $ erik.add_event(erik_thief)
            scene location_bedroom_cutscene01 with fade
            pause
            "{b}*Thump*{/b}"
            scene bedroom_cs03 with dissolve
            "{b}*Thump Thump*{/b}"
            player_name "..."
            scene bedroom_cs04 with dissolve
            player_name "What is that noise?"
            scene bedroom_night with fade
            show player 101bf
            player_name "( Sounds like it's coming from outside. )"
            player_name "( ... From {b}Erik{/b}'s yard, maybe? )"
            show player 100bf
            menu:
                "Go back to sleep.":
                    show player 101f
                    player_name "( It's probably just some animal. )"
                    player_name "( I need to get to sleep... )"
                    hide player
                "Use the telescope.":

                    show player 101bf
                    player_name "( I should probably go have a look. )"
                    show player 100f
                    player_name "Hmm..."
                    show player 101bf
                    player_name "( I'll just take a quick peek through my telescope. )"
                    hide player

                    scene windowbackyardnight02a
                    player_name "!?!"
                    player_name "What the..."
                    scene windowbackyardnight02b
                    player_name "( Is that someone sneaking into {b}Erik{/b}'s yard?! )"
                    player_name "( That's the {b}burglar{/b} I've been hearing about in the news! )"
                    scene windowbackyardnight02c
                    player_name "..."
                    player_name "( Is he going into {b}Erik{/b}'s house?! )"

                    scene bedroom_night with fade
                    show player 101bf with dissolve
                    player_name "( This is bad! )"
                    player_name "( What if {b}Erik{/b} and his Mom are in danger? )"
                    player_name "( I should go outside and see what he's doing in {b}Erik{/b}'s yard. )"
                    hide player with dissolve
                    $ gTimer.tick(4)
                    $ erik_thief.finish()
                    $ lock_ui()
                    scene black with fade
                    jump erik_house_dialogue

    elif erik.started(erik_bullying_3):
        scene bedroom_night
        show player 12 with dissolve
        player_name "( Man... What a day. )"
        show player 17
        player_name "( I guess the training at the gym is starting to pay off! )"
        pause
        show player 12
        player_name "( {b}Dexter{/b} is never going to let this go. )"
        player_name "(... I'm gonna need all the training I can get! )"
        show player 8 with dissolve
        pause
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 101 with dissolve
        player_name "( I better get some sleep. )"
        hide player with dissolve
        $ erik_bullying_3.finish()

    elif M_mia.get_state() == S_mia_midnight_call:
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        "{b}Bzzt{/b}!"
        player_name "..."
        "{b}Bzzzzzzt{/b}!"
        scene bedroom_cs04 with dissolve
        player_name "Huh?"
        player_name "Is that my phone?"
        scene black with fade
        pause
        scene bedroom_night
        show player 7 with dissolve
        pause
        show player 101
        player_name "Someone's texting me?"
        player_name "I should see who it is..."
        hide player with dissolve
        $ lock_ui()
        $ gTimer.tick(4)
        if m_mia01 not in message_list:
            $ message_list.append(m_mia01)
            $ new_message = True
        $ callScreen(location_count)

    elif M_mom.get_state() == S_mom_solo_dream:
        scene dream_mom_04 with fade:
            ypos -707
            linear 4.0 ypos 0
        mom "Mmm..."
        mom "Oh, that feels wonderful Sweetie."
        player_name "..."
        player_name "Oh, {b}[mom_name]{/b}..."
        mom "I want you {b}[firstname]{/b}!"
        mom "I want you inside me so bad!"
        player_name "*gulp*"
        player_name "Really?"
        mom "Yesss, please Sweetie. Put it inside Mommy..."
        mom "I need that big cock inside me!"
        player_name "..."
        mom "Kiss me, Baby. I can't wait any longer!!"
        scene dream_mom_05 with dissolve:
            ypos 0
        pause
        player_name "Hnnggg!!" with flash
        pause
        scene dream_mom_05 with flash:
            ypos 0
            linear 4.0 ypos -475
        player_name "... Oooooh..."
        pause

        scene location_bedroom_cutscene06 with fade
        pause
        scene location_bedroom_cutscene07
        player_name "..."
        scene location_bedroom_cutscene08
        player_name "Oh man..."
        pause
        scene location_bedroom_cutscene09
        pause
        player_name "I made a mess..."
        player_name ".. But holy crap, that was intense..."
        player_name "It all felt so real!"
        player_name "Arrgghh, I'm really losing it!"
        player_name "I just can't stop thinking about her!"
        player_name "I want to hold her and kiss her so bad..."
        player_name "Maybe I should try {b}talking to [mom_name] about kissing{/b}?"
        player_name "She seemed kind of into it at first, when I kissed her in the Mall..."
        player_name "Hmm, it's risky but I think it's worth a shot!"
        player_name "I might go nuts if I don't do something..."
        player_name "... But first I should clean up and get some more sleep."
        $ M_mom.trigger(T_mom_dream)

    elif M_mom.get_state() == S_mom_night_visit:
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        scene location_bedroom_cutscene02 with dissolve
        mom "..."
        mom "( I can’t fall asleep. )"
        mom "( Ever since I watched him masturbate... )"
        mom "( I can’t stop thinking about his- )"
        mom "( I just... )"
        mom "( I feel like being close to him... )"
        define fadehold = Fade(0.5, 1.0, 0.5)

        scene location_bedroom_sex01
        show moms 1
        with dissolve
        mom "( My beautiful boy. )"
        mom "( Always there for me. )"
        mom "( ... Always in my thoughts... )"
        show moms 2
        mom "..."
        mom "( I can't even stop thinking about his... )"
        mom "( Body... and the way he looks at me... )"
        show moms 3
        mom "( I just want to see him... )"
        show moms 4
        mom "Hmm..."
        show moms 5
        mom "( There. He must be hot under that blanket. )"
        show moms 6
        mom "( And that bulge... I feel like touching it... )"
        show moms 7_8
        pause 4
        show moms 6
        mom "( It feels like it's getting bigger... )"
        show moms 7_8
        mom "( And harder! )"
        mom "..."
        mom "( I want to see it... )"
        show moms 9
        $ renpy.pause()
        show moms 10
        mom "( It's so tight in there... )"
        show moms 11
        mom "!!!"
        show moms 12
        mom "..."
        mom "( That bulge... It's pretty... )"
        mom "( And so big! )"
        mom "( I can't believe how much he's grown. )"
        mom "( ... )"
        mom "( It seems so long since I've felt one... )"
        mom "( And I miss it so much... )"
        mom "( It's got to be alright if I just touched it... )"
        mom "( As his mother, I should check and see if anything is...abnormal... )"
        show moms 13
        pause
        show moms 14
        pause
        mom "( It's so warm. )"
        mom "( And soft... )"
        show moms 13
        mom "..."
        show moms 13_14
        pause
        mom "( What...am I doing...)"
        mom "..."
        mom "( I know a mother shouldn't be stroking her son's bare cock... )"
        mom "( But... )"
        mom "( I also let him jerk off to my naked body... )"
        pause
        mom "( He was so innoncent when I caught him masturbating and...the way he orgasmed...)"
        mom "..."
        mom "( Would it even fit- )"
        show moms 12
        mom "( Control yourself... )"
        show moms 20
        mom "( But I feel like I want it...)"
        show moms 21
        mom "( No. )"
        mom "( ...I need to leave... )"
        show moms 22 at Position(xpos = 544, ypos = 768)
        player_name "Huh...?"
        show moms 23
        player_name "Hmm..."
        player_name "( Was that? )"
        show moms 24 at Position(xpos = 512, ypos = 768)
        player_name "( Nevermind )"
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.get_state() == S_mom_night_visit_two:
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        scene location_bedroom_cutscene02 with dissolve
        pause
        scene location_bedroom_sex01
        show moms 1
        with dissolve
        mom "( I shouldn't be here... )"
        mom "( ... But I just can't stop thinking about his cock! )"
        mom "( My sweet Baby boy... )"
        show moms 2
        mom "..."
        mom "( Maybe Diane is right; Perhaps I should just relax and let myself go. )"
        mom "( The way that he looks at me, with those hungry eyes... )"
        mom "( Mmm, I'm getting wet just thinking about it... )"
        show moms 3
        mom "( I have to see it! )"
        show moms 4
        mom "Hmm..."
        show moms 5
        mom "( Ooh, this is so wrong... What are you doing, [mom]? )"
        show moms 6
        mom "( It's even bigger than I remember... )"
        show moms 7_8
        pause 4
        show moms 6
        mom "( Mmm and it's getting hard... )"
        show moms 7_8
        mom "( Sooo {b}hard{/b}! )"
        mom "..."
        mom "( ... Maybe I could just take a peak... )"
        show moms 9
        $ renpy.pause()
        show moms 10
        mom "( ... I mean it has to be uncomfortable for him. )"
        mom "( I'm just helping him relax... That's all. )"
        show moms 11
        mom "!!!"
        show moms 12
        mom "..."
        mom "( Oh my God! )"
        mom "( Oooh! )"
        show moms 13
        mom "( It's so soft and warm... )"
        mom "( And it feels so good in my hands... )"
        show moms 13_14
        mom "( It's so thick... )"
        mom "( ... and Juicy. )"
        mom "..."
        mom "( It's been so long... )"
        mom "( I want... )"
        mom "( I want to taste it. )"
        show moms 15
        mom "( I {b}NEED{/b} to taste it! )"
        mom "( Just for a second! That couldn't hurt, right? )"
        show moms 16_17
        mom "( Oh yes!! )"
        mom "( Oh God, I've missed this so much! )"
        mom "( Mmm, I'm sooo wet... )"
        show moms 18
        player_name "{b}*Moan*{/b}"
        show moms 19
        mom "!!!" with hpunch
        mom "( Oh crap! He's waking up... )"
        mom "..."
        show moms 20
        mom "( What have I done! )"
        mom "( I can't let him see me like this! )"
        show moms 21
        mom "( I have to get out of here! )"
        show moms 22 at Position(xpos = 544, ypos = 768)
        player_name "Huh...?"
        show moms 23
        player_name "Hmm..."
        player_name "( Was that? )"
        show moms 24 at Position(xpos = 512, ypos = 768)
        player_name "( ... )"
        player_name "( I guess it was nothing... )"
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.get_state() == S_mom_midnight_noises:
        scene bedroom_cs01 with fade
        "Ha ha ha..."
        "{b}*SPLASH*{/b}"
        scene bedroom_cs03 with dissolve
        player_name "..."
        scene bedroom_cs04
        player_name "Who is making all that noise outside?"
        scene bedroom_cs03
        player_name "..."
        player_name "......"
        scene bedroom_cs01 with dissolve
        pause
        "{b}*SPLASH*{/b}"
        scene bedroom_cs04 with dissolve
        player_name "What is going on?"

        scene bedroom_night
        show player 101b
        with dissolve
        player_name "Maybe, I should go check to see what's going on."
        player_name "Sounds like whoever is outside isn't going to stop any time soon."
        show player 8 with dissolve
        $ M_mom.trigger(T_mom_midnight_wakeup)
        $ gTimer.tick(4)
        $ lock_ui()
        $ callScreen(location_count)

    elif M_mom.get_state() == S_mom_night_visit_three:
        $ M_mom.set('sex speed', .175 / .75)
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        scene location_bedroom_cutscene02 with dissolve
        pause
        scene location_bedroom_sex01
        show moms 1
        with dissolve
        mom "( Oh... )"
        mom "( I'm here... )"
        show moms 3
        mom "( What am I doing! )"
        show moms 4
        mom "( WHAT AM I DOING!!! )"
        show moms 5
        mom "( Mmm! )"
        mom "( There it is! )"
        show moms 6
        mom "( Ooh, I want it so bad... )"
        show moms 7_8
        mom "( Get hard for me Sweetie... )"
        mom "( Get hard for {b}Mommy{/b}. )"
        show moms 6
        pause
        show moms 9
        pause
        show moms 10
        mom "( ... )"
        show moms 11
        mom "!!!"
        show moms 12
        mom "..."
        mom "( Oh, I'm burning up... I need it!!! )"
        show moms 15
        mom "( Mmm. )"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / .75)
        show moms 16_17
        mom "( Oh! )"
        mom "( He tastes so good! )"
        player_name "( Mmm )"
        mom "*slurp*"
        show moms 19
        player_name "Hmm?"
        show moms 20b
        player_name "What the- ?"
        show moms 20c at Position(xpos=0.53, ypos=1.0) with dissolve
        player_name "... {b}[mom_name]{/b}?"
        show moms 20d
        mom "It's alright, {b}[firstname]{/b}, it's me."
        show moms 20c
        player_name "... Okay."
        player_name "But what's going-"
        show moms 20d
        mom "Shhh..."
        show moms 20c
        player_name "{b}[mom_name]{/b}? What are you-"
        show moms 20e with dissolve
        mom "Hush Sweetie, just relax and let yourself go..."
        player_name "..."


        mom "Oh, I need it, {b}[firstname]{/b}!"
        mom "I need that cock inside of me!!!"
        show moms 20f at Position(xpos=0.5, ypos=1.0) with dissolve
        player_name "*gulp*"
        mom "I tried..."
        mom "I tried so hard to resist."
        mom "... But I just can't!"
        show moms 20g with dissolve
        mom "Please, don't think less of me..."
        pause
        show moms 20h with hpunch

        player_name "... Ooohh!!"
        mom "Haaaaaaaah!"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / 1.75)
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "Oh God!!"
        pause
        mom "Oh, it's even better than I imagined!"
        player_name "Oh, {b}[mom_name]{/b} this feels so good!"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / 2)
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "Haah! [firstname]! Oh, [firstname]!"
        mom "I'm gonna cum!"
        show moms 20h with flash
        mom "AAHHH!!"

        player_name "Are you alright, {b}[mom_name]{/b}?"
        mom "Haaah... Haaaah..."
        mom "... Don't worry, Sweetie."
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "Keep going! Fuck, this is so good!"
        player_name "..."
        mom "Give it to me!!"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / 1.5)
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "OOOHH!!!"
        mom "That's it, Baby!!"
        mom "Let Mommy ride that fat cock!!"
        $ keep_going = 0
        $ M_mom.set("change angle", False)
        label night_visit_loop:
            menu:
                "Keep going." if keep_going < 2:
                    $ keep_going += 1
                    if M_mom.get("change angle"):
                        show moms 170_171_172_173_174_175_176_177
                    else:

                        show moms 20h_20i_20j_20k_20l_20m_20n_20o
                    pause
                    jump night_visit_loop

                "Change Angle." if keep_going < 2:
                    $ keep_going += 1
                    if not M_mom.get("change angle"):
                        $ M_mom.set('sex speed', .15)
                        $ M_mom.set("change angle", True)
                        hide moms
                        scene bedroom_sex_05
                        show moms 170_171_172_173_174_175_176_177
                        with fade
                    else:

                        $ M_mom.set('sex speed', ((.175 / .75) / 3) / 1.5)
                        $ M_mom.set("change angle", False)
                        hide moms
                        scene location_bedroom_sex01
                        show moms 20h_20i_20j_20k_20l_20m_20n_20o
                        with fade
                    pause
                    jump night_visit_loop
                "Cum.":

                    player_name "Oh, {b}[mom_name]{/b}... I'm gonna..."
                    player_name "... I'm gonna!!"
                    mom "Don't stop!! Don't-"
                    $ M_mom.set('sex speed', M_mom.get('sex speed') / .075)
                    scene location_bedroom_sex01
                    show moms 20p_20q
                    with flash
                    player_name "HHNNGGG!!!!!"

                    mom "AAAAAAAAHHHH!!!"
                    pause
                    show moms 20h

                    player_name "*panting*"

                    mom "Mmm..."
                    show moms 20r with dissolve
                    mom "..."
                    show moms 20s with dissolve
                    mom "Oh gosh..."
                    show moms 20t
                    player_name "That was incredible!"
                    show moms 20s
                    mom "Hehe, it really was..."
                    mom "..."
                    mom "I'm so sorry, Sweetheart!"
                    mom "I shouldn't have done this..."
                    show moms 20t
                    player_name "What!? No, don't say that!"
                    mom "..."
                    player_name "I wanted this too!"
                    show moms 20s
                    mom "... You did?"
                    show moms 20t
                    player_name "You have no idea! It's practically all I can think about anymore!"
                    show moms 20s
                    mom "... Really?"
                    show moms 20t
                    player_name "Yeah!"
                    player_name "I love you, {b}[mom_name]{/b}!"
                    show moms 20s
                    mom "... I love you too, Sweetie!"
                    mom "..."
                    mom "I've never orgasmed that hard before!!!"
                    show moms 20t
                    player_name "For real?!"
                    show moms 20s
                    mom "Hehe, I think so..."
                    show moms 20t
                    player_name "Sorry I didn't last very long..."
                    show moms 20s
                    mom "No, you did great, Sweetheart! Especially for our first time!"
                    show moms 20t
                    player_name "... First time?"
                    mom "..."
                    player_name "Can we do this again, {b}[mom_name]{/b}?"
                    show moms 20s
                    mom "Oh Sweetie, are you sure that's what you want?"
                    show moms 20t
                    player_name "Of course!!!"
                    player_name "[mom_name], I've never wanted anything more!"
                    show moms 20s
                    mom "Oh gosh..."
                    mom "I hate to admit it but I feel the same way!"
                    mom "..."
                    mom "Alright, Sweetie..."
                    mom "... But we can only be naughty when no one else is around!"
                    mom "And you can't tell {b}ANYBODY{/b}! Especially not your {b}Sister{/b}!"
                    mom "Do you understand?!"
                    show moms 20t
                    player_name "Yes."
                    show moms 20s
                    mom "[firstname], I'm serious! You cannot tell a soul about this!"
                    show moms 20t
                    player_name "I won't, {b}[mom_name]{/b}. I promise."
                    show moms 20s
                    mom "Good boy."
                    mom "*yawn*"
                    mom "Oh, I'm exhausted now."
                    show moms 20t
                    player_name "Yeah, me too."
                    show moms 20s
                    mom "Mmm, I could fall asleep right here."
                    show moms 20t
                    player_name "You should, [mom_name]."
                    show moms 20s
                    mom "I guess it would be alright. So long as I get out of here before [sis] wakes up."



                    scene location_bedroom_cutscene_sleep
                    with fade
                    show text "[mom_name] and I had finally slept together." at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    show text "It had been spectacular! All of our pent up anxieties evaporated in an instant!" at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    show text "She fell asleep in my arms that night..." at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    show text "... And I awoke the next morning feeling better than I could ever remember." at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    hide text
                    with dissolve


                    if M_player.is_set("pet cat"):
                        scene location_sleeping4 with fade
                    else:
                        scene location_sleeping2 with fade
                    show unlock11 at truecenter with dissolve
                    $ renpy.pause()
                    hide unlock11


                    scene location_bedroom_sex04
                    show moms 20u
                    pause
                    show moms 20v
                    player_name "[mom_name]?"
                    show moms 20u
                    player_name "..."
                    show moms 20v
                    player_name "[mom_name], wake up."
                    show moms 20u
                    mom "Hmm?"
                    show moms 20x
                    mom "*yawn* Morning already?"
                    show moms 20w
                    player_name "Unfortunately."
                    show moms 20x
                    mom "Oh, I slept like a log..."
                    show moms 20w
                    player_name "Heh, yeah, me too."
                    show moms 20x
                    mom "Hmm, alright. I suppose I'd better get out of here before your {b}Sister{/b} wakes up."
                    show moms 20w
                    player_name "You sure you don't want to fool around a bit more?"
                    show moms 20x
                    mom "Hehe, don't tempt me, Sweetie. That cock of yours is hard to say no to."
                    show moms 20w
                    player_name "I'll never get tired of hearing that!"
                    show moms 20x
                    mom "Come and find me later, okay?"
                    $ M_mom.trigger(T_mom_midnight_fun)
                    $ Sleep()
                    $ callScreen(location_count)
    else:
        if MC_computer_broken:
            show expression gTimer.image("bedroom_broken{}")
        else:
            show expression gTimer.image("bedroom{}")

    if M_player.is_set("pet cat"):
        scene location_sleeping3 with fade
    else:
        scene location_sleeping with fade
    show unlock11 at truecenter with dissolve
    $ renpy.pause()
    $ Sleep()
    hide unlock11
    hide bedroom
    hide bedroom_broken
    hide bedroom_night
    hide bedroom_broken_night
    scene black with fade
    hide sleeping with fade


    if M_mom.get_state() == S_mom_smith_dream:
        scene dreammom 1 at Position(ypos=1475) with fade
        mom "Hey Sweetie."
        mom "It's {b}Mommy{/b}..."
        player_name "{b}[mom_name]{/b}?"
        player_name "Where are we?"
        mom "It's okay. Everything will be alright..."
        mom "{b}Mommy{/b} will take care of you..."
        scene dreammom 1_2:
            linear 5.0 ypos -707
        player_name "{b}[mom_name]{/b}..."
        player_name "What are you doing..."
        mom "It's okay... {b}Mommy{/b} wants you to feel good..."
        player_name "{b}[mom_name]{/b}... You're going too fast..."
        scene dreammom 3
        player_name "!!!" with hpunch
        smi "{b}[firstname]{/b}!!!"
        scene dreammom 3:
            ypos -707
            linear 1.0 ypos 0
        smi "What are you doing here???"
        smi "Are you... SLEEPING?!"

        smi "Get to class NOW or I'm sending your ass to {b}DETENTION{/b}!"
        scene black with fade
        pause .2
        if MC_computer_broken:
            scene bedroom_broken
        else:
            scene bedroom
        show player 264
        with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 265 with dissolve
        player_name "!!!"
        show player 266
        player_name "( I had such a strange dream about {b}[mom_name]{/b}! )"
        player_name "( We were doing things, and she was naked! )"
        player_name "( With me! )"
        show player 267 with hpunch
        player_name "!!!"
        show player 268
        player_name "Is this normal?!"
        player_name "( I've never had those kinds of dreams with {b}[mom_name]{/b} before... )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_dream)
    jump bedroom_dialogue

label mom_sleepover:
    $ M_mom.set('sex speed', .175)
    scene location_bedroom_sex01 with fade
    show moms 1
    player_name "( ... )"
    mom "Sweetie?"
    mom "Aww, did you fall asleep waiting on me?"
    player_name "( ... )"
    show moms 3
    pause
    show moms 4
    pause
    show moms 5
    pause
    show moms 6
    mom "... Wake up, Sweetie."
    $ M_mom.set('sex speed', M_mom.get('sex speed') / .75)
    show moms 7_8
    mom "Mmm..."
    show moms 6
    pause
    show moms 9
    pause
    show moms 10
    mom "( ... )"
    show moms 11
    mom "!!!"
    show moms 12
    pause
    show moms 20b
    mom "[firstname]?"
    player_name "... Hmm?"
    show moms 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... [mom_name]?"
    player_name "Crap, I fell asleep didn't I?"
    show moms 20d
    mom "Hehe, that's okay, Sweetie."
    show moms 20c
    player_name "Did you still wanna- ?"
    show moms 20e with dissolve
    mom "Not so loud! We don't want to wake {b}[sis]{/b}!"
    player_name "Oh! ... Yeah, sorry."
    show moms 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    mom "Hehe..."
    mom "It's alright, your just excited. Mommy is excited too!"
    mom "I could hardly wait for {b}[sis]{/b} to get in bed."
    show moms 20g with dissolve
    player_name "Oh wow, {b}[mom_name]{/b}, your sopping wet!"
    mom "I told you I was excited."
    show moms 20h with dissolve
    mom "Mmm..."
    mom "Now, let's not waste time... Give it to Mommy!"
    $ M_mom.set('sex speed', M_mom.get('sex speed') / 3)
    show moms 20h_20i_20j_20k_20l_20m_20n_20o
    if randomizer() < 33:
        mom "Ahh!!!"
        mom "Oh {b}[firstname]{/b}, it's so deep!"
        mom "You like it when Mommy squeezes you with her pussy?"
        player_name "Oh God, yes!"
        mom "Yes, Baby!"
    elif randomizer() < 66:
        mom "Oh yes!!!"
        mom "That's it, Baby! Fuck Mommy's pussy!"
        mom "Mmm, you like that?"
        player_name "Oh yeah, {b}[mom_name]{/b}!"
        mom "Faster, Baby!"
    elif randomizer() < 100:
        mom "Oh God, that's good!"
        mom "Who's Mommy's naughty boy?"
        player_name "Mmm, I am..."
        mom "That's right, Baby! Fuck Mommy harder!"
        player_name "Uuhh!! You like this hard cock, {b}[mom_name]{/b}?"
        mom "Aaahh!! Yes! Yesss! YESSSSSS!!"
        mom "Give it to meeeeee!"
    $ M_mom.set('sex speed', M_mom.get('sex speed') / 1.5)
    show moms 20h_20i_20j_20k_20l_20m_20n_20o
    pause
    $ M_mom.set("change angle", False)
    label mom_sleepover_options:
        menu:
            "Keep going.":
                if M_mom.get("change angle"):
                    show moms 170_171_172_173_174_175_176_177
                else:

                    show moms 20h_20i_20j_20k_20l_20m_20n_20o
                pause
                jump mom_sleepover_options
            "Change Angle.":

                if not M_mom.get("change angle"):
                    $ M_mom.set('sex speed', .15)
                    $ M_mom.set("change angle", True)
                    hide moms
                    scene bedroom_sex_05
                    show moms 170_171_172_173_174_175_176_177
                    with fade
                else:

                    $ M_mom.set('sex speed', ((.175 / .75) / 3) / 1.5)
                    $ M_mom.set("change angle", False)
                    hide moms
                    scene location_bedroom_sex01
                    show moms 20h_20i_20j_20k_20l_20m_20n_20o
                    with fade
                pause
                jump mom_sleepover_options
            "Cum.":

                player_name "... Oh!"
                player_name "[mom_name], I'm gonna..."
                mom "Do it, Baby! Come inside me!"
                $ M_mom.set('sex speed', M_mom.get('sex speed') / .075)
                scene location_bedroom_sex01
                show moms 20p_20q
                with flash
                player_name "Uhhhuh!!!"
                mom "Hnnngg!!"
                mom "AAAAHHhh!!!"
                player_name "Shh! Your gonna wake {b}[sis_name]{/b}!"
                player_name "..."
                show moms 20h with dissolve
                mom "Huhhh, huhhh, huhhh..."
                show moms 20r with dissolve
                pause
                show moms 20s with dissolve
                mom "Oh {b}[firstname]{/b}... That was..."
                show moms 20t
                player_name "Mindblowing?"
                show moms 20s
                mom "Phew... Yes!"
                mom "Mmm, I can't feel my legs."
                pause
                mom "Mmm... I love you, {b}[firstname].{/b}"
                show moms 20t
                player_name "I love you too, [mom_name]. You're the best!"
                show moms 20s
                mom "Hah, thanks, Sweetie."

    if M_player.is_set("pet cat"):
        scene location_sleeping4 with fade
    else:
        scene location_sleeping2 with fade
    show unlock11 at truecenter with dissolve
    $ renpy.pause()
    $ Sleep()
    hide unlock11
    $ M_player.set("just wokeup", False)

    if randomizer() < 70 and M_mom.get_state() != S_mom_note:
        scene location_bedroom_sex04
        show moms 20u
        pause
        show moms 20v
        player_name "Wake up, [mom_name]."
        show moms 20u
        mom "Mmm..."
        show moms 20w
        player_name "The sun is up."
        show moms 20x
        mom "Good morning, Sweetie."
        show moms 20w
        player_name "You sleep alright?"
        show moms 20x
        mom "... You kidding? After getting fucked like that, I slept great!"
        show moms 20w
        player_name "Heh, me too..."
        mom "..."
        show moms 20x
        mom "I should probably get out of here before {b}[sis]{/b} gets up."
        show moms 20w
        player_name "Yeah..."
        show moms 20x
        mom "Thanks for a great night, {b}[firstname]{/b}! I love you!"
        show moms 20w
        player_name "I love you too, {b}[mom_name]{/b}!"
        hide moms with dissolve
    else:

        scene location_bedroom_blur
        show player 7
        pause
        show player 8
        pause
        show player 1
        player_name "..."
        show player 2
        player_name "Hmm, {b}[mom_name]{/b} must have woken before me and snuck out..."
        player_name "Phew, what a night! I slept like a baby..."
        if not M_mom.is_set("basement sex"):
            show player 10
            player_name "Hmm, what is that note on my computer monitor?"
            player_name "... Did [mom_name] leave that?"
            $ M_mom.trigger(T_mom_delay)
        hide player with dissolve
    $ callScreen(location_count)

label sleeping_locked:
    if MC_computer_broken:
        scene bedroom_broken
    else:
        scene bedroom
    show player 35 at left
    if not erik.over(erik_intro):
        player_name "( Can't sleep right now. I should go to school before I'm late. )"
    $ callScreen(location_count)

label tired_bedroom_dialogue:
    if MC_computer_broken:
        scene bedroom_broken_night
    else:
        scene bedroom_night
    show player 55 with dissolve
    player_name "{b}*yawn*{/b}"
    show player 56
    player_name "( I'm too tired for that... )"
    hide player 56
    $ callScreen(location_count)

label M6_note:
    if MC_computer_broken:
        scene bedroom_broken
    else:
        scene bedroom
    show momnote at Position (ypos=650) with dissolve
    pause
    hide momnote with dissolve
    show player 11 with dissolve
    player_name "( {b}[mom_name]{/b} needs help with the laundry? )"
    player_name "( I should go see what it's about. )"
    hide player with dissolve
    $ M_mom.trigger(T_mom_read_note)
    $ callScreen(location_count)

label player_room_lock:
    if MC_computer_broken:
        scene bedroom_broken
    else:
        scene bedroom
    show player 10 with dissolve
    player_name "( I should see what's on that {b}note{/b}. )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label player_message_lock:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    if not gTimer.is_dark():
        show player 12 with dissolve
    else:
        show player 101 with dissolve
    player_name "I should check my text messages."
    $ callScreen(location_count)

label pet_cat:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show cat 14 with dissolve
    player_name "Hey there, [cat]!"
    show cat 12
    if randomizer() < 33:
        cat "Meow"
    elif randomizer() < 66:
        cat "Prrrr"
    else:
        cat "Brrrep"
    show cat 15 at Position(xoffset = -7)
    pause
    show cat 14
    if randomizer() < 15:
        player_name "Who's a good Kitty?!"
    elif randomizer() < 30:
        player_name "You just gonna sleep all day?"
    elif randomizer() < 45:
        player_name "What did you do today, huh?"
    elif randomizer() < 60:
        player_name "You cute little fuzz ball."
    elif randomizer() < 75:
        player_name "Aww, snuggles for Kitty!"
    elif randomizer() < 85:
        player_name "Hey, watch it with those claws!"
    elif randomizer() < 93:
        player_name "I should get you a toy, huh?"
    else:
        player_name "I just love petting my pussy..."
    show cat 16
    pause
    hide cat with dissolve
    $ callScreen(location_count)

label cookies:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show expression "objects/closeup_cookies.png" at left with dissolve
    player_name "( A box of my favorite cookies! )"
    player_name "( I should keep them in my backpack in case I get hungry. )"
    hide expression "objects/closeup_cookies.png" with dissolve
    show expression "boxes/popup_cookies.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_cookies.png" with dissolve
    $ callScreen(location_count)

label june_mcbedroom_normal_faster_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') - 0.1)
    jump june_mcbedroom_normal_sex_loop

label june_mcbedroom_normal_slower_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') + 0.1)
    jump june_mcbedroom_normal_sex_loop

label june_mcbedroom_cosplay_faster_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') - 0.1)
    jump june_mcbedroom_cosplay_sex_loop

label june_mcbedroom_cosplay_slower_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') + 0.1)
    jump june_mcbedroom_cosplay_sex_loop