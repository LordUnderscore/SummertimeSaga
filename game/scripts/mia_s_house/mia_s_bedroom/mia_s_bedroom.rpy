label mias_bedroom_screen:
    $ location_count = "Mia's Bedroom"
    if M_mia.get_state() == S_mia_tattoo_help:
        scene location_mia_bedroom_closeup
        show player 13 at left
        show mia 10 at right
        with dissolve
        mia "Hey!"
        mia "I'm so happy you could make it."
        show mia 7
        show player 17
        player_name "It's fine. It just seemed like you had something important to talk about."
        show player 14
        player_name "You wanted to ask me something?"
        show player 13
        show mia 10
        mia "Well, it's not THAT important..."
        mia "...I was hoping I could get your opinion on something, and maybe you could help me."
        show mia 7
        show player 10
        player_name "Uhh... I guess so. What is it about?"
        show player 11
        show mia 10
        mia "Do you know anything about tattoos?"
        show mia 7
        show player 10
        player_name "Tattoos?!"
        show player 12
        player_name "Why? Are you thinking about getting one?"
        show player 11
        show mia 12
        mia "I know it's bad..."
        mia "...But, I'm tired of being told what to do!"
        mia "I just feel like doing something... spontaneous and to have fun!"
        mia "To feel free..."
        show mia 8
        show player 10
        player_name "Is your mom going to be okay with this?"
        show player 5
        show mia 12
        mia "I don't care anymore."
        show mia 8
        show player 11
        player_name "..."
        show player 14
        player_name "Tattoos are pretty cool. I just don't want you to get into trouble."
        show player 13
        show mia 12
        mia "Are you going to help me?"
        show mia 8
        show player 14
        player_name "Sure, but how?"
        show player 13
        show mia 10
        mia "I know you like to draw stuff in class all the time, and I've seen your art..."
        mia "...I was hoping you would draw something for my tattoo!"
        show mia 7
        show player 22
        player_name "!!!" with hpunch
        show player 29 at Position(xoffset=8)
        player_name "Are you sure?"
        show player 13 with dissolve
        show mia 10
        mia "Yeah! You're so good at it."
        show mia 7
        show player 21
        player_name "Thanks, but I don't even know what you want!"
        show player 13
        show mia 10
        mia "Hmm... I want something... cute!"
        show mia 9
        mia "With pretty colors!"
        show mia 7
        show player 24
        player_name "What if it's bad... and you end up hating it?"
        show player 13
        show mia 10
        mia "I'm sure it will be fine!"
        show mia 7
        show player 14
        player_name "If you say so..."
        show player 13
        show mia 10
        mia "Come see me when you have something."
        show mia 7
        show player 14
        player_name "Alright."
        show player 13
        show mia 10
        mia "I have to go sleep. I'll see you at school!"
        show mia 7
        show player 36 with dissolve
        player_name "Good night!"
        hide player
        hide mia
        with dissolve
        $ gTimer.tick()
        $ M_mia.trigger(T_mia_delay)
        $ location_count = "Mia's House"
        $ callScreen(location_count)

    elif M_mia.get_state() == S_mia_midnight_help:
        scene expression gTimer.image("mia_bedroom{}")
        player_name "{b}Mia's{/b} not here... And I don't see any keys."
        $ callScreen(location_count)

    elif M_mia.get_state() == S_mia_study_sex:
        jump mia_bedroom_sex
    else:

        $ callScreen(location_count)


        scene location_mia_bedroom_closeup
        show mia 10 at right
        show player 13 at left with dissolve
        mia "I'm so happy you came!"
        show mia 7
        show player 21
        player_name "Hi, {b}Mia{/b}!"
        show player 29
        player_name "Feels kind of strange, sneaking into someone's house at night..."
        show mia 9
        show player 13
        mia "It's fine! We're not gonna get in trouble..."
        show mia 10
        show player 11
        mia "...We just have to {b}stay quiet{/b}!"
        show mia 7
        show player 17
        player_name "If you say so. Haha."
        show mia 12
        show player 1
    label mia_talk:
        mia "So... You want to hang out?"
        menu:
            "Chat":
                show mia 7
                show player 2
                player_name "Sure!"
                show player 10
                player_name "Umm... You don't have to answer this, but..."
                show mia 8
                player_name "Don't you find it odd that your parents won't let you have friends over?"
                show player 5
                mia "..."
                show mia 12
                mia "It's just... the way it is, with my mom."
                show mia 8
                show player 12
                player_name "And you don't mind??"
                show player 11
                show mia 12
                mia "She's just being protective!"
                mia "I know she just loves me a lot, and wants the best for me..."
                show mia 8
                show player 12
                player_name "But you have to meet with friends secretly..."
                show mia 12
                show player 5
                mia "I know... But she wouldn't understand."
                show mia 8
                show player 24
                player_name "I see..."
                show player 21
                player_name "As long as you're happy?"
                show mia 9
                show player 13
                mia "Yup!"
                jump mia_talk
            "Study":

                if M_mia.is_set('study'):
                    show player 14
                    player_name "Of course!"
                    scene mia_bedroom_closeup
                    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
                    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
                    with dissolve
                    mia "Thanks for sneaking up here again."
                    show mia 13
                    show player 142
                    player_name "It's not too hard with your parents glued to the tv."
                    show player 143
                    show mia 16
                    mia "Yeah, it's the only thing that keeps them from yelling at each other."
                    mia "They really like watching reruns."
                    mia "I sometimes watch with them when I'm done with homework."
                    show mia 22
                    mia "Most of the time I stay up here though... It's quieter."
                    show mia 14
                    show player 146
                    player_name "It kind of sucks your parents don't get along."
                    show player 141
                    show mia 18
                    mia "...Yeah."
                    mia "Maybe it will get back to the way it used to be."
                    show mia 14
                    pause
                    show mia 16
                    mia "You better go before my parents notice you."
                    show mia 13
                    show player 142
                    player_name "I'll stop over again, ok?"
                    show player 141
                    show mia 15
                    mia "Great! Goodnight {b}[firstname]{/b}!"
                    show mia 13
                    show player 142
                    player_name "Goodnight, {b}Mia{/b}."
                    hide player
                    hide mia
                    with dissolve
                    $ gTimer.tick()
                    $ location_count = "Mia's House"
                    $ callScreen(location_count)
                else:

                    show mia 7
                    show player 21
                    player_name "I guess we should be studying?"
                    show mia 9
                    show player 13
                    mia "Of course!"
                    show mia 10
                    mia "Let's do that, then."
                    show player 11
                    mia "Let me get all the textbooks and set up {b}on my bed{/b}?"
                    show mia 7
                    show player 21
                    player_name "Uh... Okay!"
                    jump mia_study
            "I have to go.":

                show mia 8
                show player 10
                player_name "I'd love to... But it's getting late..."
                show mia 12
                show player 5
                mia "Oh, okay..."
                mia "...Will you come back soon?"
                show player 14
                show mia 8
                player_name "Yeah. I'll see what I can do!"
                show mia 12
                show player 1
                mia "Good night..."
                $ callScreen(location_count)








