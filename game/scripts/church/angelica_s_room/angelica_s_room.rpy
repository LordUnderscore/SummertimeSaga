label church_angelicas_room_dialogue:
    $ location_count = "Angelica's Room"
    if M_mia.get_state() == S_mia_church_plan and gTimer.is_weekend() and gTimer.is_morning():
        scene church_nun_b
        show player 12 with dissolve
        player_name "( This looks like the right place. )"
        show player 30
        player_name "( There must be something I can wear in here... )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_nun_b
        show player 14f at Position (xoffset=1)
        show players robe f
        with dissolve
        player_name "That went better than I exp-"
        show player 14f at Position (xpos=182)
        show players robe f at left
        show ang 2 at right
        with fastdissolve
        ang "There you are!"
        show ang 1
        show player 23 at Position (xpos=180)
        show players robe
        with fastdissolve
        player_name "!!!" with hpunch
        show player 10
        player_name "Oh, sorry!"
        player_name "I didn't mean to-"
        show player 11
        show ang 2
        ang "Stop."
        show ang 1
        show player 22
        player_name "..."
        show ang 2
        ang "I've been watching you this whole time."
        ang "Stealing the priest's robe... Impersonating our priest in the confessional..."
        ang "...And lying to that poor woman."
        show ang 1
        show player 10
        player_name "It's not what you think!"
        player_name "I was just trying to help her..."
        show player 11
        show ang 2
        ang "Help?"
        ang "The only person you can help now is yourself..."
        ang "...Because I'm thinking about reporting you to the authorities."
        show ang 1
        show player 22
        player_name "!!!"
        show ang 2
        ang "Unless... you do something for me."
        show ang 1
        show player 11
        player_name "..."
        show player 12
        player_name "I don't see how I can be of any hel-"
        show player 11
        show ang 2
        ang "Come visit me in a week."
        ang "I'll explain what I need from you..."
        ang "...And don't try hiding from me, or everyone will know what you did..."
        ang "...Especially, that lady. The one I saw you with!"
        show ang 1
        show player 10
        player_name "Please don't say anything to her... I'll be back. I promise."
        show player 11
        show ang 2
        ang "Good."
        ang "Now return what you stole and leave my chambers..."
        show ang 1
        hide players robe
        show player 444 at left
        with dissolve
        player_name "..."
        hide player
        hide ang
        with dissolve
        $ gTimer.tick()
        $ M_mia.trigger(T_mia_priest_outfit)

    elif M_mia.get_state() == S_mia_church_night_visit and gTimer.is_dark():
        scene church_nun_n_c
        show ang 1 at right
        show player 10 at left
        with dissolve
        player_name "Hi, {b}Sister Angelica{/b}..."
        show player 5
        show ang 2
        ang "I knew I could count on you."
        ang "You value our mutual agreement... and you value secrets."
        ang "This is why I trust you will help me..."
        show ang 1
        show player 12
        player_name "So, what exactly are we talking about here?"
        show player 5
        show ang 2
        ang "I perform a private sacrament at night... in my chambers..."
        show player 11
        ang "Its purpose is to help members of our church struggling with their impurities..."
        ang "...I help them purge away their sins!"
        show ang 1
        show player 10
        player_name "Sinners?"
        show player 11
        show ang 2
        ang "That's right!"
        ang "But in order to keep performing this sacrament, I need to find appropriate candidates..."
        ang "...Freshly picked from our local worshippers!"
        show ang 1
        show player 10
        player_name "Okay, but what am I supposed to do?"
        show player 11
        show ang 2
        ang "I just need you to find some!"
        show ang 1
        show player 10
        player_name "You need me to find people?!"
        show player 11
        show ang 2
        ang "Yes, sinners."
        show ang 1
        show player 37 with dissolve
        player_name "..."
        show player 38 with dissolve
        player_name "But, I don't really know anyone like that... I don't even-"
        show player 3 with dissolve
        show ang 2
        ang "You DO know someone!"
        show ang 1
        show player 12 with dissolve
        player_name "... But, who?!"
        show player 11
        show ang 2
        ang "The lady from the confessional."
        ang "Her name is {b}Helen{/b}."
        ang "She has always been a devout servant of our {b}Lord{/b}."
        ang "She believes herself to be very righteous and would never agree to my... ritual."
        ang "But she had such a look of shame after talking with you in the confessional."
        ang "You know her secret sins."
        ang "And you will bring her to me."
        ang "I personally enjoy purging the sins of the truly faithful."
        ang "It is one of the most... satisfying... experiences of our religion."
        show ang 1
        show player 22
        player_name "!!!"
        show player 10
        player_name "You want me to bring {b}Helen{/b} here?!"
        show player 11
        show ang 2
        ang "In my chambers, at night."
        show ang 1
        show player 12
        player_name "How can I possibly convince her to come here?! I don't see how..."
        show player 11
        show ang 2
        ang "I'm sure you will find a way."
        ang "Both our interests are on the line here..."
        show ang 1
        show player 24
        player_name "{b}*Sigh*{/b}"
        show player 12
        player_name "Okay, I'll give it a try... but what's this sacrament about anyway?"
        show player 5
        show ang 2
        ang "You will find out, in due time."
        show ang 1
        show player 10
        player_name "I... I should really get going. It's getting late."
        show player 5
        show ang 2
        ang "Of course! Just make sure you remember our agreement."
        hide ang with dissolve
        show player 24
        player_name "..."
        hide player with dissolve
        $ M_mia.trigger(T_angelica_ritual_deal)

    elif M_mia.get_state() == S_mia_church_sacrement and gTimer.is_dark():
        scene church_nun_n_c
        show player 5f at right
        show helen 23 at Position (xpos=575)
        show ang 2f at left
        with dissolve
        ang "Thank you, {b}[firstname]{/b}, for bringing this wonderful disciple to us!"
        ang "{b}Helen{/b} has been attending our church for a very long time..."
        ang "...And she told me everything about her failing marriage."
        show ang 1f
        show helen 24
        helen "I... I'm just hoping this will help me deal with our ungodly ways..."
        show helen 23
        show ang 2f
        ang "Indeed, {b}Helen{/b}."
        ang "I'm proud of you for willing to face your demons."
        ang "Are you willing to follow my commands, in order to find the light?"
        show ang 1f
        show helen 24
        helen "Yes. I am..."
        show helen 23
        show ang 2f
        ang "Good! There will be three levels towards your redemption."
        ang "The first step requires that you rid yourself of all earthly materials..."
        show player 11f
        ang "...Such as {b}your clothes{/b}."
        ang "Only then, will we be able to start the process of purging your sins!"
        show ang 1f
        show helen 4 at Position (xoffset=2) with dissolve
        helen "You don't actually expect me to... Get undressed here?!"
        show helen 1 at Position (xoffset=2)
        show ang 2f
        ang "We are {b}God's{/b} creatures, {b}Helen{/b}... We are all equal!"
        ang "You shouldn't be ashamed of who you are..."
        show ang 1f
        show helen 25 with dissolve
        helen "..."
        show helen 23
        show ang 2f
        ang "Go on, {b}Helen{/b}. Rid yourself of it all..."
        show ang 1f
        show helen 27
        pause
        show helen 28
        helen "If this is what I must do, then I shall do it..."
        show player 106f
        show helen 21 with dissolve
        pause
        show player 11f
        show helen 22 at Position (xoffset=-13) with dissolve
        pause
        show helen 33 with dissolve
        show player 23f
        player_name "!!!"
        show ang 2f
        show helen 29
        ang "Well done, {b}Helen{/b}."
        show ang 1f
        show helen 33
        helen "..."
        show ang 2f
        show helen 29
        ang "{b}[firstname]{/b}?"
        show ang 1f
        show helen 31
        show player 21f
        player_name "Ehh... Yes?"
        show player 5f
        show ang 2f
        show helen 29
        ang "You can leave us now, I won't be needing your help for tonight."
        ang "Come back another time so we can continue our sessions..."
        show ang 1f
        show player 10f
        player_name "Oh, okay."
        player_name "Good night, then!"
        hide player
        hide helen
        hide ang
        with dissolve
        $ gTimer.tick()
        $ M_mia.trigger(T_helen_angelica_ritual)
        $ location_count = "Town Map"

    elif M_mia.get_state() == S_mia_angelicas_order and gTimer.is_dark():
        scene church_nun_n_c with fade
        show player 23f at right
        show helen 29 at Position (xpos=575)
        show ang 5f at left
        with dissolve
        player_name "!!!"
        show ang 6f
        ang "What is the matter, {b}[firstname]{/b}?"
        show ang 7f with dissolve
        pause
        show ang 8f
        ang "You're not having any sinful thoughts are you?"
        show player 22f
        ang "Maybe you should take {b}Helen's{/b} place-"
        show ang 7f
        show player 10f
        player_name "No! I'm... I'm just surprised to see you aren't wearing your robe!"
        show player 11f
        ang "..."
        show ang 9 with dissolve
        ang "I was just illustrating to {b}Helen{/b} how {b}God{/b} blesses his chosen few who are truly holy and devout inwardly and outwardly."
        ang "As you can see... He has showered me with a truly sacred body..."
        show ang 10
        pause
        show ang 9
        ang "Right, {b}Helen{/b}?"
        show ang 10
        show helen 34
        helen "...Yes, your body... is a temple to our {b}Lord{/b}."
        show helen 33
        show ang 8f with dissolve
        ang "In addition, from this point forward the purification sacrament requires me to lay my hands on the repentant filthy sinner."
        ang "I prefer not to get my clothes dirty..."
        show ang 6f with dissolve
        ang "Now then, if there is nothing else, I must get back to my instruction with {b}Helen{/b}."
        show ang 9 with dissolve
        ang "And if I see any sinful desires appearing in your nether regions, I won't be slow to bring about {b}God's{/b} judgement on you..."
        show ang 11
        show player 22f
        player_name "!!!"
        show ang 9
        ang "Understood?"
        show ang 10
        show player 138f at Position (xoffset=-16) with dissolve
        player_name "Y... Ye... Yes... {b}Sister Angelica{/b}."
        hide player
        hide ang
        hide helen
        with dissolve
        $ M_mia.trigger(T_angelica_sinful_thoughts)

    elif M_mia.get_state() == S_mia_angelicas_final_request and strapon in inventory.items and gTimer.is_dark():
        $ location_count = "Church Stairs"
        $ callScreen("Route Warning", False, False)
        $ location_count = "Angelica's Room"
        jump helen_final_sacrament
    $ callScreen(location_count)

