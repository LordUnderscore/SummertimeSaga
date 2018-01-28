default first_revealing = True

label home_kitchen_dialogue:
    $ location_count = "Kitchen"
    if not gTimer.is_dark():
        if gTimer.is_morning() and sister.over(sis_telescope01) and not sister.known(sis_breakfast):
            scene homekitchen
            show player 1 at left
            show mom 2 at right
            with dissolve
            mom "Hey, Sweetie!"
            mom "Hungry for some breakfast?"
            show mom 51 at Position(xpos=1025)
            show player 10
            player_name "I don't know If I have time, {b}[mom_name]{/b}."
            if gTimer.is_weekend():
                player_name "I have to meet {b}Erik{/b} at his house..."
            else:
                player_name "I'm running late for school."
            show player 11
            show mom 52
            mom "Honey, you have to eat!"
            show player 11
            if gTimer.is_weekend():
                mom "I don't care if your friend {b}Erik{/b} has to wait all day..."
            else:
                mom "I don't care if your school calls me to complain about being late..."
            show player 1
            mom "You can't just go out on an empty stomach!"
            show player 14
            show mom 51
            player_name "I guess I could take a few minutes to eat something..."
            show player 1
            show mom 2
            mom "I prepared some cereal for you in the {b}dining room{/b}."
            hide player
            hide mom
            with dissolve
            $ lock_ui()
            $ sister.add_event(sis_breakfast)
            $ callScreen(location_count)

        elif M_mom.get_state() == S_mom_start:
            scene expression gTimer.image("homekitchen{}")
            show player 1 at left with dissolve
            show mom 2 at right with dissolve
            mom "Good morning, Sweetie! I made you some breakfast!"
            mom "I thought you'd like something special for your first day back at school."
            show player 2
            show mom 1
            player_name "Thanks, {b}[mom_name]{/b}, but I'm not really hungry and I'm running late for school, so..."
            show player 1
            show mom 2
            mom "You're sure? I made your favorite..."
            mom "Happy face pancakes with three strips of baaaacon!"
            show mom 1
            show player 10
            player_name "Oh man..."
            show player 11
            player_name "..."
            show player 10
            player_name "No, I really shouldn't..."
            player_name "I think {b}Erik{/b} overslept again and I don't wanna be late on my first day back."
            show player 11
            show mom 3
            mom "Hah, again huh?"
            show player 1
            show mom 2
            mom "Well I guess you'd better get a move on then."
            show player 2
            show mom 1
            player_name "Yeah, thanks anyways, {b}[mom_name]{/b}!"
            show player 1f with dissolve
            show mom 2
            mom "My pleasure, Sweet- Oh! Wait!"
            show player 1 with dissolve
            player_name "Hmm?"
            show mom 3
            mom "I nearly forgot!"
            show mom 2
            mom "I spoke with {b}Aunt Diane{/b} yesterday and she mentioned that she could use someone to {b}help with cleaning her garden{/b} over the summer!"
            show player 10
            show mom 1
            player_name "Hmm, I don't really know much about gardening {b}[mom_name]{/b}..."
            show player 11
            show mom 3
            mom "Oh c'mon, It's easy! {b}Aunt Diane{/b} can teach you and if you do a good job she'll pay you as well!"
            show mom 2
            mom "It could be a good way to {b}earn{/b} some money for college, don't you think?"
            show player 10
            show mom 1
            player_name "Yeah, I guess you're right."
            show player 2
            player_name "I should go visit her and see what she wants me to do."
            show mom 2
            mom "That's my boy!"
            hide player
            show mom 4b
            with dissolve
            mom "I know these last few weeks have been hard..."
            mom "But your {b}Father{/b} would want us to carry on, you know?"
            mom "We'll get through this. I promise things will get better."
            show mom 5b
            player_name "Yeah, I-I know. Thanks {b}[mom_name]{/b}..."
            mom "Oh, I love you Sweetie!"
            hide mom with dissolve

            show unlock14 at truecenter
            $ renpy.pause()
            hide unlock14 with dissolve

            show unlock12 at truecenter
            $ renpy.pause()
            hide unlock12 with dissolve

            call screen mom_name_input
            if mom_char_name.strip() == "":
                $ mom_char_name = "Debbie"
            $ mom = Character("[mom_char_name]", color="#ff6df0")

            $ M_mom.trigger(T_mom_breakfast)
            $ unlock_ui()
            $ callScreen(location_count)

        elif M_mom.get_state() == S_mom_dinner and is_here("mom"):
            scene location_home_kitchen_blur
            show mom 2 at right with dissolve
            show player 203 at left with dissolve
            mom "Hey Sweetie I’m glad you’re here."
            show mom 3
            mom "Diane’s going to be over tonight."
            show mom 2
            show player 11
            mom "I don't know why, but she was very persistent about it."
            mom "Anyway, I need you to pick up some {b}sea trout{/b} at the {b}pier{/b}."
            mom "It’s {b}Diane's{/b} favorite fish, and I want to give her something special with the dinner."
            show mom 1
            show player 2
            player_name "{b}Aunt Diane{/b} is coming over? That’s a surprise!"
            player_name "It’ll be good for her to be here; she doesn’t do much at her home."
            player_name "The family hasn’t been together since the funeral, either."
            player_name "I’ll make sure to get that {b}sea trout{/b}, so the dinner's great for aunt Diane."
            show expression "boxes/popup_pier.png" at truecenter with dissolve
            $ loc_pier_unlocked = True
            $ renpy.pause()
            hide expression "boxes/popup_pier.png"
            scene homekitchen
            show player 1 at left
            show mom 62 at right
            with dissolve
            mom "{b}[firstname]{/b}, before you leave, do you have a minute? I need some help."
            show player 14
            show mom 61
            player_name "Of course, {b}[mom_name]{/b}. What do you need?"
            show player 1
            show mom 62
            mom "I want you to tell me what you think of the outfit I plan on wearing to dinner with {b}Aunt Diane{/b}."
            mom "Give me a moment, I gotta head to {b}my room{/b} so I can put it on."
            hide mom with dissolve
            scene home_livingroom_b
            show player 14
            player_name "{b}[mom_name]{/b} hasn't dressed up for an occasion in a long time..."
            show player 11
            mom "Sweetie!"
            mom "Could you come in here for a second?"
            show player 2
            player_name "I should go check up on her."
            hide player with dissolve
            $ M_mom.trigger(T_mom_dinner_help)
            $ lock_ui()
            jump home_livingroom_dialogue

        elif M_mom.get_state() == S_mom_dinner_fish and seatrout in inventory.items:
            scene location_home_kitchen_blur
            show player 13 at left
            show mom 1 at right
            with dissolve
            player_name "Hey {b}[mom_name]{/b} I have the {b}fish{/b}."
            show player 2
            mom "Good job, Sweetie! Now I can finish dinner"
            show mom 2
            mom "You can join us in the dining room, when it's done. {b}Aunt Diane{/b} would really like to see you."
            show player 203
            $ inventory.items.remove(seatrout)
            $ M_mom.trigger(T_mom_dinner_fish_caught)
            $ gTimer.tick(3)

            scene home_entrance_evening
            show aunt 137 at right
            show mom 91f
            with fade
            dia "I'm so glad to see you!"
            dia "I don't remember the last time I came over for dinner."
            show aunt 136
            show mom 93f
            mom "I know!"
            mom "I was starting to think you hated my cooking."
            show aunt 138
            show mom 91f
            dia "Haha."

            show player 203 at left with dissolve
            show aunt 137
            show mom 92f
            dia "There he is..."
            dia "The man of the house."
            show aunt 136
            show player 14
            player_name "Good evening, {b}Aunt Diane{/b}."
            show player 17
            player_name "You look really nice in that dress!"
            show aunt 138
            show player 203
            dia "Your son really knows how to greet a lady!"
            show player 13
            show aunt 136
            show mom 93f
            mom "Well, he's always been a charmer..."
            show aunt 137
            show mom 91f
            dia "Well thank you, Handsome!"
            dia "Is your {b}sister{/b} joining us tonight?"
            show player 10
            show aunt 136
            player_name "She's getting ready, I think."
            show player 12
            player_name "She's always in her room. She comes down at the last minute to eat..."
            show player 203
            show aunt 138
            dia "Still a princess, I see."
            show aunt 137
            dia "She never changes..."
            show mom 92f
            show aunt 136
            mom "So..."
            show mom 93f
            mom "I think you will be pleased to know that we prepared your favorite dish!"
            show mom 91f
            show aunt 138
            dia "Ohh... I can smell it!"
            show mom 93f
            show aunt 136
            mom "Please, come in and sit at the table!"
            show mom 92f
            mom "Dinner is ready!"
            hide mom
            hide aunt
            with dissolve
            show player 24
            player_name "I should join them in the {b}dining room{/b}."
            player_name "I'm getting hungry..."
            hide player
            with dissolve
            $ lock_ui()
            $ location_count = "Entrance"


    if M_mom.get_state() == S_mom_debt_call:
        scene expression gTimer.image("homekitchen{}")
        show mom 6 at right with dissolve
        mom "I've told you already! I don't {b}KNOW{/b} where the money is..."
        mom "I had no idea my husband was involved with any of this!"
        show mom 7 at right
        mom "But-"
        show mom 6 at right
        mom "We don't have it!!"
        show mom 7 at right
        mom "..."
        show mom 6 at right
        mom "Was that a {b}threat{/b}?!"
        mom "I'm hanging up now. Don't call back here again."
        show mom 8 at right with hpunch
        mom "Just leave us {b}ALONE!!!{/b}"
        show mom 9 at right
        show player 10 at left with dissolve
        player_name "..."
        player_name "...{b}[mom_name]{/b}?"
        player_name "...Are you okay?"
        show player 5 at left
        show mom 11 at right
        mom "I'm alright, Sweetie."
        show mom 10 at right
        show player 10 at left
        player_name "Are you sure? It sounded pretty bad..."
        show player 5 at left
        show mom 11 at right
        mom "It's nothing for you to worry about..."
        show mom 10 at right
        show player 5 at left
        player_name "..."
        show player 10 at left
        player_name "I could try and find another job. Maybe I can come up with some money for you."
        show player 5 at left
        show mom 11 at right
        mom "No."
        mom "This is not your problem Sweetheart."
        mom "You need to focus on school and {b}save your money for college{/b}."
        show mom 10 at right
        show player 10 at left
        player_name "Yeah, but {b}[mom_name]{/b}, I can help..."
        hide player 10 at left
        show mom 12 at right
        with dissolve
        mom "Oh Sweetie..."
        mom "Mommy will handle it. I promise."
        hide mom with dissolve
        $ M_mom.trigger(T_mom_debt_help)
        $ unlock_ui()
        $ callScreen(location_count)

    elif M_mom.get_state() == S_mom_diane_visit and gTimer.is_evening():
        scene homekitchen_secret
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f at Position(xpos=0.3318,ypos=1.000)
        dia "Well, it's good that he's been helping you around the house."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "I know, it's just..."
        mom "He's been so... affectionate towards me lately..."
        show aunt 122 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "Well that's not surprising, he's your only son and he just lost his {b}Father{/b}!"
        show aunt 121
        dia "He probably feels like he needs to protect you..."
        dia "Especially after all that's been happening with you guys."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 17f at Position(xpos=0.3318,ypos=1.1130)
        mom "It's not that... I feel like there's more to it, the way he looks at me you know?"
        show mom 59f at Position(xpos=0.3318,ypos=1.000)
        show aunt 124 at Position(xpos=0.7796,ypos=0.7464)
        dia "..."
        show aunt 121
        dia "What do you mean?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "Well, a little while ago I.. I started noticing things..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "...Like?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "Like how he's always getting hard around me..."
        mom "And... touching me in certain ways..."
        show aunt 124 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "..."
        show mom 60f
        mom "And the other day, I find him, on my bed... playing with himself!"
        mom "With my underwear!"
        show aunt 121
        show mom 59f at Position(xpos=0.3318,ypos=1.000)
        dia "What did you do?!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "I left!"
        mom "And I told him to not do that kind of stuff in my room, but..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "But, what?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f at Position(xpos=0.3318,ypos=1.000)
        mom "He did it again! And then said that he had urges - that he just couldn't control it..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "...So?"
        show aunt 124
        show mom 17f at Position(xpos=0.3318,ypos=1.1130)
        mom "So I let him do it... as I watched."
        show aunt 121
        show mom 20f at Position(xpos=0.3318,ypos=1.1130)
        dia "You watched him masturbate?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f at Position(xpos=0.3318,ypos=1.000)
        mom "I didn't know what to do..."
        mom "I thought maybe it would help him..."
        mom "... Just get it out of his system, you know?"
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "That's sooo naughty..."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 60f
        mom "There's more..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "More?!"
        dia "Really?!"
        dia "What else?!"
        show aunt 124
        show mom 60f
        mom "Diane..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 59f
        dia "{b}[mom]{/b}, tell me!"
        show aunt 124
        show mom 60f
        mom "We've been... taking showers together..."
        show aunt 121
        show mom 59f
        dia "Wow..."
        show aunt 125
        dia "How is he?"
        show aunt 124
        show mom 60f
        mom "Diane!!"
        show aunt 122
        show mom 59f
        dia "What?!"
        show aunt 123
        dia "Oh, come on! You can tell me!"
        show aunt 124
        show mom 60f
        mom "... What do you want to know?"
        show aunt 125
        show mom 59f
        dia "Did you... touch him?"
        show aunt 126
        show mom 60f
        mom "... Yes..."
        mom "I kinda, jerked him off..."
        show aunt 125
        show mom 59f
        dia "All the way?"
        show aunt 126
        show mom 60f
        mom "Well, yeah..."
        show aunt 125
        show mom 59f
        dia "How was he?"
        show aunt 126
        show mom 60f
        mom "What do you mean by that?"
        show aunt 125
        show mom 59f
        dia "Was he... big?"
        show aunt 126
        show mom 60f
        mom "!!!"
        show mom 59f
        mom "..."
        show aunt 127
        dia "Don't get shy on me now, girl..."
        show mom 60f
        show aunt 126
        mom "... {b}Diane{/b}, he's got the biggest... thing I've ever seen!"
        show aunt 125
        show mom 59f
        dia "... You don't say!?"
        show aunt 122
        dia "I can't believe you stopped at jerking him..."
        show aunt 126
        show mom 16f at Position(xpos=0.3318,ypos=1.1130)
        mom "{b}Diane{/b}, he's also my son!"
        show aunt 125
        show mom 15f
        dia "So wait, that means you guys haven't had sex?"
        show aunt 126
        show mom 16f
        mom "No!! Of course not..."
        show aunt 122
        show mom 15f
        dia "You could, you know... He obviously wants to!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "I can't do that!"
        show aunt 124 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "I'm just saying..."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "Please tell me that I'm not doing something terribly wrong here..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "It's your decision, but..."
        dia "I think you should relax and let go! Enjoy the intimacy with your son!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "Really? You don't think this is wrong?"
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "You both seem to be enjoying it... Where's the harm in that?"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "I suppose we aren't hurting anybody and we're both consenting adults..."
        show aunt 122 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "If he's going to learn it from somewhere, might as well do it at home! Haha!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 16f
        mom "You're laughing, but this is serious, {b}Diane{/b}."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 15f
        dia "Just see how it goes. Maybe it's just a phase that he'll grow out of."
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 62f at Position(xpos=0.3318,ypos=1.000)
        mom "You might be right..."
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        show mom 61f
        dia "Anyway, I'd better go home. It's getting late."
        show aunt 125
        dia "We'll continue this another time. I want all the juicy details!"
        show aunt 120 at Position(xpos=0.7746,ypos=0.7464)
        show mom 62f
        mom "Haha. You're becoming my new therapist!"
        mom "You should come by for dinner sometime. We'd love to have you!"
        show mom 61f
        show aunt 121 at Position(xpos=0.7796,ypos=0.7464)
        dia "Sure, we could do that. Just let me know!"
        dia "See you later, honey."
        scene home_entrance_night
        show player 5
        player_name "( That... was a lot to take in. )"
        player_name "( {b}[mom_name]{/b} seemed really conflicted about all of this... )"
        show player 203
        player_name "( She said she's enjoying it, though. )"
        player_name "( Either way, I'm glad {b}Aunt Diane{/b} thinks it's okay for us to be doing these things... )"
        $ M_mom.trigger(T_mom_diane_chat)
        $ gTimer.tick()
        jump home_entrance
    $ callScreen(location_count)