label mia_study:
    scene mia_bedroom_closeup
    $ gTimer.tick()
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "So... I don't really know how to say this..."
    show mia 18
    show player 143
    mia "...And I'm so shy in front of people, especially boys..."
    mia "...but, I didn't really want to study."
    show player 145
    show mia 19
    player_name "Huh?"
    show mia 18
    show player 143
    mia "I couldn't come up with a better excuse to hang out..."
    mia "... And I kind of like you!"
    show player 145
    show mia 14
    player_name "Why didn't you just tell me before?"
    show mia 18
    show player 143
    mia "Well, I wanted to spend time together, but my mom would never allow it, so..."
    show mia 13
    show player 145
    player_name "It's okay. I understand!"
    show player 142
    player_name "It's nice of you to invite me. I like this..."
    show mia 16
    show player 141
    mia "What about you?"
    show mia 13
    show player 145
    player_name "Huh?"
    show mia 18
    show player 143
    menu:
        mia "Do you... Also like me?"
        "Yes.":
            show mia 19
            show player 145
            player_name "I do..."
            show mia 15
            show player 141
            mia "Really??"
            show mia 16
            show player 143
            mia "So... What do you like about me?"
            show mia 19
            show player 145
            player_name "I think you're really nice... You know..."
            player_name "...Like when you talk to me at school and stuff!"
            show mia 18
            show player 141
            mia "That's sweet!"
            show mia 19
            show player 142
            player_name "I also think that you're really pretty!"
            show player 141
            mia "..."
            show mia 18
            mia "Really?"
            menu:
                "Close your eyes.":
                    show player 142
                    show mia 19
                    player_name "Close your eyes..."
                    show mia 18
                    show player 141
                    mia "Why?"
                    show mia 19
                    show player 142
                    player_name "...Just do it."
                    show mia 17
                    show player 147
                    mia "Hmm..."
                    show mia 18
                    mia "..."
                    show player 148
                    show mia 20 at Position (xpos = 647, ypos = 574) with hpunch
                    mia "{b}!!!{/b}"
                    show mia 18 zorder 1 at Position (xpos = 680, ypos = 574)
                    show player 143
                    mia "...I can't do that... Yet!"
                    show mia 14
                    show player 146
                    player_name "...Sorry, I thought-"
                    show mia 22
                    show player 144
                    mia "No! It's fine! I'm sorry. I just can't, right now..."
                    mia "...If my mom saw us, we'd be dead."
                    show mia 14
                    show player 146
                    player_name "Oh, sorry..."
                    show player 143
                    show mia 18
                    mia "It's alright..."
                    mia "My dad probably wouldn't flip out as bad as my mom would..."
                    mia "He's actually really cool when {b}Mom{/b} is not around."
                    show mia 22
                    mia "{b}Mom's{/b} just... very religious. I'd probably be locked away and forced to study the bible."
                    show mia 14
                    show player 145
                    player_name "Wow. Really?"
                    show player 141
                    show mia 18
                    mia "She's all about sins and that stuff."
                    show mia 22
                    mia "She'd think you'd corrupt me and make me do naughty things..."
                    show mia 14
                    show player 143
                    player_name "..."
                    show player 145
                    player_name "I...I wouldn't do that!"
                    show player 143
                    show mia 15
                    mia "Ha ha, I know silly."
                    show player 144
                    show mia 16
                    mia "Anyway, it's getting late and {b}Mom{/b} will be checking in on me."
                    mia "So I should get to bed."
                    show mia 13
                    show player 142
                    player_name "Alright, {b}Mia{/b}."
                    player_name "I'll see you at {b}school{/b}!"
                    scene expression gTimer.image("mia_bedroom{}")
                    show mia 7 at right
                    show player 21 at left
                    with dissolve
                    player_name "I'll see you later, then?"
                    show mia 10
                    show player 13
                    mia "Yeah..."
                    mia "Thanks for coming."
                    show mia 7
                    show player 21
                    player_name "Good night!"
                    $ M_player.set("jerk mia", True)
                    $ M_mia.trigger(T_mia_kiss)
        "No.":

            show mia 14
            show player 146
            player_name "I see you more like... a friend."
            show mia 22
            show player 144
            mia "Ohh... I see."
            show mia 14
            show player 145
            player_name "But, this the first time we've ever hung out!"
            player_name "Give it some time. Maybe we can get to know each other better!"
            show mia 22
            show player 144
            mia "Yeah, okay..."
            scene expression gTimer.image("mia_bedroom{}")
            show mia 8 at right
            show player 21 at left
            with dissolve
            player_name "I'll see you later, then?"
            show player 13
            show mia 12
            mia "Yeah..."
            mia "Thanks for coming."
            show mia 8
            show player 21
            player_name "Good night!"
    $ location_count = "Mia's House"
    $ callScreen(location_count)

