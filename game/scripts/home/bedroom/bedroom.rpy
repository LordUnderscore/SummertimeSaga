default MC_computer_broken = True
default player_room_lock = False
default m6_note = False
default cookies_taken = False
default m6_note_seen = False
default first_mom_visit = False

label bedroom_dialogue:
    $ location_count = "Bedroom"
    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump erik_bullying_3

    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom{}"
    scene expression gTimer.image(tmp_image)
    if not gTimer.is_dark():
        if player_room_count == 0:
            show player 7 with dissolve
            player_name "{b}*Yawn*{/b}"
            show player 8
            player_name "Ugh... I hate getting up early."
            show player 9
            player_name "( No text messages from {b}Erik{/b}. Maybe he's still sleeping. )"
            player_name "( I'll stop by his house on the way to school. )"
            hide player 9 with dissolve
            $ player_room_count = 2

    if gTimer.gameDay() >= event_wait_till and not erik.known(erik_bullying):
        $ just_woke_up = False
        scene black with fade
        mom "Sweetie?"
        pause
        mom "Wake up, Sweetie."
        scene bedroom with fade
        show mom 14f at left
        show player 101bf at right
        with dissolve
        player_name "Huh? {b}Mom{/b}? What time is it?"
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
        player_name "I have no idea why she's here either, {b}Mom{/b}."
        show player 100bf
        mom "..."
        show mom 13f
        mom "Ok, Sweetie."
        hide mom
        hide player
        with dissolve
        $ ui_lock_count = 1
        $ erik.add_event(erik_bullying)

    elif M_mia.get_state() == S_mia_tattoo_help and M_mia.is_set('story delay'):
        show player 35 with dissolve
        player_name "I have to make something nice for her tattoo idea."
        show player 34
        player_name "Hmm..."
        show player 35
        player_name "Perhaps, I can use one of the {b}easels in art class{/b}!"
        show player 33
        player_name "I can use it to come up with a nice design for her."
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
        show player 24 with dissolve
        player_name "I can't believe I won't be able to see {b}Mia{/b} anymore."
        show player 25
        player_name "Her parents don't trust me."
        show player 35
        player_name "Perhaps I can make it up to them somehow..."
        hide player with dissolve
        $ M_mia.trigger(T_mia_grounded)

    elif M_mia.get_state() == S_mia_strip_aftermath:
        scene bedroom
        show player 4 with dissolve
        pause
        show player 30 at Position (xoffset=-6) with dissolve
        player_name "I wonder how {b}Mia{/b} is doing."
        show player 12 at Position (xoffset=-6)
        player_name "It's been a few days, and I haven't heard anything from her..."
        player_name "...Perhaps I should visit her and see how she's doing."
        hide player with dissolve

    elif M_mia.get_state() == S_mia_urgent_message:
        scene bedroom
        show player 12 with dissolve
        player_name "Huh?"
        show player 9 at Position (xoffset=40) with dissolve
        pause
        show player 14 with dissolve
        player_name "Looks like I got a text message..."
        hide player with dissolve
        $ ui_lock_count = 1
        if m_mia02 not in message_list:
            $ message_list.append(m_mia02)
            $ new_message = True

    elif M_mia.get_state() == S_mia_angelicas_impatience:
        scene bedroom
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
        $ ui_lock_count = 1

    elif M_mia.get_state() == S_mia_angelicas_home_visit:
        scene bedroom with fade
        show player 13f at right
        show mom 2f at left
        mom "Sweetie?"
        show mom 1f
        show player 17f
        player_name "Good morning, {b}Mom{/b}."
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
        $ ui_lock_count = 1

    elif M_mia.get_state() == S_mia_angelicas_final_home_visit:
        scene bedroom with fade
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
        $ ui_lock_count = 1

    elif mom_count == 12 and mom_dialogue_advance == False and m6_note_seen == False:
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        player_name "( What a strange dream... )"
        show player 4
        player_name "( )It almost felt like someone else was in the room with me."
        show player 11
        player_name "!!!"
        show player 10
        player_name "Someone left a {b}note{/b} on my computer screen?"
        hide player with dissolve
        $ just_woke_up = False
        $ m6_note = True
        $ player_room_lock = True
        $ ui_lock_count = 1
        hide player with dissolve

    elif mom_count == 6 and just_woke_up == True:
        scene dreammom 1 at Position(ypos=1475) with fade
        mom "Hey Sweetie."
        mom "It's {b}Mommy{/b}..."
        player_name "{b}Mom{/b}?"
        player_name "Where are we?"
        mom "It's okay. Everything will be alright..."
        mom "{b}Mommy{/b} will take care of you..."
        scene dreammom 1_2:
            linear 5.0 ypos -707
        player_name "{b}Mom{/b}..."
        player_name "What are you doing..."
        mom "It's okay... {b}Mommy{/b} wants you to feel good..."
        player_name "{b}Mom{/b}... You're going too fast..."
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
        $ just_woke_up = False
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
        player_name "I had such a strange dream about {b}Mom{/b}!"
        player_name "We were doing things, and she was naked!"
        player_name "With me!"
        show player 267 with hpunch
        player_name "!!!"
        show player 268
        player_name "Is that normal?!"
        player_name "I've never had those kinds of dreams with {b}Mom{/b} before..."
        hide player with dissolve

    elif gTimer.is_morning() and not gTimer.is_weekend() and just_woke_up == True:
        $ just_woke_up = False
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        window hide
        pause
        show player 9
        player_name "( I should get ready for school... )"
        hide player 9 with dissolve

    elif just_woke_up == True and gTimer.is_morning() and gTimer.is_weekend():
        $ just_woke_up = False
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        window hide
        pause
        show player 9
        player_name "( What should I do this weekend... )"
        hide player 9 with dissolve

    if player_room_count == 1 and mom_phone_event01 == False:
        show player 34 with dissolve
        player_name "...{b}*distant voice*{/b}..."
        show player 35
        player_name "( Is that {b}Mom{/b} on the phone? )"
        show player 12
        player_name "( ...She sounds like she's mad... Is she yelling? )"
        show player 10
        player_name "( I should go see if she's alright. )"
        hide player 5 with dissolve
        $ ui_lock_count = 1
        $ mom_phone_event01 = True

    elif mom_count == 3 and mom_dialogue_advance == False and not gTimer.is_dark() and henchmen_count == 0:
        if MC_computer_broken:
            scene bedroom_broken
        else:
            scene bedroom
        show player 1 with dissolve
        player_name "( Doorbell's ringing, someone's at the door. )"
        player_name "( Must be {b}Erik{/b} or something... )"
        $ doorbell_rang = True
        $ ui_lock_count = 1

    elif mom_count == 6 and not mom_dialogue_advance and gTimer.is_dark() and mom_revealing:
        show player 34 with dissolve
        player_name "...{b}*distant voice*{/b}..."
        show player 35
        player_name "( There are weird voices coming from the kitchen... )"
        show player 12
        player_name "( ...I don't remember {b}Mom{/b} or {b}[sis]{/b} inviting anyone over... )"
        show player 10
        player_name "( I should go see if everything is okay. )"
        hide player 5 with dissolve

    elif not gTimer.is_dark():
        if gTimer.is_morning() and shower != "sister" and (
                sister.started(sis_webcam01) or
                sister.started(sis_webcam02) or
                sister.started(sis_webcam03) or
                (sister.over(sis_webcam04) and not sis_lastwebcam_show_seen)
                ):
            show player 4
            with dissolve
            player_name "Hmm..."
            player_name "( I wonder what my {b}Sister{/b} is doing right now. )"
            show player 1
            player_name "( Maybe I could connect to her {b}webcam{/b} from my computer... )"
            hide player with dissolve

        elif sister.started(sis_telescope01) and (shower != "sister" and gTimer.is_morning()):
            show player 4 with dissolve
            player_name "( I wonder what {b}Erik{/b} is doing right now. )"
            player_name "( I should use my {b}telescope{/b} and see what he's up to... )"
            hide player with dissolve

        elif sister.started(sis_telescope02) and (shower != "sister" and gTimer.is_morning()):
            show player 4 with dissolve
            player_name "( I wonder what {b}Mia{/b} is doing right now. )"
            player_name "( I should use my {b}telescope{/b} and see what she's up to... )"
            hide player with dissolve

        elif sister.started(sis_telescope03) and (shower != "sister" and gTimer.is_morning()):
            show player 4 with dissolve
            player_name "( I wonder what {b}Mrs. Johnson{/b} is doing right now. )"
            player_name "( I should use my {b}telescope{/b} and see what she's up to... )"
            hide player with dissolve

        elif training_count == 1 and training_tier == 2 and sister.over(sis_shower_cuddle01) or training_count == 2 and training_tier == 3 and sister.over(sis_couch02) or training_count == 3 and training_tier == 4 and sister.over(sis_couch03):
            show player 4 with dissolve
            player_name "( I wonder if {b}Master Somrak{/b} is ready to train me again. )"
            hide player with dissolve

    elif gTimer.is_evening():
        if sister.started(sis_couch01):
            show player 10 with dissolve
            player_name "( I hear someone in the hallway... My {b}Sister{/b}'s door? )"
            show player 4
            player_name "( I wonder if she's up to something. )"
            hide player with dissolve

        elif sister.started(sis_couch03):
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
    $ ui_lock_count = 0
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
    $ ui_lock_count = 0
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

