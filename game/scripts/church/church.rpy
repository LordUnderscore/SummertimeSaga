default church_first_time = True

label church_dialogue:
    $ location_count = "Church"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 3.9>audio/ambience_church.ogg"):
            $ playSound("<loop 3.9>audio/ambience_church.ogg")
    if church_first_time == True and not (gTimer.is_weekend() and gTimer.is_morning()):
        scene church_b with None
        show player 11 with dissolve
        player_name "( The church is empty. )"
        player_name "( Looks like I missed Mass. )"
        hide player 11
        $ church_first_time = False

    if M_mia.get_state() == S_mia_church_plan and gTimer.is_weekend() and gTimer.is_morning():
        scene church_full02_b
        show player 32 at Position (xoffset=68) with dissolve
        player_name "{b}Helen{/b} is sitting in the front."
        show player 12 with dissolve
        player_name "There must be a way to speak with her..."
        player_name "...But I need to change my attire first."
        player_name "Let's see if I can find one of those {b}priest outfits{/b} somewhere in the church..."
        hide player with dissolve

    elif M_mia.get_state() == S_mia_convince_helen:
        scene church_cs01
        with fade
        show text "The mass was still ongoing.\n{b}Helen{/b} got up and headed towards the confessional...\n...making her way inside." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        hide church_cs01
        with dissolve

        scene church_cs02
        with fade
        show text "The priest left for a brief moment.\nNow is the perfect time to get close to her...\n...And change her mind about {b}Harold{/b}." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        hide church_cs02
        with dissolve

        scene church_full03_b
        show player 30 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "I need to {b}enter the confessional{/b} from the {b}right side{/b}..."
        hide player
        hide players robe
        with dissolve
        $ M_mia.trigger(T_helen_confessional)

    elif M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_full02_b
        show player 33 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "Perfect!"
        show player 106 at Position (xoffset=-1)
        player_name "..."
        show player 14 at Position (xoffset=-1)
        player_name "I should leave and return this outfit where I found it..."
        player_name "...before someone notices..."
        hide player
        hide players robe
        with dissolve

    elif M_mia.get_state() == S_mia_nun_thoughts:
        scene church_b
        show player 10 with dissolve
        player_name "Damn... That was scary!"
        player_name "Now I have to do stuff for this nun..."
        player_name "...I just hope she doesn't tell anyone about what I did."
        hide player with dissolve
        $ ui_lock_count = 0
        $ M_mia.trigger(T_mc_nun_thoughts)

    elif M_mia.get_state() == S_mia_church_night_visit and gTimer.is_dark():
        scene church_n_b
        show player 10 with dissolve
        player_name "It's so quiet at night..."
        player_name "...I'm not sure people are allowed in here this late."
        show player 12
        player_name "Let's go see {b}Sister Angelica{/b} and see what she wants from me..."
        hide player with dissolve
    $ callScreen(location_count)