label mia_strip_show:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "You're here!!"
    show mia 7
    show player 14
    player_name "Hey {b}Mia{/b}. Am I late?"
    show player 13
    show mia 10
    mia "No, it's fine."
    show mia 12
    mia "But are you sure no one saw you come up here?"
    show mia 8
    show player 10
    player_name "Ehh... I'm pretty sure?"
    show player 12
    player_name "Is there something I should be worried about?"
    show player 11
    show mia 10
    mia "No, of course not. Just making sure no one will be disturbing us!"
    show mia 7
    show player 14
    player_name "Okay."
    player_name "So what did you want to do?"
    show player 13
    show mia 9
    mia "I have a...surprise for you."
    show mia 7
    show player 18
    player_name "..."
    show player 13
    show mia 10
    mia "I wanted to finally show you my tattoo..."
    mia "...But I want to make it special."
    show mia 7
    player_name "..."
    show mia 10
    mia "Sit on my bed..."
    scene black
    with fade
    hide player
    hide mia

    scene mia_bedroom_strip01
    show mia_strip 1 at Position (xpos=457,ypos=670)
    show player mia_strip 18 at right
    with fade
    pause
    show mia_strip 2
    mia "This is to thank you for being so nice to me..."
    show mia_strip 3 at Position (xoffset=39) with dissolve
    pause
    show mia_strip 4 at Position (xoffset=15) with dissolve
    pause
    show mia_strip 5 with dissolve
    player_name "..."
    show mia_strip 6
    mia "Do you think...I look pretty?"
    show mia_strip 5
    player_name "I- Sure! I mean, of course!"
    show mia_strip 7
    mia "Ha ha, You're sweet..."
    show mia_strip 8 with dissolve
    pause
    show mia_strip 9 with dissolve
    pause
    show mia_strip 10 with dissolve
    pause
    show mia_strip 11 with dissolve
    pause
    show mia_strip 12 with dissolve
    pause
    player_name "!!!"
    show mia_strip 13 with dissolve
    pause
    show player mia_strip 19 with dissolve
    player_name "( WOW!!! )"
    show mia_strip 14 with dissolve
    pause
    show mia_strip 15
    mia "So? Do you like it?"
    show mia_strip 14
    player_name "I- I like what? Sorry?"
    show mia_strip 16
    show player mia_strip 20 with dissolve
    mia "My tattoo, silly! Do you like-"
    show mia_strip 17
    mia "!!!"
    mia "Oh, my... What's that in your pants?!"
    scene mia_bedroom_strip02
    pause
    scene mia_bedroom_strip03
    pause
    scene mia_bedroom_strip04
    helen "..."
    scene black
    with fade
    hide player
    hide helen
    hide mia

    scene location_mia_bedroom_closeup
    show helen 6f at Position (xpos=431)
    show player 22f at right
    show mia 37 at Position (xpos=674)
    with dissolve
    pause
    show mia 39
    mia "{b}MOM{/b}!!!"
    show mia 37
    show helen 5f
    helen "What's that on your leg?!"
    show helen 7f at Position (xpos=441) with dissolve
    helen "!!!"
    helen "What's this BOY doing HERE?!!"
    show helen 8f
    show mia 36
    mia "I can explain, {b}Mom{/b}!"
    show mia 35
    show helen 7f
    helen "I can't believe you're doing this to me..."
    helen "...After raising you to be a good daughter..."
    helen "...You choose to be an adulterer, a sinner, a SCAMP!!"
    show helen 8f
    show player 16f
    show mia 38
    mia "..."
    show player 12f
    player_name "This was my idea! {b}Mia{/b} didn't-"
    show player 22f
    show helen 7f
    helen "Who said you could speak?! OR BE HERE AT ALL! {b}IN MY HOUSE{/b}!!!"
    show helen 8f
    show mia 37
    show player 23f
    player_name "!!!" with hpunch
    show player 22f
    show helen 9f at left with fastdissolve
    helen "Get out of here, {b}NOW{/b}!!"
    show mia 39
    mia "{b}Mom{/b}!!!"
    scene black
    with fade
    hide player
    hide mia
    hide helen

    scene miahouse_night
    show player 24 with dissolve
    player_name "Wow!"
    show player 37 at Position (xoffset=41) with dissolve
    player_name "{b}Helen{/b} was really mad."
    show player 25 with dissolve
    player_name "I just hope {b}Mia{/b} is not in too much trouble..."
    hide player with dissolve
    $ gTimer.tick()
    $ M_mia.trigger(T_mia_strip_tease)
    $ location_count = "Mia's House"
    $ callScreen(location_count)

