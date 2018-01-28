default tv_channel = 0
default tv_pink_channel = 7
default tv_channel_pink = True
default tv_channel_1_seen = False
default tv_channel_2_seen = False
default tv_channel_3_seen = False
default tv_channel_4_seen = False
default tv_channel_5_seen = False
default tv_channel_6_seen = False
default tv_channel_7_seen = False
default tv_channel_8_seen = False

label home_livingroom_dialogue:
    python:
        sis_caught_spying = False
    $ location_count = "Living Room"
    if sister.in_progress(sis_couch01):
        scene home_entrance_night
        show player 11 with dissolve
        pause 0.0001
        player_name "( I'm not going back in there, she'll catch me for sure. )"
        player_name "( I should go to bed. )"
        hide player with dissolve
        jump home_entrance

    elif sister.started(sis_couch03) and gTimer.is_evening() and (M_mom.get_state() != S_mom_sleepover or not is_here("mom")):
        scene home_livingroom_n_b
        show player 12
        with dissolve
        player_name "( Is someone in here? )"
        show player 11
        player_name "..."
        jump home_livingroom_tv

    elif M_mom.get_state() == S_mom_spy and not gTimer.is_dark():
        scene home_livingroom_b
        show player 30 with dissolve
        player_name "I guess it's not the TV."
        show player 4 with dissolve
        player_name "Hmm..."
        pause        
        show player 12 with dissolve
        player_name "( What was that? )"
        show player 35
        player_name "( I {b}hear{/b} something... Or someone? )"
        show player 12
        player_name "( It's like a voice, coming from... {b}[mom_name]'s bedroom{/b}? )"
        show player 10
        player_name "( I should go see if everything's okay... )"
        hide player 10 with dissolve
    $ callScreen(location_count)