label priest_outfit:
    scene church_nun_b
    show player 444f with dissolve
    player_name "..."
    player_name "( This thing is heavy! )"
    show player 106f at Position (xoffset=1)
    show players robe f
    with dissolve
    player_name "Hmm..."
    show player 33f at Position (xoffset=1)
    player_name "( Looks like this could actually work. )"
    show player 14f at Position (xoffset=1)
    player_name "( Let's see if I can get close to {b}Helen{/b}... )"
    hide player
    hide players robe
    with dissolve
    $ lock_ui()
    $ M_mia.trigger(T_mia_priest_outfit)
    $ callScreen(location_count)

label angelicas_room_dialogue:
    if M_helen.is_set('helen route'):
        jump angelica_room_new_dialogue

    elif M_mia.is_set('mia route'):
        scene church_nun_n_c with fade
        show ang 2f at left
        show player 5f at right
        with dissolve
        ang "What are you doing here?"
        show ang 1f
        show player 10f
        player_name "Are you still performing the purification sacrament?"
        show player 5f
        show ang 2f
        ang "I can, but I don't have any other sinners at the moment..."
        ang "{b}Helen{/b} doesn't visit me anymore."
        ang "She is probably having her sins purged by her husband as we speak."
        show ang 1f
        show player 12f
        player_name "Are you alright?"
        player_name "You seem sad."
        show player 5f
        show ang 2f
        ang "I'm fine. I've no need for you services anymore."
        ang "Leave me."
        show ang 1f
        show player 10f
        player_name "Okay."
        hide player
        hide ang
        with dissolve

    elif M_mia.get_state() == S_mia_harolds_thoughts:
        scene church_nun_n_c
        show player 12 with dissolve
        player_name "( I should talk with {b}Harold{/b} before I see {b}Sister Angelica{/b}. )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_find_sinners:
        scene church_nun_n_c
        show ang 1 at right
        show player 12 at left
        with dissolve
        player_name "Hi, {b}Sister Angelica{/b}..."
        show player 5
        show ang 2
        ang "...Yes?"
        ang "What is it you want?"
        show ang 1
        menu:
            "Find sinners.":
                show player 12
                player_name "What do you need me to do for you again?"
                show player 5
                show ang 2
                ang "I need you to find appropriate candidates for my sacrament."
                ang "Bring me {b}Helen{/b}, the woman from the confessional, so we can begin our meetings..."
                show ang 1
                show player 12
                player_name "Oh, right... You want me to convince her."
                player_name "All right. I'll see what I can do..."
                hide player
                hide ang
                with dissolve

    elif M_mia.get_state() == S_mia_angelicas_whip:
        scene church_nun_n_c with fade
        show player 5f at right
        show helen 29 at Position (xpos=575)
        show ang 5f at left
        with dissolve
        menu:
            "The Whip.":
                if whip in inventory.items:
                    $ inventory.items.remove(whip)
                    jump helen_sacrement_training_part2
                show ang 6f
                ang "Did you bring me my {b}whip{/b} for the flagellation ritual in my three step purification sacrament?"
                show ang 5f
                show player 10f
                player_name "No..."
                show player 5f
                show ang 6f
                ang "Then why are you here?"
                show ang 5f
                show player 12f
                player_name "Where did you say I could find one?"
                show player 5f
                show ang 6f
                ang "I'm sure someone of your age knows of dirty lustful places that sell such things."
                ang "Now stop testing my patience, and bring me a whip."
                hide ang
                hide helen
                with dissolve
                show player 10f
                player_name "( Maybe the {b}Pink store at the mall{/b} carries something like that. )"
                hide player with dissolve
            "Nothing.":

                show player 10f
                player_name "Nothing."
                show player 5f
                show ang 6f
                ang "Leave then. I'm busy right now."
                ang "I'll visit you when I require your assistance."
                hide player
                hide ang
                hide helen
                with dissolve
    else:

        scene church_nun_n_c with fade
        show player 10f at right
        show helen 37 at Position (xpos=575)
        show ang 5f at left
        with dissolve
        player_name "Hi, {b}Sister Angelica{/b}..."
        show player 5f
        show ang 6f
        ang "...Yes?"
        ang "What is it you want?"
        show ang 5f
        menu:
            "Strap on." if M_mia.get_state() in [S_mia_harolds_thoughts, S_mia_angelicas_final_request] and strapon not in inventory.items:
                show player 460f at Position (xoffset=-1) with dissolve
                player_name "Am I right in assuming you meant to hand me this photograph?"
                show player 461f at Position (xoffset=-1)
                show ang 9 with dissolve
                ang "Yes."
                ang "I don't make mistakes."
                ang "Now hurry up and go get it!"
                hide ang
                hide helen
                with dissolve
                show player 5f with dissolve
                player_name "..."
                show player 10f
                player_name "( I guess my last task is to get her a {b}strap on{/b}. )"
                player_name "( Only one place that would sell something like that is {b}Pink{/b}... )"
                hide player with dissolve
            "Nothing.":

                show player 10f
                player_name "Nothing."
                show player 5f
                show ang 6f
                ang "Leave then. I'm busy right now."
                ang "I'll visit you when I require your assistance."
                hide player
                hide ang
                hide helen
                with dissolve
    $ callScreen(location_count)