label mia_bedroom_sex:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "I'm so happy you came."
    show mia 7
    show player 14
    player_name "Hi, {b}Mia{/b}."
    player_name "Your parents are back watching tv together, huh?"
    show player 13
    show mia 10
    mia "Yeah. It feels nice that everything's back to normal again."
    mia "So you want to hang out?"
    mia "Or are you here to try that new studying technique of mine?"
    show mia 7
    menu:
        "Study":
            show player 14
            player_name "I guess we should be studying."
            show player 13
            show mia 10
            mia "Of course!"
            mia "Let's do that then!"
            mia "Let me get all my textbooks and set up on my bed?"
            show mia 7
            show player 14
            player_name "Uh... Okay."
            hide player
            hide mia
            with dissolve

            scene mia_bedroom_closeup with fade
            show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
            show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
            with dissolve
            mia "Now, at least it looks like we're studying!"
            show mia 13
            player_name "..."
            show mia 16
            mia "Sorry... I guess I'm just excited to hang out like we used to..."
            show mia 13
            show player 142
            player_name "Don't worry about that. I'm just glad your happy again."
            show player 141
            show mia 16
            mia "Thanks, {b}[firstname]{/b}."
            show mia 15
            mia "Do you still think about the time I showed you my tattoo?"
            show mia 13
            show player 145
            player_name "Of course!"
            player_name "You looked so pretty."
            show player 144
            show mia 15
            mia "Don't make me blush."
            show mia 17
            show player 141
            player_name "..."
            show player mia_bed_kiss 53
            show mia 52
            with dissolve
            mia "!!!"
            hide player
            show mia 54
            with dissolve
            pause
            mia "Mmm..."
            show player 144 zorder 0 at Position (xpos = 250, ypos = 578)
            show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
            with dissolve
            mia "You're really good at kissing..."
            show mia 13
            show player 145
            player_name "...Thanks."
            show player 144
            mia "..."
            show mia 16
            mia "Want to know about that study trick I read about?"
            show mia 13
            show player 142
            player_name "Of course!"
            show player 141
            mia "..."
            show mia 16
            mia "I was hoping to try it the night my mom caught us."
            show mia 13
            show player 142
            player_name "Oh?"
            show player 141
            show mia 16
            mia "I...I've always wanted to try studying naked..."
            show mia 13
            show player 143
            player_name "!!!"
            show mia 16
            mia "Would you like to study with me... naked?"
            show mia 13
            menu:
                "Maybe later.":
                    show player 146
                    player_name "I mean... I'd really like to but I have to get back home."
                    show player 141
                    show mia 18
                    mia "Oh? Does your mommy give you a spanking if your home late?"
                    show mia 13
                    show player 145
                    player_name "Heh... Heh... No..."
                    show player 141
                    show mia 18
                    mia "I'm just kidding. It is pretty late...and I'm getting tired too."
                    hide mia
                    hide player
                    with dissolve

                    scene location_mia_bedroom_closeup
                    show mia 7 at right
                    show player 14 at left
                    with dissolve
                    player_name "Goodnight, {b}Mia{/b}."
                    player_name "I'll see you tomorrow."
                    show player 13
                    show mia 10
                    mia "Goodnight, {b}[firstname]{/b}."
                    hide player
                    show mia 49 at left
                    with dissolve
                    pause
                    show player 13 at left
                    show mia 10 at Position (xpos=300)
                    with dissolve
                    mia "I'll be... thinking of you tonight..."
                    hide player
                    hide mia
                    with dissolve
                "Sure!":

                    show player 142
                    player_name "I'd love to help you out!"
                    show player 141
                    show mia 16
                    mia "Great!"
                    mia "Umm..."
                    show mia 16
                    mia "How about you sit on the bed while I undress again."
                    mia "My parents said they won't interrupt us again."
                    mia "So just relax..."
                    mia "...and enjoy the show."
                    hide player
                    hide mia
                    with dissolve

                    label mia_strip_repeat:
                        scene mia_bedroom_strip01 with fade
                        show player mia_strip 18 at right
                        show mia_strip 1 at Position (xpos=457,ypos=670)
                        pause
                        show mia_strip 3 at Position (xoffset=39) with dissolve
                        pause
                        show mia_strip 4 at Position (xoffset=15) with dissolve
                        pause
                        show mia_strip 5 with dissolve
                        pause
                        show mia_strip 6
                        mia "Do you think... I look pretty?"
                        show mia_strip 5
                        player_name "I- Sure! I mean, of course!"
                        show mia_strip 7
                        mia "Ha ha, You're sweet."
                        show mia_strip 8 with dissolve
                        pause
                        show mia_strip 9 with dissolve
                        pause
                        show mia_strip 10 with dissolve
                        pause
                        show mia_strip 11 with dissolve
                        pause
                        show mia_strip 12 with dissolve
                        pause
                        player_name "!!!"
                        hide player
                        show player mia_strip 18 at right
                        show mia_strip 13
                        with dissolve
                        pause
                        show player mia_strip 19 with dissolve
                        player_name "( WOW!!! )"
                        hide mia_strip
                        show mia_strip 14 at Position (xpos=457,ypos=670)
                        with dissolve
                        pause
                        show mia_strip 17
                        mia "!!!"
                        show mia_strip 16
                        mia "I guess you really do think I look pretty."
                        show mia_strip 15
                        mia "Does my tattoo still look good?"
                        show mia_strip 14
                        player_name "It looks really pretty on you."
                        show mia_strip 15
                        mia "Oh yeah?"
                        mia "...What about my butt?"
                        show mia_strip 14
                        player_name "{b}*Gulp*{/b}"
                        player_name "Uhhh... Yeah... I mean... of course!"
                        player_name "You're an all around sexy girl!"
                        show mia_strip 16
                        mia "Ha ha ha."
                        show mia_strip 15
                        mia "Don't tell me you're... nervous, {b}[firstname]{/b}."
                        player_name "Maybe a little..."
                        show mia_strip 22 with dissolve
                        mia "Me too..."
                        show mia_strip 21
                        show player mia_strip 20 with dissolve
                        pause
                        show mia_strip 22
                        mia "Let me get my homework."
                        show mia_strip 23 with dissolve
                        pause
                        show mia_strip 26 with dissolve
                        mia "Here it is!"
                        show mia_strip 25
                        mia "Are you ready?"
                        show mia_strip 24
                        player_name "Yeah!"
                        show mia_strip 25
                        mia "Wow..."
                        mia "I had no idea they got that big..."
                        show mia_strip 24
                        player_name "Oh... Yeah..."
                        show mia_strip 25
                        mia "Ummm... Okay, let me lay down on the bed..."
                        mia "...And you join me..."
                        show mia_strip 27 with dissolve
                        pause
                        scene black with fade
                        hide player
                        hide mia
                        pause
                        scene mia_bed_sex with fade
                        if M_mia.get('cum 1st choice') == "":
                            show mias 2 with dissolve
                            mia "Silly boy. How are you going to study way back there?"
                            show mias 1
                            player_name "Oh... I can see everything back here."
                            player_name "I'm good."
                            show mias 2
                            mia "I bet you are."
                            mia "..."
                            show mias 5
                            mia "Um..."
                            mia "{b}[firstname]{/b}?"
                            show mias 1
                            player_name "Yes, {b}Mia{/b}?"
                            show mias 5
                            mia "..."
                            mia "Do you want to have sex?"
                            show mias 1
                            player_name "!!!"
                            show mias 2
                            mia "Whenever I've thought about studying naked..."
                            mia "...I've kinda ended up fantasizing that I ended up having...sex."
                            show mias 5
                            mia "It's my little secret fantasy..."
                            show mias 2
                            mia "Do you to try it?"
                            show mias 1
                            player_name "Yes!"
                            show mias 2
                            mia "I figured you would..."
                            show mias 5
                            mia "But... umm..."
                            mia "I have one request."
                            mia "Can you do it..."
                            mia "In my butt?"
                            show mias 2
                            mia "My parents say I should wait till I get married to actually do it."
                            mia "But I figure it won't hurt to do it in my butt."
                            mia "Is that alright?"
                            show mias 5
                            mia "If your disgusted... I understand..."
                            show mias 1
                        else:

                            show mias 2
                            mia "I thought you wanted to study naked this time?"
                            show mias 1
                            player_name "I'm studying...you."
                            show mias 2
                            mia "It's going to be hard to study if you aren't relaxed."
                            mia "Ha ha!"
                            mia "Want to do it in my butt?"
                            show mias 1
                        menu:
                            "Butt is fine.":
                                $ M_mia.set('anal sex', True)
                                player_name "I don't think it's disgusting."
                                player_name "It's kinda of rare to hear a girl want to do it there."
                                show mias 2
                                mia "Ha ha."
                                mia "I'm a rare kinda girl."

                                label mia_butt_start:
                                    show mias 4
                                    mia "Just...go slowly so it won't hurt."
                                    mia "I didn't think you'd be so...big."
                                    show mias 3
                                    pause
                                    show mias 5
                                    player_name "Alright, here's just the tip..."
                                    show mias 6b
                                    mia "Ouch!"
                                    player_name "Sorry!"
                                    mia "Don't move... Please..."
                                    player_name "Alright. Tell me when I can go deeper."
                                    mia "..."
                                    mia "Okay... Go slow."
                                    show mias 7b
                                    pause
                                    show mias 8b
                                    pause
                                    show mias 9b
                                    mia "..."
                                    player_name "There I'm all the way in."
                                    player_name "Just relax."
                                    mia "It's so big!"
                                    player_name "Yeah... it's pretty tight."
                                    mia "Alright. Just go slow."
                                    show mias 10b
                                    pause
                                    show mias 11b
                                    mia "It's not... too bad..."
                                    player_name "Ready?"
                                    mia "Uh huh."

                                    $ anim_toggle = True
                                    $ xray = False

                                    label mia_bedroom_sex_loop:
                                        hide screen mia_bedroom_sex_options
                                        show screen xray_scr
                                        pause
                                        hide screen xray_scr
                                        if anim_toggle and M_mia.is_set('anal sex'):
                                            $ animcounter = 0
                                            while animcounter < 3:
                                                show mias 7b_8b_9b_10b_11b
                                                pause 6
                                                if animcounter == 2:
                                                    mia "Ahhhh!!!{p=1}{nw}"
                                                pause 3
                                                $ animcounter += 1

                                        elif anim_toggle and not M_mia.is_set('anal sex'):
                                            $ animcounter = 0
                                            while animcounter < 3:
                                                show mias 7_8_9_10_11
                                                pause 6
                                                if animcounter == 2:
                                                    mia "Ahhhh!!!{p=1}{nw}"
                                                pause 3 
                                                $ animcounter += 1

                                        elif not anim_toggle and M_mia.is_set('anal sex'):
                                            $ animcounter = 0
                                            while animcounter < 4:
                                                show mias 7b
                                                pause
                                                show mias 8b
                                                pause
                                                show mias 9b
                                                pause
                                                show mias 10b
                                                pause
                                                show mias 11b
                                                pause
                                                $ animcounter += 1
                                                if animcounter == 2:
                                                    mia "Ahhhh!!!"
                                        else:

                                            $ animcounter = 0
                                            while animcounter < 4:
                                                show mias 7
                                                pause
                                                show mias 8
                                                pause
                                                show mias 9
                                                pause
                                                show mias 10
                                                pause
                                                show mias 11
                                                pause
                                                $ animcounter += 1
                                                if animcounter == 2:
                                                    mia "Ahhhh!!!"

                                        jump mia_bedroom_sex_menu

                            "I like the other way." if pStats.chr() < 7:
                                $ M_mia.set('anal sex', True)
                                show mias 1
                                player_name "[chr_warn]But the other way is so much better {b}Mia{/b}."
                                player_name "[chr_warn]...It's not like anyone would know we did it."
                                show mias 4
                                mia "[chr_warn]I would know, though."
                                show mias 3
                                player_name "[chr_warn]Well... it would feel a lot bette-"
                                show mias 5
                                mia "[chr_warn]No, if you want to do it with me, use my butt."
                                player_name "[chr_warn]...Alright."
                                jump mia_butt_start

                            "Just the tip!" if pStats.chr() >= 7:
                                $ M_mia.set('anal sex', False)
                                if not M_mia.is_set('vaginal sex'):
                                    $ M_mia.set('vaginal sex', True)
                                    player_name "I promise i won't go all the way in."
                                    show mias 2
                                    mia "Just the tip? ...Are you sure?"
                                    show mias 1
                                    player_name "It doesn't even count if it's just the tip..."
                                    show mias 2
                                    mia "Ha ha!"
                                    mia "It might be okay, then..."
                                    mia "But just go slowly... It's my first time..."
                                    show mias 6
                                    mia "Oh!"
                                    mia "Even the tip of you is so big!"
                                    show mias 7
                                    mia "How...does it feel?"
                                    player_name "Really good."
                                    mia "..."
                                    mia "...Go in a little deeper..."
                                    player_name "What?"
                                    mia "Can you go in a little deeper?"
                                    player_name "...Alright."
                                    show mias 8
                                    pause
                                    show mias 7
                                    pause
                                    show mias 8
                                    player_name "It's going in and out easier now."
                                    show mias 7_8
                                    pause
                                    mia "Oh...."
                                    pause
                                    mia "Ohhhh...."
                                    mia "Deeper {b}[firstname]{/b}."
                                else:

                                    show mias 2
                                    mia "Your tip sure goes in pretty far."
                                    show mias 1
                                    player_name "...Yeah..."
                                    player_name "Sorry."
                                    show mias 2
                                    mia "Don't worry. I liked it."
                                    mia "And I want your tip again."
                                    show mias 6
                                    mia "Oh!"
                                    show mias 7_8
                                    pause
                                    mia "How...does it feel?"
                                    player_name "Really good."
                                    mia "...Go in all the way..."

                                show mias 9
                                mia "Ohhh!!!"
                                show mias 7_8_9_10_11
                                pause
                                mia "Ahhh!!!"
                                mia "That feels incredible!"
                                pause
                                mia "Faster, {b}[firstname]{/b}!"
                                $ M_mia.set('sex speed', M_mia.get('sex speed') - .05)
                                jump mia_bedroom_sex_loop

                                label mia_bedroom_sex_menu:
                                    player_name "Where do you want me to cum, {b}Mia{/b}?"
                                    mia "...Anywhere."

                                    show screen mia_bedroom_sex_options
                                    pause
                                    jump mia_bedroom_sex_loop


                                    label mia_bedroom_sex_cum_outside:
                                        hide screen mia_bedroom_sex_options
                                        show mias 14 with flash
                                        player_name "UHH!!!"
                                        mia "Oh!!!"
                                        pause

                                        if M_mia.get('cum 1st choice') == "":
                                            $ M_mia.set('cum 1st choice', "Outside")
                                            show mias 16
                                            mia "So much came out of it."
                                            show mias 15
                                            player_name "Yeah."
                                            show mias 16
                                            mia "I can feel it running down my back."
                                            show mias 15
                                            player_name "Sorry."
                                            show mias 16
                                            mia "Can you get me tissues?"
                                            mia "I don't want it to leak on the sheets..."
                                        else:

                                            show mias 16
                                            mia "That was great!"
                                            mia "You sure cum pretty fast!"
                                            show mias 15
                                            player_name "Sorry..."
                                            show mias 16
                                            mia "I'm just kidding."
                                            if M_mia.is_set('cum 1st choice') == "Inside":
                                                mia "It is easier to clean up when you just cum inside me though."

                                        mia "I better get cleaned up."
                                        mia "My mom might see stains on the bedsheets..."
                                        show mias 15
                                        player_name "Sorry..."
                                        show mias 16
                                        mia "Oh don't worry."
                                        mia "That was great, {b}[firstname]{/b}."
                                        show mias 15
                                        player_name "Yeah, it was."
                                        jump mia_bedroom_sex_end

                                    label mia_bedroom_sex_cum_inside:
                                        hide screen mia_bedroom_sex_options
                                        if M_mia.get('cum 1st choice') == "":
                                            $ M_mia.set('cum 1st choice', "Inside")

                                        if M_mia.is_set('anal sex'):
                                            show mias 12b_13b with flash
                                        else:

                                            show mias 12_13 with flash
                                        player_name "UHH!!!"
                                        mia "OHH!!!"

                                        if M_mia.is_set('anal sex'):
                                            show mias 18b with dissolve
                                            mia "Wow!"
                                            if M_mia.get('sex 1st choice') == "":
                                                $ M_mia.set('sex 1st choice', "Anal")
                                                mia "So that's what anal sex feels like..."
                                                show mias 17b
                                                player_name "Did it hurt a lot?"
                                                show mias 18b
                                                mia "It wasn't so bad."
                                            mia "Did you like it?"
                                            show mias 17b
                                            player_name "Yeah!"
                                            player_name "It was really...tight."
                                            show mias 18b
                                            mia "Thanks for going slow."
                                            show mias 17b
                                            player_name "You're welcome, {b}Mia{/b}."
                                            show mias 18b
                                            mia "I better get cleaned up."
                                            mia "My mom might see stains on the bedsheets..."
                                            show mias 17b
                                            player_name "Sorry..."
                                            show mias 18b
                                            mia "Oh don't worry."
                                            mia "That was great, {b}[firstname]{/b}."
                                            show mias 17b
                                            player_name "Yeah, it was."

                                        elif M_mia.get('sex 1st choice') == "":
                                            $ M_mia.set('sex 1st choice', "Vaginal")
                                            show mias 18 with dissolve
                                            mia "That was amazing!"
                                            mia "I've never felt anything like that before."
                                            show mias 17
                                            player_name "!!!"
                                            player_name "You mean you've never...climaxed?"
                                            show mias 18
                                            mia "No, I've had orgasm before..."
                                            mia "...I meant... Like, feeling you cumming in me and stuff."
                                            show mias 17
                                            player_name "Oh..."
                                            show mias 18
                                            mia "Don't feel bad. I wanted you to."
                                        else:

                                            show mias 18
                                            mia "That felt fantastic!"
                                            mia "I still can't believe that's what an orgasm feels like."
                                            mia "It gives me the shivers thinking about it."
                                            show mias 17
                                            player_name "Really? I... really liked it too."
                                            show mias 18
                                            mia "I better get cleaned up."
                                            mia "My mom might see stains on the bedsheets..."
                                            show mias 17
                                            player_name "Sorry..."
                                            show mias 18
                                            mia "Oh don't worry."
                                            mia "That was great, {b}[firstname]{/b}."
                                            show mias 17
                                            player_name "Yeah, it was."
                                        jump mia_bedroom_sex_end

                                label mia_bedroom_sex_end:
                                if M_mia.is_set('anal sex') and M_mia.get('butt speed') < 2:
                                    $ M_mia.set('butt speed', M_mia.get('butt speed') + 1)
                                scene black with fade
                                hide mias
                                pause



                                scene location_mia_bedroom_closeup with fade
                                show player 13 at left
                                show mia 10 at right
                                with dissolve
                                mia "Thanks for helping me study, and spending time with me."
                                show mia 9
                                mia "It was a little hard to concentrate on studying, though."
                                show player 17
                                player_name "Hah hah!"
                                show mia 7
                                show player 14
                                player_name "Yeah, I liked studying with you too."
                                show player 17
                                player_name "It's the kind of studying I can definitely get behind."
                                show player 18
                                show mia 9
                                mia "Ha ha!"
                                show mia 7
                                pause
                                show player 10
                                player_name "...Does it hurt?"
                                show player 5
                                show mia 10
                                mia "A little... Heh heh."
                                mia "But I enjoyed it a lot."
                                show mia 7
                                show player 14
                                player_name "Me too."
                                player_name "I should get going. It's getting late."
                                hide player
                                show mia 49 at left
                                with dissolve
                                pause
                                show player 13 at left
                                show mia 10 at Position (xpos=300)
                                with dissolve
                                mia "Goodnight, {b}[firstname]{/b}."
                                mia "Come back and visit me again...if you want to study."
                                show mia 7
                                show player 14
                                player_name "Will do!"
                                player_name "Goodnight, {b}Mia{/b}."
                                hide player
                                hide mia
                                with dissolve
    $ gTimer.tick()
    if gTimer.is_night():
        $ location_count = "Mia's House"
    $ M_mia.trigger(T_mia_sex)
    $ callScreen(location_count)