label mom_movie_night:
    scene location_home_livingroom_night_blur
    $ M_mom.set("sex speed", .175)
    if M_mom.get_state() == S_mom_romance_movie:
        show player 1 at left
        show mom 63 at right
        mom "There he is..."
        mom "You ready?"
        show player 2
        show mom 61
        player_name "Yup! What are we watching?"
        show player 1
        show mom 60
        mom "Hmm, I don't know... I'm kind of in the mood for a romance."
        show player 10
        show mom 61
        player_name "... Seriously?"
        show player 90
        show mom 62
        mom "Hehe, yeah! Why? What would you like to watch?"
        show player 10
        show mom 61
        player_name "I dunno... Something with some action maybe?"
        show player 90
        show mom 62
        mom "Pfft, typical man..."
        show player 10
        show mom 61
        player_name "Heh, is that a bad thing?"
        show player 90
        show mom 62
        mom "Hehehe, no. I suppose not."
        show mom 60
        mom "Ughh but you always make me watch those!"
        mom "Can't you let Mommy choose one?"
        show player 10
        show mom 59
        player_name "... I suppose."
        show player 2
        player_name "Let's see what we can find."
        show player 1
        show mom 62
        mom "That's my boy!"

        scene home_livingroom_tv
        show home_tv_channel_02 at Position(xpos=522, ypos=521)
        pause
        show home_tv_channel_06 at Position(xpos=522, ypos=521)
        pause
        show home_tv_channel_04 at Position(xpos=522, ypos=521)
        pause
        show home_tv_channel_06b at Position(xpos=522, ypos=521)

        mom "Oooh! There we go!"
        mom "I haven't seen this one yet!"
        player_name "... Great."

        scene location_home_livingroom_couch03
        show playerf 2df zorder 0 at Position(xpos=0.805, ypos=1.0095)
        show playerfa 1f zorder 2 at Position(xpos=0.8235, ypos=0.7345)
        show momf 3bf zorder 3 at Position(xpos=0.435, ypos=1.025)
        show momfa 1f zorder 4 at Position(xpos=0.5725, ypos=0.7175)
        with dissolve
        mom "Haha, don't be like that."
        mom "You never know, you might like it..."
        show momf 3f
        show playerf 2cf
        player_name "I won't."
        player_name "Believe me, I know..."
        show momf 3bf
        show playerf 2df
        mom "Oh, just hush and watch!"

        scene location_home_couch_cutscene01 with fade
        show text "I'll admit, the film wasn't so bad." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Not much action but at least it had some good humor to it." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "[mom_name] certainly seemed to be enjoying it. Her melodic laughter filled the room and brought a smile to my face." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        scene location_home_couch_cutscene02
        with fade
        show text "She made herself comfortable as we watched and I constantly found my eyes drawn to her body..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Especially when the movie took an erotic turn, the two lover's on screen embraced, kissing passionately.\nTheir hands exploring as they hurried to undressed one another..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text
        hide location_home_couch_cutscene02
        with dissolve

        scene location_home_livingroom_couch04
        show playerf 1bf zorder 0 at Position(xpos=0.805, ypos=1.0095)
        show playerfa 1f zorder 1 at Position(xpos=0.8235, ypos=0.7345)
        show moms 136b zorder 3 at Position(xpos=0.4115, ypos=1.005)
        with dissolve
        player_name "( Wow, this is getting pretty intense... )"
        show playerf 3cf
        player_name "( ...It's a bit awkward but [mom_name] doesn't seem to be bothered. )"
        show moms 136c with dissolve
        show playerf 4flip

        player_name "( !!! )" with hpunch
        show playerf 4bf
        player_name "( What is she doing!? )"
        player_name "( She's touching my... )"
        show playerf 3cf
        player_name "( Did she put her foot there on purpose? )"
        player_name "( ... )"
        show playerf 4bf
        player_name "( ...No, I don't think she even realizes-- Uh oh... )"
        show playerf 4flip
        show playerfb 1f zorder 2 at Position(xpos=0.8185, ypos=0.75) with dissolve
        pause
        show playerf 3bf
        player_name "( Ah no! Ah crap! Ah jeeze! )"
        player_name "( I didn't mean to... It's just the movie and her foot... I couldn't help it! )"
        show playerf 3cf
        player_name "( Please, don't notice... )"
        player_name "( Please, oh please, oh please! )"
        mom "( Phew, this is getting pretty hot and heavy. )"
        mom "( I hope this isn't making, {b}[firstname]{/b} uncomfortable. )"
        show playerf 4ef
        show moms 136d
        mom "( Hmm, what is- )"
        show moms 135 with hpunch
        mom "( Oh my god! )"
        mom "( Is that his... )"
        show moms 136e
        mom "( ... )"
        mom "( I still can't believe my {b}son{/b} is {b}hung like this{/b}."
        show moms 136d
        mom "( Where the heck did it come from?! )"
        mom "( I mean his {b}father{/b} was {b}big{/b}, but {b}nothing like this{/b}! )"
        show moms 136e
        mom "( Poor thing... )"
        mom "( This has got to be awkward for him. What am I supposed to do, ignore it? )"
        show moms 136d
        pause
        show moms 136f
        mom "( ... )"
        show moms 136e
        mom "( Oh gosh, {b}I'm staring{/b}... Snap out of it, [mom]! )"
        scene location_home_livingroom_couch03
        show playerf 3f zorder 0 at Position(xpos=0.805, ypos=1.0095)
        show playerfb 1f zorder 1 at Position(xpos=0.8185, ypos=0.75)
        show playerfa 1f zorder 2 at Position(xpos=0.8235, ypos=0.7345)
        show momf 5cf zorder 3 at Position(xpos=0.4225, ypos=1.0225)
        show momfa 1f zorder 4 at Position(xpos=0.56, ypos=0.715)
        with dissolve
        player_name "( ... )"
        player_name "( This is not good. Should I say something? )"
        show playerf 5f
        player_name "I uhh... This movie got kinda {b}naughty{/b}, huh?"
        show playerf 3f
        show momf 5bf
        mom "Y-yeah... It sure did."
        show momf 5flip
        pause
        show momf 5ff
        pause
        show momf 5cf
        show playerf 4ef
        player_name "( {b}Is she blushing?{/b} )"
        pause
        mom "..."
        show momf 5bf
        mom "Sorry about... You know... I had no idea..."
        show playerf 5f
        show momf 5flip
        player_name "No, it's okay! Nothing I haven't seen before."
        show momf 5ff
        pause
        show momf 5cf
        show playerf 4ef
        mom "( Oh no, I hope he didn't notice me {b}staring{/b}... )"
        show momf 5flip
        mom "( It's just so {b}huge{/b}! I wonder what something that big would even feel- )"
        show momf 5gf with hpunch
        mom "( ... What the heck am I thinking!? )"
        show momf 5cf
        pause
        show playerf 5f
        player_name "*Ahem* So, ehh... Other than this scene, the movie is pretty good."
        show momf 5ff
        player_name "... Well, I mean, it's better than I thought it would be."
        show playerf 5bf
        show momf 5gf
        mom "Hehe, y-yeah? I'm glad you liked it."
        show momf 5ff
        pause
        show momf 5flip
        pause
        show momf 5ff
        pause
        show momf 5cf
        show playerf 4ef
        player_name "( ... )"
        mom "( ... )"

        scene location_home_livingroom_night_blur with fade
        show player 2 at left
        show mom 61 at right
        with dissolve
        player_name "Well, thanks for the movie, {b}[mom_name]{/b}."
        show player 1
        show mom 62
        mom "Aww, of course! Thanks for watching it with me, Sweetie!"
        mom "Mommy loves spending time with her boy!"
        show player 2
        show mom 61
        player_name "Okay, well... Goodnight!"
        show player 1
        show mom 62
        mom "Goodnight, Sweetheart!"
        hide player with dissolve
        show mom 29 at Position(xpos=0.75, ypos=1.115) with dissolve
        player_name "( Mmm, she smells good! )"
        mom "( My boy is growing up so fast, he's practically a man now... )"
        mom "( ... and he has the biggest... {b}thing{/b} I've ever seen... )"
        mom "( Oh gosh, What is the matter with me today!? )"

    elif M_mom.get_state() == S_mom_romance_movie_two:
        show player 1 at left
        show mom 62 at right
        mom "There he is..."
        mom "You ready?"
        show player 2
        show mom 61
        player_name "Yup!"
        show player 1
        show mom 63
        mom "I figured we could watch one of your cheesy action flicks tonight, if you wanted?"
        show player 2
        show mom 61
        player_name "Actually, I was thinking something romantic..."
        show player 1
        show mom 62
        mom "What?! Who are you and what have you done with my son?"
        show player 2
        show mom 61
        player_name "Hehe, well they make you happy and I like seeing you happy, [mom_name]..."
        show player 1
        show mom 62
        mom "Aww, such a Sweetheart!"
        mom "Well, have a seat and lets see what we can find."
        show player 2
        show mom 61
        player_name "Okay, sure!"

        scene home_livingroom_tv
        show home_tv_channel_02 at Position(xpos=522, ypos=521)
        pause
        show home_tv_channel_06 at Position(xpos=522, ypos=521)
        pause
        show home_tv_channel_04 at Position(xpos=522, ypos=521)
        pause
        show home_tv_channel_06b at Position(xpos=522, ypos=521)

        mom "There we go!"
        mom "Ooh, this is a good one!"
        player_name "... Great!"

        scene location_home_livingroom_couch04
        show playerf 3cf zorder 0 at Position(xpos=0.805, ypos=1.0)
        show playerfa 1f zorder 2 at Position(xpos=0.8235, ypos=0.7275)
        show moms 136c zorder 3 at Position(xpos=0.4115, ypos=1.005)
        with dissolve
        player_name "..."
        show playerf 2ef
        player_name "So, here we are again."
        show playerf 2ff
        show moms 133
        mom "Mmmhmm."
        show moms 135
        mom "You know, Sweetie. I sure am glad you wanted to watch another movie with me."
        $ M_mom.set('sex speed', M_mom.get('sex speed') / .45)
        show moms 133_134
        show playerf 3bf

        player_name "*gulp*"
        show playerf 4flip
        player_name "O-of course, I love spending time with you, [mom_name]."
        show playerf 3bf
        show moms 135
        mom "Mmm, always so sweet..."
        show moms 133_134
        pause
        show moms 135
        mom "I think you deserve a reward."
        show playerf 4flip
        show moms 133_134
        player_name "... Really?"
        show playerf 4bf
        show moms 135
        mom "Mmmhmm!"
        show moms 133_134
        pause
        show playerf 4bf
        show moms 135
        mom "A nice..."
        show moms 133_134
        pause
        show moms 135
        mom "... Big..."
        show moms 133_134
        pause
        show moms 135
        mom "... Juicy..."
        show moms 133_134
        show playerf 4cf
        show playerfb 1f zorder 1 at Position(xpos=0.8185, ypos=0.75) with dissolve
        pause
        show moms 135
        mom "... Reward."
        show moms 133_134 zorder 2
        show playerf 2ef
        player_name "Oooh [mom_name], that feels wonderful."
        show playerf 4bf
        pause

        scene location_home_livingroom_couch05
        show playerf 3cf zorder 0 at Position(xpos=0.805, ypos=1.0)
        show playerfb 1f zorder 1 at Position(xpos=0.8185, ypos=0.75)
        show playerfa 1f zorder 2 at Position(xpos=0.8235, ypos=0.7275)
        show moms 137 zorder 3 at Position(xpos=0.4735, ypos=0.8080)
        with dissolve
        pause
        show playerf 2ef
        player_name "W-what are you doing, [mom_name]?"
        show playerf 2ff
        show moms 138
        mom "I'm just getting more comfortable, Sweetie..."
        show moms 139
        pause
        show moms 140
        mom "Why don't you come over here and lay with Mommy?"
        show playerf 2ef
        show moms 139
        player_name "Y-Yeah, okay."
        pause
        scene location_home_livingroom_couch06

        show moms 142 zorder 0 at Position(xpos=0.5200, ypos=.9)
        show momp 2 zorder 1 at Position(xpos=0.4917, ypos=0.7625)
        with dissolve
        pause
        player_name "L-like this?"
        show moms 141
        mom "Just like that..."
        mom "Doesn't that feel good, Sweetie?"
        show moms 142
        player_name "... Yes, very good."
        show moms 141
        mom "Mmmhmm, now give Mommy a kiss."
        show moms 142
        player_name "O-okay..."
        show moms 143 with dissolve
        pause
        show moms 144
        pause
        show moms 143
        mom "Mmm..."
        pause
        show moms 141 with dissolve
        mom "Such a good kisser..."
        show moms 142
        player_name "Thanks, [mom_name]."
        show moms 143 with dissolve

        pause 
        show moms 144
        pause
        show moms 143
        pause
        show moms 142 with dissolve
        player_name "Can I kiss you someplace else?"
        show moms 141
        mom "Mmm, maybe... What do you have in mind?"
        show momp 1
        show moms 145
        with dissolve

        player_name "How about, here!?"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / 1)
        show moms 146_147
        mom "Oooh!"
        mom "Oh yes, {b}[firstname]{/b}! Mmm..."
        player_name "..."
        mom "That's it Baby, don't stop!"
        mom "Haah!"
        pause
        show momp 2
        show moms 142
        with dissolve
        mom "!??"
        show moms 141
        mom "... What's the matter?"
        show moms 142
        player_name "[mom_name], your getting my shorts all wet..."
        show moms 141
        mom "Ooh... Oh gosh! What am I doing!? Stop! {b}[firstname]{/b}, stop!"
        show moms 142
        player_name "What's the matter?"
        show moms 141
        mom "This is too much! I-"
        mom "We just need to stop, Okay!?"
        show moms 142
        player_name "O-okay... Sorry, [mom_name]."
        show moms 141
        mom "... No. Sweetie, you didn't do anything wrong."
        mom "It's just..."
        mom "I..."
        mom "How about we just cuddle for awhile and finish the movie?"
        mom "Would that be alright?"
        show moms 142
        player_name "Of course."
        show momp 1
        show moms 162b at Position(xpos=0.5175, ypos=.8625)
        with dissolve
        mom "Thanks, Sweetie."
        mom "..."
        mom "( Phew, I almost lost my head there for a second. )"

        scene location_home_livingroom_night_blur
        show player 2 at left with dissolve
        show mom 61 at right with dissolve
        player_name "Thanks for the movie, {b}[mom_name]{/b}. It was fun!"
        show player 1
        show mom 62
        mom "It sure was, Sweetie. I'm so happy we are getting all this quality time together!"
        mom "Mommy loves spending time with her boy!"
        show player 2
        show mom 61
        player_name "I love spending time with you too, [mom_name]."
        hide player
        show mom 29 at Position(xpos=0.75, ypos=1.115) with dissolve
        player_name "Okay, well... Goodnight!"
        show mom 28
        mom "Goodnight, Sweetheart!"
        show mom 59 at Position(xpos=0.75, ypos=1.0) with dissolve
        mom "( He's such a sweet boy... )"
        mom "( ... and so understanding. He stopped when I asked him to with no complaints whatsoever. )"
        mom "( I should have done something to finish him. Poor thing... )"
    else:

        show player 2 at left
        show mom 61 at right
        player_name "You ready?"
        show player 1
        show mom 63
        mom "Oh, I'm ready! I've been looking forward to this all day!"
        show player 2
        show mom 61
        player_name "Alright, just give me a second to get it set up..."

        scene location_home_livingroom_couch03 with fade
        show playerf 1f zorder 0 at Position(xpos=0.805, ypos=1.0095)
        show playerfa 1f zorder 2 at Position(xpos=0.8235, ypos=0.7345)
        show momf 3f zorder 3 at Position(xpos=0.415, ypos=1.0205)
        show momfa 1f zorder 4 at Position(xpos=0.5535, ypos=0.732)
        with dissolve
        player_name "There we go, all set!"
        show playerf 2df
        show momf 3bf
        mom "Mmm, all set..."
        show momf 3f
        pause
        show momf 4f
        pause
        show momfa 2f at Position(xpos=0.6225, ypos=0.7175) with dissolve
        show playerf 3bf
        show momf 5bf
        mom "Mommy's been thinking about you..."
        show playerf 5f
        show momf 5flip
        player_name "Oh yeah?"
        player_name "... And what have you been thinking?"
        show playerf 5bf
        show momf 3bf
        mom "How sweet you are."
        mom "... And brave..."
        mom "... And strong."
        show momf 3f
        show playerf 5f
        player_name "Is that all?"
        show momf 3bf
        show playerf 5bf
        mom "No..."
        show momf 5bf
        show momfa 3f at Position(xpos=0.705, ypos=0.77) with dissolve
        show playerf 4hf
        mom "I've also been thinking about that big..."
        $ M_mom.set('sex speed', M_mom.get('sex speed') / .5)
        show momfa 3f_3bf
        show momf 5flip
        pause
        show momf 5bf
        mom "... Hard..."
        show momf 5flip
        pause
        show momf 5bf
        mom "... Juicy..."
        show momf 4f
        show playerf 4gf
        player_name "Oh..."
        show momfa 4f at Position(xpos=0.6915, ypos=0.775) with dissolve
        show playerfb 1f zorder 1 at Position(xpos=0.8185, ypos=0.75) with dissolve
        show playerf 4hf
        pause
        show momf 4bf
        mom "... Cock."
        show momf 3f
        show playerf 2df
        pause
        show momf 3bf
        mom "So..."
        hide playerfb
        show momf 4bf
        show momfa 5f at Position(xpos=0.7255, ypos=0.7625) with dissolve
        pause
        show momf 4f
        show playerf 4hf
        hide playerfb
        show momfa 5bf_5cf
        pause
        show momf 3bf
        show playerf 2df
        mom "What are we gonna do about this?"
        show momf 3f
        menu:
            "Blowjob.":
                show playerf 5f
                player_name "Could you... use your mouth?"
                show momf 3bf
                show playerf 5bf
                mom "... My mouth?"
                show momf 4f
                pause
                show momf 3bf
                mom "Sure, Sweetie. Anything for you!"
                show momf 3f
                pause
                hide momfa
                show playerfb 1f zorder 1 at Position(xpos=0.8185, ypos=0.75)
                show momf 7bf at Position(xpos=0.4085, ypos=1.0165)
                mom "Just lay back and relax, Sweetie..."
                show playerf 4hf
                hide playerfb
                show momf 11f at Position(xpos=0.504, ypos=1.0165) with dissolve
                pause
                show momf 12f
                pause
                show momf 7bf at Position(xpos=0.4085, ypos=1.0165) with dissolve
                show playerfb 3f zorder 1 at Position(xpos=0.8055, ypos=0.75)
                mom "Mommy will take care of you."
                show momf 7f
                show playerf 2cf
                player_name "... Thanks, [mom_name]."
                show playerf 4bf
                hide playerfb
                show momf 8flip at Position(xpos=0.515, ypos=1.0165) with dissolve
                pause
                $ M_mom.set('sex speed', M_mom.get('sex speed') / 3)
                show momf 8flip_8bf_8cf_8df_8ef_8ff_8gf
                pause 2
                show playerf 4flip
                player_name "Oh, wow!"
                show playerf 4bf
                pause 4
                show playerf 4flip
                player_name "Unngghh..."
                show playerf 4bf
                mom "Mmm..."
                pause 4
                show playerf 4flip
                player_name "Your so good at this..."
                show playerf 4bf
                mom "Mmmhmm..."
                pause 4
                mom "Mmm..."
                pause
                label mom_movie_night_blowjob_options:
                    menu:
                        "Keep going.":
                            show momf 8flip_8bf_8cf_8df_8ef_8ff_8gf
                            pause
                            jump mom_movie_night_blowjob_options
                        "Cum.":

                            show playerf 4flip
                            player_name "[mom_name], I'm gonna..."
                            show playerf 4bf
                            pause
                            show playerf 4df
                            show momf 9f
                            player_name "Hnnnggg!!!" with flash
                            show playerf 4gf
                            player_name "Uhhh, man..."
                            show momf 10f zorder 3 at Position(xpos=0.415, ypos=1.0205) with dissolve
                            show playerfb 2f zorder 1 at Position(xpos=0.8185, ypos=0.75) with dissolve
                            show playerf 5f
                            player_name "[mom_name], that was incredible!"
                            show momf 5cf
                            show momfa 2f zorder 4 at Position(xpos=0.6225, ypos=0.7175)
                            with dissolve
                            mom "*gulp*"
                            show momf 5gf
                            mom "Goodness, that was alot..."
                            show momf 5ff
                            show playerf 5f
                            player_name "Heh, sry."
                            show playerf 5bf
                            show momf 5gf
                            mom "Not at all, Sweetie!"
                            mom "That was yummy."
                            show momf 5ff
                            show playerf 5f
                            player_name "Oh, well I'm glad you like it."
                            show playerf 5bf
                            mom "Mmmhmm."
                            show momf 5gf
                            mom "I love you, Sweetheart."
                            show momf 5ff
                            show playerf 5f
                            player_name "I love you too, [mom_name]."
            "Sex.":

                show playerf 5f
                player_name "I want you..."
                show momf 3f
                show playerf 5bf
                mom "Mmm..."
                show momf 3bf
                mom "I was hoping you'd say that..."
                show momf 5gf
                show momfa 4f at Position(xpos=0.6915, ypos=0.775)
                with dissolve
                show playerfb 1f zorder 1 at Position(xpos=0.8185, ypos=0.75)
                mom "I've been waiting all day for this."
                scene location_home_livingroom_couch05
                show playerf 3cf zorder 0 at Position(xpos=0.805, ypos=1.0)
                show playerfb 1f zorder 1 at Position(xpos=0.8185, ypos=0.75)
                show playerfa 1f zorder 2 at Position(xpos=0.8235, ypos=0.7275)
                show moms 137 zorder 3 at Position(xpos=0.4735, ypos=0.8080)
                with dissolve
                pause
                show moms 138
                mom "Oh, Sweetie. Mommy's so wet..."
                show moms 139
                pause 
                show moms 140
                mom "Come kiss me."
                show playerf 2ef
                player_name "O-okay."
                scene location_home_livingroom_couch06
                show moms 141 zorder 0 at Position(xpos=0.5200, ypos=.8965)
                show momp 2 zorder 1 at Position(xpos=0.4917, ypos=0.7590)
                with dissolve
                mom "That's it, Baby."
                show moms 143 with dissolve
                pause
                show moms 144
                mom "Mmm..."
                show moms 143
                pause
                show moms 141 with dissolve
                mom "I'm ready, {b}[firstname]{/b}!"
                mom "Give it to me..."
                hide momp
                show moms 148 at Position(xpos=0.5202, ypos=.8575)
                with dissolve
                pause
                show moms 149 at Position(xpos=0.5208, ypos=.8950) with dissolve
                mom "Oh, give me that big dick!"
                show moms 150 at Position(xpos=0.5208, ypos=.8960) with dissolve
                mom "Ahhh..."
                mom "Yes..."
                show moms 151 at Position(xpos=0.5100, ypos=.8580) with dissolve
                mom "Yes!"
                $ M_mom.set('sex speed', M_mom.get('sex speed') / 3)
                show moms 151_152_153_154_155_156_157
                mom "YES!!!"
                pause 4
                mom "Oh, god..."
                pause 4
                mom "It's so good!"
                pause 4
                mom "Oh, {b}[firstname]{/b}!"
                pause 4
                player_name "Uhhh..."
                mom "That's it, Baby. Fuck Mommy!"
                pause 4
                mom "Fuck Mommy Harder!"
                $ M_mom.set('sex speed', M_mom.get('sex speed') / 2)
                show moms 151_152_153_154_155_156_157
                pause
                mom "Aaahh!"
                pause 4
                player_name "You like that, [mom_name]?"
                mom "Yes, Baby!"
                pause 4
                mom "Aahh, god!"
                pause 4
                mom "Harder! Harder, {b}[firstname]{/b}!"
                pause
                $ M_mom.set('sex speed', M_mom.get('sex speed') / 2)
                show moms 151_152_153_154_155_156_157
                mom "That's it!!!"
                pause 4
                mom "AAAAAHHHH!!!"
                player_name "Oh, god!"
                pause
                label mom_movie_night_sex_options:
                    menu:
                        "Keep going.":
                            show moms 151_152_153_154_155_156_157
                            pause
                            jump mom_movie_night_sex_options
                        "Cum.":

                            player_name "[mom_name], I'm can't hold it."
                            mom "It's okay, Sweetie."
                            mom "I'm there too!"
                            mom "I'm gonna-"
                            mom "I'M CUMMING!!"
                            player_name "Hhhnngggg!!!"
                            show moms 158 with flash
                            mom "AAAAHHHHHH!!!"
                            pause
                            show moms 159 at Position(xpos=0.5200, ypos=.8915) with dissolve
                            player_name "Haaah... Haaah..."
                            show moms 161 with dissolve
                            mom "That was amazing, {b}[firstname]{/b}!"
                            show moms 160
                            player_name "Haaah... Yeah."
                            show moms 161
                            mom "I love you, Sweetie."
                            show moms 160
                            player_name "I love you too."
                            show moms 162 at Position(xpos=0.5200, ypos=.8575) with dissolve
                            mom "Such a good boy..."

        hide momf
        hide momfa
        hide moms
        hide playerf
        hide playerfa
        hide playerfb
        scene location_home_livingroom_night_blur
        show player 2 at left with dissolve
        show mom 61 at right with dissolve
        player_name "That was wonderful, [mom_name]."
        show player 1
        show mom 62
        mom "It sure was, Sweetie! You wore Mommy out!"
        show player 2
        show mom 61
        player_name "Yeah, I'm tired too."
        show player 1
        show mom 62
        mom "... Did you wanna sleep in my bed tonight?"
        menu:
            "Yes":
                show player 2
                show mom 61
                player_name "Sure, I'd love too."
                show player 1
                show mom 62
                mom "Great! I sleep so much better beside you..."
                show player 2
                show mom 61
                player_name "Y-yeah, me too."
                hide mom
                hide player
                scene black
                with fade
                jump mom_sleeping
            "No":

                show player 10
                show mom 61
                player_name "Oh uh, actually, [mom_name]..."
                player_name "I'm gonna sleep in my bed tonight."
                player_name "... Sorry."
                show player 11
                show mom 63
                mom "Oh, that's fine, Sweetie."
                mom "That's probably for the best."
                show mom 63b
                player_name "..."
                show player 10
                player_name "Well, goodnight, [mom_name]."
                show player 11
                show mom 63
                mom "Goodnight, {b}[firstname]{/b}."
                hide mom
                hide player
                with dissolve
    $ M_mom.set("movie night", False)
    $ M_mom.trigger(T_mom_watch_movie)
    $ unlock_ui()
    $ gTimer.tick(4)
    $ callScreen(location_count)

