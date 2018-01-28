label mom_button_dialogue:
    if M_mom.get_state() == S_mom_relaxing:
        scene location_home_kitchen_closeup
        show player 1 at left with dissolve
        show mom 2 at right with dissolve
        mom "Hey Sweetie! Shouldn't you get going?"
        show player 2 at left
        show mom 1 at right
        player_name "Yeah. I was on my way."
        hide player
        hide mom
        with dissolve
        $ callScreen(location_count)

    elif M_mom.is_set("sleep together") and not M_mom.is_set("revealing") and location_count == "Kitchen":
        scene location_home_kitchen_closeup
        show mom 47 at Position(xpos=656,ypos=768)
        with dissolve
        pause
        show mom 48 at Position(xpos=660,ypos=768) with dissolve
        mom "!!!"
        show mom 48c
        mom "Sweetie, what are you doing?"
        show mom 50j
        player_name "Is having your panties exposed like this not supposed to be an open invitation?"
        show mom 50k
        mom "Sweetie!"
        mom "But what if your sister saw us?"
        mom "What would she think?"
        show mom 50j
        player_name "I don't know..."
        player_name "I just thought you wanted a massage."
        player_name "...and I felt like touching you..."
        show mom 50k
        mom "Sweetie..."
        mom "I guess it's okay, just try and keep an eye out."
        mom "I'd hate to be interrupted..."
        show mom 49_50_50b at Position(xpos=660,ypos=768) with dissolve
        pause
        pause
        show mom 48c with dissolve
        mom "Alright already."
        show mom 50k
        mom "I'd hate to have to change my panties already."
        show player 1 at left
        show mom 52 at right
        with dissolve
        mom "What else can I help you with?"
        show mom 1
        $ M_mom.set("revealing", True)
        $ M_mom.set("panties available", True)
        jump mom_options

    if location_count == "Basement":
        scene expression gTimer.image("home_basement{}")
    elif location_count == "Kitchen":
        scene expression gTimer.image("location_home_kitchen{}")

    if M_mom.is_set("fetch lotion") and not M_mom.is_set("retrieved lotion"):
        show player 13 at left
        show mom 2 at right
        with dissolve
        mom "Did you find my {b}lotion{/b} in my {b}bedroom dresser{/b}?"
        show mom 1
        show player 10
        player_name "No, not yet."
        show player 5
        show mom 2
        mom "Well, what are you waiting for?"

    elif M_mom.is_set("fetch lotion") and M_mom.is_set("retrieved lotion"):
        jump mom_lotion_fun

    elif M_mom.get_state() == S_mom_car_condition:
        show player 10 at left
        show mom 61 at right
        with dissolve
        player_name "I found out why the car wont start..."
        show player 5
        show mom 63
        mom "Oh?! Did you fix it already?"
        show mom 61
        pause
        show player 25
        player_name "It's pretty bad, {b}[mom_name]{/b}... I don't think I can fix it."
        show player 5
        show mom 39
        mom "Oh."
        show mom 38
        show player 10
        player_name "The engine is completely busted... I think we might have to replace it."
        player_name "It could be expensive..."
        show player 5
        pause
        show mom 60
        mom "Well. We do have insurance. Try and see what the car dealership will do for us."
        mom "Hopefully, they'll cover most of the repairs, otherwise..."
        show mom 39
        mom "I don't know what we'll do, Sweetie."
        show mom 38
        pause
        show player 10
        player_name "It'll be alright, {b}[mom_name]{/b}. I'll see if the {b}dealership{/b} can help us."
        show player 5
        pause
        show player 14
        player_name "I'll get it fixed."
        player_name "One way or another."
        show mom 61
        show player 13
        pause
        show mom 62
        mom "It's good to have your support, Sweetie."
        mom "Thank you."
        show expression "boxes/popup_car.png" at truecenter with dissolve
        $ loc_dealership_unlocked = True
        $ renpy.pause()
        hide expression "boxes/popup_car.png" with dissolve
        $ M_mom.trigger(T_mom_deliver_car_news)
    else:

        if M_mom.is_set("revealing") and location_count == "Kitchen":
            show momobj 2 at Position(xpos=590,ypos=768)
            menu:
                "Feel Ass":
                    if M_mom.is_set("sex available"):
                        scene location_home_kitchen_closeup
                        show mom 47 at Position(xpos=656,ypos=768)
                        with dissolve
                        pause
                        show mom 48 at Position(xpos=660,ypos=768) with dissolve
                        mom "!!!"
                        show mom 48c
                        mom "Sweetie?"
                        mom "What are you doing back there?"
                        show mom 50j
                        player_name "It looked so...inviting!"
                        show mom 50k
                        mom "Mmm..."
                        mom "Just don't let your sister see us."
                        mom "Promise?"
                        show mom 50j
                        player_name "I can stop if I hear something..."
                        show mom 49_50_50b at Position(xpos=660,ypos=768) with dissolve
                        pause
                        pause
                        pause
                        show mom 50j with dissolve
                        player_name "Does that feel good?"
                        show mom 50k
                        mom "That feels great, Sweetie..."
                        mom "But now I want something else besides your fingers..."
                        mom "Will you take me right here, Sweetie?"
                        show mom 50j
                        player_name "Not worried about [sis_name] catching us now?"
                        show mom 50k
                        mom "Just do it quick."
                        mom "I'm more than ready..."
                        show mom 50j
                        player_name "Okay..."
                        show mom 50c with dissolve
                        pause
                        show mom 50d with dissolve
                        pause
                        hide mom
                        show mom 50e at right
                        with dissolve
                        pause
                        show mom 50g with dissolve
                        mom "Give it to me."
                        hide mom
                        show moms 164 at right
                        with dissolve
                        mom "Ahh..."
                        player_name "{b}[mom_name]{/b}, you're so wet..."
                        $ M_mom.set('sex speed', .175)
                        show moms 164_165_166_167_168 at right with dissolve
                        mom "Oh!"

                        label mom_kitchen_fuck_loop:
                            show screen sex_anim_buttons
                            pause
                            if anim_toggle == True:
                                $ animcounter = 0
                                while animcounter < 4:
                                    hide screen sex_anim_buttons
                                    show moms 164_165_166_167_168
                                    pause 4
                                    if animcounter == 1:
                                        if randomizer() <= 50:
                                            mom "Oh!!!{p=1}{nw}"
                                        else:
                                            mom "AHHH!!!{p=1}{nw}"
                                    elif animcounter == 3:
                                        if randomizer() <= 50:
                                            mom "Did you cum, yet?{p=2}{nw}"
                                            player_name "Not yet...{p=2}{nw}"
                                            mom "Hurry, Sweetie... I don't think...I can take...anymore!{p=3}{nw}"
                                    pause 3
                                    $ animcounter += 1
                            else:
                                $ animcounter = 0
                                while animcounter < 4:
                                    hide screen sex_anim_buttons
                                    show moms 164
                                    pause
                                    show moms 165
                                    pause
                                    show moms 166
                                    pause
                                    show moms 167
                                    pause
                                    show moms 168
                                    pause
                                    if animcounter == 1:
                                        if randomizer() <= 50:
                                            mom "Oh!!!"
                                        else:
                                            mom "AHHH!!!"
                                    elif animcounter == 3:
                                        if randomizer() <= 50:
                                            mom "Did you cum, yet?"
                                            player_name "Not yet..."
                                            mom "Hurry, Sweetie... I don't think...I can take...anymore!"
                                    $ animcounter += 1
                            call screen mom_kitchen_fuck_options

                        label mom_kitchen_fuck_cum:
                            player_name "!!!"
                            player_name "Oh, {b}[mom_name]{/b}!"
                            player_name "I'm-"
                            mom "Shhhh!"
                            show moms 169 with flash
                            player_name "UHH!!!"
                            hide moms
                            show mom 50h at right
                            with dissolve
                            pause
                            mom "You get so rough when you take me from behind."
                            player_name "Did it hurt?"
                            mom "It's fine, I don't mind when you take me like this..."
                            show mom 50i at right
                            show player 434 at left
                            with dissolve
                            mom "I think I'm going to need to change my panties after this..."
                            mom "...I can't have it dripping down my leg."
                            pause
                            show mom 61 with dissolve
                            show player 10
                            player_name "Sorry."
                            show player 13
                            show mom 62
                            mom "It's alright, Sweetie."
                            show mom 61
                            show player 14
                            player_name "Thanks for letting me do it..."
                            show player 13
                            show mom 62
                            mom "No, thank you!"
                            hide player
                            hide mom
                            with dissolve
                            $ gTimer.tick()
                            $ callScreen(location_count)
                    else:

                        scene location_home_kitchen_closeup
                        hide momobj
                        show mom 47 at Position(xpos=656,ypos=768)
                        with dissolve
                        pause
                        show mom 50k at Position(xpos=660,ypos=768) with dissolve
                        mom "Well hello to you to, Sweetie..."
                        show mom 50j
                        player_name "Hey, {b}[mom_name]{/b}..."
                        show mom 50k
                        mom "Just be careful..."
                        show mom 49_50_50b at Position(xpos=660,ypos=768) with dissolve
                        pause
                        pause
                        show mom 50k with dissolve
                        mom "Alright already."
                        mom "I'd hate to have to change my panties already."
                        show player 1 at left
                        show mom 52 at right
                        with dissolve
                        mom "What else can I help you with?"
                        show mom 1
                        jump mom_options
                "Talk":

                    scene location_home_kitchen_closeup
                    hide momobj
                    show mom 1 at right
                    show player 2 at left
                    with dissolve
                    player_name "Hey {b}[mom_name]{/b}, got a minute?"
                    show mom 2
                    show player 1
                    mom "Need something, {b}[firstname]{/b}?"
                    show mom 1
                    jump mom_options

        if M_mom.is_set("revealing"):
            show player 1 at left
            show mom 2 at right
            with dissolve
            if randomizer() <= 10:
                mom "There's my big man..."
            elif randomizer() <= 20:
                mom "Hey there, Sweetie."
                mom "What can your mommy do for you?"
            elif randomizer() <= 30:
                mom "Awww..."
                mom "No hello squeeze?"
            elif randomizer() <= 70:
                mom "Looking for me, I hope."
            elif randomizer() <= 80:
                mom "Need something, Sweetie?"
                mom "Or can I do something for you?"
            elif shower.occupied("sis"):
                mom "Your sister is in the shower."
                mom "In case you needed me for a quick sec."
            else:
                mom "I was hoping I'd see you today."
            show mom 1
            show player 14
            if randomizer() <= 50:
                player_name "Hello, {b}[mom_name]{/b}."
            else:
                player_name "You're looking good today."
            show player 13
        else:

            show player 1 at left
            show mom 2 at right
            with dissolve
            mom "Hi Sweetie!"
            mom "Is everything okay at school?"
            show player 14 at left
            show mom 1 at right
            player_name "Yeah..."
            show player 13 at left
            show mom 13 at right
            mom "I'm sorry you fell behind at your school after what happened..."
            show mom 14 at right
            show player 14 at left
            player_name "It's okay, {b}[mom_name]{/b}, I'm doing fine!"
            show player 13 at left
            show mom 13 at right
            mom "I'm just checking on my beautiful son, to make sure he's okay!"
            show player 21 at left
            show mom 14 at right
            player_name "Okay, {b}[mom_name]{/b}..."
            player_name "I gotta go."
            show player 13 at left
            show mom 3 at right
            mom "Don't stay out too late!"
            show mom 1
        label mom_options:
            menu:
                "Ask about {b}Dad{/b}." if M_mom.is_set("dad question"):
                    $ M_mom.set("dad question", False)
                    show player 10 at left
                    show mom 1 at right
                    player_name "{b}[mom_name]{/b}... What happened to {b}Dad{/b}?"
                    show player 11
                    show mom 60 at Position (xoffset=-28) with dissolve
                    mom "Oh... Sweetie, I..."
                    show mom 59 at Position (xoffset=-28)
                    show player 10
                    player_name "Please! I want to know..."
                    show player 11
                    show mom 60 at Position (xoffset=-28)
                    mom "I'm sorry... I don't know."
                    mom "The investigation came up with nothing..."
                    mom "They couldn't find any evidence, so they put the case on hold..."
                    show mom 59 at Position (xoffset=-28)
                    show player 10
                    player_name "They have to find something eventually, right?"
                    show player 11
                    show mom 60 at Position (xoffset=-28)
                    mom "We can only hope."
                    show mom 59 at Position (xoffset=-28)
                    pause
                    show mom 60 at Position (xoffset=-28)
                    mom "Sweetie..."
                    mom "I want closure as much as you and your {b}sister{/b}..."
                    mom "But we can't let ourselves get dragged down by this."
                    show mom 63 at Position (xoffset=-28)
                    mom "You're still a teenager. Live your life."
                    mom "It's what he would've wanted."
                    show player 10
                    show mom 59 at Position (xoffset=-28)
                    player_name "Okay. I think I understand..."
                    show player 14
                    show mom 61 at Position (xoffset=-28)
                    player_name "Thanks, {b}[mom_name]{/b}."
                    show player 1
                    show mom 2 with dissolve
                    mom "Anything else you wanted to talk about?"
                    show mom 1
                    show player 1
                    jump mom_options

                "Ask about money problems." if M_mom.is_set("money question"):
                    $ M_mom.set("money question", False)
                    show mom 1
                    show player 10
                    player_name "{b}[mom_name]{/b}, about what you said on the phone back there..."
                    show mom 13
                    show player 11
                    mom "I told you earlier, it's not a big deal."
                    mom "We'll be alright!"
                    show mom 14
                    show player 14
                    player_name "But... What if... I wanted to help you?"
                    player_name "What if I got a real job?"
                    show player 10
                    player_name "I don't like seeing you so stressed out by this..."
                    show mom 52 at Position (xoffset=1)
                    show player 11
                    mom "You're still in school!"
                    mom "I don't think it's wise for you to take up full time work..."
                    mom "Your education is what's most important right now."
                    show mom 51 at Position (xoffset=1)
                    show player 10
                    player_name "I'll work after school, and on weekends!"
                    show mom 53 at Position (xoffset=-18) with dissolve
                    show player 13
                    mom "*sigh* Stubborn like your father..."
                    show mom 59 at Position (xoffset=-28) with dissolve
                    mom "Hmm..."
                    show mom 63 at Position (xoffset=-28)
                    mom "You could always check the {b}mail box{/b}!"
                    mom "There should be some job postings in there..."
                    mom "Maybe There's something in there you'll like?"
                    show mom 61 at Position (xoffset=-28)
                    show player 18
                    player_name "Thanks {b}[mom_name]{/b}, I'll take a look."
                    show mom 62 at Position (xoffset=-28)
                    show player 1
                    mom "Anything else you wanted to talk about, Sweetie?"
                    show mom 1 with dissolve
                    jump mom_options

                "Ask about the men in suits." if M_mom.is_set("bad guys question"):
                    $ M_mom.set("bad guys question", False)
                    show player 10
                    player_name "{b}[mom_name]{/b}, about what that gangster said..."
                    show mom 59 at Position (xoffset=-28) with dissolve
                    player_name "Did you know about {b}Dad{/b}?"
                    show player 11
                    show mom 53 at Position (xoffset=-18) with dissolve
                    mom "{b}*Sigh({/b} I can't keep you in the dark forever..."
                    mom "It was going fine, until a few years ago..."
                    mom "Then your father started gambling, and eventually built up a lot of debt..."
                    mom "He told me he was able to pay it off, so I didn't press the issue too much."
                    mom "Suddenly, the accident happened..."
                    show mom 60 at Position (xoffset=-28) with dissolve
                    mom "And now, they're trying to get the money from us..."
                    show player 10
                    show mom 59 at Position (xoffset=-28)
                    player_name "Are you sure we can't tell the police about this?"
                    show player 11
                    show mom 60 at Position (xoffset=-28)
                    mom "If what that man said is true... I can't risk them harming you or {b}[sis]{/b}."
                    show player 10
                    show mom 59 at Position (xoffset=-28)
                    player_name "Are we going to pay them?"
                    show player 11
                    show mom 60 at Position (xoffset=-28)
                    mom "We don't have the money, Sweetie."
                    show mom 53 at Position (xoffset=-18) with dissolve
                    mom "{b}*Sigh({/b} Maybe we should just move away and start fresh..."
                    show player 1
                    show mom 63 at Position (xoffset=-28) with dissolve
                    mom "We'll figure something out."
                    show mom 51 at Position (xoffset=1)
                    show player 2
                    player_name "I'm sure we will, {b}[mom_name]{/b}."
                    show mom 2 with dissolve
                    show player 1
                    mom "Now... Is there something else you wanted to talk about?"
                    show mom 1
                    jump mom_options
                "Help {b}[mom_name]{/b} around the house.":

                    if M_mom.get_state() in [S_mom_fill_mower, S_mom_mow_lawn]:
                        show player 10
                        player_name "Did you need help with anything?"
                        show player 5
                        show mom 2
                        mom "Did you finish mowing the yard?"
                        show mom 1
                        show player 10
                        player_name "Oh! Um...."
                        player_name "I forgot about that, but it shouldn't take me too long to finish."
                        show player 13
                        show mom 2
                        mom "I'd really appreciate it, sweetie."
                        show mom 1
                        show player 14
                        player_name "I'm on it!"
                        hide player
                        hide mom
                        with dissolve
                        $ callScreen(location_count)

                    elif M_mom.get_state() in [S_mom_sis_check, S_mom_close_valve, S_mom_pipe_check, S_mom_fix_pipe]:
                        show player 4
                        player_name "( I gotta fix the {b}bathroom sink{/b} somehow... )"

                    elif M_mom.get_state() in [S_mom_vacuum_help, S_mom_dishes_help, S_mom_laundry_help]:
                        show player 14
                        player_name "Anything else you need help with?"
                        show player 13
                        show mom 2
                        if M_mom.get_state() == S_mom_laundry_help and M_mom.is_set("chores"):
                            mom "No. Not right now, Sweetie."
                            mom "Maybe later, if you're still available."
                        else:
                            mom "No. Not today, Sweetie."
                            mom "Maybe tomorrow, if you're still available."
                        show mom 3
                        mom "Thanks for asking!"
                        show mom 1
                        show player 14
                        player_name "You're welcome, {b}[mom_name]{/b}."

                    elif M_mom.get_state() == S_mom_check_car:
                        show player 4
                        player_name "( I should go check the {b}car{/b} like [mom_name] asked me to. )"

                    elif M_mom.get_state() == S_mom_fix_car:
                        show player 4
                        player_name "( I have to visit the {b}car dealership{/b}. Maybe they can fix [mom_name]'s car... )"
                    else:

                        show player 2
                        player_name "Hey, {b}[mom_name]{/b}, anything I can do to help around the house?"
                        show player 1
                        mom "Hmm..."
                        show mom 2
                        mom "Nothing I can think of right now, no."
                        show mom 1
                        show player 2
                        player_name "Cool. Let me know if something comes up."
                    show player 1
                    jump mom_options

                "Apply lotion." if M_mom.is_set("lotion fun"):
                    if M_mom.is_set("sex available") and location_count == "Kitchen":
                        show player 14
                        player_name "Need me to rub some more lotion on...your legs?"
                        show player 13
                        show mom 2
                        mom "That sounds wonderful, Sweetie."
                        mom "I could really use your gentle touch right about now."
                    else:

                        show player 10
                        player_name "Need me to rub some more lotion on... your legs?"
                        show player 5
                        show mom 13
                        mom "Oh... again? Well, I..."
                        show mom 14
                        show player 10
                        player_name "Did I do a bad job?"
                        show player 5
                        show mom 13
                        mom "Oh, no, Sweetie. It was... really good."
                        show mom 14
                        pause
                        show mom 13
                        mom "Sure, I guess I could use a break."
                        show mom 1
                        show player 14
                        player_name "Great!"
                        show player 13
                        show mom 2
                    mom "Go and grab the {b}lotion from my bedroom dresser{/b}."
                    show mom 1
                    show player 14
                    player_name "Alright!"
                    $ M_mom.set("fetch lotion", True)
                    $ lock_ui()

                "Shopping" if M_mom.get_state() == S_mom_hang_out_return and location_count == "Kitchen":
                    scene location_home_kitchen_blur
                    show player 2 at left
                    show mom 1 at right
                    player_name "Remember when you asked me to go shopping with you?"
                    show player 1
                    show mom 2
                    mom "Yeah."
                    show player 2
                    show mom 1
                    player_name "Well I'm free now. Do you still wanna go?"
                    show player 1
                    show mom 3
                    mom "Really?! Great!"
                    show mom 2
                    mom "Just let me get ready and I'll meet you in the car, okay?!"
                    show mom 1
                    show player 2
                    player_name "Alright."
                    $ M_mom.trigger(T_mom_hang_out_accept)

                "Shower." if M_mom.is_set("sex available"):
                    if location_count == "Basement":
                        show player 2
                        show mom 1
                        player_name "Hey, {b}[mom_name]{/b}."
                        player_name "I was thinking we could maybe...take a shower together?"
                        show player 13
                        show mom 2
                        mom "Right now?"
                        show mom 1
                        mom "Hmm..."
                        show mom 3
                        mom "I suppose I could use a shower too."
                        show mom 2
                        mom "Let me just finish putting this load of laundry in and I'll meet you upstairs."
                        scene shower_closeup
                        show moms 27
                        with dissolve
                        pause
                        show moms 28 at Position(xpos=487,ypos=768) with dissolve
                        pause
                        show moms 34 with dissolve
                        mom "Hope you're not almost done..."
                        mom "I was hoping we could spend some time in here."

                    elif location_count == "Kitchen":
                        show player 2
                        show mom 1
                        player_name "Hey, {b}[mom_name]{/b}!"
                        player_name "I was wondering..."
                        show player 21
                        player_name "Would you like to take a shower with me?"
                        show player 14
                        show mom 2
                        mom "It is getting pretty hot in the house..."
                        show mom 3
                        mom "Sure! A shower sounds lovely right now."
                        show mom 2
                        mom "Give me a minute. I'll join you after I'm done here."
                        scene shower_closeup
                        show moms 27
                        with dissolve
                        pause
                        show moms 28 at Position(xpos=487,ypos=768) with dissolve
                        pause
                        show moms 34 with dissolve
                        mom "Sorry to keep you waiting, Sweetie..."
                    jump mom_shower_question

                "Sex in your room." if M_mom.is_set("sex available"):
                    if location_count == "Basement":
                        show player 14
                        player_name "Want to...take a break with me in your bedroom?"
                        show player 13
                        show mom 3
                        mom "Is this supposed to be a sly way of getting me naked?"
                        show mom 1
                        show player 10
                        player_name "No, I just-"
                        show player 5
                        show mom 2
                        mom "It's fine! I don't mind."
                        show player 13
                        mom "Is your sister busy?"
                        show mom 1
                        show player 14
                        player_name "I think so."
                        show player 13
                        show mom 2
                        mom "Alright."
                        mom "But we can't do this all the time. You're going to wear me out!"
                        show mom 1
                        show player 14
                        player_name "How could I ever get tired of having sex with you?"
                        show player 13
                        show mom 3
                        mom "Ha Ha Ha."
                        show mom 2
                        mom "Get up stairs then, Sweetie!"
                        scene mom_bedroom_closeup2
                        show mom 86 at left
                        show player 434f at right
                        with dissolve
                        mom "The bed sheets are so nice and soft... Why don't you come lay with me..."
                        show mom 84
                        show player 8f with dissolve
                        pause
                        show player 261 with dissolve
                        pause
                        show mom 85
                        show player 263 with dissolve
                        mom "Naughty boy."
                        show mom 84
                        show player 262
                        player_name "What?"
                        show player 263
                        show mom 85
                        mom "You truly are insatiable."
                        show mom 84
                        show player 262
                        player_name "You can just lay on your back and I can do the rest."
                        show player 263
                        show mom 86
                        mom "Do I have to get naked?"
                        show mom 84
                        show player 262
                        player_name "Huh?"
                        show player 263
                        show mom 84
                        mom "I was just teasing you!"
                        show mom 89 with dissolve

                    elif location_count == "Kitchen":
                        show player 14
                        player_name "Can we do it quick in your room?"
                        show player 13
                        show mom 2
                        mom "Oh!"
                        mom "Umm... I guess so."
                        mom "Just make sure your sister doesn't see you enter my room!"
                        show mom 1
                        show player 14
                        player_name "Alright!"
                        show player 13
                        scene mom_bedroom_closeup2
                        show player 434f at right
                        show mom 86 at left
                        with dissolve
                        mom "You know, I was hoping you wanted to have some fun."
                        show mom 84
                        show player 435f
                        player_name "Oh yeah? What were you thinking about?"
                        show player 434f
                        show mom 86
                        mom "Just of all those things you do that make me feel...good..."
                        mom "And what made you think of me?"
                        show mom 84
                        show player 435f
                        player_name "Every time I see your cleavage through your robe I just..."
                        show player 434f
                        show mom 89 with dissolve
                        mom "You mean these?"
                        show mom 90
                        show player 435f
                        player_name "Yeah..."
                        show player 434f
                        show mom 89
                        mom "Why don't you get undressed so we can play together..."
                        show mom 90
                        show player 8f with dissolve
                        pause
                        show player 261 with dissolve
                        pause
                        show player 263
                        show mom 102
                        with dissolve
                        mom "Mmmm..."
                        show mom 103
                    mom "Come to {b}Momma{/b}, big boy!"
                    hide player
                    show mom 104 at left
                    with dissolve
                    pause
                    scene mom_bedroom_closeup_sex
                    jump mom_sex

                "Sex in my room." if M_mom.is_set("sex available") and not M_mom.is_set("room sneak"):
                    show player 2
                    player_name "You wanna sleep in my room tonight?"
                    show player 1
                    show mom 2
                    mom "Mmm, I would love that, Sweetie."
                    show player 2
                    show mom 1
                    player_name "Great! I'll wait up for you then."
                    show player 1
                    show mom 2
                    mom "Can't wait!"
                    $ M_mom.set("room sneak", True)

                "Hang out in the car." if M_mom.is_set("sex available"):
                    show player 14
                    player_name "{b}[mom_name]{/b}, remember the last time we were in the car?"
                    show player 13
                    show mom 2
                    mom "Yes, Sweetie."
                    show mom 1
                    show player 14
                    player_name "Do you think you could jerk me off again?"
                    show player 13
                    show mom 2
                    mom "!!!"
                    show mom 2
                    mom "Oh, that's what you were thinking about?"
                    show mom 3
                    mom "Ha Ha Ha!"
                    show mom 2
                    mom "Oh, Sweetie...you are naughty."
                    mom "Who could have thought I'd raise such a bad boy."
                    show mom 1
                    show player 14
                    player_name "Well, if I remember properly, you were the one that reached over and started rubbing me!"
                    player_name "The apple doesn't fall far from the tree."
                    show player 13
                    show mom 3
                    mom "Ha Ha Ha!"
                    show mom 2
                    mom "Well said."
                    show mom 1
                    mom "..."
                    show mom 2
                    mom "I don't see why not."
                    mom "Did you want to go now?"
                    show mom 1
                    show player 14
                    player_name "Uh... Yeah!"
                    show mom 2
                    mom "Okay. Let's go quickly while your sister is upstairs."
                    hide player
                    hide mom
                    scene black
                    with fade
                    jump car_sex

                "Watch a Movie." if M_mom.is_set("sex available") and not M_mom.is_set("movie night"):
                    show player 2
                    player_name "I was thinking about another Mother/Son movie night. Interested?"
                    show player 1
                    show mom 2
                    mom "Mmm, a movie night, huh?"
                    mom "That sounds like a great idea, Sweetheart!"
                    show player 2
                    show mom 1
                    player_name "Awesome!"
                    player_name "I'll see you tonight in the living room then?"
                    show player 1
                    show mom 2
                    mom "Absolutely! I can't wait..."
                    $ M_mom.set("movie night", True)

                "Laundry." if M_mom.is_set("basement sex"):
                    if location_count == "Basement":
                        show mom 122
                        show player 14
                        player_name "Are you almost done with the laundry?"
                        show player 13
                        show mom 123
                        mom "Pretty much. I just have to wait to move this load into the dryer."
                        mom "Why? What did you need?"
                        show player 14
                        show mom 122
                        player_name "I was hoping you could clean some of my clothes quick...they are a bit dirty."
                        show player 13
                        show mom 123
                        mom "Of course. Bring them down and I'll wash them."
                        show player 8 with dissolve
                        pause
                        show player 261f with dissolve
                        pause
                        show mom 123
                        mom "Oh!"
                        show player 263f with dissolve
                        mom "I think you want...something else..."
                        show mom 121
                        show player 432
                        player_name "...Maybe."
                        show player 431
                        pause
                        show mom 123
                        mom "Hop up on that washing machine and let {b}Mommy{/b} take care of that for you..."
                        scene home_basement_sex_01
                        show player 271 at Position(xpos=655,ypos=768)
                        show mom 107 zorder 0 at Position(xpos=200)
                        with dissolve
                        pause
                        show mom 108
                        mom "My turn..."
                        show mom 109
                        pause
                        show mom 110
                        pause
                        show mom 111
                        pause
                        show mom 112
                        pause
                        show mom 113
                        pause
                        show mom 114
                        pause
                        player_name "You look beautiful, {b}[mom_name]{/b}."
                        show mom 115
                        mom "Thanks, Sweetie."
                        mom "Let me get on top of you..."
                        mom "...Just make sure you hold on to me."
                        hide player
                        hide mom
                        show moms 124 at Position(xpos=650)
                        with dissolve
                        pause
                        show moms 125 at Position(xpos=655)
                        pause
                        show moms 126f with dissolve
                        mom "Oh!"
                        show moms 126e
                        pause
                        show moms 126d
                        pause
                        show moms 126c
                        pause
                        show moms 126b
                        pause
                        show moms 126
                        if M_mom.get_state() != S_mom_give_laundry and randomizer() <= 50:
                            $ mom_basement_rand = True
                        else:
                            $ mom_basement_rand = False
                        if mom_basement_rand:
                            mom "Mmmm..."
                            mom "I can barely fit you all in."
                        else:
                            mom "Ahh..."
                            player_name "!!!"
                            player_name "You're so warm..."
                        $ M_mom.set('sex speed', .4)
                        $ location_count = "Basement"
                        $ cum = False
                        $ anim_toggle = False
                        $ xray = False
                        jump basement_mom_sex_loop

                    elif location_count == "Kitchen":
                        show player 14
                        player_name "Hey, {b}[mom_name]{/b}... Do you want to hang out in the basement for some quick fun?"
                        show player 13
                        show mom 2
                        mom "Oh?"
                        show mom 1
                        show player 14
                        player_name "I figured we could turn on the dryer and you could be as loud as you wanted..."
                        show player 13
                        show mom 3
                        mom "Ha Ha."
                        show mom 2
                        mom "That's quite naughty, Sweetie."
                        show mom 1
                        pause
                        show mom 2
                        mom "Hmm... Alright!"
                        mom "I have some free time and I could use some... attention."
                        show mom 1
                        show player 14
                        player_name "Really?"
                        show player 13
                        show mom 2
                        mom "Sure!"
                        mom "Just meet me down there in a minute..."
                        hide mom
                        hide player
                        with dissolve
                        jump basement_mom_sex

                "Kissing" if M_mom.get_state() == S_mom_kissing_practice and location_count == "Kitchen":
                    show player 10 at left
                    show mom 1 at right
                    player_name "Hey... Umm, [mom_name]?"
                    show player 5
                    show mom 2
                    mom "Yes, Sweetie?"
                    show player 10
                    show mom 1
                    player_name "Could I ask you something?"
                    show player 5
                    show mom 3
                    mom "Of course! You can ask me anything."
                    show player 10
                    show mom 1
                    player_name "Well, it's kinda... Embarrassing."
                    show player 5
                    show mom 13
                    mom "Oh? Well that's okay, [firstname]."
                    mom "There's no need to feel embarrassed."
                    mom "Not with me..."
                    show mom 14
                    show player 10
                    player_name "Okay."
                    menu:
                        "Can you teach me?":
                            show player 10 at left
                            show mom 14 at right
                            player_name "I was wondering if you could..."
                            player_name "Well..."
                            show player 5
                            show mom 13
                            mom "If I could what, Sweetheart?"
                            show player 10
                            show mom 14
                            player_name "Err... Remember the other day at the mall?"
                            show player 5
                            show mom 14b
                            player_name "..."
                            show mom 13
                            mom "... Yes."
                            show player 10
                            show mom 14b
                            player_name "Well... I was hoping you could teach me more, you know, about kissing?"
                            show player 5
                            show mom 13
                            mom "What?!"
                            show mom 14b
                            player_name "..."
                            show mom 13
                            mom "That was a mistake, Sweetie. I should never have..."
                            mom "What am I supposed to teach you anyways?"
                            show player 10
                            show mom 14b
                            player_name "You know, like, how to do it."
                            player_name "I thought you could show me what women like?"
                            show player 5
                            show mom 13
                            mom "Hmm, well I could certainly tell you what women like."
                            mom "But I don't think showing you is a good idea. It would be kind of inappropriate..."
                            show mom 14b
                            if pStats.chr() >= 5:
                                jump mom_kissing_practice
                            else:

                                show player 10 at left
                                show mom 14b at right
                                player_name "[chr_warn]Are you sure?"
                                player_name "[chr_warn]I'd really like to practice with you."
                                show player 5
                                mom "..."
                                show mom 13
                                mom "It's just not a good idea, Sweetie."
                                show player 10
                                show mom 14b
                                player_name "[chr_warn]Oh... A-alright."
                                show player 5
                                show mom 13
                                mom "Sorry, Sweetheart."
                                show player 10
                                show mom 14b
                                player_name "[chr_warn]It's okay, [mom_name]."
                        "Nothing":

                            show player 10 at left
                            show mom 14 at right
                            player_name "... Actually."
                            player_name "Never mind."
                            show mom 13
                            show player 5
                            mom "Are you sure?"
                            mom "You can always talk to me, [firstname]."
                            show player 10
                            show mom 14
                            player_name "Yeah, it's nothing."
                            player_name "Sorry to bug you."
                            show player 5
                            show mom 13
                            mom "You never bug me, Sweetie."

                "Practice Kissing" if M_mom.is_set("practice kissing") and location_count == "Kitchen":
                    show player 2 at left
                    show mom 1 at right
                    player_name "Do you think we could practice again?"
                    player_name "You know... Kissing?"
                    show player 1
                    show mom 13
                    mom "Again?"
                    show player 2
                    show mom 14b
                    player_name "Y-yeah. I think I'm getting better!"
                    show player 1
                    show mom 13
                    mom "... Alright."
                    mom "But just a little!"
                    show player 2
                    show mom 14
                    player_name "Okay, sure."
                    hide player
                    show mom 79 at Position(xpos=0.70, ypos=1.0) with dissolve
                    pause
                    show mom 80
                    mom "Mmm..."
                    show mom 79
                    pause
                    show mom 78 at Position(xpos=0.80, ypos=1.0) with dissolve
                    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
                    pause 
                    show mom 77
                    mom "Wow... I'd say your definitely getting better."
                    mom "... and you were already so good to begin with!"
                    show player 232
                    show mom 76
                    player_name "Thanks [mom_name]!"
                    show player 231
                    show mom 74
                    pause
                    show player 230
                    pause
                    show player 232
                    show mom 76
                    player_name "Sorry about the... You know."
                    show player 231
                    show mom 75
                    mom "Hehe, it's alright, Sweetheart."
                    mom "Perfectly natural."
                    mom "The girls in this town are in trouble."
                    show player 232
                    show mom 72
                    player_name "Hah, you bet!"
                    show player 231
                    show mom 73
                    mom "Go get em, Sweetie!"
                    show player 232
                    show mom 72
                    player_name "Yes, ma'am!"
                    $ gTimer.tick()
                "Nevermind.":

                    show player 2
                    player_name "Actually, nevermind, see you later, {b}[mom_name]{/b}."
    hide player
    hide mom
    with dissolve
    $ callScreen(location_count)