label mia_bedroom_faster_sex:
    if not M_mia.is_set('vaginal sex'):
        if M_mia.get('butt speed') == 1:
            $ M_mia.set('sex speed', .125)
        elif M_mia.get('butt speed') > 1:
            $ M_mia.set('sex speed', M_mia.get('sex speed') - .05)
    else:
        $ M_mia.set('sex speed', M_mia.get('sex speed') - 0.05)
    jump mia_bedroom_sex_loop

label mia_bedroom_slower_sex:
    $ M_mia.set('sex speed', M_mia.get('sex speed') + 0.05)
    jump mia_bedroom_sex_loop

label mia_bedroom_teddy:
    scene location_mia_bedroom_blur
    if M_mia.is_set("telescope teddy seen"):
        show player 439 with dissolve
        player_name "This is the teddy bear {b}Mia{/b} was playing with earlier."
        player_name "Seems to have a bit of an odd funk to it..."
        show player 441
        player_name "Something smells kind of..."
        show player 440 with dissolve
        player_name "*Sniff*"
        pause
        show player 441 with dissolve
        player_name "Fishy..."
        player_name "Mr. Teddy, you've seen some terrible things haven't you."
        player_name "I wonder why she likes him so much?"
        show player 438
        pause
        show player 439
        player_name "Looks like there's a hole in the back..."
        player_name "Huh. He has a little pouch."
        player_name "Looks like you could hide something in there."
    else:

        show player 438 with dissolve
        pause
        show player 439
        player_name "This teddy bear has been in her room since we were kids."
        player_name "I wonder why she still keeps it around..."
    hide player with dissolve
    $ callScreen(location_count)