label couch_dialogue:
    scene home_livingroom_n_c with None
    show player 11 at left
    with dissolve
    player_name "( Someone's definitely in here. )"
    scene home_livingroom_couch01
    show sissex 1 zorder 2
    with dissolve
    pause
    show sissex 4
    show player 298 zorder 1 at Position(xpos=450,ypos=308) with dissolve
    player_name "( Is that... lesbian porn? )"
    show sissex 1
    player_name "( Since when do we have that channel? )"
    show sissex 4
    show player 299 at Position(xpos=555,ypos=337) with dissolve
    player_name "( This is some pretty hardcore stuff. )"
    show sissex 3
    show player 300 at Position(xpos=566,ypos=331)
    player_name "!!!" with vpunch
    show sissex 2
    show player 302 at Position(xpos=593,ypos=387) with fastdissolve
    player_name "( Oh, crap! )"
    show sissex 3
    show player 301 at Position(xpos=602,ypos=386) with fastdissolve
    player_name "( {b}[sis_name]{/b} is here... )"
    show sissex 2
    player_name "( She is't wearing panties?! )"
    show sissex 4
    player_name "( It looks like she's playing with herself... )"
    player_name "( ...and she doesn't know I'm here. )"
    $ sis_couch01.finish()
    $ sister.add_event(sis_couch02)
    menu:
        "Leave.":
            player_name "( I better leave before she sees me. )"
            hide player with fastdissolve
            show unlock33 zorder 3 at truecenter
            pause
            hide unlock33 with dissolve
            hide sissex
            jump home_entrance
        "Keep watching.":

            show sissex 2_3_1_4
            pause 8
            show sissex 1
            player_name "( That's hot, but I shouldn't push my luck. )"
            hide player with fastdissolve
            show unlock33 zorder 3 at truecenter
            pause
            hide unlock33 with dissolve
            hide sissex
            jump home_entrance