label angelica_dialogue:
    if M_mia.is_set('helen dialogue change'):
        scene church_c with fade
        show player 10 at left
        show ang 1 at right
        with dissolve
        player_name "Hi, {b}Sister Angelica{/b}."
        show player 5
        show ang 2
        ang "You, again."
        ang "What is it you want?"
        show ang 1
        menu:
            "Talk.":
                show player 10
                player_name "I just wanted to talk."
                show player 5
                show ang 2
                ang "Quiet."
                show ang 1
                show player 24
                player_name "Oh..."
                show ang 2
                ang "If you want to talk, come visit me at night in my chambers..."
                show ang 1
                show player 25
                player_name "Alright, then. Sorry."
                hide player
                hide ang
                with dissolve
            "Graveyard.":

                show player 10
                player_name "How do you access the graveyard?"
                show player 5
                show ang 2
                ang "It is off limits."
                ang "Although, it is locked and still pesky kids keep finding ways to {b}sneak through the fence{/b}."
                show ang 1
                show player 12
                player_name "But my dad is buried in there."
                show player 5
                ang "..."
                show ang 2
                ang "I'm sure he is."
                show ang 1
                show player 12
                player_name "But-"
                show player 16
                show ang 2
                ang "Be gone. You are wasting my time."
                hide ang
                hide player
                show player 16
                with dissolve
                player_name "..."
                show player 12
                player_name "Maybe I can find {b}a way through the fence{/b} too."
                hide player with dissolve
            "Nevermind.":

                show player 10
                player_name "Nevermind, I have to go."
                show player 5
                ang "..."
                show ang 2
                ang "Don't waste my time like that again."
                show ang 1
                show player 25
                player_name "You're right, I'm sorry..."
                hide player
                hide ang
                with dissolve
    else:

        scene church_c
        show ang 2 at right
        show player 1 at left
        with dissolve
        ang "Are you from this Parish, young man?"
        show ang 1
        show player 14
        player_name "Hi, I was wo-"
        show ang 2
        show player 11
        ang "Are you from this Parish, young man?"
        show ang 1
        show player 14
        player_name "Uhh... Not really."
        show ang 2
        show player 11
        ang "Do you believe in God?"
        show ang 1
        show player 10
        player_name "Well..."
        show ang 2
        show player 11
        ang "I'm sorry."
        ang "I can only help those who share the faith of our lord!"
        hide player
        hide ang
        with dissolve
    $ callScreen(location_count)

label confessional_left:
    if M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_full02_b
        show player 10 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "I need to return this robe before someone sees me."
        hide player
        hide players robe
        with dissolve

    elif M_mia.get_state() == S_mia_priest_act:
        scene church_full02_b
        show player 10 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "I can't go in that side."
        player_name "I have to use the door on the {b}right side{/b} of the confessional..."
        hide player
        hide players robe
        with dissolve
    else:

        scene church_confession
        show player 283 at Position(xpos=280)
        with dissolve
        player_name "Bless me father, for I have sinned."
        show player 278
        player_name "..."
        show player 284
        player_name "......"
        show player 280
        player_name "Father?"
        player_name "There's no one here?"
        show player 10
        player_name "( I guess there's no priest around at this time... )"
        hide player
        hide church_confession
    $ callScreen(location_count)

