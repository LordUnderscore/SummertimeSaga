label mrsj_button_dialogue:
    if location_count == "Erik's House Entrance":
        scene expression gTimer.image("erik_entrance{}_c")
    elif location_count == "Mrs Johnson's Room":
        if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
            scene erik_upstairs_night_c
            show erikmom 42 at right
            show player 11 zorder 2 at left
            show erik 1f zorder 1 at Position(xpos=300)
            with dissolve
            erimom "Hey, boys..."
            show erikmom 41
            show player 21
            player_name "H-hi, {b}Mrs. Johnson{/b}!"
            show player 13
            show erik 4f
            eri "You're... very pretty, Mom."
            show erik 1f
            show erikmom 40b with fastdissolve
            erimom "Well, are you just gonna keep staring at me or do you want to ask me something?"
            show erikmom 39
            jump mrsj_button_dialogue_repeat

        elif gTimer.is_dark() and erik.over(erik_gf):
            scene erik_upstairs_night_c2
            show erikmom 54 at Position(xpos=734,ypos=650)
            show player 433 zorder 2 at left
            with dissolve
            erimom "Hello, {b}[firstname]{/b}..."
            show erikmom 53
            player_name "!!!"
            show erikmom 54
            erimom "Is there something wrong?"
            show player 435
            show erikmom 53
            player_name "You.. you're naked, {b}Mrs. Johnson{/b}."
            show player 434
            show erikmom 54
            erimom "I like to feel... comfortable in my room..."
            erimom "Weren't you about to ask me something?"
            show erikmom 53
            jump mrsj_button_dialogue_repeat
        scene erik_house_upstairs_n_c01
    show player 14 at left
    show erikmom 14 at right
    with dissolve
    player_name "Hi, {b}Mrs. Johnson{/b}!"
    show player 1
    show erikmom 17
    erimom "Hey, {b}[firstname]{/b}!"
    erimom "How are you?"
    show player 14
    show erikmom 14
    player_name "I'm good, thanks!"
    show player 1
    show erikmom 17
    erimom "Is there anything I can do for ya?"
    show erikmom 14
    menu mrsj_button_dialogue_repeat:
        "About {b}Erik{/b}." if erik.started(erik_path_split):
            show player 14 at left
            show erikmom 14 at right
            player_name "I wanted to talk about {b}Erik{/b}..."
            show player 1
            show erikmom 19
            erimom "Oh, Is he okay?"
            show player 14
            show erikmom 19c
            player_name "Yeah, he's fine."
            player_name "I was talking to him about what happened the other night..."
            show player 11
            show erikmom 19
            erimom "Is he upset?"
            show player 14
            show erikmom 19c
            player_name "No, not at all."
            show player 10
            player_name "He's just not sure about what he wants..."
            show player 11
            show erikmom 19
            erimom "How so?"
            show player 10
            show erikmom 19c
            player_name "I think he's given up on meeting girls."
            player_name "I could try and help him get a girlfriend, but I think he likes you more..."
            show player 13
            show erikmom 19
            erimom "Oh, my..."
            show erikmom 20
            erimom "Have I really sheltered him too much?"
            show erikmom 19
            erimom "What do you think I should do?"
            show erikmom 19c
            $ config.skipping = None
            show popup_warning at truecenter with dissolve
            $ renpy.pause(3, hard=True)
            pause
            hide popup_warning with dissolve
            menu mrsj_route_split:
                "Sex education.":
                    hide screen save
                    show player 14 at left
                    show erikmom 19c at right
                    player_name "I think it's best if you give him the attention he needs..."
                    show erikmom 19
                    show player 1
                    erimom "You really think so?"
                    show erikmom 19c
                    show player 14
                    player_name "Well, I don't think he wants to see any other girls..."
                    player_name "... And he really likes you!"
                    show erikmom 19
                    show player 1
                    erimom "He's always been close to me..."
                    show erikmom 19c
                    show player 14
                    player_name "We had such a great time the other night!"
                    player_name "I've never seen {b}Erik{/b} this happy."
                    show erikmom 19
                    show player 11
                    erimom "Do you think...you boys would like more of that kind of...attention?"
                    show erikmom 19c
                    show player 21
                    player_name "I...I think so!"
                    show erikmom 20
                    show player 13
                    erimom "If none of the girls from school will give him the attention he needs..."
                    show erikmom 19
                    erimom "...Maybe I should be the one?"
                    show erikmom 14
                    show player 14
                    player_name "I think he would like that."
                    show erikmom 49
                    show player 11
                    erimom "What If I gave you guys some...personal sex education?"
                    show erikmom 50
                    player_name "!!!" with vpunch
                    show erikmom 49
                    erimom "It's only for educational purposes of course..."
                    show erikmom 50
                    show player 29 at Position(xoffset=8)
                    player_name "Oh, I emm... I wouldn't mind at all!"
                    show erikmom 49
                    show player 13
                    erimom "I'd have to think it over first, though."
                    show erikmom 50
                    show player 14
                    player_name "Sure, {b}Mrs. Johnson{/b}!"
                    show erikmom 14
                    show player 1
                    $ erik_path_split.finish()
                    $ erik.add_event(erik_sex_ed)
                    jump mrsj_button_dialogue_repeat
                "Get him a girlfriend.":

                    hide screen save
                    show player 14 at left
                    show erikmom 19c
                    player_name "I think we should try and find him a girlfriend."
                    show player 1
                    show erikmom 19
                    erimom "You really think so?"
                    show player 14
                    show erikmom 19c
                    player_name "Well, I think he would be happier..."
                    player_name "... and it'd build up his confidence!"
                    show player 1
                    show erikmom 20
                    erimom "He does need to go out more..."
                    show player 10
                    show erikmom 19c
                    player_name "Don't get me wrong, we had a lot of fun the other night..."
                    show player 14
                    player_name "... but I think {b}Erik{/b} needs to meet other girls."
                    show player 13
                    show erikmom 20
                    erimom "You're right..."
                    show player 11
                    show erikmom 19
                    erimom "But what about... me?"
                    show player 10
                    show erikmom 19c
                    player_name "What do you mean?"
                    show player 11
                    show erikmom 19
                    erimom "Well..."
                    erimom "If {b}Erik{/b} finds a girlfriend... What will I do?"
                    show erikmom 20
                    erimom "I won't have anyone to give my attention to..."
                    show player 21
                    show erikmom 19c
                    player_name "Oh, I'm sure you will find someone {b}Mrs. Johnson{/b}!"
                    show erikmom 14
                    player_name "You're very... attractive, and loving!"
                    show player 13
                    show erikmom 17
                    erimom "Aww, that's very sweet of you to say."
                    show erikmom 50
                    erimom "Hmm..."
                    show erikmom 49
                    show player 1
                    erimom "I have a different idea!"
                    erimom "What If I took that attention..."
                    show player 11
                    erimom "... and gave it to {b}you{/b}?"
                    show erikmom 50
                    player_name "!!!" with vpunch
                    show erikmom 49
                    erimom "What's wrong?"
                    erimom "Only if you wanted to, is what I meant to say..."
                    show player 21
                    show erikmom 50
                    player_name "I-I wouldn't mind at all!"
                    player_name "But, only as long as {b}Erik{/b} is okay with it."
                    show player 1
                    show erikmom 49
                    erimom "Just ask him!"
                    erimom "I'm sure he would be okay with that..."
                    show player 13
                    erimom "... especially if he's too busy playing with another girl! Ha ha."
                    show player 29 at Position(xoffset=8)
                    show erikmom 50
                    player_name "I suppose so, ha ha."
                    show player 14
                    player_name "I'll try and find someone for him..."
                    show player 13
                    show erikmom 49
                    erimom "Come back and let me know what happens."
                    show player 17
                    show erikmom 50
                    player_name "Sure, {b}Mrs. Johnson{/b}!"
                    show erikmom 14
                    show player 1
                    $ erik_path_split.finish()
                    $ June.add_event(june_intro)
                    jump mrsj_button_dialogue_repeat
                "Save Menu.":

                    show screen save
                    pause
                    hide screen save
                    jump mrsj_route_split

        "Sex education." if mrsj.started(mrsj_sex_ed):
            show erikmom 14 at right
            show player 10 at left
            player_name "How can we help you get ready for our sex education again?"
            show player 5
            show erikmom 17
            erimom "I'll need a good instructional book, like {b}Kama Sutra{/b}."
            erimom "And some {b}birth control pills{/b}!"
            show erikmom 49
            erimom "You can never be too careful..."
            show erikmom 50
            show player 14
            player_name "Alright."
            player_name "I'll try and find them..."
            hide player
            hide erikmom
            with dissolve

        "Sex education." if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
            jump mrsj_3some

        "Private Yoga." if gTimer.is_dark() and erik.over(erik_gf):
            jump mrsj_private_yoga

        "Girlfriend." if erik.started(erik_gf):
            show player 14
            player_name "I think I was able to introduce {b}Erik{/b} to a girl at school!"
            show player 1
            show erikmom 17
            erimom "Really?!"
            show player 14
            show erikmom 14
            player_name "Yeah!"
            player_name "They have so much in common, they would be perfect for each other!"
            show erikmom 17
            show player 17
            player_name "I think it's going to work out for sure!"
            show player 1
            show erikmom 18
            erimom "That's wonderful!!"
            show erikmom 17
            erimom "I can't believe you've been so good to my son."
            show erikmom 49
            erimom "I think it's time for me to give you a little reward..."
            show player 21
            show erikmom 50
            player_name "A... A reward?"
            show player 11
            show erikmom 49
            erimom "How about I give you some... {b}private{/b} yoga lessons..."
            erimom "The kind you don't get to see in the gym."
            show erikmom 50
            show player 21
            player_name "That would be awesome, {b}Mrs. Johnson{/b}!"
            show player 13
            show erikmom 49
            erimom "Just come visit me at night in my room... make sure you're well rested!"
            show player 11
            erimom "It can be... quite exhausting."
            show player 21
            show erikmom 50
            player_name "Y-yes, {b}Mrs. Johnson{/b}."
            show player 13
            show erikmom 49
            erimom "See you later, I'll be waiting!"
            hide player
            hide erikmom
            with dissolve
            $ erik_gf.finish()
            jump erik_house_dialogue

        "Girlfriend." if erik.in_progress(erik_gf_stolen):
            show erikmom 19c at right
            show player 10 at left
            player_name "I don't think it's going to work out with June..."
            show player 11
            show erikmom 19
            erimom "The girl from school?"
            show player 10
            show erikmom 19c
            player_name "Yeah."
            show player 5
            show erikmom 19
            erimom "That's such a shame..."
            erimom "What happened?"
            show player 10
            show erikmom 19c
            player_name "She's just not interested, and..."
            show erikmom 51
            player_name "... she might be coming over to my house later to hang with me."
            show player 5
            show erikmom 52
            erimom "Oh my..."
            erimom "Is Erik okay with this?"
            show player 10
            show erikmom 51
            player_name "I'm not sure... probably not?"
            show player 5
            show erikmom 52
            erimom "I have to say... I'm a little disappointed in you, {b}[firstname]{/b}."
            show erikmom 51
            player_name "..."
            show erikmom 52
            erimom "You knew {b}Erik{/b} liked her..."
            erimom "... I thought he was your friend!"
            show player 10
            show erikmom 51
            player_name "I'm sorry, {b}Mrs. Johnson{/b}."
            player_name "I'll head home now."
            hide erikmom
            hide player
            jump erik_house_dialogue

        "Girlfriend." if June.started(june_intro_2):
            show player 14
            player_name "There's this girl at school that I think {b}Erik{/b} likes."
            show player 1
            show erikmom 17
            erimom "Really?"
            show erikmom 18
            erimom "That's wonderful!"
            show erikmom 17
            erimom "Do you know her? What is she like?!"
            show erikmom 14
            show player 14
            player_name "No, I haven't spoken to her yet."
            player_name "She's from a different class, I think."
            show erikmom 17
            show player 1
            erimom "Oh, I see."
            show player 11
            erimom "Is {b}Erik{/b} speaking to her?"
            show erikmom 14
            show player 10
            player_name "I don't think so... He says he's too shy."
            player_name "I told him I would find out more about her and let him know what she's like."
            show erikmom 18
            show player 13
            erimom "That's so nice of you!!"
            show erikmom 17
            erimom "He's very lucky to have you as a friend..."
            show erikmom 14
            show player 14
            player_name "Oh, I'm sure he would do the same for me!"
            show erikmom 49
            show player 1
            erimom "Tell you what, let me know how all of this goes..."
            show player 11
            erimom "If you can find {b}Erik{/b} a girlfriend, there's a special reward waiting for you..."
            show erikmom 50
            player_name "..."
            show player 21
            player_name "Sure, {b}Mrs. Johnson{/b}!"
            show player 1
            show erikmom 14
            $ june_intro_2.finish()
            jump mrsj_button_dialogue_repeat

        "Breastfeeding." if erik.over(erik_breastfeeding_2) and (not erik.known(erik_sex_ed) and not mrsj.known(mrsj_sex_ed) and not June.known(june_intro)):
            show erikmom 38 at right
            show player 12 at left
            player_name "So how long have you...been breastfeeding {b}Erik{/b}?"
            show player 5
            show erikmom 52
            erimom "Oh..."
            erimom "Listen, it's not what you might think."
            erimom "I just always nurtured him like this."
            show erikmom 38
            show player 11
            erimom "..."
            show erikmom 52
            erimom "You know he doesnt get much attention from the girls at school."
            erimom "I felt so bad for him!"
            erimom "I just wanted my baby boy to experience and see what women are all about!"
            show erikmom 20
            erimom "But maybe I...I over did it?"
            show erikmom 19c
            show player 5
            player_name "..."
            show player 12
            player_name "It's great that you care so much and give him attention!"
            show erikmom 14
            show player 10
            player_name "I think he's very lucky..."
            show player 11
            show erikmom 18
            erimom "Oh, ha ha!"
            show erikmom 17
            erimom "Well, thank you..."
            erimom "I think nice young men like yourselves need all the attention you can..."
            show erikmom 14
            show player 13
            player_name "..."
            show erikmom 49
            erimom "I mean, thanks for understanding, [firstname]."
            show erikmom 52
            erimom "Just...remember to keep this between us, okay?"
            show erikmom 14
            show player 14
            player_name "Yes, {b}Mrs. Johnson{/b}."
            hide player
            hide erikmom
            with dissolve

        "Where's Erik?" if not gTimer.is_dark():
            show player 14
            if gTimer.is_morning() and not gTimer.is_weekend():
                player_name "Do you know where I could find {b}Erik{/b}?"
                show player 1
                show erikmom 17
                erimom "Well, he should be at {b}school{/b} right now."
            else:

                show erikmom 14
                player_name "Do you know where I could find {b}Erik{/b}?"
                show player 1
                show erikmom 17
                erimom "Well, I think I saw him go into the {b}basement{/b}."
                erimom "You should see if he's there!"
                show erikmom 14
                show player 17
                player_name "Thanks, {b}Mrs. Johnson{/b}!"
            show erikmom 14
            jump mrsj_button_dialogue_repeat

        "You're so fit!" if not gTimer.is_dark():
            show erikmom 14 at right
            show player 29 at left
            player_name "I have to say, {b}Mrs. Johnson{/b}, you are really fit!"
            player_name "Do you excercise a lot?"
            show erikmom 18 at right
            show player 13 at left
            erimom "Aw... You're so nice!"
            show erikmom 17 at right
            erimom "Well, I try to use the Gym as often as I can..."
            erimom "...I also go jogging! And I do yoga in my room at night as well..."
            show erikmom 19 at right
            show player 21 at left
            player_name "Well, it's working!"
            show player 13 at left
            erimom "You think?"
            show erikmom 15 at right
            show player 11 at left
            erimom "My {b}butt{/b} is still a bit big..."
            show erikmom 16 at right
            show player 23 at left
            erimom "...And my {b}boobs{/b} are not like the used to..."
            player_name "..."
            show player 28 at left
            show erikmom 19 at right
            player_name "*gulp*"
            show player 1 at left
            show erikmom 18 at right
            erimom "Is there anything else you wanted to talk about?"
            jump mrsj_button_dialogue_repeat

        "Invite to poker." if mrsj.known(mrsj_poker_night) and not gTimer.is_night():
            show player 14 at left
            show erikmom 14 at right
            if gTimer.is_morning() and not gTimer.is_weekend():
                player_name "I was wondering if you could teach us how to play poker?"
                show player 11
                show erikmom 19
                erimom "Shouldn't you be at school right now??"
                erimom "Erik already left!"
                show player 29 at Position(xoffset=8)
                show erikmom 14
                player_name "Oh, crap! You're right..."
                player_name "Maybe later then!"

            elif pStats.chr() >= 5 and poker_bot02 == "" and not gTimer.is_morning():
                if mrsj.completed(mrsj_poker_night_2):
                    show player 14 at left
                    show erikmom 14 at right
                    player_name "Would you like to play some poker with us again?"
                    show player 1
                    show erikmom 17
                    erimom "Still looking for friends to play with?."
                    show player 14
                    show erikmom 14
                    player_name "Well, It's just that-"
                    show player 1
                    show erikmom 18
                    erimom "It's fine!!"
                    show player 1
                    show erikmom 17
                    erimom "I'll play with you boys..."
                    show player 14
                    show erikmom 14
                    player_name "Really?"
                    show player 1
                    show erikmom 20
                    erimom "Well... last time was a bit much..."
                    show player 13
                    show erikmom 18
                    erimom "But, why not?"
                    show player 14
                    show erikmom 14
                    player_name "Okay."
                    show erikmom 17
                    erimom "When are we playing?"
                    show player 14
                    show erikmom 14
                    player_name "After dinner tonight."
                    player_name "{b}Erik{/b} and I will set up the game."
                    show player 1
                    show erikmom 18
                    erimom "Haha, alright."
                    show erikmom 17
                    erimom "See you then!"
                else:

                    player_name "I was wondering if you'd like to join me and Erik for poker?"
                    show player 1
                    show erikmom 17
                    erimom "Right now?"
                    show player 14
                    show erikmom 14
                    player_name "Yeah... I mean, you don't have to!"
                    player_name "{b}Erik{/b} and I are just looking for a third player..."
                    show player 1
                    show erikmom 17
                    erimom "He's waiting downstairs?"
                    show player 14
                    show erikmom 14
                    player_name "Yeah, we'd like to play now, if you're free?"
                    show player 1
                    erimom "Hmm..."
                    show erikmom 17
                    erimom "I guess I could play a game or two."
                    show erikmom 18
                    show player 13
                    erimom "Alright, I'll meet you two downstairs in a bit!"
                    show player 18
                    show erikmom 14
                    player_name "Awesome! Thanks, {b}Mrs. Johnson{/b}!"
                $ poker_bot02 = "erik_mom"
                $ poker_sayer02 = erimom
            else:

                if pStats.chr() < 5 and not gTimer.is_morning():
                    $ stat_warn = chr_warn
                else:
                    $ stat_warn = ""
                player_name "[stat_warn]I was wondering if you could teach us to play poker?"
                show erikmom 17
                show player 1
                erimom "[stat_warn]The card game?"
                show erikmom 14
                show player 14
                player_name "[stat_warn]Yeah, Erik and I are just looking for a third player."
                show erikmom 17
                show player 14
                erimom "[stat_warn]Oh, I'd love to."
                show player 19
                erimom "[stat_warn]But I really just don't have the time right now, sorry..."
                show erikmom 14
                show player 14
                player_name "[stat_warn]That's alright, maybe some other time."
            hide player
            hide erikmom
            with dissolve
        "I have to go!":

            show erikmom 14 at right
            show player 14 at left
            player_name "I should go find {b}Erik{/b}!"
            show erikmom 18 at right
            show player 1 at left
            erimom "Alright, then!"
            show erikmom 14 at right
            show player 17 at left
            player_name "Bye, {b}Mrs. Johnson{/b}!"
            hide player
            hide erikmom
            with dissolve
    $ callScreen(location_count)