label home_livingroom_tv_locked:
    scene expression gTimer.image("home_livingroom{}_b") with None
    show popup_tv_locked at truecenter with dissolve
    pause
    hide popup_tv_locked with dissolve
    $ callScreen(location_count)

label home_livingroom_tv:
    if masturbated_tv:
        if sister.known(sis_couch02) and M_mom.is_set("jerk available"):
            scene home_livingroom_n_b with None
            show player 11
            with dissolve
            player_name "( I'm not risking that again, tonight... )"
            player_name "( I should go to bed. )"
        else:

            scene home_livingroom_n_b with None
            show player 11
            with dissolve
            player_name "( I think that's enough for one night. )"
            player_name "( I should go to bed. )"
        hide player with dissolve
        hide home_livingroom_n
        jump home_livingroom_dialogue
    $ tv_channel = 0
    jump tv_channel_responses

label tv_channel_responses:
    if sister.started(sis_couch03) and gTimer.is_evening():
        scene home_livingroom_couch01 with None
        show playersex 82 at Position(xpos=497)
        with dissolve
        player_name "Let's see what's on TV..."

        scene home_livingroom_tv
        show home_tv_channel_08 at Position(xpos = 522, ypos = 521)
        player_name "( Someone left it on the Pink Channel? )"
        player_name "The password was..."
        pause .4
        show text "{color=#ff4bdf}L6bv12R{/color}" as username at Position(xpos = 433, ypos = 341)
        pause .4
        show text "{color=#ff4bdf}12345{/color}" as password at Position(xpos = 423, ypos = 411)
        pause 1
        hide username
        hide password
        show home_tv_channel_10 at Position(xpos = 522, ypos = 521)
        player_name "Woah!"
        player_name "( I've never seen someone use their feet like {b}that{/b}. )"
        player_name "( Actually, that's kind of hot. )"
        jump couch_footjob

    scene home_livingroom_tv

    $ pink_user = ""
    $ pink_pass = ""

    if tv_channel == -1:
        $ tv_channel = 7

    elif tv_channel == 8:
        $ tv_channel = 0

    if tv_channel == 0 and not tv_channel_1_seen:
        show home_tv_channel_01 at Position(xpos=522, ypos=521)
        player_name "Hmm... Let's see what's on TV."
        $ tv_channel_1_seen = True

    elif tv_channel == 1 and not tv_channel_2_seen:
        show home_tv_channel_02 at Position(xpos=522, ypos=521)
        player_name "( Local news. Boring! )"
        $ tv_channel_2_seen = True

    elif tv_channel == 2 and not tv_channel_3_seen:
        show home_tv_channel_03 at Position(xpos=522, ypos=521)
        player_name "( That's the kind of sport I could get into. )"
        $ tv_channel_3_seen = True

    elif tv_channel == 3 and not tv_channel_4_seen:
        show home_tv_channel_04 at Position(xpos=522, ypos=521)
        player_name "( Hey, it's Mayor Rump! )"
        $ tv_channel_4_seen = True

    elif tv_channel == 4 and not tv_channel_5_seen:
        show home_tv_channel_05 at Position(xpos=522, ypos=521)
        player_name "..."
        player_name "( These nature channels are so strange... )"
        $ tv_channel_5_seen = True

    elif tv_channel == 5 and not tv_channel_6_seen:
        show home_tv_channel_06 at Position(xpos=522, ypos=521)
        player_name "( Who watches this stuff? )"
        $ tv_channel_6_seen = True

    elif tv_channel == 6 and not tv_channel_7_seen:
        show home_tv_channel_07 at Position(xpos=522, ypos=521)
        player_name "( This channel's a dud. )"
        $ tv_channel_7_seen = True

    elif tv_channel == 7:
        if sis_watch_tv_tonight and gTimer.is_evening():
            $ tv_pink_channel = 8

        elif sister.over(sis_couch03):
            $ tv_pink_channel = renpy.random.randint(7,8)
        else:

            $ tv_pink_channel = 7

        if tv_pink_channel == 7 and not tv_channel_pink:
            show home_tv_channel_09 at Position(xpos=522, ypos=521)
            if gTimer.is_evening():
                if sister.completed(sis_couch02)and M_mom.is_set("jerk available"):
                    pause .4
                    hide home_tv_channel_09
                    scene home_livingroom_couch01
                    show playersex 82 at Position(xpos=497)
                    with dissolve
                    player_name "( That's pretty hot. )"
                    show playersex 83 with fastdissolve
                    player_name "( Hmm... )"
                    player_name "( Everyone should be sleeping. )"
                    show playersex 84 with fastdissolve
                    player_name "( I'll just have to be quiet... )"
                    show playersex 85 with fastdissolve
                    pause .4
                    show playersex 86_85
                    pause 8
                    scene home_livingroom_couch02
                    show playersex 80 at Position(xpos=497)
                    player_name "!!!" with hpunch
                    player_name "( Oh, Shit! {b}[mom_name]{/b}'s coming out of her room! )"
                    show playersex 81
                    pause
                    show mom 126 at Position (xpos=917,ypos=694)
                    show player 303 at left
                    hide playersex
                    with dissolve
                    pause
                    show mom 127 at Position (xpos=872,ypos=540) with fastdissolve
                    mom "Is someone in here?"
                    show mom 128 at Position (xpos=862,ypos=511) with fastdissolve
                    mom "Oh, my!"
                    show mom 129
                    player_name "( Shit-shit-shit! I left the TV on! )"
                    show player 305
                    show mom 132 at Position (xpos=680,ypos=768) with dissolve
                    mom "I wonder who..."
                    show player 304
                    mom "No, It can't be him. It must be his sister."
                    mom "They never used to do this sort of thing."
                    mom "Maybe I'm being too lenient..."
                    show player 305
                    show mom 133 at Position (xpos=812,ypos=767) with fastdissolve
                    mom "{b}*sigh*{/b}"
                    mom "They'll be fine. I'm going back to bed."
                    show mom 134 at Position (xpos=868,ypos=546) with fastdissolve
                    pause
                    scene home_livingroom_couch01
                    show player 305 at left
                    with dissolve
                    pause
                    show player 306
                    player_name "Man, that was close!"
                    player_name "( Too close... )"
                else:

                    player_name "( Woah! That's the one she was watching last time. )"
                    hide home_tv_channel_09
                    scene home_livingroom_couch01
                    show playersex 82 at Position(xpos=497)
                    with dissolve
                    player_name "( That's pretty hot. )"
                    show playersex 83 with fastdissolve
                    player_name "( Hmm... )"
                    player_name "( Everyone should be sleeping. )"
                    show playersex 84 with fastdissolve
                    player_name "( I'll just have to be quiet. )"
                    show playersex 85 with fastdissolve
                    pause .4
                    show playersex 86_85
                    pause 8
                    player_name "( Almost there... )"
                    show playersex 86
                    show white
                    pause 0.001
                    show playersex 87
                    hide white
                    with dissolve
                    pause
                    show playersex 88 with fastdissolve
                    pause
                    show playersex 85b
                    player_name "( It looks like they have new porn videos every night. )"
                    player_name "( I should {b}come back another time{/b} to watch some... )"
                    show playersex 89
                    with dissolve
                    player_name "( Damn it. I made a mess. )"
                    player_name "( I better clean this up before someone walks in. )"
                    $ sis_couch02.finish()
                hide player
                hide home_livingroom_couch01
                $ masturbated_tv = True
                jump home_livingroom_dialogue

        elif tv_pink_channel == 8 and not tv_channel_pink:
            show home_tv_channel_10 at Position(xpos=522, ypos=521)
            if gTimer.is_evening():
                if sis_watch_tv_tonight:
                    scene home_livingroom_couch01
                    show playersex 82 at Position(xpos=497)
                    with dissolve
                    pause
                    show playersex 83
                    player_name "( Hmm... )"
                    player_name "( I guess she decided not to come down. )"
                    show playersex 84 with fastdissolve
                    player_name "( Oh well, since I'm already here... )"
                    show playersex 85 with fastdissolve
                    pause
                    show playersex 86_85
                    pause 4
                    show playersex 86
                    show sis 77 at Position(xpos=559,ypos=333) with dissolve
                    pause
                    show playersex 85
                    show sis 78 at Position(xpos=878,ypos=510) with dissolve
                    pause
                    show sis 79
                    show playersex 90
                    sis "What, you really couldn't wait for me?" with hpunch
                    sis "You wouldn't want to miss out on your sister's feet, now would you?"
                    show sis 78
                    player_name "I... I didn't know if you'd come!"
                    hide sis
                    show playersex 92 at Position(xpos=533)
                    with dissolve
                    sis "Why are you hiding it?"
                    show playersex 94
                    sis "No one's around, idiot." with fastdissolve
                    show playersex 95
                    sis "Come on, let's see that horny cock of yours." with fastdissolve
                    show playersex 97 with fastdissolve
                    pause
                    show playersex 96_97
                    pause 4
                    show playersex 97
                    menu:
                        "Jump on her." if pStats.dex() < 7:
                            show playersex 108
                            sis "You want to cum on my feet, don't you?"
                            show playersex 109
                            player_name "Yes..."
                            show playersex 108
                            sis "You're such a pervert."
                            show playersex 131 at Position(xpos=587)
                            sis "[dex_warn]What are you doing?!" with hpunch
                            show playersex 132
                            sis "[dex_warn]Who said you could touch me?!"
                            sis "[dex_warn]I think you got more than you deserved for today."
                            sis "[dex_warn]Go finish in your room, pervert.."
                            hide playersex
                            hide sis
                            $ masturbated_tv = True
                            $ sis_watch_tv_tonight = False
                            jump home_livingroom_dialogue

                        "Jump on her." if pStats.dex() >= 7:
                            show playersex 108
                            sis "You want to cum on my feet, don't you?"
                            show playersex 109
                            player_name "Yes..."
                            show playersex 108
                            sis "You're such a pervert."
                            show playersex 133 at Position(xpos=578)
                            sis "What are you-" with hpunch
                            show playersex 134 at Position(xpos=553)
                            player_name "{b}[sis_name]{/b}!!!"
                            show playersex 135
                            player_name "I want you! Now!"
                            show playersex 136
                            sis "You pervert!!! Ahh!!!"
                            show playersex 137
                            pause
                            $ M_sis.set('sex speed', .4)
                            show playersex 134_135_136_137
                            pause 8
                            sis "Stop moving your hips like that... It's... Too deep!!"
                            show playersex 134
                            sis "We... We have to stop..."
                            show playersex 135
                            sis "We're too loud. {b}[mom_name]{/b} will..."
                            show playersex 136
                            sis "... It's so good!!"
                            show playersex 137

                            label sis_couch_sex_loop:
                                hide screen sis_couch_sex_options
                                show screen xray_scr
                                pause
                                hide screen xray_scr
                                if anim_toggle:
                                    $ animcounter = 0
                                    while animcounter < 4:
                                        show playersex 134_135_136_137
                                        pause 5
                                        if animcounter == 1:
                                            sis "Ahhhh!!!{p=1}{nw}"
                                        if animcounter == 3:
                                            sis "Oh!!!{p=1}{nw}"
                                            player_name "Uhhh...{p=1}{nw}"
                                        pause 3
                                        $ animcounter += 1
                                else:

                                    $ animcounter = 0
                                    while animcounter < 4:
                                        show playersex 134
                                        pause
                                        show playersex 135
                                        pause
                                        show playersex 136
                                        pause
                                        show playersex 137
                                        pause
                                        if animcounter == 1:
                                            sis "Ahhhh!!!"
                                        if animcounter == 3:
                                            sis "Oh!!!"
                                            player_name "Uhhh..."
                                        $ animcounter += 1

                                show screen sis_couch_sex_options
                                pause
                                jump sis_couch_sex_loop

                                label sis_couch_sex_cum:
                                    hide screen sis_couch_sex_options
                                    if anim_toggle:
                                        sis "...Are you?!"
                                        player_name "I'm cumming!!"
                                        sis "Don't-"
                                    else:
                                        show playersex 134
                                        sis "...Are you?!"
                                        show playersex 135
                                        player_name "I'm cumming!!"
                                        show playersex 136
                                        sis "Don't-"
                                    show playersex 138
                                    sis "{b}AHHH{/b}!!!" with hpunch
                                    show white
                                    hide white with dissolve
                                    pause
                                    show white
                                    hide white with fastdissolve
                                    pause
                                    show playersex 142 at Position(xpos=574)
                                    sis "What the {b}FUCK{/b}?!" with dissolve
                                    show playersex 141
                                    player_name "I'm sorry!! I couldn't hold it..."
                                    show playersex 142
                                    sis "Why do you keep cumming inside me, you {b}IDIOT{/b}!?"
                                    show playersex 141
                                    player_name "I don't know..."
                                    show playersex 140
                                    sis "Ugh..."
                                    sis "You know I need you fresh and rested for my cam shows!!"
                                    sis "And what if I get {b}pregnant{/b}?!"
                                    show playersex 139
                                    player_name "..."
                                    show playersex 141
                                    sis "I really shouldn't watch these pornos with you..."
                                    sis "I have to clean myself up now."
                                    sis "Thanks a lot, pervert."
                                    hide playersex
                                    hide sis
                                    $ masturbated_tv = True
                                    $ sis_watch_tv_tonight = False
                                    jump home_livingroom_dialogue
                        "Cum.":

                            pause .4
                            show playersex 108
                            sis "You want to cum on my feet, don't you?"
                            show playersex 109
                            player_name "Yes..."
                            show playersex 108
                            sis "You're such a pervert."
                            show playersex 97
                            player_name "Stop! I'm-"
                            show white
                            pause 0.001
                            show playersex 98
                            hide white with dissolve
                            pause
                            show playersex 99 with dissolve
                            player_name "Ahh..."
                            show playersex 100 with fastdissolve
                            sis "Gross..."
                            show playersex 101
                            player_name "Sorry about the mess..."
                            show playersex 100
                            sis "Next time you need something, just ask!"
                            show playersex 103
                            sis "Now get me a tissue box, so I can clean this off, you pervert!" with hpunch
                            hide playersex
                            hide sis
                            $ masturbated_tv = True
                            $ sis_watch_tv_tonight = False
                            jump home_livingroom_dialogue
                else:

                    label couch_footjob:
                        pause .4
                        hide home_tv_channel_10
                        scene home_livingroom_couch01
                        show playersex 83 at Position(xpos=497)
                        player_name "( Hmm... )"
                        player_name "( The others should be asleep. )"
                        show playersex 84 with fastdissolve
                        player_name "( I'll just have to be quiet. )"
                        show playersex 85 with fastdissolve
                        pause .4
                        show playersex 86_85
                        pause 8
                        show playersex 86
                        show sis 77 at Position(xpos=559,ypos=333) with dissolve
                        pause
                        show playersex 85
                        show sis 78 at Position(xpos=878,ypos=510) with dissolve
                        pause
                        show sis 79
                        show playersex 90
                        sis "Well, well!" with hpunch
                        sis "Really?"
                        sis "You don't think I saw that?"
                        hide sis
                        show playersex 92 at Position(xpos=533)
                        with dissolve
                        sis "So, I was wondering..."
                        sis "How exactly were you able to access the Pink Channel?"
                        show playersex 91
                        player_name "It was already there when I turned the TV on!"
                        show playersex 92
                        sis "I think you're lying."
                        sis "I also think you went through someone else's emails, and found their Pink Channel subscription."
                        show playersex 91
                        player_name "I'm sorry... I didn't-"
                        show playersex 92
                        sis "Cut the crap!"
                        show playersex 93
                        sis "If you were so horny..."
                        show playersex 92
                        sis "... you could've just asked me for it."
                        show playersex 91
                        player_name "I..."
                        show playersex 92
                        sis "So..."
                        sis "You're into feet, huh?"
                        show playersex 91
                        player_name "I don't know what you mean."
                        show playersex 94
                        sis "I think..." with fastdissolve
                        show playersex 95
                        sis "... you know exactly what I mean." with fastdissolve
                        show playersex 108
                        sis "Just like this, right?" with fastdissolve
                        show playersex 97
                        pause .4
                        $ anim_toggle = False
                        label couch_footjob_loop:
                            show screen sex_anim_buttons
                            pause
                            if anim_toggle == True:
                                hide screen sex_anim_buttons
                                hide playersex 97
                                show playersex 96_97 at Position(xpos=533)
                                pause 8
                                hide playersex 96_97
                                show playersex 97 at Position(xpos=533)
                            else:

                                hide screen sex_anim_buttons
                                $ animcounter = 0
                                while (animcounter < 2):
                                    show playersex 96
                                    pause
                                    show playersex 97
                                    pause
                                    $ animcounter += 1
                                show playersex 96
                                pause
                                show playersex 97
                        menu:
                            "Keep Going.":
                                jump couch_footjob_loop
                            "Cum.":

                                pause .4
                                show playersex 108
                                sis "How is it?"
                                show playersex 109
                                sis "Does this feel good?"
                                show playersex 108
                                sis "You little pervert..."
                                show playersex 97
                                player_name "Stop! I'm-"
                                show white
                                pause 0.001
                                show playersex 98
                                hide white with dissolve
                                pause
                                show playersex 99 with dissolve
                                player_name "Ahh..."
                                show playersex 100 with fastdissolve
                                sis "Gross..."
                                show playersex 101
                                player_name "Sorry about the mess..."
                                show playersex 100
                                sis "Next time you need something, just ask!"
                                show playersex 103
                                sis "Now get me a tissue box, so I can clean this off, you pervert!" with hpunch
                                hide playersex
                                hide sis
                                $ sis_couch03.finish()
                                $ masturbated_tv = True
                                jump home_livingroom_dialogue

        elif not tv_channel_8_seen:
            show home_tv_channel_08 at Position(xpos=522, ypos=522)
            player_name "Pink channel?"
            player_name "( That must be the channel my sister was watching. )"
            player_name "( I wonder where I could find her account password... )"
            player_name "( I bet they emailed it to her. )"
            $ tv_channel = 7
            $ tv_channel_8_seen = True
    hide home_tv_channel_01
    hide home_tv_channel_02
    hide home_tv_channel_03
    hide home_tv_channel_04
    hide home_tv_channel_05
    hide home_tv_channel_06
    hide home_tv_channel_07
    hide home_tv_channel_08
    hide home_tv_channel_09
    hide home_tv_channel_10
    call screen home_livingroom_tv