label mom_kissing_practice:
    show player 2 at left
    show mom 14b at right
    player_name "Aww, c'mon [mom_name]!"
    player_name "You're the one who said I need to get out and start dating."
    player_name "It would definitely help if I knew how to kiss a girl properly, wouldn't it?"
    show player 1
    mom "..."
    show mom 13
    mom "... Well."
    mom "Y-yeah, I suppose I could give you a few pointers."
    show mom 14
    show player 2
    player_name "I would really appreciate it, [mom_name]."
    show player 1
    show mom 73 at Position(xpos=0.85, ypos=1.0) with dissolve
    mom "O-okay, umm... Come in close to me."
    show player 227c at Position(xpos=0.25, ypos=1.0) with dissolve
    show mom 72
    player_name "Alright."
    show player 227
    show mom 73
    mom "Good. Now, lean in, that's it."
    show player 227c zorder 1 at Position(xpos=0.30, ypos=1.0) with dissolve
    show mom 72 zorder 0 at Position(xpos=0.80, ypos=1.0) with dissolve
    player_name "Okay."
    show player 227
    show mom 73
    mom "... Close your eyes and gently press your lips against mine..."
    hide player
    show mom 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show mom 80
    pause
    show mom 79
    mom "Mmm."
    show mom 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show player 227c
    player_name "How was that?"
    show player 227
    show mom 77
    mom "... Wow."
    show player 227c
    show mom 76
    player_name "Bad?"
    show player 227
    show mom 73
    mom "N-no. That was quite good!"
    show player 227c
    show mom 72
    player_name "Really?!"
    show player 227
    show mom 73
    mom "Yeah."
    show player 227c
    show mom 72
    player_name "So no pointers?"
    show player 227
    mom "..."
    show mom 73
    mom "Well, let's see..."
    mom "Oh, I know!"
    mom "Kiss me again and I'll show you something."
    hide player
    show mom 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show mom 80
    pause
    show mom 79
    pause
    show mom 80c
    player_name "( !!! )" with hpunch
    show mom 76 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    mom "..."
    show player 227c
    player_name "Whoa!"
    player_name "That thing you did with your tongue, that was so cool!"
    show player 227
    show mom 75
    mom "Hehe, yeah."
    show mom 73
    mom "It's a trick I picked up awhile back. Your father loved it too!"
    show player 227c
    show mom 72
    player_name "Hmm, can I try it?"
    show player 227
    show mom 73
    mom "Oh... uh."
    show player 227c
    show mom 72
    player_name "Please?"
    show player 227c
    show mom 73
    mom "Y-yeah... Sure!"
    hide player
    show mom 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show mom 80
    pause
    show mom 79
    pause
    show mom 80b
    mom "( !!! )" with hpunch
    show mom 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    mom "..."
    show player 227c
    player_name "How was that?!"
    show player 227
    mom "Mmm..."
    show player 227c
    player_name "[mom_name]?"
    show player 227
    show mom 77
    mom "Oh, sorry!"
    show mom 75
    mom "That was REALLY good Sweetie!"
    mom "I mean, wow! Your gonna be quite the little heart breaker once you get out into the dating world!"
    show player 227c
    show mom 76
    player_name "Really? Thanks [mom_name]!"
    show player 227
    mom "Mmmhmm."
    hide player
    show mom 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show mom 80
    pause
    show mom 79
    pause
    show mom 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause 
    show mom 77
    pause
    show mom 74
    mom "Oh!"
    mom "Oh my..."
    show player 230
    player_name "..."
    show player 232
    player_name "Sorry, [mom_name]."
    player_name "I didn't mean to..."
    show player 231
    show mom 75
    mom "Hehe, it's okay Sweetie. It's perfectly understandable."
    show mom 73
    mom "We should probably take a break though..."
    show player 232
    show mom 72
    player_name "... Yeah. O-okay."
    player_name "Do you think, maybe, we could do this again sometime?"
    show player 231
    mom "..."
    show player 232
    player_name "You know... Just, if I need to practice?"
    show player 231
    show mom 73
    mom "I suppose that would be okay."
    mom "Just to practice though?!"
    show player 232
    show mom 72
    player_name "Yeah! Just to practice."
    show player 231
    show mom 73
    mom "Alright. Feel free to ask me anytime."
    show player 232
    show mom 72
    player_name "Thanks [mom_name]!"
    show player 231
    show mom 73
    mom "No problem. I love you, Sweetie!"
    show player 232
    show mom 72
    player_name "Love you too!"
    hide mom with dissolve
    show player 1 at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "..."
    show player 21f at Position (xpos=0.5, ypos=1.0) with dissolve
    player_name "That was awesome!"
    $ M_mom.trigger(T_mom_kiss)
    $ gTimer.tick()
    $ callScreen(location_count)

