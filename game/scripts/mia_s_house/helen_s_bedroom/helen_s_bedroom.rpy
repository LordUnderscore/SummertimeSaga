label helens_bedroom:
    $ location_count = "Helen's Bedroom"
    if M_mia.get_state() == S_mia_midnight_help:
        scene mia_house_helen_n_b
        player_name "The key must be somewhere in here..."

    elif M_mia.get_state() == S_mia_helen_talk:
        scene expression gTimer.image("mia_house_helen_c{}")
        show helen 1f at right
        show player 10 at left
        with dissolve
        player_name "Uhm... Hello?"
        show player 5
        show helen 4
        helen "!!!"
        show helen 5
        helen "You...again?!"
        show helen 6
        show player 10
        player_name "{b}Mia{/b} asked me to come and speak with you."
        show player 5
        show helen 2
        helen "{b}Mia{/b} asked you?"
        show helen 1
        show player 12
        player_name "I don't know what's going on exactly, and it's none of my business..."
        show player 10
        player_name "...But I don't think {b}Mia{/b} wants her parents to split up like this."
        show player 11
        show helen 5
        helen "You're right. It is none of your business!"
        show helen 4
        helen "Besides...there's nothing we can do at the moment..."
        show helen 3
        helen "...everything is in the hands of {b}God{/b}!"
        show helen 1
        show player 12
        player_name "Huh?"
        show player 5
        show helen 4
        helen "You should leave now..."
        hide player
        hide helen
        with dissolve
        $ M_mia.trigger(T_mia_helen_deny)

    elif M_mia.get_state() == S_mia_unexpected_visit:
        scene mia_house_helen_sneak
        show helens 1_2 at Position (xpos=465,ypos=565) with dissolve
        player_name "!!!"
        player_name "...{b}Helen{/b}?!"
        player_name "Is that... A police baton?!"
        helen "Uuuhh! Ooohh yesss..."
        helen "{b}Harold{/b}..."
        helen "Uuhhhh..."
        helen "It's been...so long..."
        show helens 3 with dissolve
        player_name "!!!" with hpunch
        player_name "She saw me!!"
        scene black
        scene mia_house_helen_c
        show helen 33 at right
        show player 10 at left
        with dissolve
        player_name "I'm so sorry, {b}Helen{/b}!!!"
        player_name "I heard voices and thought {b}Mia{/b} was in here with you..."
        player_name "...I didn't mean to see..."
        show player 5
        show helen 34
        helen "I... I'm sorry you had to see me like this..."
        show helen 29
        show player 24
        player_name "I didn't see much anyway... I just..."
        player_name "I should really leave, this was innapropriate of me."
        show player 11
        show helen 30
        helen "Wait!"
        helen "I need you to tell me something."
        show helen 29
        show player 3 with dissolve
        player_name "..."
        show helen 34
        helen "Do you think I still look...attractive?"
        show helen 33
        show player 22 with dissolve
        player_name "!!!" with hpunch
        show player 10
        player_name "Emm... I don't know if I should-"
        show player 11
        show helen 30
        helen "Just tell me!"
        show helen 29
        show player 37 with dissolve
        player_name "...Yes?"
        show player 24
        show helen 41 at Position (xoffset=1)
        with dissolve
        helen "*Sigh*"
        show helen 42 at Position (xoffset=1)
        show player 11
        helen "Ever since I started attending those sessions with {b}Sister Angelica{/b}..."
        helen "...I've been having these desires and sexual urges that I never felt before!"
        helen "My body is constantly craving attention..."
        helen "...But what if my husband won't take me back?"
        show helen 33 with dissolve
        show player 12
        player_name "From what I've seen, I think {b}Harold{/b} likes you a lot, {b}Helen{/b}."
        show player 5
        show helen 34
        helen "I'm just not sure he finds me attractive anymore..."
        helen "...And I realise that I should have been more...sexual, towards my husband."
        helen "Which is why I want to change a few things."
        show helen 29
        show player 12
        player_name "Change things?"
        show player 5
        show helen 30
        helen "I want to change my looks, {b}[firstname]{/b}."
        show helen 29
        show player 10
        player_name "Oh..."
        show player 5
        show helen 30
        helen "I want him to desire me again. I have to find something...sexy!"
        show helen 29
        show player 11
        player_name "..."
        show helen 34
        helen "Do you think you could...do me a favor?"
        show helen 33
        show player 12
        player_name "A favor?"
        show player 5
        show helen 30
        helen "I need to find something sexy to wear for him..."
        show helen 29
        show player 23
        player_name "!!!"
        show player 30
        player_name "I'm not sure how I could help with that, {b}Helen{/b}. I just-"
        show player 11
        show helen 30
        helen "Just go and find me something to wear for him..."
        helen "...And I'll give you some money!!"
        show helen 29
        show player 12
        player_name "Why not go yourself? I'm sure you have a better idea of what to wear."
        show player 5
        show helen 30
        helen "There's no way I can be seen walking into a {b}sex shop{/b}."
        helen "You must help me... Please?!"
        show helen 29
        show player 10
        player_name "Uhh... What do you want me to buy?"
        show player 5
        show helen 34
        helen "I always wanted to wear a corset...and {b}Harold{/b} loves to see me in red."
        show helen 29
        show player 12
        player_name "A {b}red corset{/b}, then?"
        show player 5
        show helen 30
        helen "If you can find one, bring it back to me."
        show helen 29
        show player 10
        player_name "I'll try to..."
        show player 5
        show helen 34
        helen "Thank you, {b}[firstname]{/b}."
        hide player
        hide helen
        with dissolve
        $ pinkstore.items.append(red_corset_lingerie)
        $ ui_lock_count = 0
        $ M_mia.trigger(T_helen_caught_masturbating)

    elif M_mia.get_state() == S_mia_helen_outfit_request and red_corset in inventory.items:
        scene mia_house_helen_c
        show helen 23 at right
        show player 14 at left
        with dissolve
        player_name "Hi, {b}Helen{/b}!"
        show player 13
        show helen 24
        helen "There you are."
        helen "How's your search going?"
        show helen 23
        show player 33
        player_name "I think I found something you will like..."
        show player 239_240 with dissolve
        pause
        show player 449 with dissolve
        pause
        show player 451
        player_name "Here it is!"
        player_name "It's a sexy red corset, just as you asked."
        show player 450
        show helen 24
        helen "Wow."
        show player 13
        show helen 18
        with dissolve
        helen "This is...quite extravagant..."
        show helen 17
        show player 10
        player_name "You don't like it?"
        show player 5
        show helen 18
        helen "No, it's just that... I've never worn anything like that before."
        show helen 17
        show player 36 with dissolve
        player_name "Well, I should get going, then."
        show player 11 with dissolve
        show helen 20
        helen "Wait!"
        helen "You won't stay and give me your thoughts?"
        show helen 19
        show player 12
        player_name "Huh?"
        show player 5
        show helen 20
        helen "Let me put it on first and you can tell me if I look good in it!"
        show helen 21 with dissolve
        pause
        show helen 22 at Position (xoffset=-14) with dissolve
        pause
        show helen 35 with dissolve
        pause
        show helen 36 with dissolve
        pause
        show helen 38 with dissolve
        show player 433
        player_name "!!!"
        show helen 45 with dissolve
        pause
        show helen 46 with dissolve
        pause
        show player 11
        show helen 48 at Position (xpos=970) with dissolve
        helen "It's a little tight... But it pushes my breasts up a bit which is good..."
        show helen 49 at Position (xoffset=18) with dissolve
        helen "And what's this crack at the bottom here?!"
        show player 433
        pause
        show player 435
        player_name "Oh, that, I ehh...didn't see that when I was buying it!"
        show player 79 with dissolve
        player_name "Ha ha..."
        show player 82
        show helen 48
        with dissolve
        helen "What do YOU think?"
        show helen 47
        show player 83
        player_name "Oh, I... I think it looks great!"
        player_name "I was just really hoping it would fit you well..."
        show player 82
        show helen 48
        helen "It's fine... I think {b}Harold{/b} will definitely like this."
        helen "Thank you, {b}[firstname]{/b}."
        show helen 47
        show player 79 with dissolve
        player_name "You're welcome, {b}Helen{/b}... But I should really go now."
        player_name "See you later!"
        hide player
        hide helen
        with dissolve
        $ inventory.items.remove(red_corset)
        $ M_mia.trigger(T_helen_sexy_lingerie)

    elif M_helen.get_state() == S_helen_master_servant_fun:
        scene mia_house_helen_window0 with fade
        show expression "objects/character_helen_02.png" at Position (xpos = 211, ypos = 732)
        player_name "Woah..."
        player_name "It's kind of dark in here."
    $ callScreen(location_count)