label tv_pink_channel_pass_check:
    if pink_user.lower().strip() == "l6bv12r" and pink_pass.strip() == "12345":
        $ tv_channel_pink = False
        jump tv_channel_responses
    else:

        show home_tv_channel_08 at Position(xpos=522, ypos=522)
        show sis_wrong_pass at Position(xpos=520, ypos= 510) with dissolve
        pause 1
        hide sis_wrong_pass with dissolve
        jump tv_channel_responses

label mom_bedroom_locked:
    scene expression gTimer.image("home_livingroom{}_b")
    if not gTimer.is_dark():
        if not erik.over(erik_intro):
            show player 22 at left
            show mom 2 at right
            with dissolve
            mom "{b}[firstname]{/b}? Are you looking for something in my room?"
            show player 21 at left
            show mom 1 at right
            player_name "I was... Umm... Looking for my phone!"
            show player 18 at left
            player_name "But it's right here in my pocket actually!"
            show mom 3 at right
            show player 11 at left
            mom "Isn't {b}Erik{/b} waiting for you?"
            show mom 1 at right
            show player 17 at left
            player_name "Yeah, I'm on my way!"
        else:

            show player 10 with dissolve
            player_name "( I shouldn't snoop around {b}[mom_name]'s{/b} bedroom. )"
    else:


        if M_mom.get_state() == S_mom_debt_call:
            show player 10 with dissolve
            player_name "( I should see go see if {b}[mom_name]{/b} is alright. )"
        else:

            show player 10 with dissolve
            player_name "( I really shouldn't disturb {b}[mom_name]{/b} when she's sleeping. )"
    hide player
    hide mom
    with dissolve
    $ callScreen(location_count)