label helen_sacrement_training_part2:
    scene church_nun_n_c with fade
    show helen 29 at Position (xpos=575)
    show player 5f at right
    show ang 6f at left
    with dissolve
    ang "Well?"
    ang "Have you brought what I need?"
    show ang 5f
    show player 12f
    player_name "Yes, I think I found something."
    show player 239_240f with dissolve
    pause
    show player 455f
    player_name "Will this work?"
    show player 456f
    ang "Hmm..."
    hide helen
    show helen 29 at Position (xpos=575)
    show player 5f
    show ang 18f
    with dissolve
    ang "I'm impressed."
    ang "You seem to have a great eye for biblical accuracy."
    show ang 17f
    show helen 30
    helen "What are you going to do with that whip?"
    show helen 29
    show ang 18f
    ang "Quiet."
    show helen 33
    show ang 17f
    show player 10f
    player_name "Well I'd better get home. It's getting late."
    show player 11f
    show ang 18f
    ang "Hold. I want you to stay for this next step in {b}Helen's{/b} purification."
    ang "{b}Helen{/b} told me you saw her defiling her body the other day."
    ang "It appears she is pulling you into her wickedly sinful ways."
    show ang 17f
    show helen 32
    helen "I'm sorry, {b}[firstname]{/b} I-"
    show helen 33
    show ang 18f
    ang "Quiet!"
    show ang 17f
    pause
    show ang 18f
    ang "As you can see: {b}Helen{/b} is still questioning my methods."
    ang "I want you to witness her punishment..."
    ang "...And see how I prefer to expunge all her vile deeds from her body."
    show ang 17f
    show helen 30
    helen "!!!"
    show player 22f
    player_name "!!!"
    helen "Isn't that going to hurt? I think-"
    show helen 29
    show ang 18f
    ang "{b}Helen{/b}, rejoice! Today begins the 2nd ritual of the purification sacrament!"
    ang "This will hurt, but pain is a product of sin."
    ang "Once you are able to tolerate pain you will be closer to holy redemption."
    ang "Now. I want you to rid yourself of all your clothing."
    show ang 17f
    show helen 33
    helen "..."
    show helen 30
    helen "But, {b}[firstname]{/b} is here... Is it appropriate?"
    show helen 29
    show ang 18f
    ang "{b}Helen{/b}. I'm not asking you to start masturbating in front of him as you were earlier."
    ang "Besides, your old sin riddled body shouldn't stir any response out of a male."
    show ang 17f
    show helen 33
    helen "..."
    show ang 18f
    ang "Remember, you came to me looking for a way to forgiveness and to make your body holy."
    show ang 17f
    show helen 34
    helen "A... All right. If it will at least make me right in {b}God's{/b} eyes."
    show helen 35 at Position (xoffset=12) with dissolve
    pause
    show player 106f
    show helen 36 with dissolve
    pause
    show player 11f
    show helen 38 with dissolve
    show ang 12 at left with dissolve
    ang "Good. Now come over here."
    show helen 37 at Position (xpos=464) with dissolve
    show ang 13 with dissolve
    pause
    show ang 14 with dissolve
    ang "I'm restraining you {b}Helen{/b} as your sinful impulse will be to cover yourself."
    hide helen
    show ang 15
    with dissolve
    ang "As I work your body over with this whip you will learn to remember what awaits you in hell if you dont submit to my... {b}God's{/b} will."
    helen "What?"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312)
    hide player
    with dissolve
    ang "QUIET! Stop questioning me!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    helen "Owwww!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Repent {b}Helen{/b}!"
    ang "Feel the wrath of {b}God{/b} licking at your backside!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Owww! enough! Please!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Don't give up so easily {b}Helen{/b}!"
    ang "You need this!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Owww!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Beg for me... Beg for forgiveness!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Owwwwwww!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "You are such a dirty, stubborn woman..."
    ang "{b}Helen{/b}, I need to hear you say it..."
    helen "I'm-"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhh! I'm sorry! I... repent!"
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhhh! Please {b}Sister{/b}... punish... my body..."
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "What's this? Are you enjoying this {b}Helen{/b}?"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhhh!!! Yes!!! I mean... no... I'm..."
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "A harlot! First, you were masturbating in front of this young man and now you are enjoying being beaten."
    ang "I want to hear you say it, harlot. Confess to me what you!"
    show ang 17 at Position (xoffset=312)
    helen "I..."
    helen "I'm a slut..."
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "So vulgar, {b}Helen{/b}. Now ask me to whip you more... slut."
    show ang 17 at Position (xoffset=312)

    helen "..."
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Ask me!"
    show ang 17 at Position (xoffset=312)

    helen "Whip my slutty body, {b}Sister{/b}! Help me!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "More {b}Sister{/b}... I want... more..."
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhhhhhh!!!"
    show helen whip 2 at left
    show ang 17 at Position (xoffset=312) with dissolve
    helen "Ohhhhh..."
    show ang 18 at Position (xoffset=312)
    ang "Such a greedy perverted sinner you are..."
    ang "I'm going to enjoy our future rituals..."
    show ang 17 at Position (xoffset=312)
    pause

    show ang 18f at Position (xpos=300) with dissolve
    ang "{b}[firstname]{/b}?"
    show ang 17f
    show player 24f at right with dissolve
    player_name "Yes?"
    show ang 18f
    ang "You did very well too."
    ang "Didn't he, {b}Helen{/b}?"
    show ang 17f
    show player 22f
    helen "Yes..."
    show ang 18f
    ang "Thank him for bringing me the whip, {b}Helen{/b}."
    show ang 17f
    show player 11f
    helen "Thank... you... {b}[firstname]{/b}..."

    show ang 18f
    ang "You may leave us now, {b}[firstname]{/b}."
    ang "{b}Helen{/b} will require further training, but first I need to have her more subservient and more tolerant to the pains of this world."
    ang "Perhaps, when the time comes, I can use you for something a little more...thorough, if you'd like."
    show ang 17f
    show player 10f
    player_name "I dont kn-"
    show player 11f
    show ang 18f
    ang "Leave us. I'll get you when I have need for you."
    hide ang
    hide helen
    hide player
    with dissolve
    scene black with fade
    pause

    scene church_stairs_n with fade
    show player 12
    player_name "This is crazy! I should say something to someone, but {b}Sister Angelica{/b} seems to have such control over {b}Helen{/b}."
    player_name "{b}Helen{/b} probably would say she is willingly participating..."
    show player 25
    player_name "I should talk to her and see if she's alright."
    hide player with dissolve
    $ gTimer.tick()
    $ M_mia.trigger(T_helen_torture)
    $ location_count = "Town Map"
    $ callScreen(location_count)