label mom_dialogue_button_room:
    scene mom_bedroom_closeup2
    show mom 55 at left
    show player 110 at right
    with dissolve
    mom "Hi, Sweetie..."
    mom "Were you looking for me?"
    show mom 54
    show player 111
    player_name "Yeah..."
    show player 110
    show mom 55
    mom "Is there something you wanted from me?"
    show mom 54
    jump mombedmenu_beforekiss
    label mombedmenu_afterkiss:
        mom "Now, is there anything else you wanted?"
        show mom 54
        menu mombedmenu_beforekiss:
            "Kiss.":
                show player 111 at right
                show mom 54 at left
                player_name "Can I have a kiss?"
                show player 110
                show mom 55
                mom "Of course, Sweetie! Come here."
                scene mom_bedroom
                show mom 79
                with fade
                mom "Mmmm..."
                show mom 80_79
                pause 3
                show mom 75 at Position(xpos=750)
                show player 227 at Position(xpos=200)
                with fastdissolve
                mom "You're getting better at this!"
                scene mom_bedroom_closeup2
                show mom 55 at left
                show player 110 at right
                with fade
                jump mombedmenu_afterkiss
            "Shower.":

                show player 111
                player_name "Hey, {b}[mom_name]{/b}!"
                player_name "Want to take a shower with me?"
                show player 110
                show mom 55
                mom "It is getting pretty hot in the house..."
                mom "Sure! A shower sounds lovely right now."
                mom "You go ahead, Sweetie. I'll be there in a minute."
                scene shower_closeup
                show moms 27
                with dissolve
                pause
                show moms 28 at Position(xpos=487,ypos=768) with dissolve
                pause
                show moms 34 with dissolve
                mom "Sorry to keep you waiting, Sweetie..."
                jump mom_shower_question
            "Have sex.":

                if randomizer() <= 50:
                    show mom 54
                    show player 111
                    player_name "I feel like... Doing it with you again."
                    show player 110
                    show mom 55
                    mom "That's okay!"
                    mom "I was hoping you'd want to..."
                    show player 111
                    show mom 54
                    player_name "Really?"
                    show player 110
                    show mom 58 with dissolve
                    mom "Of course! You're my man, after all."
                    show mom 57
                    player_name "!!!"
                    show mom 58
                    mom "Take your clothes off, Sweetie."
                    show mom 57
                    show player 8f
                    pause
                    show player 261
                    pause
                    show player 263
                    pause
                    show mom 103
                    mom "Now, lay on top of {b}Mommy{/b}..."
                    show player 262 at right
                    show mom 102 at left
                    player_name "Don't have to tell me twice..."
                else:

                    show mom 54
                    show player 111
                    player_name "{b}[mom_name]{/b}, want to have some fun?"
                    show player 110
                    show mom 54
                    mom "Oh?"
                    show mom 56 with dissolve
                    mom "Like...this kinda fun?"
                    show mom 57
                    show player 111
                    player_name "Of course..."
                    show player 110
                    show mom 58
                    mom "Let me see that cock of yours..."
                    show mom 57
                    show player 8f with dissolve
                    pause
                    show mom 101
                    show player 261 with dissolve
                    pause
                    show player 263 with dissolve
                    pause
                    show mom 58
                    mom "It looks like you are ready!"
                    show mom 57
                    show player 262
                    player_name "I've been wanting to do it with you since I got up."
                    show player 263
                    show mom 58
                    mom "Me too."
                    show mom 102 with dissolve
                    pause
                    show mom 103
                    mom "Come and get it, Sweetie."
                hide player
                show mom 104 at left
                with dissolve
                pause
                hide mom
                hide player
                with dissolve
                scene mom_bedroom_closeup_sex
                jump mom_sex

            "Laundry." if M_mom.is_set("basement sex"):
                show mom 54
                show player 111
                player_name "I was wondering if you wanted some help in the basement."
                show player 110
                show mom 55
                mom "In the basement? What for?"
                show player 111
                show mom 54
                player_name "Maybe I can help you with laundry... Like we did last time?"
                show player 110
                show mom 55
                mom "Oh, I see... I know exactly what you want!"
                mom "Give {b}Mommy{/b} a minute to get ready."
                mom "I'll meet you down there..."
                hide mom
                hide player
                with dissolve
                jump basement_mom_sex


            "Watch a Movie." if not M_mom.is_set("movie night"):
                show player 111
                player_name "I was thinking about another Mother/Son movie night. Interested?"
                show player 110
                show mom 55
                mom "Mmm, a movie night, huh?"
                mom "That sounds like a great idea, Sweetheart!"
                show player 111
                show mom 54
                player_name "Awesome!"
                player_name "I'll see you tonight in the living room then?"
                show player 110
                show mom 55
                mom "Absolutely! I can't wait..."
                $ M_mom.set("movie night", True)
            "Nevermind.":

                show mom 54
                show player 111
                player_name "Nothing, {b}[mom_name]{/b}."
                player_name "Just wanted to say hi."
                show player 110
                show mom 55
                mom "Oh, okay..."
                mom "Well, come back if you'd like... {b}Mommy{/b} is a bit bored..."
                mom "We can have fun whenever you'd like."
    hide player
    hide mom
    with dissolve
    $ callScreen(location_count)