label mom_lotion_block:
    if location_count == "Entrance":
        scene home_entrance
    elif location_count == "Living Room":
        scene home_livingroom_b
    elif location_count == "Kitchen":
        scene homekitchen
    show player 14 with dissolve
    if M_mom.is_set("retrieved lotion"):
        $ tmp = where_is("mom")
        player_name "I need to go to the {b}[tmp]{/b} to give the lotion to {b}[mom_name]{/b}."
    else:
        player_name "{b}[mom_name]{/b} said the {b}lotion is in her bedroom dresser{/b}."
    hide player with dissolve
    $ callScreen(location_count)

label mom_movie_block:
    if location_count == "Entrance":
        scene home_entrance_night
    elif location_count == "Living Room":
        scene home_livingroom_n_b
    show player 13 with dissolve
    player_name "{b}[mom_name]{/b} is waiting for me in the {b}living room{/b}..."
    player_name "I should go join her."
    hide player with dissolve
    $ callScreen(location_count)

label mom_laundry_block:
    scene home_livingroom_b
    show player 14 with dissolve
    player_name "{b}[mom_name]'s note{/b} said the {b}laundry is in her bedroom{/b}."
    hide player with dissolve
    $ callScreen(location_count)

label sis_couch_faster_sex:
    $ M_sis.set('sex speed', M_sis.get('sex speed') - 0.1)
    jump sis_couch_sex_loop

label sis_couch_slower_sex:
    $ M_sis.set('sex speed', M_sis.get('sex speed') + 0.1)
    jump sis_couch_sex_loop