default attic_key_taken = False

label home_entrance:
    $ location_count = "Entrance"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.started(erik_bullying):
        scene home_entrance
        show erikmom 19c at right with dissolve
        show player 10 at left with dissolve
        player_name "Is everything ok, {b}Mrs. Johnson{/b}?"
        show player 5
        show erikmom 19
        erimom "Sorry to disturb you this morning."
        show erikmom 52
        erimom "It's just... it's about {b}Erik{/b}."
        erimom "Has {b}Erik{/b} been having trouble lately at school?"
        show erikmom 19c
        show player 12
        player_name "Huh?"
        show player 35
        player_name "Not that I know of?"
        show player 10
        player_name "He usually does well at school..."
        show player 5
        show erikmom 20
        erimom "No. I'm not talking about grades."
        show erikmom 52
        erimom "Have the other kids in school been giving {b}Erik{/b} a hard time?"
        erimom "He's been asking to stay home instead of going to class."
        show erikmom 20
        erimom "I... I even saw him come home last week with bruises."
        show erikmom 19c
        show player 23
        player_name "!!!" with hpunch
        show player 12
        player_name "{b}Erik{/b} is pretty quiet at school."
        player_name "I've never seen him get involved in any kind of bad stuff."
        show player 5
        show erikmom 19
        erimom "Maybe, if a close friend stopped over to him see him, he'd be more willing to talk..."
        show erikmom 19c
        show player 10
        player_name "You want me to ask him?"
        show player 5
        show erikmom 19
        erimom "I just want what's best for him, and you're his only friend."
        show erikmom 19c
        show player 12
        player_name "Okay. I'll go see him."
        hide erikmom
        hide player
        with dissolve
        $ erik_bullying.finish()
        $ unlock_ui()

    elif M_mia.get_state() == S_mia_angelicas_impatience:
        scene home_entrance
        show mom 1f at Position (xpos=500)
        show ang 1 at right
        with dissolve
        pause.5
        show player 5 at left
        show mom 3
        with dissolve
        mom "There he is!"
        show mom 1
        show player 22
        player_name "!!!" with hpunch
        show mom 2
        mom "I'm so happy to hear my son visited our local church lately..."
        mom "...And offered volunteer work with the clergy!"
        show mom 1
        show player 24
        player_name "Uhh..."
        show mom 2
        mom "Well! I will leave you two to it, I have things cooking in the kitchen!"
        show mom 2f with dissolve
        mom "It was great meeting you {b}Sister Angelica{/b}!"
        hide mom with dissolve
        show player 12
        player_name "Volunteer work?"
        player_name "And why are you here?!"
        show player 11
        show ang 2
        ang "I thought we had an agreement?"
        show ang 1
        show player 24
        player_name "..."
        show ang 2
        ang "Did you think I would just let you slip away from me?!"
        show ang 1
        show player 10
        player_name "No, I just... What do you want from me?"
        show player 11
        show ang 2
        ang "The door of the church will be left unlocked at night."
        ang "Come visit me in my chamber and I will explain what I need from you..."
        ang "...And don't try to hide from me again, or else-"
        show ang 1
        show player 12
        player_name "Okay, okay!"
        player_name "Just don't say anything to my mom..."
        show player 11
        show ang 2
        ang "That will be up to you..."
        hide ang with dissolve
        show player 12
        player_name "Now I have to go see her at church? In the middle of the night?!"
        show player 10
        player_name "This is strange..."
        hide player with dissolve
        $ M_mia.trigger(T_angelica_house_visit)
        $ unlock_ui()

    elif M_mia.get_state() == S_mia_angelicas_home_visit:
        scene home_entrance with fade
        show mom 2f at Position (xpos=500)
        show ang 1 at right
        with dissolve
        pause.5
        show player 5 at left
        show mom 3f
        with dissolve
        mom "It's always a pleasure to hear that my son is actively involved with the church."
        mom "You two must be getting to know each other quite well."
        show mom 1f
        show ang 2
        ang "Yes, {b}[firstname]{/b} has been very helpful bringing in remorsefully wretched sinners."
        ang "{b}God{/b} will surely remember his fruits of love to his neighbors."
        show ang 1
        show mom 3f
        mom "That's great!"
        mom "I know we all can be naughty at times..."
        show mom 2f
        mom "Well then I better get going. The laundry isn't going to fold itself."
        hide mom with dissolve
        show ang 3
        player_name "..."
        show player 30
        player_name "What now?"
        player_name "I brought you {b}Helen{/b}. Isn't that enough?"
        show player 5
        show ang 4
        ang "Oh no my dear child. {b}God{/b} has many things in store for you."
        ang "{b}Helen{/b} is far from being purified. Her stubbornness is most annoying."
        show ang 3
        show player 26
        player_name "Tell me about it."
        show player 5
        show ang 2
        ang "The most penitent christians require extra care."
        ang "They need to be broken down from their pedestal so that we may build them back up."
        ang "I believe it will take two more rituals for her..."
        ang "That is why I have come to see you."
        ang "I am in need of an essential tool used throughout bibical times."
        show ang 1
        show player 11
        player_name "..."
        show player 12
        player_name "What do you need?"
        show player 5
        show ang 2
        ang "I intend to subvert {b}Helen{/b} through the means of flagellation."
        show ang 1
        show player 12
        player_name "What?"
        show player 5
        show ang 4
        ang "Get me {b}a whip{/b}."
        show ang 3
        show player 23
        player_name "{b}A whip{/b}!?"
        show player 11
        show ang 4
        ang "I'd prefer a cat o' nine tails of which our {b}Savior{/b} was subjected to."
        ang "But I fear that might be more difficult to come by."
        ang "{b}A standard leather whip{/b} will do."
        show ang 2
        ang "Bring it to me in my chambers."
        show ang 1
        show player 10
        player_name "This doesn't seem right at-"
        show player 11
        show ang 2
        ang "Do you forget your place? Don't make me remind you and everyone else of your depraved sins!"
        show ang 1
        show player 15
        player_name "But you want to whip {b}Helen{/b}!"
        show player 16
        show ang 2
        ang "You made a deal with me. Don't question my...the church's methods."
        show ang 1
        show player 12
        player_name "It's just not right."
        show player 5
        show ang 4
        ang "And who are you to judge right from wrong?"
        show ang 3
        show player 24
        player_name "..."
        show player 12
        player_name "Fine. Where am I even supposed to get {b}a whip{/b} though?"
        show player 17
        player_name "Is there a listing of distributors in the back of the bible?"
        show player 5
        show ang 1
        ang "..."
        show ang 2
        ang "I'm sure someone of your age knows of dirty lustful places that sell such things."
        ang "Don't keep me waiting."
        hide ang with dissolve
        show player 37 with dissolve
        player_name "I should never have gone to church."
        pause
        show player 38 with dissolve
        player_name "Where am I going to get {b}a whip{/b}?"
        player_name "Maybe the {b}Pink store at the mall{/b} carries something like that."
        show player 37 with dissolve
        player_name "..."
        hide player with dissolve
        $ M_mia.trigger(T_angelica_requires_whip)
        $ unlock_ui()

    elif M_mia.get_state() == S_mia_angelicas_final_home_visit:
        scene home_entrance with fade
        show player 11 at left
        show ang 2 at right
        with dissolve
        ang "It's about time you came downstairs."
        ang "I have need of you again."
        show ang 1
        show player 5
        player_name "..."
        show player 12
        player_name "I'm not sure I want to continue helping after what you did to {b}Helen{/b}, I-"
        show player 5
        show ang 4
        ang "Oh, don't be so naive!"
        ang "Despite her reluctance, we both know she enjoyed it."
        show ang 3
        show player 11
        player_name "..."
        show ang 2
        ang "I didn't come here to argue with a sinner."
        show ang 39 with dissolve
        ang "If you truly intend to help {b}Helen{/b} you will help me obtain this..."
        show ang 38
        pause
        show ang 3
        show player 459 at Position (xoffset=1)
        with dissolve
        player_name "..."
        hide player
        hide ang
        show note_01_c
        with dissolve
        pause
        hide note_01_c
        show player 1 at left
        show ang 3 at right
        show player 460 at Position (xoffset=1)
        with dissolve
        player_name "What...is it?"
        show player 461 at Position (xoffset=1)
        show ang 4
        ang "It is a crucial element to the final ritual of {b}Helen's{/b} purification..."
        ang "...And your last task."
        show ang 3
        show player 460 at Position (xoffset=1)
        player_name "But how is this going to be used to purify {b}Helen{/b}?"
        show player 11 with dissolve
        show ang 2
        ang "Don't question me!"
        ang "Sinners should just accept the words spoken by {b}God's{/b} chosen."
        ang "Now get me the item in the photograph and meet me in my chambers."
        show ang 1
        show player 5
        player_name "..."
        show player 12
        player_name "Alright..."
        show player 5
        show ang 2
        ang "Good. And be quick about it."
        hide ang with dissolve
        show player 5
        player_name "..."
        show player 10
        player_name "{b}Helen{/b} doesn't even seem to realize {b}Sister Angelica{/b} is transforming her into..."
        player_name "...A sex freak!"
        show player 12
        player_name "I should talk with {b}Harold{/b} before I help out {b}Sister Angelica{/b}."
        player_name "Maybe he can help me figure out what to do."
        show unlock55 at truecenter with dissolve
        $ inventory.items.append(strapon_drawing)
        pause
        hide unlock55 with dissolve
        hide player with dissolve
        $ M_mia.trigger(T_angelica_strapon_request)
        $ unlock_ui()

    elif M_mom.get_state() == S_mom_overheard:
        if not gTimer.is_dark():
            scene home_entrance
        else:
            scene home_entrance_night
        show player 34 with dissolve
        player_name "...{b}*distant voice*{/b}..."
        show player 35
        player_name "( Is that {b}[mom_name]{/b} on the phone? )"
        show player 12
        player_name "( ...She sounds like she's mad. Is she yelling? )"
        show player 10
        player_name "( I should go see if she's okay. )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_check)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_lawn_help and not gTimer.is_dark():
        scene home_entrance
        show player 1 at left
        show mom 2 at right
        with dissolve
        if gTimer.is_morning():
            mom "Good morning, Sweetie."
        else:
            mom "Hello, Sweetie."
        show mom 1
        show player 2
        if gTimer.is_morning():
            player_name "Morning, {b}[mom_name]{/b}."
        else:
            player_name "Hello, {b}[mom_name]{/b}."
        show player 1
        show mom 2
        if gTimer.is_morning():
            mom "Ready for yet another day at school?"
        else:
            mom "Happy to be back at school?"
        show mom 1
        show player 10
        player_name "I guess so... I have a lot of homework to catch up on."
        show player 1
        show mom 3
        mom "Oh, I'm sure you'll do fine."
        show mom 2
        mom "It's good to get back into a normal routine."
        show mom 1
        show player 14
        player_name "I guess."
        player_name "What are you doing today?"
        show player 13
        show mom 13
        mom "Oh, me?"
        mom "Well...there's plenty of housework to keep me busy."
        mom "Especially, now that your dad isn't here to help me."
        show mom 14b
        show player 5
        pause
        show player 2
        player_name "I could help you, {b}[mom_name]{/b}."
        show player 1
        show mom 13
        mom "Around the house?"
        show mom 1
        show player 29 with dissolve
        player_name "Sure! I don't mind."
        show player 1 with dissolve
        show mom 2
        mom "That's really sweet!"
        show mom 1
        mom "Hmm..."
        show mom 2
        mom "Well, the lawn hasn't been mowed in weeks."
        mom "You can start there if you want!"
        mom "The {b}lawn mower{/b} should be in the {b}garage{/b}."
        show mom 1
        show player 14
        player_name "All right. I'll get on it."
        show player 13
        show mom 2
        mom "Thanks. I better get back to cleaning."
        mom "Have a good day, Sweetie!"
        hide mom
        hide player
        with dissolve
        $ M_mom.trigger(T_mom_help_mow)

    elif M_mom.get_state() == S_mom_clothes_dirty:
        scene home_entrance
        show player 11 zorder 1 at left
        show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
        show sis 9 at right
        with dissolve
        sis "Eugh, what's that smell?!"
        show player 14
        show sis 10
        player_name "I was just outside mowing the lawn and-"
        show player 11
        show sis 9
        sis "That's disgusting! You're getting grass everywhere, you slob!"
        show player 12
        show sis 10
        player_name "I'm sorry. I was just trying to help {b}[mom_name]{/b}."
        show player 11
        show sis 9
        sis "What's with you and doing things around the house all of a sudden?"
        sis "Are you trying to be {b}[mom_name]'s{/b} \"special boy\" or something?"
        show player 10
        show sis 10
        player_name "No! I'm just-"
        show player 11
        show sis 9
        sis "Don't act stupid! I know what you're doing!"
        hide sis with dissolve
        pause
        show player 12
        player_name "What's with her lately? She's so tense all the time..."
        show player 10
        player_name "Anyway... I should head down to the {b}basement{/b} to get all of this off me..."
        hide player with dissolve
        $ M_mom.trigger(T_mom_sis_bitch)

    elif M_mom.get_state() == S_mom_debt_collectors:
        scene henchman_cs1 2 with fade
        $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
        show text "I was expecting to see {b}Erik{/b}, instead I saw a strange man...\nHe was wearing an all black suit coupled with a stern look that would put coach Bridget's to shame." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text
        scene henchman_cs1 1
        show player 2 at left
        show henchman2 1 at right
        with dissolve
        player_name "Hi?"
        show henchman2 2
        show player 1
        henchman2 "Where's your {b}mother{/b}?"
        show henchman2 1
        show player 11
        player_name "..."
        show player 12
        player_name "Who's asking?"
        show player 11
        show henchman2 3
        henchman2 "It's personal matters, kid."
        show henchman2 1
        show player 12
        player_name "Well, she's kind of busy at the moment, so why don't you come another time."
        show henchman2 2
        show player 11
        henchman2 "Just give her this message will ya..."
        show henchman2 3
        henchman2 "She needs to hurry it up, or else."
        henchman2 "We ain't the patient type."
        show henchman2 1
        show player 11
        player_name "..."
        show player 12
        player_name "Or else, what?"
        show player 11
        show henchman2 3
        henchman2 "Just give her the message."
        henchman2 "We'll be back soon..."
        show henchman2 1
        player_name "..."
        $ playMusic()
        hide henchman2
        with dissolve
        scene home_entrance
        show player 10 at left
        with fade
        player_name "( What was {b}that{/b} all about... )"

        show player 5
        show mom 62 at right with dissolve
        mom "Was someone at the door, Sweetie?"
        show player 10
        show mom 61
        player_name "Yeah, some strange guy in a black suit came by..."
        show player 5
        show mom 59
        mom "!!!"
        show player 11
        show mom 60
        mom "...What did he want?"
        show mom 59
        show player 10
        player_name "He said you need to hurry up and that he'll be back soon, but refused to say why."
        show player 11
        show mom 60
        mom "It must be about..."
        mom "But I already paid off all the-"
        show mom 59
        mom "..."
        show player 10
        player_name "What is it?"
        show player 11
        show mom 60
        mom "It's nothing, Sweetie."
        show player 1
        show mom 62
        mom "They must've gotten the wrong address, that's all."
        hide mom
        hide player
        with dissolve
        $ M_mom.trigger(T_mom_bad_guys)
        $ unlock_ui()

    elif M_mom.get_state() == S_mom_pipe_help and gTimer.is_morning():
        scene home_entrance
        show player 11 at left
        show mom 13 at right
        with dissolve
        mom "Sweetie! Thank God you're here!"
        show mom 14b
        show player 10
        player_name "{b}[mom_name]{/b}?"
        show player 5
        show mom 13
        mom "Your sister's been freaking out all morning."
        show mom 14b
        show player 12
        player_name "Huh?"
        show player 5
        show mom 13
        mom "She was about to shower when the pipe under the bathroom sink broke."
        mom "She says there's water everywhere and she can't get ready to go out..."
        mom "...Do you mind taking a look at it?"
        show mom 14b
        show player 10
        player_name "Me? I err..."
        show player 5
        show mom 13
        mom "I was going to call a repairman but... you know, with our money situation and all..."
        show mom 14b
        show player 10
        player_name "It's okay, {b}[mom_name]{/b}."
        show player 14
        player_name "I'll go look at it and see if I can fix it."
        show player 13
        show mom 2
        mom "Thanks, Sweetie! Let me know if there's anything I can do to help."
        show mom 1
        show player 14
        player_name "Alright."
        hide mom
        hide player
        with dissolve
        $ M_mom.trigger(T_mom_broken_pipe)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_movie_night and gTimer.is_evening():
        scene location_home_entrance_night_blur
        show player 1 at left
        show mom 62 at right
        mom "Oh, hey Sweetie!"
        mom "Heading to bed?"
        show player 2
        show mom 61
        player_name "I'm just heading up to my room for a bit..."
        show player 14
        player_name "Why, what are you up to?"
        show player 1
        show mom 62
        mom "I was thinking about watching a movie."
        show player 2
        show mom 61
        player_name "Cool."
        show player 1
        mom "..."
        show mom 63
        mom "Say, why don't you come join me?"
        show player 10
        show mom 61
        player_name "Really?"
        show player 11
        show mom 62
        mom "Sure, why not? It's still early and I would love the company!"
        show player 2
        show mom 61
        player_name "Y-yeah, okay! I'd love to, {b}[mom_name]{/b}!"
        show player 1
        show mom 62
        mom "Great!"
        mom "I'll go get situated and you just come join me when you're ready, alright?"
        show player 2
        show mom 61
        player_name "Sounds good!"
        hide mom
        hide player
        with dissolve
        $ M_mom.trigger(T_mom_movie_invite)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_hang_out and not gTimer.is_dark():
        scene location_home_entrance_blur
        show player 1 at left with dissolve
        show mom 165 at right with dissolve
        mom "Hey Sweetheart!"
        show player 2
        show mom 164
        player_name "Hey [mom_name]!"
        player_name "You look nice! Where are you off to?"
        show player 1
        show mom 165
        mom "Oh, I just need to run the mall and pick up a few things."
        show mom 164
        mom "..."
        show mom 165
        mom "Say, why don't you come along?"
        show player 11
        show mom 164
        player_name "Hmm?"
        show player 10
        player_name "Oh I dunno, I was gonna-"
        show player 11
        show mom 165
        mom "Aww, c'mon! It'll do you good to get some fresh air."
        show mom 164
        player_name "..."
        show mom 165
        mom "... And besides, I don't want to go all by myself..."
        mom "Won't you come and keep me company?"
        show mom 164
        menu:
            "Yes.":
                show player 2
                player_name "Heh, sheesh [mom_name]! Alright, I'll go."
                show player 1
                show mom 166
                mom "Great!"
                show mom 165
                mom "I'll meet you in the car then, Sweetie!"
                $ M_mom.trigger(T_mom_hang_out_accept)
                $ lock_ui()
            "No.":

                show player 10
                player_name "Sorry [mom_name], I have something else planned for today..."
                show player 11
                show mom 168
                mom "Oh."
                show mom 169
                mom "..."
                show mom 168
                mom "Okay Sweetie, well... Just stay safe and be home for dinner."
                show player 2
                show mom 169
                player_name "Sure thing."
                $ M_mom.trigger(T_mom_hang_out_refuse)
        hide mom
        hide player
        with dissolve

    elif M_mom.get_state() == S_mom_spy and not gTimer.is_dark():
        scene home_entrance
        show player 10 with dissolve
        player_name "Huh?"
        player_name "What was that noise?"
        show player 11
        pause
        show player 10
        player_name "Maybe the TV is on in the living room."
        hide player with dissolve

    elif M_mom.get_state() == S_mom_kissing_practice and not gTimer.is_dark():
        scene home_entrance
        show player 4 with dissolve
        player_name "I wonder if I'd be able to kiss {b}[mom_name]{/b} again."
        player_name "I should probably try {b}ask her{/b} about it..."
        hide player with dissolve

    elif M_mom.get_state() == S_mom_car_broken and gTimer.is_morning():
        scene home_entrance
        show mom 3 at right
        show player 1 at left
        with dissolve
        mom "Good morning, Sweetie."
        show mom 1
        show player 14
        player_name "Morning, {b}[mom_name]{/b}."
        show player 13
        show mom 2
        mom "Did you sleep well last night?"
        show mom 1
        show player 10
        player_name "...Yeah... sorta."
        player_name "I've been having alot of weird dreams lately."
        show player 11
        show mom 2
        mom "Oh? What kind of weird dreams?"
        show mom 1
        show player 10
        player_name "Oh, umm..."
        player_name "Well, it's kinda embarrassing."
        show player 11
        show mom 2
        mom "... Naughty dreams?"
        show mom 1
        show player 10
        player_name "Err... Yeah."
        show player 11
        show mom 2
        mom "Well that's nothing to be embarrassed about, Sweetheart!"
        show mom 3
        mom "You're at that age afterall."
        show mom 1
        pause
        show mom 2
        mom "So who's the lucky girl?"
        show player 10
        show mom 1
        player_name "The girl?"
        player_name "Umm, I don't really wanna talk about it..."
        show player 11
        show mom 3
        mom "Hehe, Oh? I wonder if it's somebody I would know?"
        show player 11
        player_name "..."
        show mom 3
        mom "Oh, fine. Keep your secrets!"
        show mom 2
        mom "While your here, I need your help with something. Got a minute?"
        show mom 14
        show player 10
        player_name "Uh... Yeah. What is it?"
        show player 1
        show mom 13
        mom "Can you look at the car and see why it's not starting?"
        show mom 1
        show player 10
        player_name "I thought you just had it out a couple weeks ago?"
        show player 1
        show mom 13
        mom "I did. For some reason it won't even start now."
        show mom 1
        show player 2
        player_name "Maybe you left the lights on and the battery's dead. I'll give it a try."
        show mom 2
        show player 1
        mom "Thanks! I left the keys in the car so you can try to start it."
        show mom 1
        show player 14
        player_name "Okay!"
        hide player
        hide mom
        with dissolve
        $ M_mom.trigger(T_mom_car_help)

    elif M_mom.get_state() == S_mom_panties_masturbation_again and not gTimer.is_dark():
        $ temp = where_is("mom")
        scene home_entrance
        show player 1
        player_name "( I can't believe [mom_name] actually rubbed my Cock! )"
        player_name "( ... a couple more seconds and I would have popped. )"
        player_name "( Arrgh, I want her so bad! This is torture! )"
        show player 11
        player_name "( .... )"
        player_name "( Hmm, I know I promised not to jerk off in her room but... )"
        show player 13
        player_name "( It just felt so good last time! )"
        player_name "( ... )"
        player_name "( Maybe if I do it quickly and quietly, I can snag a pair of her panties and bust a nut without her noticing. )"
        player_name "( She seems to be {b}busy in the [temp]{/b} which should allow me to sneak into her room and rub one out in her bed. )"
        player_name "( I think it's worth a shot... I need the release... To clear my head! )"
        hide player with dissolve

    elif M_mom.get_state() == S_mom_diane_visit and gTimer.is_evening():
        scene home_entrance_evening
        show player 34 with dissolve
        player_name "...{b}*distant voice*{/b}..."
        show player 35
        player_name "( There're weird voices coming from the kitchen... )"
        show player 12
        player_name "( ...I don't remember {b}[mom_name]{/b} or {b}[sis_name]{/b} inviting anyone over... )"
        show player 10
        player_name "( I should go see if everything is okay. )"
        hide player with dissolve

    elif M_mom.get_state() == S_mom_midnight_search:
        jump mom_midnight_swim_block

    elif sister.started(sis_couch01) and gTimer.is_evening():
        scene home_entrance_night
        show player 11 with dissolve
        player_name "( What's that sound? )"
        player_name "( It sounds like the TV is on. )"
        show player 4 at Position(xpos=518)
        player_name "( Who could be watching TV this late? )"
        hide player with dissolve

    elif sister.started(sis_couch02) and gTimer.is_evening():
        scene home_entrance_night
        show player 26 with dissolve
        player_name "( That porno {b}Sis{/b} was watching was hot! I kind of feel like watching it, too... )"
        show player 33
        player_name "Hmm... Maybe {b}another night{/b}."
        hide player with dissolve

    elif sister.started(sis_couch03) and gTimer.is_evening() and (M_mom.get_state() != S_mom_sleepover or where_is("mom") != "Living Room"):
        scene home_entrance_night
        show player 11 with dissolve
        player_name "( What was that sound? )"
        hide player with dissolve
        jump home_livingroom_dialogue
    $ callScreen(location_count)

