label mia_button_dialogue:
    if M_helen.is_set('helen route'):
        if location_count == "Mia's Bedroom":
            scene mia_bedroom_c
        elif location_count == "Science Classroom":
            scene science_classroom_c
        elif location_count == "Mia's House Entrance":
            scene mia_house_c
        show mia 8 at right
        show player 10 at left
        with dissolve
        player_name "Hi, {b}Mia{/b}."
        show player 5
        show mia 12
        mia "Oh... Hello, {b}[firstname]{/b}."
        show mia 8
        show player 10
        player_name "..."
        show player 11
        pause
        show player 10
        player_name "So how are you doing?"
        show player 5
        show mia 12
        mia "I'm still feeling a bit sad about my family not being together."
        show mia 46f
        mia "I miss waking up and seeing my dad every morning."
        mia "And {b}Mom{/b} seems more distant lately."
        show mia 45f
        show player 10
        player_name "Huh..."
        show player 12
        player_name "Hey, do you want to do something later?"
        show player 10
        player_name "There's another quiz coming up. Want to study?"
        show player 5
        show mia 46f
        mia "No. I don't feel like doing anything right now."
        show mia 45f
        show player 24
        player_name "..."
        show player 10
        player_name "Well, I'll catch up with you later then!"
        show player 5
        mia "..."
        hide player
        hide mia
        with dissolve
        $ callScreen(location_count)

    elif M_mia.get_state() == S_mia_helen_change_news:
        if location_count == "Mia's Bedroom":
            scene mia_bedroom_c
        elif location_count == "Science Classroom":
            scene science_classroom_c
        elif location_count == "Mia's House Entrance":
            scene mia_house_c
        show player 13 at left
        show mia 10 at right
        with dissolve
        mia "{b}[firstname]{/b}!"
        mia "What happened?"
        show mia 7
        show player 14
        player_name "I talked to your mom. I think I got through to her!"
        show player 13
        show mia 10
        mia "You did?! But how..."
        show mia 7
        show player 17
        player_name "I know, it's a long story..."
        show player 14
        player_name "...But everything will be fine. I promise!"
        player_name "We spoke and she agreed to try changing things so they can get back together!"
        show player 13
        show mia 9
        mia "That's amazing!"
        show mia 7
        show player 14
        player_name "I think she will be more lenient with you also..."
        player_name "...I feel like she will change her attitude."
        show player 13
        show mia 10
        mia "Wow... You must have really worked hard on convincing her!"
        show mia 7
        show player 17
        player_name "I have a few tricks up my sleeve. Ha ha!"
        show player 13
        show mia 10
        mia "I'm so happy! Thank you, {b}[firstname]{/b}!"
        show mia 7
        pause
        hide player
        show mia 49 at left
        with dissolve
        player_name "!!!"
        show player 11 at left
        show mia 10 at right
        with dissolve
        mia "I'll see you later, then!"
        show mia 7
        show player 21
        player_name "Bye."
        hide player
        hide mia
        with dissolve
        $ M_mia.trigger(T_mia_thanks)
        $ callScreen(location_count)

    if location_count == "Mia's Bedroom":
        if M_mia.get_state() == S_mia_end:
            scene location_mia_bedroom_closeup
            show player 13 at left
            show mia 10 at right
            with dissolve
            mia "I'm so happy you came."
            show mia 7
            show player 14
            player_name "Hi, {b}Mia{/b}."
            show player 13
            show mia 10
            mia "So you want to hang out?"
            mia "Or are you here to try that new studying technique of mine?"
            show mia 7
            menu:
                "Study":
                    player_name "Want to...study naked again?"
                    show player 13
                    show mia 10
                    mia "Yeah!"
                    mia "Sit on the bed while I change."
                    hide player
                    hide mia
                    with dissolve
                    $ M_mia.set('sex speed', .175)
                    jump mia_strip_repeat
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

        elif M_mia.get_state() == S_mia_night_visit:
            jump mia_strip_show

        elif M_mia.get_state() == S_mia_tattoo_help:
            scene location_mia_bedroom_closeup
            show player 13 at left
            show mia 10 at right
            with dissolve
            mia "Hey!"
            mia "I'm so happy you could make it!"
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
            show player 29
            player_name "Are you sure?"
            show player 13 with dissolve
            show mia 10
            mia "Yeah! You're so good at it."
            show mia 7
            show player 21
            player_name "Thanks, but I don't even know what you want!"
            show player 13
            show mia 10
            mia "Hmm... I want something cute!"
            show mia 9
            mia "With pretty colors!"
            show mia 7
            show player 24
            player_name "What if it's bad, and you end up hating it?"
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

        elif M_mia.get_state() == S_mia_church_plan:
            scene location_mia_bedroom_closeup
            show player 13 at left
            show mia 12 at right
            with dissolve
            player_name "Hey, {b}Mia{/b}."
            player_name "Thought I'd sneak up and see you."
            show player 5
            show mia 10
            mia "Aww, thanks. I appreciate it."
            mia "What's up?"
            show mia 7
        else:

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

    elif location_count == "Science Classroom":
        if M_mia.get_state() == S_mia_strip_aftermath:
            scene school_science_c02
            show player 5 at left
            show mia 12 at right
            with dissolve
            mia "Hey, {b}[firstname]{/b}..."
            show mia 8
            show player 10
            player_name "How are you?"
            show player 5
            show mia 12
            mia "I'm okay, but we really shouldn't be talking."
            mia "I'm in enough trouble as it is... Sorry."
            show mia 8
            show player 24
            player_name "..."
            hide mia
            hide player
            with dissolve
            $ callScreen(location_count)

        elif M_mia.get_state() == S_mia_consult:
            scene science_classroom_c
            show player 1 at left
            show mia 9 at right
            with dissolve
            mia "{b}[firstname]{/b}!"
            show mia 7
            show player 14
            player_name "Hey, {b}Mia{/b}!"
            show mia 10
            show player 13
            mia "I wanted to thank you for coming to visit me the other night..."
            show player 11
            mia "... I really enjoyed it, but..."
            show mia 7
            player_name "..."
            show mia 8
            show player 10
            player_name "Is something wrong?"
            show mia 12
            show player 11
            mia "Well, my mom is growing suspicious."
            show mia 8
            show player 10
            player_name "Of me?"
            show mia 12
            show player 5
            mia "Yeah, I think she knows you came over."
            show mia 8
            show player 10
            player_name "Is it really that big of a deal?"
            show mia 12
            show player 5
            mia "She's definitely NOT okay with it."
            show player 11
            mia "I mean, maybe if somehow... you got on my dad's good side? I'm sure he could talk to her."
            show mia 8
            show player 10
            player_name "Your dad? But how?"
            show mia 7
            player_name "He seems pretty strict too!"
            show mia 9
            show player 11
            mia "No way, he's a big softie..."
            show mia 10
            show player 1
            mia "He used to be really cool, you know?"
            show mia 7
            show player 14
            player_name "Okay, so how can I get on his good side?"
            show mia 10
            show player 1
            mia "Hmm... I'm not sure..."
            mia "Maybe try and get him something he likes, like a box of donuts!"
            show mia 7
            show player 14
            player_name "Donuts?"
            show mia 9
            show player 1
            mia "Ha ha. I know... So typical. But, he really likes them!"
            show mia 8
            show player 14
            player_name "Does he have a favourite kind of donut?"
            show mia 12
            show player 1
            mia "Oh, I'm not really sure..."
            show mia 7
            show player 14
            player_name "Alright! Maybe I can find out and get him something."
            show mia 10
            show player 1
            mia "Thanks! You're so sweet... I'm sure he'll love it!"
            show unlock50 at truecenter with dissolve
            $ loc_donuts_unlocked = True
            pause
            hide unlock50 with dissolve
            show mia 7
            $ M_mia.trigger(T_mia_plan)

        elif M_mia.get_state() == S_mia_parent_unblock:
            scene science_classroom_c
            show player 1 at left
            show mia 9 at right
            with dissolve
            mia "{b}[firstname]{/b}!"
            show mia 10
            show player 11
            mia "You won't believe this!"
            show player 14
            show mia 7
            player_name "Huh? What happened?"
            show player 1
            show mia 10
            mia "Last night, I heard my dad talking about you with my mom!"
            show player 14
            show mia 7
            player_name "About me? For real?"
            show player 1
            show mia 9
            mia "Yeah!"
            show mia 10
            mia "He was saying how important it was to make friends at my age..."
            mia "... how he thought she should let me see you, since you're a good person and all..."
            show player 14
            show mia 7
            player_name "Woa..."
            player_name "So, your mom is cool with me now?!"
            show player 11
            show mia 10
            mia "Well, she wasn't too pleased with the idea, that's for sure!"
            show player 1
            show mia 9
            mia "But, I think it might have worked a little bit."
            show player 17
            show mia 7
            player_name "I guess it's something."
            show player 13
            show mia 10
            mia "Thanks for speaking with my dad..."
            show player 14
            show mia 7
            player_name "It's not a big deal, and your dad seems like a cool guy, actually!"
            show player 1
            show mia 10
            mia "Yeah... He used to have more say in our lives."
            show player 14
            show mia 8
            player_name "Anyway, I should get back to class-"
            show player 11
            show mia 12
            mia "Wait!! I..."
            mia "I wanted to get your opinion on something."
            show player 14
            show mia 8
            player_name "Something?"
            show player 11
            show mia 12
            mia "I don't really feel comfortably talking about it here..."
            show player 13
            mia "But maybe... you could visit me tonight?"
            show player 14
            show mia 7
            player_name "I'd love to!"
            show player 1
            show mia 9
            mia "Sweet!"
            show mia 10
            mia "I'll be waiting for you at home, then."
            hide mia
            hide player
            with dissolve
            $ M_mia.trigger(T_mia_results)
            $ callScreen(location_count)

        elif M_mia.get_state() == S_mia_favor:
            scene school_science_c02 with fade
            show player 13 at left
            show mia 10 at right
            with dissolve
            mia "Good morning, {b}[firstname]{/b}!"
            show mia 7
            show player 14
            player_name "Good morning, {b}Mia{/b}."
            show player 13
            show mia 10
            mia "I was hoping you could help me with something... once again?"
            show mia 7
            show player 14
            player_name "Of course, {b}Mia{/b}. I don't mind!"
            show player 13
            show mia 10
            mia "I want you to work your magic and get my dad to come out for dinner with my mom and I."
            mia "He listens to you..."
            show mia 7
            show player 14
            player_name "Dinner? Sounds like your parents are on goods terms again."
            player_name "I'll stop by his work and see what I can do!"
            show player 13
            show mia 12
            mia "I appreciate your help, {b}[firstname]{/b}. I just don't know what I'd do with myself if they don't get back together."
            show mia 46f
            mia "I feel like all of this is my fault..."
            show mia 45f
            show player 10
            player_name "Oh, come on, {b}Mia{/b}... You can't think that way!"
            show player 14
            player_name "Don't worry, I'll get your dad to that dinner date."
            show player 13
            show mia 46f
            mia "Thanks... You're sweet."
            hide mia
            hide player
            with dissolve
            $ M_mia.trigger(T_mia_dinner_plan)
            $ callScreen(location_count)

        elif M_mia.get_state() == S_mia_need_space:
            scene school_science_c02
            show player 10 at left
            show mia 8 at right
            with dissolve
            player_name "Hey, {b}Mia{/b}..."
            player_name "How are you?"
            show player 5
            show mia 12
            mia "I'm doing okay."
            show mia 8
            mia "..."
            show player 3 with dissolve
            player_name "..."
            show mia 12
            mia "I think I just want some space right now."
            show mia 8
            show player 10 with dissolve
            player_name "Alright..."
            player_name "I'll talk to you later. Just let me know if you need something, though."
            show player 5
            show mia 12
            mia "Thanks, {b}[firstname]{/b}..."
            hide mia
            hide player
            with dissolve
            $ callScreen(location_count)

        elif M_mia.get_state() == S_mia_church_plan:
            scene school_science_c02
            show player 12 at left
            show mia 8 at right
            with dissolve
            player_name "Hey, {b}Mia{/b}!"
            player_name "How are you?"
            show player 5
            show mia 12
            mia "I'm alright."
            mia "But I wish things could go back to the way they were before at home."
            show mia 8
            show player 10
            player_name "Sorry..."
            show player 5
            show mia 12
            mia "Is there something you wanted to talk about?"
            show mia 8

        elif M_mia.get_state() == S_mia_urgent_help:
            scene school_science_c02
            show player 5 at left
            show mia 12 at right
            with dissolve
            mia "Hey, {b}[firstname]{/b}!"
            mia "Please {b}stop at my house later today{/b}, alright?"
            show mia 8
            show player 10
            player_name "Alright."
            show player 5
            show mia 12
            mia "Anything else you needed?"
            show mia 8
        else:

            scene school_science_c02
            show player 14 at left
            show mia 7 at right
            with dissolve
            player_name "Hey, {b}Mia{/b}!"
            player_name "How are you?"
            show player 13
            show mia 10
            mia "I'm doing okay."
            show mia 12
            mia "Not really looking forward to my next class."
            show mia 7
            show player 17
            player_name "Yeah. I hear ya."
            show player 13
            show mia 10
            mia "Is there something you wanted to talk about?"
            show mia 7

    elif location_count == "Mia's House Entrance":
        if M_mia.get_state() == S_mia_favor:
            scene mia_house_c with fade
            show player 13 at left
            show mia 10 at right
            with dissolve
            mia "Good morning, {b}[firstname]{/b}!"
            show mia 7
            show player 14
            player_name "Good morning, {b}Mia{/b}."
            show player 13
            show mia 10
            mia "I was hoping you could help me with something...once again?"
            show mia 7
            show player 14
            player_name "Of course, {b}Mia{/b}. I don't mind!"
            show player 13
            show mia 10
            mia "I want you to work your magic and get my dad to come out for dinner with my mom and I."
            mia "He listens to you..."
            show mia 7
            show player 14
            player_name "Dinner? Sounds like your parents are on goods terms again."
            player_name "I'll stop by his work and see what I can do!"
            show player 13
            show mia 12
            mia "I appreciate your help, {b}[firstname]{/b}. I just don't know what I'd do with myself if they don't get back together."
            show mia 46f
            mia "I feel like all of this is my fault..."
            show mia 45f
            show player 10
            player_name "Oh, come on, {b}Mia{/b}... You can't think that way!"
            show player 14
            player_name "Don't worry, I'll get your dad to that dinner date."
            show player 13
            show mia 46f
            mia "Thanks... You're sweet."
            hide mia
            hide player
            with dissolve
            $ M_mia.trigger(T_mia_dinner_plan)
            $ callScreen(location_count)

        elif M_mia.get_state() == S_mia_helen_talk:
            scene mia_house_c
            show player 5 at left
            show mia 12 at right
            with dissolve
            mia "Can you talk to my mom?"
            show player 10
            show mia 8
            player_name "I'll try, {b}Mia{/b}."
            hide mia
            hide player
            with dissolve
            $ callScreen(location_count)

        elif M_mia.get_state() in [S_mia_church_plan, S_mia_clues]:
            scene mia_house_c
            show player 13 at left
            show mia 12 at right
            with dissolve
            mia "Hi, {b}[firstname]{/b}."
            show player 5
            pause
            show player 10
            show mia 8
            player_name "Hello, {b}Mia{/b}."
            show player 5
            show mia 12
            mia "What's up?"
            show mia 8
        else:

            scene mia_house_c
            show player 13 at left
            show mia 10 at right
            with dissolve
            mia "Hi, {b}[firstname]{/b}."
            show player 14
            show mia 7
            player_name "Hello, {b}Mia{/b}."
            show player 13
            show mia 10
            mia "What's up?"
            show mia 7

    menu mia_dialogue:
        "Chat" if location_count == "Mia's Bedroom":
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
            jump mia_dialogue

        "Parents." if location_count == "Science Classroom" and M_mia.get_state() in [S_mia_start, S_mia_do_homework, S_mia_wait_homework, S_mia_parent_blocking, S_mia_consult, S_mia_impress_harold, S_mia_parent_unblock, S_mia_tattoo_help, S_mia_find_easel, S_mia_draw_tattoo, S_mia_show_tattoo, S_mia_get_tattoo, S_mia_buy_tattoo, S_mia_return_favor, S_mia_night_visit, S_mia_strip_aftermath, S_mia_midnight_call, S_mia_midnight_help, S_mia_locked_room, S_mia_need_space, S_mia_concerning_visit, S_mia_helen_fight, S_mia_helen_talk, S_mia_helen_refusal]:
            show player 14
            player_name "So, how are your parents doing?"
            show player 13
            show mia 10
            mia "Busy. My mom is always at church and dad is always working."
            show mia 12
            mia "Probably best that way."
            show mia 8
            show player 10
            player_name "How so?"
            show player 11
            show mia 12
            mia "When my parents get together all they do is argue."
            show player 5
            mia "I hate it so much."
            mia "I wish they got along better, like they used to..."
            show mia 8
            show player 10
            player_name "I didn't know it was like that. They seemed alright."
            show player 5
            show mia 12
            mia "Yeah, my mom seems to stir the pot the most, though."
            mia "She is very heavy handed and won't take no for an answer."
            mia "So {b}Dad{/b} just goes along anything she says now..."
            show mia 8
            show player 10
            player_name "That sucks."
            show player 5
            show mia 12
            mia "She's even been forcing me to do bible studies lately..."
            mia "...And says I should meet a boy from the church, when I'm ready."
            show mia 8
            show player 11
            player_name "..."
            show mia 12
            mia "I know, it's... weird."
            show mia 9
            mia "Anyway! Let's talk about something else."
            show mia 7
            show player 13
            jump mia_dialogue

        "{b}Harold{/b}." if M_mia.get_state() == S_mia_clues:
            show player 10
            player_name "Where did you say I could find clues about {b}Harold's{/b} whereabouts?"
            show player 5
            show mia 12
            mia "Start by questioning his coworkers at the {b}police station{/b}..."
            mia "...And look for {b}clues{/b} around his workplace."
            show mia 8
            show player 12
            player_name "I suppose I can ask around to see where he could be..."
            show player 5
            show mia 12
            mia "Thank you..."
            hide player
            hide mia
            with dissolve

        "{b}Harold{/b}." if M_mia.get_state() == S_mia_convince_harold:
            show player 10
            player_name "What did you need me to get your dad to do again?"
            show player 13
            show mia 10
            mia "I want you to invite him out to dinner with my mother and I."
            mia "You both get along so well together. Maybe you can twist his arm if needed."
            show mia 7
            show player 14
            player_name "Sure! I'll catch up with him at the {b}police station{/b}."
            show player 13
            show mia 10
            mia "Thanks, {b}[firstname]{/b}."
            hide mia
            hide player
            with dissolve

        "Glasses." if M_mia.get_state() == S_mia_harold_gift:
            show player 12
            player_name "What did you want me to do with these glasses again?"
            show player 5
            show mia 10
            mia "Oh, I was hoping you could drop them off at my dad's work."
            show mia 7
            show player 14
            player_name "That's right... I remember now."
            player_name "I'll get to it, then!"
            hide player
            hide mia
            with dissolve

        "Donuts." if M_mia.get_state() == S_mia_impress_harold:
            show player 14 at left
            show mia 7 at right
            player_name "Any ideas on how can I find out what kind of donuts your dad likes?"
            show player 1
            show mia 10
            mia "Oh, ehmm..."
            mia "Maybe ask around his work?"
            mia "They LOVE eating donuts over there..."
            show mia 7
            show player 17
            player_name "Ha ha, maybe you're right, that could work."
            show mia 10
            show player 1
            mia "Anything else you want to talk about?"
            show mia 7
            show player 1
            jump mia_dialogue

        "Tattoo." if M_mia.get_state() in [S_mia_find_easel, S_mia_draw_tattoo]:
            show mia 7 at right
            show player 10 at left
            player_name "About that tattoo art you wanted..."
            show player 5
            show mia 10
            mia "Oh! Do you have it?!"
            show mia 7
            show player 10
            player_name "No, not yet."
            player_name "But, what was it you wanted again?"
            show player 5
            show mia 10
            mia "Hmm... Something cute and colorful!"
            show mia 7
            show player 17
            player_name "Ha ha, alright."
            show player 14
            player_name "I'll see what I can do."
            show player 13
            show mia 9
            mia "Thank you so much, {b}[firstname]{/b}."
            hide player
            hide mia
            with dissolve

        "Tattoo." if list(set([tattoo_dolphin, tattoo_stars, tattoo_flowers, tattoo_skull, tattoo_cookie]) & set(inventory.items)):
            show mia 7 at right
            show player 2 at left
            player_name "About that tattoo art you wanted..."
            show player 13
            show mia 10
            mia "Oh! Do you have it?!"
            show mia 7
            show player 14
            player_name "Yup!"
            show player 239_240 with dissolve
            player_name "It took me a while to make it..."
            show player 386 with dissolve
            player_name "Here it is!"
            show player 13
            show mia 32
            with dissolve
            mia "Hmm..."
            show player 10
            player_name "Is something wrong?"
            show player 11
            show mia 33
            mia "Well, I was hoping for something different."
            show mia 34
            show player 25
            player_name "Oh..."
            show player 24
            show mia 30
            mia "I like it!!"
            show mia 33
            mia "But maybe you can try something else?"
            show mia 34
            show player 10
            player_name "Like what?"
            show player 5
            show mia 30
            mia "Try something cute, that has pretty colors!"
            show mia 31
            show player 14
            player_name "Alright, I'll try and make something else..."
            show player 13
            show mia 30
            mia "Thank you so much, {b}[firstname]{/b}."
            hide player
            hide mia
            with dissolve
            $ inventory.items.remove(tattoo_choices[drawn_tattoo])
            $ M_mia.trigger(T_mia_wrong_tattoo)

        "Tattoo." if tattoo_butterfly in inventory.items:
            show mia 7 at right
            show player 2 at left
            player_name "About that tattoo art you wanted..."
            show player 13
            show mia 10
            mia "Oh! Do you have it?!"
            show mia 7
            show player 14
            player_name "Yup!"
            show player 239_240 with dissolve
            player_name "It took me a while to make it..."
            show player 386 with dissolve
            player_name "Here it is!"
            show player 13
            show mia 29
            with dissolve
            mia "WOW!!!"
            show mia 30
            mia "I absolutely LOVE it!"
            show mia 31
            show player 17
            player_name "Really?"
            show player 18
            show mia 30
            mia "Yeah!"
            show mia 29
            mia "It's so pretty..."
            show mia 31
            show player 14
            player_name "Cool! I'm glad you like it."
            show player 13
            show mia 30
            mia "We should visit {b}Sugar Tats{/b} and see if they can make it for me."
            show mia 7 with dissolve
            show player 12
            player_name "Now?!"
            show player 5
            show mia 9
            mia "Not right now, silly!"
            show mia 10
            mia "How about {b}Saturday{/b}?"
            show mia 7
            show player 10
            player_name "Okay, I can meet you there on {b}Saturday{/b}."
            show player 5
            show mia 10
            mia "Promise you'll meet me there {b}during the day{/b}!"
            show mia 7
            show player 14
            player_name "I promise!"
            show player 13
            show mia 10
            mia "Okay, good. I'm not sure I can do it on my own, ha ha."
            mia "See you then."
            hide player
            hide mia
            with dissolve
            show unlock47 at truecenter with dissolve
            $ loc_tattoo_unlocked = True
            $ renpy.pause()
            hide unlock47 with dissolve
            $ inventory.items.remove(tattoo_choices[drawn_tattoo])
            $ M_mia.trigger(T_mia_right_tattoo)

        "Sugar Tats" if M_mia.get_state() in [S_mia_get_tattoo, S_mia_buy_tattoo]:
            show mia 7 at right
            show player 12 at left
            player_name "About that tattoo..."
            show player 5
            show mia 12
            mia "Are you still coming?"
            show mia 8
            show player 14
            player_name "Of course!"
            show player 10
            player_name "But when did you want to go?"
            show player 11
            show mia 12
            mia "You already forgot?!"
            show mia 8
            show player 21
            player_name "I guess I just have a lot on my mind lately..."
            show player 13
            show mia 9
            mia "It's okay, ha ha."
            show mia 10
            mia "I need you to meet me on {b}Saturday{/b} at the {b}tattoo parlour{/b}, {b}during the day{/b}!"
            show mia 7
            show player 14
            player_name "Alright, I'll make sure to be there with you."
            show player 13
            show mia 10
            mia "Thank you so much, {b}[firstname]{/b}."
            hide player
            hide mia
            with dissolve

        "Church." if M_mia.get_state() == S_mia_church_plan:
            show player 12
            player_name "When does your mom go to church?"
            show player 5
            show mia 12
            mia "On the {b}weekend in the morning{/b}."
            show mia 8
            show player 34
            player_name "Hmm..."
            show player 14
            player_name "Alright, thanks."
            show player 13
            show mia 12
            mia "What are you going to do?!"
            show mia 8
            show player 12
            player_name "I'm not totally sure yet, but I'll get back to you if I find a way."
            show player 13
            show mia 12
            mia "Okay..."
            hide player
            hide mia
            with dissolve

        "Homework." if location_count == "Science Classroom":
            show player 14
            player_name "What did you want to study together on?"
            show player 13
            if M_mia.get_state() not in [S_mia_start, S_mia_do_homework, S_mia_wait_homework, S_mia_parent_blocking, S_mia_consult, S_mia_impress_harold, S_mia_parent_unblock, S_mia_tattoo_help, S_mia_find_easel, S_mia_draw_tattoo, S_mia_show_tattoo, S_mia_get_tattoo, S_mia_buy_tattoo, S_mia_return_favor, S_mia_night_visit, S_mia_strip_aftermath, S_mia_midnight_call, S_mia_midnight_help, S_mia_locked_room, S_mia_need_space, S_mia_concerning_visit, S_mia_helen_fight, S_mia_helen_talk, S_mia_helen_refusal, S_mia_study_sex, S_mia_end]:
                show mia 12
                mia "I'm not really feeling up to it right now."
                show mia 8
                show player 10
                player_name "Alright..."
                show player 5
                show mia 12
                mia "Sorry."
                mia "I just want my parents to be back together."
                show mia 8
                show player 10
                player_name "I know."
                player_name "Just let me know if you need my help."
                show player 5
                show mia 12
                mia "Thanks, {b}[firstname]{/b}."
                show mia 8
            else:
                show mia 10
                mia "We'd be studying things related to the last {b}French class homework{/b}. Did you hand that assignment in yet?"
                show mia 7
                if M_mia.get_state() == S_mia_do_homework:
                    show player 24
                    player_name "No. I'm still working on it."
                    show player 13
                    show mia 10
                    mia "Well once you have it done, {b}stop over to my house{/b}."
                    hide mia with dissolve
                    show player 5 with dissolve
                    player_name "( I should try and finish my {b}french homework{/b}, so I can study with {b}Mia{/b}. )"
                    show player 4 with dissolve
                    pause
                    player_name "( I wonder why she picked me to help her study. )"
                    player_name "( She usually studies with {b}Judith{/b} and she's really good in French... )"
                    player_name "( ...I'm not sure how I could help her. )"
                    show player 13 with dissolve
                    player_name "( At least we'll get to hang out, and she's really cute... )"
                    hide player with dissolve
                    $ callScreen(location_count)
                else:

                    show player 14
                    player_name "I turned it in not that long ago."
                    show player 13
                    show mia 10
                    mia "When you have the time, {b}sneak up to my room{/b} in the evening so we can study then."
                    show mia 7
                    show player 17
                    player_name "Will do!"
                    show player 13
                jump mia_dialogue

        "Study" if location_count == "Mia's Bedroom":
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
                player_name "It's not too hard with your parents glued to the TV."
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
                mia "You better get going before my parents notice you."
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

                if M_mia.get_state() in [S_mia_start, S_mia_do_homework, S_mia_wait_homework, S_mia_parent_blocking, S_mia_consult, S_mia_impress_harold, S_mia_parent_unblock, S_mia_tattoo_help, S_mia_find_easel, S_mia_draw_tattoo, S_mia_show_tattoo, S_mia_get_tattoo, S_mia_buy_tattoo, S_mia_return_favor, S_mia_night_visit, S_mia_strip_aftermath, S_mia_midnight_call, S_mia_midnight_help, S_mia_locked_room, S_mia_need_space, S_mia_concerning_visit, S_mia_helen_fight, S_mia_helen_talk, S_mia_helen_refusal]:
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
                else:
                    show player 12
                    player_name "Did you want to study together?"
                    show player 5
                    show mia 12
                    mia "I'm not really feeling up to it right now."
                    show mia 8
                    show player 10
                    player_name "Alright..."
                    show player 5
                    show mia 12
                    mia "Sorry."
                    mia "I just want my parents to be back together."
                    show mia 8
                    show player 10
                    player_name "I know."
                    player_name "Just let me know if you need my help."
                    show player 5
                    show mia 12
                    mia "Thanks, {b}[firstname]{/b}."
                    show mia 8
                    jump mia_dialogue

        "Nothing." if location_count == "Science Classroom":
            show player 10
            player_name "Actually, I better get back to class."
            show player 5
            show mia 12
            mia "Oh, okay... Talk to you later then!"
            show mia 8
            show player 14
            player_name "See ya!"
            hide player
            hide mia
            with dissolve

        "I have to go." if location_count == "Mia's Bedroom":
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

        "I have to go." if location_count == "Mia's House Entrance":
            show player 10
            player_name "Actually, I remember I had something I needed to do."
            show player 5
            show mia 12
            mia "Oh, okay... Talk to you later then!"
            show mia 8
            show player 14
            player_name "See ya!"
            hide player
            hide mia
            with dissolve
    $ callScreen(location_count)