label helen_final_sacrament:
    $ inventory.items.remove(strapon_drawing)
    $ inventory.items.remove(strapon)
    $ M_mia.trigger(T_angelicas_final_ritual)
    scene church_nun_n_c with fade
    show helen whip 1 at left
    show ang 5f at Position (xpos=418)
    show player 12f at right
    with dissolve
    player_name "Oh, good. You guys are already here..."
    show player 5f
    show ang 6f
    ang "Where else would we be, {b}[firstname]{/b}?"
    show ang 5f
    show player 34f
    player_name "..."
    show player 35f
    player_name "In the church, sitting around a table reading the bible...with your clothes on?"
    show player 5f
    show ang 8f at Position (xoffset=3) with dissolve
    ang "{b}Helen's{/b} soul requires more than common church education."
    ang "She needs only complete my last ritual."
    ang "We've already completed the pre-ritual preparations..."
    show ang 9 at Position (xoffset=22) with dissolve
    ang "Right {b}Helen{/b}?"
    show ang 10 at Position (xoffset=22)
    helen "Yes... {b}Sister Angelica{/b}..."
    helen "My body... is waiting for your final ritual."
    helen "I want to be purified..."
    helen "I understand now, that I need to be cleansed... from the inside..."
    show ang 9 at Position (xoffset=22)
    ang "Do you have the object required to penetrate {b}Helen's{/b} sinful flesh?"
    show ang 10 at Position (xoffset=22)
    show player 239_240f with dissolve
    pause
    show player 457f with dissolve
    player_name "...This is what you wanted, right?"
    show player 458f
    show ang 8f at Position (xoffset=3) with dissolve
    ang "It's... perfect."
    ang "Put it on me."
    show ang 28 at Position (xpos=393) with dissolve
    show player 457f
    player_name "Wha?"
    show player 458f
    show ang 29
    ang "Did I stutter?"
    show ang 28
    show player 457f
    player_name "Alright..."
    hide player
    show ang 30 at right
    with dissolve
    player_name "Hmmm..."
    player_name "I guess there's no easy way to do this..."
    hide ang
    show ang 32 at Position (xpos=483)
    with dissolve
    ang "Careful now!"
    show ang 31
    pause
    player_name "( ...Her breasts... )"
    player_name "( ...They're so big! )"
    show ang 32
    ang "Hey! Mind your fingers down there..."
    ang "I’ve gotten better at using that whip..."
    show ang 31
    player_name "( ... )"
    show ang 33 at Position (xpos=412)
    show player 10f at right
    with dissolve
    player_name "There. It's on."
    show player 5f
    pause
    show ang 34
    ang "Did you know this strapon has a special feature?"
    show ang 35 at Position (xoffset=79)
    show player 6f
    pause
    show ang 33
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "Wha-"
    show player 22f
    show ang 34
    ang "Hurry up and undress."
    show ang 33
    show player 23f
    player_name "Undress?!"
    show player 10f
    player_name "You're not going to use that...on m-"
    show player 11f
    show ang 34
    ang "We all have to be exposed for the last purification ritual."
    show ang 33
    show player 12f
    player_name "Alright! I'm getting undressed!"
    show player 8f with dissolve
    pause
    show player 261 with dissolve
    pause
    show player 8bf with dissolve
    pause
    show player 64f
    show ang 37
    pause
    show ang 34
    ang "Well... Well..."
    ang "This could get interesting..."
    show ang 33
    show player 63f
    pause
    show player 61f at Position (xoffset=-19) with dissolve
    player_name "..."
    show player 68f at Position (xoffset=-19)
    show ang 34f at Position (xpos=475) with dissolve
    ang "{b}Helen{/b}?"
    show ang 33f
    helen "Yes, {b}Sister Angelica{/b}?"
    show ang 34f
    ang "Are you ready?"
    show ang 33f
    helen "Yes."
    helen "Purge me, {b}Sister Angelica{/b}."
    show ang 34f
    ang "Good girl."
    ang "Turn around and show {b}[firstname]{/b} the root of your lust..."
    show ang 33f
    show helen whip 3 with dissolve
    pause
    hide helen
    show ang 22f at left
    with dissolve
    pause
    show ang 23f with dissolve
    pause
    show ang 24f with dissolve
    pause
    show ang 25f with dissolve
    pause
    show player 68bf at Position (xoffset=-19)
    player_name "!!!"
    show ang 26f
    ang "Do you like what you see, {b}[firstname]{/b}?"
    ang "Her... Wet... Obedient... Pussy?"
    show player 65f with dissolve
    pause
    show player 66f with dissolve
    pause
    show player 430bf
    show ang 25bf
    ang "!!!"
    show ang 22_23_24f
    pause
    show ang 26f
    ang "What's wrong..."
    show player 430f
    show ang 22_23_24f
    pause
    show ang 26bf
    ang "...Getting excited?"
    show ang 26f
    ang "I must say, I'm impressed by how helpful you've been towards {b}Helen{/b}..."
    show player 67bf
    ang "You must care about her..."
    show ang 26bf
    ang "Or at least your body is eager to help her..."
    show ang 22_23_24f
    pause
    show player 430f
    show ang 25f
    helen "Ohh..."
    show player 430bf
    player_name "I... I don't think she's as bad as you say she is."
    show player 430f
    show ang 26f
    ang "Good to know..."
    show ang 25f
    pause
    show ang 26f
    ang "Now then, I'm sure you're wondering why I asked for the item in the photo."
    ang "The last step of my purification sacrament requires a long...rod of judgement."
    ang "You see... in order to cure {b}Helen{/b}, and become one with her body, she needs holy seeds."
    ang "It needs to be planted deep... inside her!"
    ang "Only then can {b}Helen's{/b} inner soul be salvaged from all her sins."
    show ang 22_23_24f
    show player 430bf
    player_name "What do you mean?"
    show player 430f
    show ang 26f
    ang "I'm graciously offering you a choice, {b}[firstname]{/b}."
    ang "Either you let me purge {b}Helen{/b} and leave her undefiled, so she may return to her husband purified..."
    ang "Or..."
    ang "Better yet, you purge her yourself..."
    show ang 25f
    show player 67bf
    player_name "..."
    show ang 26f
    ang "She'll then become your holy servant, {b}[firstname]{/b}."
    show ang 22_23_24f
    show player 430bf
    player_name "!!!"
    helen "Please, fuck me!!"
    show ang 26f
    ang "{b}Helen{/b} needs one of us to penetrate her sinful flesh..."
    ang "...I leave this decision in your hands."
    show ang 25f
    show player 67cf
    player_name "( If I do... {b}Helen{/b}. {b}Mia's{/b} parents won't get back together. )"
    player_name "( And {b}Mia{/b}... {b}Mia{/b} will be so upset. )"
    show player 67bf
    show ang 26f
    ang "So? Will you help {b}Helen{/b}, or not?"
    show ang 22_23_24f
    menu mia_helen_route_spilt:
        "Fuck {b}Helen{/b}.":
            show player 430bf
            player_name "I'll... I'll do it."
            show player 430f
            show ang 26f
            ang "Perfect. Your deeds won't go unnoticed in the eyes of the {b}Lord{/b}, {b}[firstname]{/b}..."
            ang "...Or mine."
            ang "Then let us begin the last ritual."
            hide ang
            hide player
            with dissolve
            label helen_mc_churchsex:
                scene church_nun_n_hs_1
                show helens 4_4b
                with fade
                ang "Just the tip, {b}[firstname]{/b}."
                ang "I want you to go slow."
                if not M_helen.get_state() == S_helen_start:
                    ang "The first time is always so...special."
                show helens 5 with dissolve
                helen "Ohhhh, {b}[firstname]{/b}!"
                $ M_helen.set('sex speed', .175)
                show helens 6_7_8_9_10 with dissolve
                helen "Ahhhh... Be gentle...."
                player_name "It's so...wet!"
                player_name "Holy s-"
                ang "Ah ah ah. We are in a place of worship."
                ang "Good. Now go deeper and don't release your seed till I say."
                ang "Don't forget I have my whip..."
                pause
                $ M_helen.set('sex speed', .125)
                show helens 6_7_8_9_10
                ang "Deeper! Faster {b}[firstname]{/b}! Make her understand what a sinful woman she is!"
                ang "{b}Helen{/b} needs to realize she can never truly be free of her sin now!"
                $ M_helen.set('sex speed', .075)
                pause
                $ anim_toggle = True
                $ xray = False

                label helen_mc_churchsex_repeat:
                    hide screen helen_ang_chamber_mc_sex_options
                    show screen xray_scr
                    pause
                    hide screen xray_scr
                    if anim_toggle:
                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 6_7_8_9_10
                            pause 2
                            $ animcounter += 1
                            if animcounter == 1:
                                player_name "Ohhh!!!{p=1}{nw}"
                            if animcounter == 2:
                                helen "Ahhhh!!!{p=1}{nw}"
                            elif animcounter == 4:
                                helen "{b}[firstname]{/b}!!!{p=1}{nw}"
                            pause 4
                    else:

                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 6
                            pause
                            show helens 7
                            pause
                            show helens 8
                            pause
                            show helens 9
                            pause
                            show helens 10
                            pause
                            $ animcounter += 1
                            if animcounter == 1:
                                player_name "Ohhh!!!{p=1}{nw}"
                            if animcounter == 2:
                                helen "Ahhhh!!!{p=1}{nw}"
                            elif animcounter == 4:
                                helen "{b}[firstname]{/b}!!!{p=1}{nw}"

                ang "Now! {b}[firstname]{/b}, cum for me!"
                ang "Cum deep in {b}Helen{/b}!"
                show screen helen_ang_chamber_mc_sex_options
                pause
                jump helen_mc_churchsex_repeat

                label helen_ang_chamber_mc_sex_cum:
                    hide screen helen_ang_chamber_mc_sex_options
                    show helens 11_11b with flash
                    player_name "UHHH!!"
                    helen "AHHHH!!!!"
                    show helens 11b with fastdissolve
                    helen "I... I feel...cleansed..."
                    show helens 12 with dissolve
                    helen "Ohhh...so...much..."
                    scene black with fade
                    pause 1
                    if not M_helen.get_state() == S_helen_start:
                        jump sacrament_complete



                scene church_nun_n_c with fade
                show helen whip 2 at left
                show ang 34 at Position (xpos=412)
                show player 5f at right
                with dissolve
                ang "Bless you, {b}[firstname]{/b}!"
                ang "{b}Helen's{/b} body is once again purged from her sins..."
                ang "...And you have just made her your holy servant!"
                show ang 33
                show player 10f
                player_name "What... does that mean?"
                show player 5f
                show ang 34
                ang "You have just bound {b}Helen's{/b} desires to you."
                ang "She will now obey to your commands..."
                show player 11f
                ang "You have taken her husband's place in their marriage bed."
                ang "{b}Helen{/b} will now require a daily serving of your holy seed."
                ang "In order for you to keep each other pure and faithful."
                show ang 33
                show player 12f
                player_name "What?!"
                show player 22f
                show ang 34
                ang "Isn't that right, {b}Helen{/b}?"
                show ang 33
                helen "Y...yes... I must now serve, {b}[firstname]{/b}."
                helen "I... will accept his holy seed... as a submissive and obedient wife should."
                show ang 34
                ang "Good, {b}Helen{/b}."
                ang "This concludes our holy sacrament. You two may now leave in peace."
                ang "I will continue to offer the various rituals of the sacrament at night."
                ang "Feel free to visit if you wish to... participate."
                show ang 33
                show player 12f
                player_name "That's nice and all..."
                show player 10f
                player_name "...But I better get back home."
                hide player
                hide helen
                hide ang
                with dissolve
                $ M_helen.trigger(T_helen_route)
                $ M_helen.set('helen route', True)
        "Watch {b}Sister Angelica{/b}.":

            show player 67cf
            player_name "I..."
            player_name "I can't do it."
            player_name "{b}Helen{/b} needs her husband, and {b}Mia{/b} needs her parents."
            show player 67bf
            show ang 26f
            ang "Fine, I guess I'll have to be the one to save {b}Helen{/b}."
            ang "Stand back, {b}[firstname]{/b}."
            show ang 23f
            pause
            show ang 22f
            show player 430f
            player_name "..."
            helen "Thank you, {b}Sister Angelica{/b}..."
            hide ang
            hide player
            with dissolve


            scene church_nun_n_hs_2 with fade
            show helens 13 with dissolve
            ang "{b}Helen{/b}, I've been looking forward to this moment."
            ang "You've always presented yourself as the most devout and pious member of {b}God's{/b} flock."
            ang "I've always wanted to penetrate a dirty sinner's soul... and not using {b}God's Word{/b}."
            helen "Oh?"
            ang "You are not greater than anyone else..."
            ang "You are worse..."
            ang "You are a slut, {b}Helen{/b}."
            ang "Receive my rod of judgement!"
            show helens 14 with dissolve
            helen "Ohhh!!!"
            ang "Deeper, slut!"
            ang "Take it all!"
            $ M_helen.set('sex speed', .175)
            show helens 15_16_17_18_19 with dissolve
            helen "Ohhh!!!"
            helen "Faster! {b}Sister Angelica{/b}! Faster!"
            $ M_helen.set('sex speed', .125)
            $ anim_toggle = True
            $ xray = False

            label helen_ang_churchsex_repeat:
                hide screen helen_ang_chamber_ang_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show helens 15_16_17_18_19
                    pause 2
                    $ animcounter += 1
                    if animcounter == 1:
                        helen "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 2:
                        helen "Ohhh!!!{p=1}{nw}"
                    elif animcounter == 4:
                        helen "{b}Sister{/b}!!!{p=1}{nw}"
                    pause 4
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show helens 15
                        pause
                        show helens 16
                        pause
                        show helens 17
                        pause
                        show helens 18
                        pause
                        show helens 19
                        pause
                        $ animcounter += 1
                        if animcounter == 1:
                            helen "Ahhhh!!!"
                        if animcounter == 2:
                            helen "Ohhh!!!"
                        elif animcounter == 4:
                            helen "{b}Sister{/b}!!!"

            helen "I'm sooo close!"
            show screen helen_ang_chamber_ang_sex_options
            pause
            jump helen_ang_churchsex_repeat

            label helen_ang_chamber_ang_sex_cum:
                hide screen helen_ang_chamber_ang_sex_options
                show helens 14 with fastdissolve
                ang "Now, release your sins!"
                ang "Cum for me, {b}Helen{/b}!"
                show helens 20 with flash
                helen "OHHHH!!!!!"
                helen "OHHHHHHHH!!!!"
                show helens 21 with dissolve
                ang "Good slut..."
                scene black with fade
                pause 1



            scene church_nun_n_c with fade
            show helen whip 2 at left
            show ang 34 at Position (xpos=412)
            show player 5f at right
            with dissolve
            ang "{b}Helen{/b} has now been purified."
            ang "Through my training, she has become more submissive."
            ang "{b}God's{/b} demand of all holy wives to their husbands."
            show ang 33

            helen "Thank you, {b}Sister Angelica{/b}."
            show player 11f
            show ang 34
            ang "As for you {b}[firstname]{/b}, I have to say, I am a bit disappointed."
            show player 24f
            ang "{b}God{/b} called upon your aid, and you turned your back..."
            ang "...When you should have been the one to share your seeds with {b}Helen{/b}!"
            show player 5f
            ang "But perhaps, this is faith."
            ang "Thank you for you assistance."
            ang "I release you of your duties and will not require your services anymore."
            show ang 33
            show player 12f
            player_name "I'm just glad our deal is over."
            show player 10f
            player_name "I truly hope that {b}Helen{/b} feels better after all this."
            hide player
            hide helen
            hide ang
            with dissolve
            $ M_mia.trigger(T_mia_route)
    $ gTimer.tick()
    $ location_count = "Town Map"
    $ callScreen(location_count)