label mom_midnight_swim_towel_block:
    if location_count == "Entrance":
        scene home_entrance_night
    elif location_count == "Hallway":
        scene hallway_night
    show player 12 with dissolve
    player_name "I need to get a {b}towel from the bathroom{/b} for {b}[mom_name]{/b}."
    hide player with dissolve
    $ callScreen(location_count)

label mom_midnight_swim_block:
    scene home_entrance_night
    show player 12 with dissolve
    player_name "It's definitely coming from the backyard."
    player_name "I should go through the dining room and take a peek outside."
    hide player with dissolve
    $ callScreen(location_count)

label attic_key:
    $ suffix = ""
    if (M_mom.get_state() == S_mom_diane_visit and gTimer.is_evening()) or (M_mom.get_state() == S_mom_diane_dinner and gTimer.is_evening()):
        $ suffix = "_evening"
    elif gTimer.is_dark():
        $ suffix = "_night"
    scene expression "home_entrance{}".format(suffix)
    show expression "objects/closeup_key.png" with dissolve
    player_name "( I've never seen this key before. )"
    player_name "( It's rather small... )"
    hide expression "objects/closeup_key.png" with dissolve
    show expression "boxes/popup_key.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_key.png" with dissolve
    jump home_entrance

label vacuum_dialogue:
    scene location_home_entrance_fight
    show mom 94 at right with dissolve
    pause
    show mom 95
    pause
    show mom 94
    pause
    show mom 95
    pause
    show mom 94
    show player 1 at left with dissolve
    pause
    show mom 95
    pause
    show mom 97 with dissolve
    mom "Oh!!"
    mom "You startled me..."
    show mom 98
    show player 17
    player_name "Sorry, {b}[mom_name]{/b}."
    show player 14
    player_name "I didn't mean to!"
    show mom 97
    show player 1
    mom "Sorry about the noise."
    mom "It's taking me a while to clean up, but I should be done soon."
    mom "My poor old back is killing me..."
    show mom 98
    menu:
        "Let me help.":
            show mom 98 at right
            show player 14 at left
            player_name "Here, {b}[mom_name]{/b}, pass me the vacuum."
            show player 1
            show mom 96
            mom "..."
            show mom 97
            mom "You want the vacuum?"
            show mom 96
            show player 14
            player_name "Yeah, I'll take over from here."
            player_name "You deserve a rest, {b}[mom_name]{/b}."
            show player 10
            player_name "I don't like seeing you hurting like this..."
            show mom 97
            show player 11
            mom "It's okay, Sweetie. You don't have-"
            show mom 98
            show player 10
            player_name "No, {b}[mom_name]{/b}!"
            player_name "I want to do it."
            show mom 97
            show player 1
            mom "Well, if you insist..."
            show player 257
            show mom 100
            with dissolve
            mom "Thanks for helping... It's very sweet of you."
            show player 259
            show mom 99
            player_name "No problem!"
            hide player
            hide mom
            with dissolve
            scene help_mom_mc_home_cutscene with fade
            show text "I felt bad {b}[mom_name]{/b} was having a hard time with her back pain. \nI was glad I could help, even if it took a while to finish. \nI have to say, doing the stairs was harder than I thought... \nAt least {b}[mom_name]{/b} kept me company until I finished both floors." at Position (xpos= 512, ypos = 700) with dissolve
            pause
            hide text with dissolve
            $ gTimer.tick()
            $ M_mom.trigger(T_mom_vacuumed)
        "It's too loud.":

            show mom 96 at right
            show player 10 at left
            player_name "Can you please finish cleaning another time?"
            player_name "I can't study with all the noise..."
            show mom 97
            show player 11
            mom "I'm sorry, Sweetie!"
            mom "I didn't mean to bother you like this."
            show mom 96
            show player 14
            player_name "It's okay, {b}[mom_name]{/b}."
            show mom 97
            show player 1
            mom "I guess I could rest my back for a while..."
            show mom 96
            show player 17
            player_name "Thanks!"
            hide player
            hide mom
            with dissolve
    $ M_mom.set("chores", False)
    $ callScreen(location_count)

