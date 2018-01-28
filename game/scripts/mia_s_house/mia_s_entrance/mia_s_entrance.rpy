label mias_entrance:
    $ location_count = "Mia's House Entrance"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_mia.get_state() == S_mia_parent_blocking:
        scene mia_house_c
        show helen 2 zorder 1 at right
        show player 1 at left
        with dissolve
        helen "And you are?"
        show helen 1
        show player 14
        player_name "I'm {b}[firstname]{/b}!"
        player_name "I'm a friend from school..."
        show helen 2
        show player 1
        helen "A friend?"
        show player 11
        helen "Our daughter doesn't bring guests home."
        helen "She also didn't mention anything about your visit..."
        helen "Have you two met at church?"
        show helen 1
        show player 10
        player_name "No?"
        show helen 2
        show player 11
        helen "Are you a church goer, {b}[firstname]{/b}?"
        show helen 1
        show player 10
        player_name "Uhh... Not really, Ma'am."
        show helen 2
        show player 11
        helen "Of course not."
        show helen 1
        show player 1
        show harold 2 zorder 0 at Position (xpos = 670, ypos = 768) with dissolve
        harold "Hey, dear!"
        harold "Is this one of {b}Mia's{/b} friends?"
        show harold 1
        show helen 3
        show player 5
        helen "It's a young man who's about to leave."
        hide helen
        hide harold
        hide player
        with dissolve
        show unlock30 at truecenter with dissolve
        $ loc_church_unlocked = True
        pause
        hide unlock30
        pause .4
        show unlock32 at truecenter with dissolve
        $ loc_police_unlocked = True
        pause
        hide unlock32 with dissolve

        $ M_mia.trigger(T_mia_kicked_out)
        jump mias_house_dialogue

    elif M_mia.get_state() == S_mia_helen_fight:
        scene mia_house_c
        show helen 6f at left
        show mia 46f at right
        with dissolve
        mia "{b}MOM{/b}!"
        mia "How can you let this happen?!"
        show mia 45f
        show helen 5f
        helen "Oh, stop being so childish!"
        helen "Your father and I are simply taking a break..."
        helen "...We are not breaking our divine sacrament over a dispute!"
        helen "We're not wicked..."
        hide helen with dissolve
        pause
        show player 10 at left with dissolve
        player_name "{b}Mia{/b}!"
        player_name "I just saw your dad outside and he-"
        show player 11
        show mia 46f
        mia "I need your help!"
        show mia 45f
        show player 10
        player_name "Wait, what?"
        show player 5
        show mia 46f
        mia "My mom and dad are splitting up and I need your help getting them back together!"
        show mia 45f
        show player 11
        player_name "!!!"
        show mia 46f
        mia "Will you...help me?"
        show mia 45f
        show player 10
        player_name "Well, I'm not sure how I could-"
        show player 11
        show mia 46f
        mia "Try talking to my mom first."
        mia "I tried everything, but she won't listen..."
        show mia 45f
        show player 12
        player_name "She would never listen to me."
        show player 5
        show mia 46f
        mia "Please?!"
        show mia 45f
        show player 3 with dissolve
        player_name "..."
        show player 12 with dissolve
        player_name "Okay, I'll try."
        player_name "But I can't promise you it will work..."
        show player 5
        show mia 46f
        mia "Thank you, {b}[firstname]{/b}."
        hide player
        hide mia
        with dissolve
        $ M_mia.trigger(T_mias_request)

    elif M_mia.get_state() == S_mia_helen_refusal:
        scene mia_house_c
        show player 5 at left
        show mia 12 at right
        with dissolve
        mia "Did you speak with her?"
        show mia 8
        show player 24
        player_name "Yeah..."
        show mia 12
        mia "So, what did she say?"
        show mia 8
        show player 12
        player_name "She's too stubborn."
        player_name "I told you she wouldn't listen to me..."
        show player 5
        show mia 12
        mia "*Sigh*"
        mia "{b}Mom{/b} only listens to {b}God{/b}...or {b}our church{/b}."
        show mia 8
        show player 37 with dissolve
        player_name "..."
        show player 38 with dissolve
        player_name "Wait."
        show player 29 with dissolve
        player_name "I think I've got an idea!"
        show player 13 with dissolve
        show mia 12
        mia "What is it?"
        show mia 8
        show player 14
        player_name "When does your mom go to church?"
        show player 13
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
        $ M_mia.trigger(T_mia_church_mention)
        $ ui_lock_count = 0

    elif M_mia.get_state() == S_mia_urgent_help:
        scene mia_house_c
        show helen 25 at Position (xpos=700)
        show player 5 at left
        show mia 12 at right
        with dissolve
        mia "You got my text message?"
        show mia 8
        show helen 23
        show player 10
        player_name "Yeah, what's going on?"
        show player 11
        show helen 25
        show mia 46f
        mia "We can't find my dad..."
        show mia 45f
        show helen 26
        helen "No need to get alarmed yet, of course. But..."
        show player 5
        show helen 24
        helen "...He hasn't called in days, and it's not like him."
        show helen 25
        show mia 46f
        mia "He usually calls every day and checks up on us..."
        mia "...What if something {b}BAD{/b} happened?!"
        show mia 45f
        show player 22
        player_name "!!!"
        show helen 26
        helen "{b}Mia{/b}!"
        helen "Don't say things like that, I'm sure he will be back."
        show helen 23
        show player 10
        player_name "I'm not sure how I could be useful..."
        player_name "...But I'm willing to help!"
        show player 5
        show helen 24
        helen "If you're going to help us, start by questioning his coworkers at the {b}police station{/b}..."
        helen "...And look for {b}clues{/b} around his workplace."
        helen "That would be a good start."
        show helen 25
        show mia 46f
        mia "Will you do it, {b}[firstname]{/b}?"
        show mia 45f
        show helen 23
        show player 35
        player_name "I suppose I can ask around to see where he could be..."
        show player 34
        helen "..."
        show helen 24
        helen "Perhaps I was wrong about you, {b}[firstname]{/b}."
        show player 13
        helen "Thank you...for caring about us, and my husband."
        show helen 23
        show player 12
        player_name "Let's just try and find {b}Harold{/b}."
        show player 5
        show helen 25
        show mia 46f
        mia "Come back if you find anything!!"
        show mia 45f
        show helen 23
        show player 14
        player_name "I will!"
        hide player
        hide mia
        hide helen
        with dissolve
        $ M_mia.trigger(T_harold_missing)

    elif M_mia.get_state() == S_mia_harold_found_news:
        scene mia_house_c
        show player 13 at left
        show helen 24 at Position (xpos=700)
        with dissolve
        helen "{b}[firstname]{/b}?"
        show helen 23
        show player 14
        player_name "Oh, hi {b}Helen{/b}!"
        show player 13
        show helen 24
        helen "I have to ask... Any news about my husband?"
        show helen 23
        show player 12
        player_name "Actually, I just spoke with him."
        show player 10
        player_name "He was...taking a break and driving around."
        show player 5
        show helen 24
        helen "I see."
        helen "So, how did he look?"
        show helen 23
        show player 10
        player_name "He looked a bit...rough."
        show player 5
        show helen 24
        helen "I... I want you to be honest with me. What did {b}Harold{/b} say to you?"
        show helen 23
        show player 10
        player_name "I'm not sure he will be back...but he said he would call."
        show player 5
        show helen 24
        helen "Hmm... Did he say anything about me?"
        show helen 23
        show player 10
        player_name "Ehh... Well, he said you had changed...and that you two used to be happier..."
        show player 5
        show helen 3 with dissolve
        helen "*Sigh*"
        show helen 24 with dissolve
        helen "Okay, thanks for letting me know..."
        show helen 25
        show mia 10 at right with dissolve
        mia "{b}[firstname]{/b}?!"
        show mia 7
        show helen 23
        show player 14
        player_name "Hey, {b}Mia{/b}!"
        show player 13
        show helen 25
        show mia 10
        mia "When did you get here?"
        show mia 7
        show helen 23
        show player 14
        player_name "Just now."
        show player 12
        player_name "I was telling your mom that I saw your dad."
        show player 5
        show helen 25
        show mia 12
        mia "Is he okay?!"
        show mia 8
        show helen 3 with dissolve
        helen "Your father is fine, dear."
        show helen 26 with dissolve
        helen "He's just...taking a break, but he will visit us soon. I promise."
        show helen 25
        show mia 10
        mia "...Really?"
        show mia 7
        show helen 23
        show player 29 with dissolve
        player_name "I think so, yeah."
        show player 3
        show helen 25
        show mia 10
        mia "That's great news!"
        mia "Thanks for helping us, {b}[firstname]{/b}..."
        mia "...Sorry to have bothered you with all this."
        mia "I'm just glad it turned out to be nothing serious."
        show mia 7
        show helen 23
        show player 12
        player_name "{b}Harold{/b} will be back, don't worry."
        show player 14
        player_name "See you at school!"
        hide player
        hide mia
        hide helen
        with dissolve
        $ M_mia.trigger(T_mia_give_news)

    elif M_mia.get_state() == S_mia_route_split:
        scene mia_indoors with fade
        show player 13 at left
        show harold 1 at right
        show helen 50 at Position (xpos=700)
        show mia 7 at Position (xpos=500)
        with dissolve
        harold "There he is!"
        show harold 1
        show player 14
        player_name "Hey! I didn't expect to see you all here."
        show player 13
        show helen 51
        helen "{b}Harold{/b} has slowly started to move back in with us."
        show helen 50
        show harold 2
        harold "It feels great to be back home."
        show harold 1
        show mia 10
        mia "Now that we are reunited, we can move onto better things, as a family."
        mia "Thank you, {b}[firstname]{/b} for helping and being there for us."
        show mia 7
        show harold 2
        harold "I'm glad we got to know you better..."
        harold "...And feel free to come by more often, or sleep over!"
        show harold 1
        show helen 26
        helen "{b}Harold{/b}?! I'm not so sure this is-"
        show helen 25
        show harold 2
        harold "Oh come on, {b}Helen{/b}, this young man may become our future son in law!"
        show harold 1
        show helen 50
        show mia 10
        mia "{b}Dad{/b}!"
        show mia 7
        show helen 51 with dissolve
        helen "{b}Harold{/b}!"
        show helen 50
        harold "..."
        show harold 2
        harold "Let's go in the living room and let the kids have a little alone time."
        show harold 1
        show helen 26
        helen "Of course dear."
        hide harold
        hide helen
        with dissolve
        show player 14
        player_name "I'm so happy that things worked out."
        player_name "Your parents seem to get along well..."
        show player 13
        show mia 9
        mia "I know! Things couldn't have worked out any better!"
        show mia 10
        mia "Thank you ,{b}[firstname]{/b}...for everything."
        show mia 7
        show player 14
        player_name "You're wel-"
        hide player
        show mia 49 at left
        with dissolve
        player_name "!!!" with hpunch
        show player 13 at left
        show xtra 21 at left
        hide mia
        show mia 9 at Position (xpos=500)
        with dissolve
        mia "Sooo listen, now that things are back to normal."
        show mia 10
        mia "I was thinking we could...study again?"
        show mia 7
        show player 21
        player_name "That sounds like a great idea!"
        show player 13
        show mia 10
        mia "Stop over any night."
        mia "I got a new magazine that mentioned a great new study trick."
        mia "I was hoping we...could try it out."
        show mia 7
        show player 21
        player_name "Awesome! Count me in!"
        show player 13
        show mia 10
        mia "I'll be waiting! See you later, {b}[firstname]{/b}."
        show mia 7
        show player 21
        player_name "Bye, {b}Mia{/b}."
        hide player
        hide xtra 21
        hide mia
        with dissolve
        $ M_mia.trigger(T_mia_family_reunion)

    elif M_helen.get_state() in [S_helen_route_split, S_helen_harold_moved_on]:
        scene mia_indoors with fade
        show mia 45f at right
        show player 10 at left
        with dissolve
        player_name "{b}Mia{/b}?!"
        show player 5
        show mia 46f
        mia "{b}[firstname]{/b}!"
        show mia 45f
        show player 10
        player_name "What's wrong?"
        show player 5
        show mia 46f
        mia "My parents split up for good!"
        show mia 45f
        show player 10
        player_name "I... I'm so sorry."
        show player 5
        show mia 46f
        mia "I just feel so guilty... I didn't try hard enough."
        mia "It's all my fault!"
        show mia 45f
        show player 37 with dissolve
        player_name "..."
        show player 10 with dissolve
        player_name "No, {b}Mia{/b}. It's really not your fault..."
        player_name "Sometimes...people don't always stay together."
        show player 11
        show mia 47f with dissolve
        mia "Well then relationships suck! Love doesn't even exist."
        show mia 48f
        show player 22
        player_name "!!!"
        show player 24
        show mia 45f with dissolve
        mia "..."
        show mia 46f
        mia "Thanks for trying to help my family..."
        show player 25
        mia "I need to be alone..."
        hide mia with dissolve
        show player 24
        player_name "Shit..."
        player_name "{b}Mia{/b} is taking this worse than I thought."
        show player 37 with dissolve
        player_name "Now she's going to blame herself for this..."
        show player 24 with dissolve
        pause
        show helen 23 at right with dissolve
        show player 11
        player_name "!!!"
        show player 10
        player_name "{b}Helen{/b}... Hi..."
        show player 5
        show helen 24
        helen "Hello, {b}[firstname]{/b}."
        helen "I appreciate hearing your concern for my daughter."
        helen "But don't worry about {b}Mia{/b}, I'll take care of her."
        show helen 23
        show player 10
        player_name "Oh..."
        show player 5
        show helen 24
        helen "You should visit our house more."
        helen "I want you to feel at home here."
        helen "We've got an extra bed in my room..."
        show helen 23
        show player 21
        player_name "Heh heh... I...I thought those rituals were over."
        show player 5
        show xtra 21 at left
        show helen 24
        helen "But, {b}[firstname]{/b}, I am your holy servant now."
        show helen 28
        helen "You know how I struggle with my desires."
        helen "In fact, I feel so...unclean right now."
        helen "I need a stiff...deep...purging..."
        show helen 23
        show player 10
        player_name "Are you suggesting, I-"
        show player 11
        show helen 24
        helen "Of course, won't you...{b}Master{/b}?"
        show helen 23
        show player 22
        player_name "!!!"
        show helen 28
        helen "If you are busy though, I'll wait for you to purge my sins in our bed during the day..."
        helen "...Or at night you can penetrate my sinful flesh in the nun's chamber."
        show helen 27
        show player 10
        player_name "You really need me to?"
        show player 5
        show helen 24
        helen "Of course!"
        helen "I desperately need to be kept in line..."
        helen "Otherwise, my sinful hands can't stop themselves from...getting dirty."
        helen "Please visit me soon, {b}Master{/b}."
        show helen 23
        show player 11
        player_name "..."
        hide xtra
        hide player
        hide helen
        with dissolve
        $ M_helen.trigger(T_helen_master_servant)

    elif M_mia.get_state() == S_mia_unexpected_visit:
        scene mia_indoors
        show player 10 with dissolve
        player_name "Hello?"
        show player 12
        player_name "Hmm... No one's home?"
        player_name "Maybe she's upstairs..."
        hide player with dissolve
        $ ui_lock_count = 1
    $ callScreen(location_count)

label helen_masturbating_block:
    scene mia_indoors
    show player 12 with dissolve
    player_name "I should find {b}Mia{/b} before I leave..."
    hide player with dissolve
    $ callScreen(location_count)

label mias_house_sneak:
    $ location_count = "Mia's House Entrance"
    scene black with dissolve
    with Pause(0.5)

    show mia_sneak01 with dissolve
    show text "The door is unlocked.\n I hope I don't get in trouble for this...\n Alright, I'm going in." at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide text with dissolve

    if not M_mia.is_set('harold left'):
        scene black with dissolve
        with Pause(0.5)

        show mia_sneak02 with dissolve
        show text "Both her parents are watching TV.\n I just have to be quiet and make my way upstairs now...\n" at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

    hide mia_sneak01
    hide mia_sneak02
    scene black
    with dissolve
    with Pause(0.5)
    $ callScreen(location_count)