label dishes_dialogue:
    scene location_home_kitchen_closeup
    show mom 116 at right
    with dissolve
    pause
    show mom 117 at Position(xpos=1014)
    pause
    show mom 116 at right
    pause
    show mom 117 at Position(xpos=1014)
    pause
    show mom 116 at right
    show player 1 at left with dissolve
    pause
    show mom 117 at Position(xpos=1014)
    pause
    show mom 119 at Position(xpos=1014)
    mom "Oh, hey Sweetie!"
    show mom 120
    show player 14
    player_name "Hey, {b}[mom_name]{/b}!"
    show mom 119
    show player 1
    mom "If you need something, it'll have to wait."
    mom "I need to finish drying these dishes."
    show mom 120
    menu:
        "Let me help.":
            show mom 118
            show player 14
            player_name "Take a break, {b}[mom_name]{/b}."
            player_name "I'll take it from here."
            show mom 119
            show player 1
            mom "Sweetie, you know you don't have to."
            show mom 118
            show player 14
            player_name "No, it's fine. I'm kind of bored anyway."
            show mom 119
            show player 1
            mom "Well... Okay."
            show player 272
            show mom 62
            mom "Put the dishes away in the cupboard after you're finished."
            show player 273
            show mom 61
            player_name "Will do."
            show mom 63
            show player 272
            mom "Thanks for helping out, Sweetie!"
            show player 274
            show mom 61
            player_name "No problem, {b}[mom_name]{/b}!"
            scene help_mom_kitchen_cutscene with fade
            show text "{b}Dad{/b} was usually the one helping {b}[mom_name]{/b} with dishes... \nBut, I didn't mind being the one to help her now. \nShe stayed with me in the kitchen and we talked the whole time... \nIt was nice seeing {b}[mom_name]{/b} happy for once." at Position (xpos= 512, ypos = 700) with dissolve
            pause
            hide text with dissolve
            $ gTimer.tick()
            $ M_mom.trigger(T_mom_washed_dishes)
        "Nevermind.":

            show player 14 at left
            show mom 120 at Position(xpos=1014)
            player_name "Okay. I'll come back later, then."
    $ M_mom.set("chores", False)
    $ callScreen(location_count)

label sis_breakfast_force:
    scene homekitchen with None
    show player 11 at left
    show mom 2 at right
    with dissolve
    mom "Where are you going? Your breakfast is ready in the {b}dining room{/b}, Sweetie..."
    show player 14
    show mom 1
    player_name "Sorry, {b}[mom_name]{/b}! I'll go eat now."
    hide player
    hide mom
    with dissolve
    $ callScreen(location_count)

label sis_breakfast_force_mom:
    scene homekitchen with None
    show player 11 at left
    show mom 2 at right
    with dissolve
    mom "Your breakfast is ready in the {b}dining room{/b}, Sweetie..."
    show player 14
    show mom 1
    player_name "Thanks, {b}[mom_name]{/b}! I'll go eat now."
    hide player
    hide mom
    with dissolve
    $ callScreen(location_count)