label bedroom_check_on_mom:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I should really go check on {b}Mom{/b}... )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label sleeping:
    if erik.over(erik_breastfeeding_2) and not erik.over(erik_thief) and randomizer() > 66:
        if erik.in_progress(erik_thief):
            $ erik_thief.unfinish()
            $ ui_lock_count = 0
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
                    $ ui_lock_count = 1
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
        $ ui_lock_count = 1
        $ gTimer.tick(4)
        if m_mia01 not in message_list:
            $ message_list.append(m_mia01)
            $ new_message = True
        $ callScreen(location_count)

    elif mom_revealing_tommorow and not first_mom_visit:
        $ first_mom_visit = True
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
        mom "( And that bulge! I feel like touching it... )"
        show moms 7_8
        pause 4
        show moms 6
        mom "( It feels like it's getting bigger... )"
        show moms 7_8
        pause 4
        mom "( And harder! )"
        mom "..."
        show moms 119
        mom "( What am I doing?! )"
        mom "( What if he wakes up and finds me like this? )"
        show moms 120
        mom "( No. I should leave! )"
        show moms 121 at Position(xpos = 544, ypos = 768)
        player_name "Huh...?"
        show moms 122
        player_name "Hmm..."
        player_name "( Was that? )"
        show moms 123 at Position(xpos = 512, ypos = 768)
        player_name "( Nevermind )"

    elif mom_count == 11 and mom_dialogue_advance:
        $ gTimer.tick(3)
        scene location_bedroom_cutscene01
        with dissolve
        player_name "Zzz..."
        scene location_bedroom_cutscene02
        with dissolve
        mom "..."
        mom "( I can’t fall asleep. )"
        mom "( Ever since he’s been visiting me in bed... )"
        mom "( I can’t stop thinking about him. )"
        mom "( I just... Feel like being close to him... )"
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
        mom "( It's so... Pretty... )"
        mom "( And so big! )"
        show moms 13
        mom "( ... I can't believe how much he's grown... )"
        mom "( And I love feeling it in my hands... )"
        show moms 13_14
        mom "( It's so warm... )"
        mom "( And soft. )"
        mom "..."
        show moms 15
        mom "( It feels so nice on my lips. )"
        mom "( I want... )"
        mom "( To taste it. )"
        show moms 16_17
        mom "( I love feeling it in my mouth... )"
        mom "( It's getting harder... )"
        show moms 18
        player_name "{b}*Moan*{/b}"
        show moms 19
        mom "!!!" with hpunch
        mom "( He's waking up? )"
        mom "..."
        show moms 20
        mom "( What am I doing? )"
        mom "( What if he wakes up and finds me like this? )"
        show moms 21
        mom "( No. I should leave! )"
        show moms 22 at Position(xpos = 544, ypos = 768)
        player_name "Huh...?"
        show moms 23
        player_name "Hmm..."
        player_name "( Was that? )"
        show moms 24 at Position(xpos = 512, ypos = 768)
        player_name "( Nevermind )"
    if MC_computer_broken:
        show expression gTimer.image("bedroom_broken{}")
    else:
        show expression gTimer.image("bedroom{}")
    show sleeping with fade
    show unlock11 at truecenter
    $ renpy.pause()
    hide unlock11
    hide bedroom
    hide bedroom_broken
    hide bedroom_night
    hide bedroom_broken_night
    scene black with fade
    hide sleeping with fade

    if aunt_dialogue_advance == True:
        $ aunt_dialogue_advance = False
        $ aunt_count += 1

    if mom_dialogue_advance == True:
        $ mom_dialogue_advance = False
        $ mom_count += 1

    if mom_dialogue_daily == True:
        $ mom_time_passing += 1
        if mom_time_passing > 2:
            $ mom_time_passing = 0

    $ mom_dialogue_daily = False

    if mom_door_count == 0:
        $ mom_door_count = 1

    if sis_dialogue_advance and sis_bedroom_count < 2:
        $ sis_dialogue_advance = False
        $ sis_bedroom_count += 1

    $ diary_scene = False

    if left_hall_dialogue_advancement:
        $ left_hall_dialogue_advancement = False
        $ left_hall_dialogue_count += 1

    if pizza_dialogue_advance:
        $ pizza_dialogue_advance = False
        $ pizza_count += 1

    if renpy.random.randint(0,4) != 0:
        $ player_mail = [renpy.random.choice(player_mailbox_items)]

    if renpy.random.randint(0,4) != 0:
        $ erik_mail = [renpy.random.choice(erik_mailbox_items)]

    if renpy.random.randint(0,4) != 0:
        $ mia_mail = [renpy.random.choice(mia_mailbox_items)]

    $ gTimer.sleep()
    $ erik_drunk = False
    $ just_woke_up = True
    $ judith_daylock = False
    $ mom_door_lock = False
    $ training_done = False
    $ masturbated_tv = False
    $ moms_panties_taken = False
    $ roxxy_shower_lock = False
    $ mrsj_filled = False
    $ erik_funky = False

    if gTimer.dayOfWeek() == "Tue" and erik.completed(erik_orcette):
        $ orcette_mail_lock = True

    $ random_message = renpy.random.randint(0,9)

    if judith_sex_sequence_unlocked and m_judith01 not in message_list:
        if random_message == 9:
            $ message_list.append(m_judith01)
            $ new_message = True

    $ erik_telescope_random = renpy.random.randint(0,1)
    $ erikmom_telescope_random = renpy.random.randint(0,2)
    $ mia_telescope_random = renpy.random.randint(0,1)

    $ tick_skip_active = True

    if not gTimer.is_weekend():
        $ rump_n_cunt = randomizer()
    else:
        $ rump_n_cunt = 0

    if mom_revealing_tommorow:
        $ mom_revealing = True

    if mom_count == 4:
        if renpy.random.randint(1,2) == 1:
            $ mom_vacuuming = True
        else:
            $ mom_vacuuming = False

    python:



        for event in store.my_events:
            event.complete_events()
        Machine.trigger(T_all_sleep)

    $ shower = renpy.random.choice([If(mom_vacuuming or mom_count == 12 and not mom_dialogue_advance, "", "mom"), "sister", ""])
    jump bedroom_dialogue

label sleeping_locked:
    if MC_computer_broken:
        scene bedroom_broken
    else:
        scene bedroom
    show player 35 at left
    if player_room_count == 2:
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
    player_name "I'm too tired for that..."
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
    player_name "( {b}Mom{/b} needs help with the laundry? )"
    player_name "( I should go see what it's about. )"
    hide player with dissolve
    $ m6_note = False
    $ m6_note_seen = True
    $ player_room_lock = False
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