label helen_button_dialogue:
    if M_helen.get_state() == S_helen_master_servant_fun:
        jump helen_bedroom_sex

    scene expression gTimer.image("mia_house_helen_c{}")
    if M_mia.is_set('mia route'):
        show helen 50 at right
        show player 14 at left
        with dissolve
        player_name "Hello, {b}Helen{/b}."
        show player 13
        show helen 51
        helen "Hello, {b}[firstname]{/b}."
        show helen 50
        show player 14
        player_name "How are things going lately?"
        show player 13
        show helen 51
        helen "Much better."
        helen "It feels so good knowing that I have been purified."
        helen "The church sacrament really helped improve my relationship with {b}Harold{/b}."
        show helen 24
        helen "But...no one else needs to know about that."
        show helen 50
        show player 21
        player_name "Heh... Yeah, I suppose."
        show player 29
        show xtra 21 at left
        with dissolve
        player_name "It's a bit of a blur, for me..."
        show player 13
        hide xtra 21
        with dissolve
        show helen 51
        helen "Thank you for your help again. Our family appreciates what you did...and didn't do."
        helen "I should let you go. You probably want to hang out with {b}Mia{/b}."
        show helen 50
        show player 14
        player_name "Yeah."
        show player 36 with dissolve
        player_name "I'll see you later!"
        hide player
        hide helen
        with dissolve

    elif M_helen.get_state() == S_helen_end:
        show player 13 at left
        show helen 63 at right
        with dissolve
        helen "Hello, {b}[firstname]{/b}."
        show helen 62
        show player 14
        player_name "Hi, {b}Helen{/b}."
        show player 13
        show helen 63
        helen "Have you come to purify my sinful body?"
        show helen 62
        menu:
            "Another time.":
                show player 10
                player_name "Thanks {b}Helen{/b}..."
                player_name "Maybe another time."
                show player 12
                player_name "I have...other things to do."
                show player 5
                show helen 48
                helen "Oh..."
                helen "I was really hoping to serve you..."
                helen "Don't hesitate to come visit me more often."
                show helen 47
                show player 12
                player_name "Sure... I'll let you know, {b}Helen{/b}."
                hide player
                hide helen
                with dissolve
            "Purify your body.":

                show player 26
                player_name "Yes."
                show player 13
                show helen 63
                helen "Thank the {b}Lord{/b}!"
                helen "I've been busy praying you'd return soon."
                helen "Remove your clothes and I'll let in some light."
                helen "Now lay on your back so I can let the light of {b}God{/b} shine on me."
                hide helen
                scene mia_house_helen_window1
                show player helen_sex 59
                with fade
                pause
                scene mia_house_helen_window2
                show player helen_sex 59
                pause
                scene mia_house_helen_window3
                show player helen_sex 59
                show helen 54 with dissolve
                $ M_helen.set('sex speed', .175)
                jump helen_bedroom_sex_start

    elif M_mia.is_set('helen dialogue change'):
        show helen 1 at right
        show player 10 at left
        with dissolve
        player_name "Hi, {b}Helen{/b}!"
        show player 5
        helen "..."
        show helen 3
        helen "Hi, {b}[firstname]{/b}."
        show helen 1
        show player 12
        player_name "You seem in a better mood than usual!"
        show player 5
        show helen 2
        helen "I'm trying to be...open minded...even with individuals such as yourself."
        show helen 1
        show player 14
        player_name "That's nice."
        show player 13
        show helen 2
        helen "What is it you want?"
        show helen 1
        menu:
            "{b}Harold{/b}." if not M_mia.get_state() == S_mia_clues:
                show player 10
                player_name "Have you spoken to {b}Harold{/b}?"
                show player 11
                show helen 4
                helen "No..."
                show helen 3
                helen "...Everything is in the hands of {b}God{/b}."
                show helen 1
                show player 12
                player_name "Huh?"
                show player 5
                show helen 4
                helen "You should leave now..."
                hide player
                hide helen
                with dissolve

            "{b}Harold{/b}." if M_mia.get_state() == S_mia_clues:
                show player 10
                player_name "Where did you say I could find clues about {b}Harold's{/b} whereabouts?"
                show player 5
                show helen 24 with dissolve
                helen "Start by questioning his coworkers at the {b}police station{/b}..."
                helen "...And look for {b}clues{/b} around his workplace."
                show helen 23
                show player 12
                player_name "I suppose I can ask around to see where he could be..."
                show player 5
                show helen 24
                helen "Thank you..."
                hide player
                hide helen
                with dissolve

            "Corset." if M_mia.get_state() == S_mia_helen_outfit_request:
                show player 10
                player_name "What kind of lingerie were you looking for again?"
                show player 5
                show helen 28
                helen "I always wanted to wear a corset...and {b}Harold{/b} loves to see me in red."
                show helen 23
                show player 12
                player_name "A {b}red corset{/b}, then?"
                show player 5
                show helen 24
                helen "If you can find one, bring it back to me."
                show helen 23
                show player 10
                player_name "I'll try to..."
                show player 5
                show helen 28
                helen "Thank you, {b}[firstname]{/b}."
                hide player
                hide helen
                with dissolve

            "Angelica." if M_mia.is_set('helen angelica training'):
                show player 10
                player_name "How's the sacrament going?"
                player_name "Are you and {b}Sister Angelica{/b} making any progress?"
                show player 5
                show helen 27
                helen "..."
                show helen 24
                helen "I... I think we're doing fine..."
                show helen 28
                helen "...{b}Sister Angelica{/b} is very...thorough and more knowledgeable than I."
                show helen 23
                show player 10
                player_name "I see..."
                player_name "Well, let me know if you guys need my help!"
                hide player
                hide helen
                with dissolve

            "Whipping." if M_mia.get_state() == S_mia_helen_condition:
                show player 10
                player_name "Are you alright? I still cant believe I watched you get whipped by {b}Sister Angelica{/b}."
                show player 5
                show helen 25
                helen "..."
                show helen 28
                helen "I'm a little sore, but..."
                show helen 24
                helen "...I'm a sinner {b}[firstname]{/b}. I...I need this."
                show helen 28
                helen "If it helps rid me of my sinfulness, I must do it."
                show helen 27
                show player 37 with dissolve
                player_name "..."
                show player 10 with dissolve
                player_name "Alright, I guess."
                player_name "If you need help or want out let me know."
                player_name "I'll do everything I can to help you."
                show player 5
                show helen 24
                helen "Thanks, {b}[firstname]{/b}. You are so helpful."
                helen "{b}Sister Angelica{/b} is helping me to see that it is my sinfullness that has led to all my problems in life."
                helen "I need to complete this training and maybe I'll be as helpful and as nice...as you."
                show helen 27
                show player 37 with dissolve
                player_name "{b}Helen{/b}..."
                show helen 23
                show player 10 with dissolve
                player_name "I don't think you're bad."
                show player 5
                show helen 28
                helen "Thanks, {b}[firstname]{/b}."
                hide player
                hide helen
                with dissolve
                $ M_mia.trigger(T_helen_thanks)

            "Ritual." if M_mia.get_state() == S_mia_find_sinners:
                show player 10
                player_name "You know... I've been spending more time at church lately..."
                show player 5
                show helen 2
                helen "...You have?"
                show helen 1
                show player 14
                player_name "Yeah!"
                show player 10
                player_name "I'm trying to learn more...you know...about {b}God{/b} and stuff!"
                show player 5
                show helen 2
                helen "Hmm... Really?"
                show helen 1
                show player 12
                player_name "Did you know that, err...there's a late night sacrament?"
                show player 5
                show helen 4
                helen "Night services?"
                show helen 1
                show player 10
                player_name "Yeah! They're like...rituals?"
                show player 5
                show helen 4
                helen "I was never aware of such a thing and I've been attending our church for over 20 years."
                show helen 2
                helen "How come I never heard of such a...sacrament?"
                show helen 1

                menu:
                    "I don't know." if pStats.chr() < 5:
                        show player 10
                        player_name "[chr_warn]I'm not sure I, emm... I can't really explain..."
                        show player 5
                        show helen 4
                        helen "[chr_warn]Sounds like this thing isn't very serious..."
                        show helen 1
                        show player 24
                        player_name "[chr_warn]..."
                        show player 25
                        player_name "[chr_warn]Well I haven't gone yet either, so I don't know much about what it involves."
                        show player 24
                        show helen 4
                        helen "[chr_warn]I'm not sure I quite understand the purpose of this all..."
                        show helen 2
                        helen "[chr_warn]...But good luck with your volunteer work and let me know when you have more details."
                        show helen 1
                        show player 25
                        player_name "[chr_warn]Oh... Okay."
                        hide player
                        hide helen
                        with dissolve

                    "Ancient sacrament." if pStats.chr() >= 5:
                        show player 12
                        player_name "{b}Sister Angelica{/b} is in charge!"
                        player_name "She said I should spread the word and find...ehh...faithful followers to join us!"
                        show player 14
                        player_name "I know you're extremely devout..."
                        show player 33
                        player_name "And with 20 years at the church, I'm surprised you never attended evening sacraments. Maybe i-"
                        show helen 4
                        helen "Hold on."
                        show helen 1
                        show player 13
                        player_name "..."
                        show helen 4
                        helen "You're attending this?"
                        show helen 1
                        show player 14
                        player_name "Let's just say that emm... I like to do volunteer work for the church!"
                        show player 13
                        show helen 2
                        helen "I have to say I'm pleasantly suprised by your devotion towards our church..."
                        show helen 4
                        helen "...I'm just not sure I quite understand the purpose of it all."
                        show helen 1
                        show player 14
                        player_name "{b}Sister Angelica{/b} seems to think this is a great way to absolve sins and purify the soul..."
                        show player 13
                        show helen 3
                        helen "Hmm..."
                        show helen 2
                        helen "It's at night you say?"
                        show helen 1
                        show player 14
                        player_name "Yes, Ma'am! It's ehh...in the nun chamber!"
                        show player 13
                        show helen 3
                        helen "Okay, you convinced me."
                        show helen 2
                        helen "I'll go with you to visit {b}Sister Angelica{/b} at night and see what this is all about..."
                        show helen 1
                        show player 14
                        player_name "That sounds great!"
                        hide player
                        hide helen
                        with dissolve
                        $ M_mia.trigger(T_helen_secret_sacrement)

    elif M_mia.is_set('helen button'):
        show helen 1 at right
        show player 10 at left
        with dissolve
        player_name "Hi, {b}Helen{/b}!"
        show player 5
        show helen 4
        helen "You again."
        helen "What is it you want?!"
        show helen 1
        menu helen_dialogue:
            "{b}Harold{/b}.":
                show player 10
                player_name "Have you spoken to {b}Harold{/b}?"
                show player 11
                show helen 5
                helen "Our situation is none of your business."
                show helen 4
                helen "Besides, there's nothing we can do at the moment..."
                show helen 3
                helen "...everything is in the hands of {b}God{/b}!"
                show helen 1
                show player 12
                player_name "Huh?"
                show player 5
                show helen 4
                helen "You should leave now..."
                hide player
                hide helen
                with dissolve
    else:

        show player 5 at left
        show helen 2 at right
        with dissolve
        helen "!!!"
        show helen 4
        helen "What are you doing here?!"
        show player 22
        helen "This is my bedroom! Get out!!"
        show helen 6
        show player 10
        player_name "Sorry!"
        hide player
        hide helen
        with dissolve
    $ callScreen(location_count)