label angelica_room_new_dialogue:
    scene church_nun_n_c with fade
    show helen 37 at Position (xpos=575)
    show ang 6f at left
    show player 5f at right
    with dissolve
    ang "Good evening, {b}[firstname]{/b}. Have you come to assist in my training of {b}Helen{/b}?"
    show ang 5f
    show player 10f
    player_name "Only if you need my help."
    show player 5f
    show ang 9 with dissolve
    ang "The {b}Lord{/b} always needs help from his followers."
    ang "Besides, {b}Helen{/b} has been hoping you'd stop in again."
    show ang 10
    show helen 39
    helen "I'm happy to see you here, {b}Master{/b}."
    show helen 37
    show ang 9
    ang "{b}Helen{/b}, let's get you setup for tonight's ritual."
    show helen 37 at Position (xpos=464) with dissolve
    show ang 13 with dissolve
    pause
    show ang 14 with dissolve
    ang "I'm restraining you still, just in case you get some sinful impulse to cover yourself."
    hide helen
    show ang 15
    with dissolve
    ang "I enjoy seeing you heeding my commands so submissively, {b}Helen{/b}."
    show helen whip 1 at Position (xpos=161)
    hide ang
    show ang 9 at Position (xpos=462)
    with dissolve
    ang "Now."
    ang "Is there something you'd like to have done to {b}Helen{/b}?"
    show ang 10
    menu angelica_new_dialouge_repeat:
        "Spanking.":
            show player 24f
            player_name "I want to watch you... whip..."
            show player 29f
            player_name "Nevermind."
            show player 5f
            show ang 9
            ang "Oh?"
            ang "Are you to shy to ask me to punish {b}Helen{/b}?"
            show ang 10
            show player 24f
            player_name "..."
            show ang 9
            ang "Don't worry, {b}[firstname]{/b}."
            ang "{b}Helen{/b}, likes being whipped. Right, {b}Helen{/b}?"
            show ang 10
            helen "Yes, {b}Sister Angelica{/b}."
            show ang 18f at Position (xoffset=27) with dissolve
            ang "Sit back, {b}[firstname]{/b} and enjoy the show."
            show helen whip 1 at left
            show ang 18 at left
            show ang 18 at Position (xoffset=312)
            hide player
            with dissolve
            ang "Repent, {b}Helen{/b}!"
            ang "Feel the wrath of {b}God{/b} licking at your backside!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Ohhhh!"
            show ang 18 at Position (xoffset=312)
            ang "Beg for me... Beg me for more!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "More! Punish my sinful flesh!"
            show ang 18 at Position (xoffset=312)
            ang "You are such a dirty woman..."
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 18 at Position (xoffset=312) with dissolve
            ang "Such a slut."
            ang "Tell me...who's cock is better?"
            show ang 17 at Position (xoffset=312)
            helen "Wha-"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 18 at Position (xoffset=312) with dissolve
            ang "I want to hear you say it, slut. Is {b}[firstname]{/b} penis better than {b}Harold's{/b}?"
            show ang 17 at Position (xoffset=312)
            helen "..."
            helen "......"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Ahhhhh!!! {b}[firstname]{/b}! I... love... his fat cock!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 18 at Position (xoffset=312) with dissolve
            ang "So vulgar, {b}Helen{/b}... Now ask me to whip you more, slut."
            show ang 17 at Position (xoffset=312)
            helen "Whip my slutty body, {b}Sister Angelica{/b}! Help me!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "More {b}Sister{/b}... I want... more..."
            helen "Why... are... you waiting?"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 2 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Ohhhhhhh!!!"
            show ang 18 at Position (xoffset=312)
            ang "Such a greedy perverted sinner you are..."
            hide ang
            hide helen
            with dissolve
            jump sacrament_complete
        "Holy Seed.":

            show player 10f
            player_name "I'm here to help purge {b}Helen's{/b} sins."
            show ang 9
            ang "Perfect. Your deeds won't go unnoticed in the eyes of the {b}Lord{/b}, {b}[firstname]{/b}..."
            ang "...Or mine."
            ang "Then let us begin the last ritual."
            hide ang
            hide helen
            hide player
            with dissolve
            jump helen_mc_churchsex
        "Spread {b}Helen{/b}.":

            show player 24f
            player_name "Could you... spread {b}Helen's{/b}..."
            show ang 9
            ang "Pussy?"
            ang "I suppose I could."
            ang "First you have to get naked."
            ang "I want to see how {b}Helen's{/b} pussy excites you."
            show ang 10
            pause
            player_name "Alright."
            show player 8f with dissolve
            pause
            show player 261 with dissolve
            pause
            show player 8bf with dissolve
            pause
            show player 64f
            show ang 9
            ang "Good boy."
            show ang 9f at Position (xoffset=100) with dissolve
            ang "Turn around {b}Helen{/b}."
            show ang 10f at Position (xoffset=100)
            show helen whip 3 with dissolve
            pause
            hide helen
            show player 68bf at Position (xoffset=-19)
            show ang 22f at left
            with dissolve
            pause
            show ang 23f with dissolve
            pause
            show ang 24f with dissolve
            pause
            show ang 25f with dissolve
            pause
            show ang 22_23_24f
            helen "Ohhhh..."
            show player 65f with dissolve
            pause
            show player 430bf with dissolve
            helen "Ahhhh..."
            show ang 26f
            ang "Did you like that?"
            show player 430f
            show ang 25f
            helen "Yes..."
            show ang 26f
            ang "Quiet, slut. I meant {b}[firstname]{/b}."
            show ang 22_23_24f
            show player 430bf
            player_name "Yes."
            pause
            hide player
            hide ang
            with dissolve
            scene black with fade
            pause 1
            jump sacrament_complete
        "Have you sinned?":

            show popup_unfinished at truecenter with dissolve
            $ renpy.pause()
            hide popup_unfinished with dissolve
            jump angelica_new_dialouge_repeat
        "Nothing.":

            show player 10f
            player_name "Nothing."
            show player 5f
            show ang 6f at Position (xoffset=-22) with dissolve
            ang "Leave then. I'm busy right now."
            hide player
            hide ang
            hide helen
            with dissolve
    $ callScreen(location_count)

label sacrament_complete:
    scene church_nun_n_c with fade
    show helen whip 2 at left
    show ang 6f at Position (xpos=434)
    show player 5f at right
    with dissolve
    ang "Feel free to visit again if you wish to participate in my nightly sacrament."
    show ang 5f
    show player 10f
    player_name "I better get back home."
    hide player
    hide helen
    hide ang
    with dissolve
    $ gTimer.tick()
    $ location_count = "Town Map"
    $ callScreen(location_count)

label helen_ang_chamber_ang_faster_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') - 0.05)
    jump helen_ang_churchsex_repeat

label helen_ang_chamber_ang_slower_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') + 0.05)
    jump helen_ang_churchsex_repeat

label helen_ang_chamber_mc_faster_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') - 0.05)
    jump helen_mc_churchsex_repeat

label helen_ang_chamber_mc_slower_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') + 0.05)
    jump helen_mc_churchsex_repeat