label lawn_mower_dirty:
    if location_count == "Home Front":
        scene home_front
    elif location_count == "Entrance":
        scene home_entrance
    elif location_count == "Living Room":
        scene home_livingroom_b
    show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
    show player 11 zorder 1
    with dissolve
    player_name "( I should get my clothes cleaned up before I do that... )"
    hide player
    hide xtra
    with dissolve
    $ callScreen(location_count)

label mom_outing_block:
    scene home_entrance
    show player 4 with dissolve
    player_name "I should hurry up and meet [mom_name] at the car..."
    hide player with dissolve
    $ callScreen(location_count)

label mom_dinner_outfit:
    if location_count == "Entrance":
        scene home_entrance
    elif location_count == "Living Room":
        scene home_livingroom_b
    show player 10 with dissolve
    player_name "{b}[mom_name]{/b} called for me, I should check up on her..."
    hide player with dissolve
    $ callScreen(location_count)

label erik_bullying_3:
    $ location_count = "Entrance"
    scene home_entrance_evening
    show erikmom 19c at Position (xpos=700)
    show mom 13 at right
    with dissolve
    show player 5 at left with dissolve
    mom "Sweetie!! Are you okay?!"
    show mom 14b
    show player 10
    player_name "I'm fine, {b}[mom_name]{/b}. The nurse said I just had a small concussion."
    show player 11
    show mom 13
    mom "You had a concussion!"
    show mom 14b
    show player 10
    player_name "Everything is fine. I'll be okay, {b}[mom_name]{/b}."
    show player 5
    show mom 13
    mom "I didn't even know you were in the hospital!"
    mom "Oh, I'm the worst mother in the world!"
    show mom 14b
    show player 10
    player_name "{b}[mom_name]{/b}, it's alright. I'm really fine! Calm down."
    show player 11
    show mom 13
    mom "I left the house this morning and when I got back I realized you still weren't home yet!"
    mom "Then {b}Mrs. Johnson{/b} stopped over and..."
    show mom 14b
    show erikmom 19
    erimom "I got a hold of your mother when I saw she was home and filled her in on your scuffle at school."
    erimom "I told her you were on your way back from the hospital with {b}Erik{/b}."
    erimom "You did a good thing standing up for {b}Erik{/b}."
    show erikmom 38
    show mom 13
    mom "Yes, it was really brave of you to stand up for your friend at school."
    mom "But, be please be careful!"
    show mom 14b
    show player 24
    player_name "I know {b}[mom_name]{/b}..."
    show player 25
    player_name "I promise I'll try and stay out of trouble."
    show player 24
    show mom 13
    mom "Come here."
    hide player
    hide mom
    hide erikmom
    with dissolve
    show erikmom 14 at right
    show mom 4
    with dissolve
    mom "I'm so glad your safe."
    mom "I love you."
    player_name "I love you too, {b}[mom_name]{/b}."
    hide mom
    hide erikmom
    with dissolve
    show erikmom 14 at Position (xpos=700)
    show mom 1 at right
    show player 13 at left
    with dissolve
    show erikmom 17
    erimom "Thanks again, {b}[firstname]{/b}."
    erimom "You're always welcome to stop over and visit."
    show erikmom 14
    show player 14
    player_name "It's fine. Just helping a friend."
    show player 13
    show erikmom 17
    erimom "Thank you."
    show erikmom 14
    show player 36 with dissolve
    player_name "Good night {b}Mrs. Johnson{/b}."
    show player 13 with dissolve
    show erikmom 17
    erimom "Good night."
    hide erikmom with dissolve
    show mom 2
    mom "Now hurry up to bed and get some rest."
    hide player
    hide mom
    with dissolve
    $ erik.add_event(erik_bullying_3)
    $ callScreen(location_count)