label helens_mary_statue:
    scene mia_house_statue
    show key3 at Position (xpos=450,ypos=450):
        rotate -45
    player_name "There's a golden key on this rosery... Could it be the one to unlock that room?"
    player_name "I could try it..."
    show unlock52 at truecenter with dissolve
    $ inventory.items.append(key03)
    pause
    hide unlock52 with dissolve
    $ M_mia.trigger(T_mia_key_found)
    $ callScreen(location_count)

label helen_bedroom_sex:
    scene mia_house_helen_closed_c with fade
    show player 5 at left
    show helen 63 at right
    with dissolve
    helen "Hello, {b}[firstname]{/b}."
    helen "I'm glad to see you've come."
    helen "Now I can finally serve you, {b}Master{/b}."
    show helen 62
    show player 11
    player_name "..."
    show helen 63
    helen "Did you close the door behind you?"
    show helen 62
    show player 12
    player_name "No, I didn't."
    show player 11
    show helen 63
    helen "Good. I don't mind if someone comes in and sees us...together."
    show helen 62
    show player 10
    player_name "Umm... But...what about {b}Mia{/b}?"
    player_name "Don't you think she'd be...upset?"
    show player 5
    show helen 63
    helen "Don't worry about chasing after young girls like her."
    helen "Helping me exorcise my sins is a greater deed."
    show helen 62
    show player 11
    player_name "..."
    show helen 63
    helen "Do you like my attire? Does it please you?"
    show helen 62
    show player 10
    player_name "I... I think you are pretty with or without that outfit."
    show player 5
    show helen 49 with dissolve
    helen "Oh? Would you prefer I be fully naked?"
    pause
    show helen 62 with dissolve
    show player 23
    player_name "!!!"
    show player 37 with dissolve
    player_name "No, {b}Helen{/b}! I mean...yes, but..."
    show player 29 with dissolve
    player_name "I meant you look good naked too."
    show player 3
    show helen 63
    helen "Hee Hee... I'll always wear this outfit for you then."
    helen "You know that...I'm here to serve you, {b}Master{/b}."
    show helen 62
    show player 29
    player_name "Heh...Heh... You really don't have to, {b}Helen{/b}."
    show player 5 with dissolve
    show helen 63
    helen "Oh, but I must!"
    helen "{b}Sister Angelica{/b} said that your seed is the only way to stay pure."
    helen "My sinful body needs to be cleansed by your holy seed."
    helen "Therefore, I offer you my body and will use it to grant any wish of yours."
    show helen 62
    show player 11
    player_name "..."
    menu:
        "Another time.":
            show player 10
            player_name "Thanks {b}Helen{/b}..."
            player_name "Maybe another time."
            show player 12
            show helen 47
            player_name "I have...other things to do."
            show player 5
            show helen 48
            helen "Oh..."
            helen "I was really hoping to serve you..."
            helen "Don't hesitate to come visit me more often."
            show helen 47
            show player 12
            player_name "Sure... I'll let you know, {b}Helen{/b}."
            hide player
            hide helen
            with dissolve
        "I want to.":

            show player 14
            player_name "Sure... I'd like to try..."
            show player 13
            show helen 63
            helen "Great!"
            helen "Before we start, why don't you remove your clothes and I'll let in some light."
            show helen 62
            show player 10
            player_name "Huh? Let in some light?"
            show player 5
            show helen 63
            helen "Don't worry, {b}[firstname]{/b}."
            helen "Just get naked and sit at the foot of the bed."
            helen "I won't take long."
            show helen 62
            show player 10
            player_name "Okay..."
            hide helen
            hide player
            with dissolve

            scene mia_house_helen_window1
            show player helen_sex 52
            with fade
            helen "I've hidden my sinful desires for too long."
            helen "I'm not going to hide anymore."
            scene mia_house_helen_window2
            show player helen_sex 52
            helen "I want {b}God{/b} and all the neighbors to see me for what I am."
            scene mia_house_helen_window3
            show player helen_sex 52
            show helen 54 with dissolve
            helen "A sinful woman trying her best to follow the church's teachings."
            show helen 53
            player_name "!!!"
            player_name "Are you sure that's such a good idea?"
            show helen 54
            helen "You worry too much, {b}[firstname]{/b}."
            helen "There is nothing shameful about our bodies..."
            helen "...Now lay on your back, so I can let the light of {b}God{/b} shine on me."
            show helen 53
            player_name "Alright."
            show player helen_sex 59 with dissolve
            show helen 54

            label helen_bedroom_sex_start:
                helen "Before we commence this sacred ritual, would you like me to be naked?"
                show helen 53
                menu:
                    "Keep the corset.":
                        $ M_helen.set('corset lingerie', True)
                    "Get naked.":

                        $ M_helen.set('corset lingerie', False)

                show helen 54
                helen "Anything for you, {b}Master{/b}."
                if M_helen.is_set('corset lingerie'):
                    show helen 54
                else:

                    show helen 55 with dissolve
                    pause
                    show helen 56 with dissolve
                    pause
                    show helen 58 with dissolve
                helen "Be a good boy now and let me insert your holy rod."
                helen "Don't hold back either."
                helen "I want you to release every last drop of your holy seed inside me."
                hide player
                if M_helen.is_set('corset lingerie'):
                    show helen 61
                else:

                    show helen 60
                with dissolve
                if not M_helen.get_state() == S_helen_master_servant_fun:
                    helen "Oh my..."
                    helen "Your...cock..."
                    helen "I didn't get to see it last time."
                    helen "The {b}Lord{/b} has truly blessed you."
                else:

                    pause

                scene mia_house_helen_bed1 with fade
                hide helen
                show helens 22
                if M_helen.is_set('corset lingerie'):
                    show h_corset 22b
                with dissolve
                if M_helen.get_state() == S_helen_master_servant_fun:
                    helen "I'm still amazed at the size of your cock."
                    helen "{b}God{/b} truly blessed you."
                helen "Be gentle with me...at first."
                pause
                show helens 23
                if M_helen.is_set('corset lingerie'):
                    show h_corset 23b
                with dissolve
                helen "Ohhh!!! [firstname]!"
                helen "Not so deep yet!"
                helen "I'm still not used to how big your holy cock is."
                helen "But I love it..."
                $ anim_toggle = True
                $ xray = False

                label helen_bedroom_sex_loop:
                    hide screen helen_bedroom_sex_options
                    show screen xray_scr
                    pause
                    hide screen xray_scr
                    if anim_toggle and M_helen.is_set('corset lingerie'):
                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 23_24_25_26_27
                            show h_corset 23_24_25_26_27
                            pause 4
                            if animcounter == 1:
                                helen "Ahhhh!!!{p=1}{nw}"

                            if animcounter == 3:
                                helen "{b}[firstname]{/b}!!!{p=1}{nw}"
                                player_name "Uhhh...{p=1}{nw}"

                            pause 3
                            $ animcounter += 1

                    elif anim_toggle and not M_helen.is_set('corset lingerie'):
                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 23_24_25_26_27
                            pause 4
                            if animcounter == 1:
                                helen "Ahhhh!!!{p=1}{nw}"

                            if animcounter == 3:
                                helen "{b}[firstname]{/b}!!!{p=1}{nw}"
                                player_name "Uhhh...{p=1}{nw}"

                            pause 3 
                            $ animcounter += 1

                    elif not anim_toggle and M_helen.is_set('corset lingerie'):
                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 23
                            show h_corset 23b
                            pause
                            show helens 24
                            show h_corset 24b
                            pause
                            show helens 25
                            show h_corset 25b
                            pause
                            show helens 26
                            show h_corset 26b
                            pause
                            show helens 27
                            show h_corset 27b
                            pause
                            $ animcounter += 1
                            if animcounter == 2:
                                helen "Ahhhh!!!"

                            if animcounter == 3:
                                helen "{b}[firstname]{/b}!!!"
                                player_name "Uhhh..."
                    else:

                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 23
                            pause
                            show helens 24
                            pause
                            show helens 25
                            pause
                            show helens 26
                            pause
                            show helens 27
                            pause
                            $ animcounter += 1
                            if animcounter == 2:
                                helen "Ahhhh!!!"

                            if animcounter == 3:
                                helen "{b}[firstname]{/b}!!!"
                                player_name "Uhhh..."

                helen "I'm...almost..."

                show screen helen_bedroom_sex_options
                pause
                jump helen_bedroom_sex_loop

                label helen_bedroom_sex_cum:
                    hide screen helen_bedroom_sex_options
                    helen "Cum hard for me {b}[firstname]{/b}! Bury your cock deep in me!"
                    show helens 28
                    if M_helen.is_set('corset lingerie'):
                        show h_corset 28b
                    with flash
                    player_name "UHHH!!!"
                    helen "OHHHH!!!"
                    show helens 29
                    if M_helen.is_set('corset lingerie'):
                        show h_corset 29b
                    with dissolve
                    pause
                    helen "I felt your holy seed pouring into me..."
                    show helens 30
                    if M_helen.is_set('corset lingerie'):
                        show h_corset 30b
                    with dissolve
                    pause
                    show helens 31
                    if M_helen.is_set('corset lingerie'):
                        show h_corset 31b
                    with dissolve
                    pause
                    show helens 32
                    if M_helen.is_set('corset lingerie'):
                        show h_corset 32b
                    with dissolve
                    pause
                    helen "Thank you, {b}Master{/b}."
                    scene black with fade
                    hide helens
                    hide h_corset
                    pause

                scene mia_house_helen_c with fade
                show player 13 at left
                if M_helen.is_set('corset lingerie'):
                    show helen 63 at right
                else:

                    show helen 65 at right
                with dissolve
                helen "I must confess, {b}Master{/b}."
                helen "I was waiting for you all day."
                helen "I'm glad you choose to cleanse me..."
                if M_helen.is_set('corset lingerie'):
                    show helen 62
                else:

                    show helen 64
                show player 26
                player_name "Yeah... I really enjoyed doing...it...with you."
                show player 13
                if M_helen.is_set('corset lingerie'):
                    show helen 63
                else:

                    show helen 65
                helen "Will you be back soon?"
                if M_helen.is_set('corset lingerie'):
                    show helen 62
                else:

                    show helen 64
                show player 10
                player_name "Maybe..."
                show player 35
                player_name "Depends if I don't have a lot of school work..."
                if not M_helen.get_state() == S_helen_master_servant_fun:
                    $ gTimer.tick()
                    show player 29 with dissolve
                    player_name "...But could you please do me a favor and not mention what we did here?"
                    player_name "I would rather not let {b}Mia{/b} know about this."
                    show player 13 with dissolve
                    if M_helen.is_set('corset lingerie'):
                        show helen 63
                    else:

                        show helen 65
                    helen "Don't worry about my daughter. She'll understand."
                    if M_helen.is_set('corset lingerie'):
                        show helen 62
                    else:

                        show helen 64
                    show player 11
                    player_name "..."
                else:

                    $ location_count = "Mia's House Upstairs"
                    $ ui_lock_count = 1
                    show player 13
                if M_helen.is_set('corset lingerie'):
                    show helen 63
                else:

                    show helen 65
                helen "Don't make your servant wait too long."
                helen "My body will be eagerly awaiting your return."
                if M_helen.is_set('corset lingerie'):
                    show helen 62
                else:

                    show helen 64
                show player 10
                player_name "Okay."
                show player 36 with dissolve
                player_name "Well, I better get going."
                show player 13 with dissolve
                if M_helen.is_set('corset lingerie'):
                    show helen 63
                else:

                    show helen 65
                helen "Goodbye, {b}Master{/b}."
                helen "Thank you for the gift of your holy seed."
                $ M_helen.trigger(T_helen_master_servant_sex)
                hide player
                hide helen
                with dissolve
$ callScreen(location_count)

label helen_bedroom_faster_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') - 0.05)
    jump helen_bedroom_sex_loop

label helen_bedroom_slower_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') + 0.05)
    jump helen_bedroom_sex_loop