label confessional_right:
    if M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_full02_b
        show player 10 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "I need to return this robe before someone sees me."
        hide player
        hide players robe
        with dissolve

    elif M_mia.get_state() == S_mia_priest_act:
        scene church_confession
        show player 5f at Position (xpos=795)
        show players robe f at Position (xpos=794)
        show helen 16 at Position (xpos=300)
        with dissolve
        helen "Forgive my family {b}Father{/b} for they have sinned. It has been 7 days since my last confession."
        show helen 15
        helen "..."
        show helen 13
        helen "{b}Father{/b}? Are you there?"
        show helen 12
        show player 23f
        player_name "*Cough*"
        show player 10f
        player_name "Yes... I err... I am listening..."
        show player 5f
        show helen 16
        helen "O {b}Lord{/b}, I am heartily sorry for the way my family has offended you..."
        helen "...By my husband failing our marriage... And my daughter's whorish behavior..."
        helen "I've tried feverishly to make them see their errors."
        helen "I've instructed them that they were headed to hell if they didn't change."
        helen "...But it seems they've lost the holy path and succumbed to darkness."
        show helen 14
        helen "What should I do, {b}Father{/b}?"
        show helen 15
        menu:
            "Pray?" if pStats.chr() < 3:
                show player 10f
                player_name "[chr_warn]Perhaps you could... Err... Pray?"
                show player 22f
                show helen 12
                helen "[chr_warn]..."
                show helen 13
                helen "[chr_warn]Pray?"
                show helen 12
                show player 10f
                player_name "[chr_warn]Sure!"
                show player 22f
                show helen 13
                helen "[chr_warn]I don't quite see how this will help my family, {b}Father{/b}."
                helen "[chr_warn]Something must be done! Something must change for them to recognize their sinful and vile behavior."
                show helen 12
                show player 21f
                player_name "[chr_warn]Err... The {b}Lord{/b} works in mysterious ways!"
                show player 22f
                helen "[chr_warn]..."
                show helen 14
                helen "[chr_warn]Okay... I will do what I can, {b}Father{/b}."
                show helen 16
                helen "[chr_warn]Please ask the {b}Lord{/b} to forgive them and could you pray for them too?"
                show helen 15
                show player 10f
                player_name "[chr_warn]Sure! Shouldn't be a big deal!"
                show player 5f
                show helen 12
                helen "[chr_warn]..."
                show helen 14
                helen "[chr_warn]And what, dear {b}Father{/b}, would you have your faithful servant do as Penance in my family's stead?"
                show helen 12
                show player 10f
                player_name "[chr_warn]Err... Ummm...two prayers will suffice?"
                show player 5f
                helen "[chr_warn]..."
                show helen 13
                helen "[chr_warn]Thank you..."
                hide helen with dissolve
                show player 24f
                player_name "[chr_warn]Damn, I got too nervous..."
                player_name "[chr_warn]...I need to try again later, with more confidence."
                hide players robe
                show player 444f
                with dissolve
                pause
                hide player with dissolve
                $ ui_lock_count = 0
                $ M_mia.trigger(T_helen_convince_fail)

            "Change." if pStats.chr() >= 3:
                show player 12f
                player_name "Perhaps it is {b}you{/b} who needs to change, in order for them to return to the path..."
                show player 5f
                show helen 14
                helen "Me?! ...But I've done eveything right... I..."
                show helen 12
                show player 12f
                player_name "Yes, you've done a good job pointing out their flaws, but what about your own?"
                player_name "I have yet to hear about your wrong doing. You can't be perfect?"
                show player 5f
                show helen 15
                helen "..."
                show helen 14
                helen "*sigh*"
                show helen 16
                helen "Maybe you're right, {b}Father{/b}."
                helen "I...may have...gone too far..."
                show helen 14
                helen "It's just they don't seem to understand their peril... like I do..."
                helen "I do it, because I love them..."
                show helen 15
                show player 10f
                player_name "You can still redeem yourself!"
                show player 5f
                show helen 14
                helen "Redeem? But what could I do?"
                show helen 15
                show player 12f
                player_name "Maybe you could try to be more accepting of your husband..."
                player_name "...And give your daughter some freedom to grow!"
                show player 10f
                player_name "They don't need to be suffocated by {b}God's{/b} rules, instead show them how much you love them, like {b}God{/b} loves everyone."
                player_name "You can't control everyone... But you can change yourself."
                show player 5f
                show helen 14
                helen "You're right... I will do what I can, {b}Father{/b}."
                show helen 15
                show player 14f
                player_name "Now go out and show some compassion and forgiveness just as the {b}Lord{/b} forgives you."
                show player 13f
                show helen 16
                helen "Thank you for your insight... and forgiveness..."
                show helen 15
                show player 17f
                player_name "No problem!"
                show helen 12
                helen "..."
                show player 21f
                player_name "Err... Umm...have a blessed day."
                show player 13f
                show helen 16
                helen "What would you have me do as Penance, {b}Father{/b}?"
                show helen 15
                show player 12f
                player_name "Two prayers will suffice as your Penis... err.. Penance."
                show player 22f
                show helen 12
                pause        
                show helen 16
                show player 13f
                helen "Thank you..."
                hide helen
                hide player
                hide players robe
                with dissolve
                $ M_mia.trigger(T_helen_convince_change)
                jump church_dialogue
    else:

        scene church_confession
        show player 43f at Position(xpos=760)
        with dissolve
        player_name "( Cool! )"
        player_name "( I've never been on this side of the confessional. )"
        show player 4f
        player_name "Hmm..."
        show player 14f
        player_name "( Looks the same as the other side, actually. )"
        player_name "( I should get out of here... )"
        hide player
        hide church_confession
    $ callScreen(location_count)