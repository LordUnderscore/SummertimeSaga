label backyard_dialogue:
    $ location_count = "Backyard"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_mom.get_state() == S_mom_midnight_search:
        jump mom_midnight_swim
    $ callScreen(location_count)

label backyard_chair_dialogue:
    $ callScreen(location_count)

label mom_pool_dialogue:
    if M_mom.get_state() == S_mom_fetch_towel and towel not in inventory.items:
        scene backyard_n_c
        show mom 204 at left
        show player 13f at right
        with dissolve
        mom "Did you forget to get me a {b}towel from the bathroom{/b}?"
        show mom 205
        show player 14f
        player_name "Sorry! I'll be right back."
    else:

        scene home_diningroom_n_c
        show mom 207 at left
        show player 10f at right
        with dissolve
        player_name "!!!"
        show player 14f
        player_name "You startled me. I thought you were still outside."
        show player 239_240f with dissolve
        pause
        show player 495f with dissolve
        player_name "Here's the towel."
        show player 494f
        show mom 208
        mom "You know what, I don't think I need it anymore..."
        mom "I feel warmer and a lot better now that I'm inside."
        show player 11f with dissolve
        mom "See something you like?"
        show player 26f
        show mom 209_210 with dissolve
        mom "...I've always noticed you staring at my boobs..."
        mom "Do you..."
        mom "Do you want to touch them?"
        show mom 207 with dissolve
        show player 11f
        player_name "{b}*Gulp*{/b}"
        show player 10f
        player_name "I... Uhhh-"
        show player 5f
        show mom 209_210 with dissolve
        mom "What's the matter? I know you're not always this shy..."
        show mom 208 with dissolve
        mom "...Or do you want more from your momma?"
        show mom 207
        show player 11f
        player_name "!!!"
        show mom 208
        mom "Tell you what."
        mom "I think I need something more then your hands right now..."
        show mom 183bf with dissolve
        show player 434f
        show mom 184df with dissolve
        mom "I need something from you."
        show mom 184cf
        show player 435f
        player_name "I..."
        show player 434f
        show mom 184df
        mom "Be a good boy and come over here."
        mom "Mommy wants to feel your fingers."
        hide player
        show mom 190f
        show player finger 193bf
        with dissolve
        player_name "Uhh... Okay..."
        show mom 191f
        mom "Put your fingers in here, Sweetie."
        show mom 193f with dissolve
        mom "Mommy wants you to slide your fingers...inside..."
        $ M_mom.set("sex speed", .225)
        $ M_mom.set("sex flip", True)
        $ M_mom.set("robe on", False)
        $ first_pass = True

        label mom_finger_loop:
            show screen sex_anim_buttons
            pause
            hide screen sex_anim_buttons
            hide player
            if anim_toggle:
                $ animcounter = 0

                while animcounter < 4:
                    if M_mom.is_set("sex flip"):
                        show mom 194f_195f_196f at left
                        if M_mom.is_set("robe on"):
                            show mom_robe 194bf_195bf_196bf
                    else:

                        show mom 194_195_196 at right
                        if M_mom.is_set("robe on"):
                            show mom_robe 194b_195b_196b
                    pause 4

                    if animcounter == 0:
                        if randomizer() <= 50:
                            mom "Ohh...{p=1}{nw}"
                            mom "Just like that, Sweetie.{p=2}{nw}"
                        else:

                            mom "Your fingers... So good...{p=2}{nw}"
                            mom "You're such a good boy...{p=2}{nw}"

                    if animcounter == 1:
                        if randomizer() <= 50:
                            mom "Oh, baby...{p=1}{nw}"
                        else:

                            mom "How did you get so good?{p=2}{nw}"

                    if M_mom.get_state() != S_mom_fetch_towel and first_pass and randomizer() <= 50 and animcounter == 2:
                        $ first_pass = False
                        player_name "You're so wet {b}[mom_name]{/b}.{p=2}{nw}"
                        player_name "What were you thinking about before I came into the kitchen?{p=3}{nw}"
                        mom "...You..."

                    elif M_mom.get_state() != S_mom_fetch_towel and first_pass and animcounter == 2:
                        $ first_pass = False
                        player_name "Do you like having your son finger you on the kitchen counter?{p=3}{nw}"
                        mom "Oh, baby...I...I...{p=2}{nw}"
                        mom "I do...{p=1}{nw}"
                        mom "Your Momma is a naughty girl...{p=2}{nw}"

                    if animcounter == 3:
                        if randomizer() <= 50:
                            mom "I'm... I'm...almost!{p=2}{nw}"
                        else:

                            mom "Oh!!!{p=1}{nw}"
                            mom "That's the spot, Sweetie!{p=2}{nw}"
                            mom "Ahh!!{p=1}{nw}"
                    pause 3

                    $ animcounter += 1
            else:

                $ animcounter = 0

                while animcounter < 4:
                    if M_mom.is_set("sex flip"):
                        show mom 194f at left
                        if M_mom.is_set("robe on"):
                            show mom_robe 194bf
                        pause
                        show mom 195f
                        if M_mom.is_set("robe on"):
                            show mom_robe 195bf
                        pause
                        show mom 196f
                        if M_mom.is_set("robe on"):
                            show mom_robe 196bf
                    else:

                        show mom 194 at right
                        if M_mom.is_set("robe on"):
                            show mom_robe 194b
                        pause
                        show mom 195
                        if M_mom.is_set("robe on"):
                            show mom_robe 195b
                        pause
                        show mom 196
                        if M_mom.is_set("robe on"):
                            show mom_robe 196b
                    pause

                    if animcounter == 0:
                        if randomizer() <= 50:
                            mom "Ohh..."
                            mom "Just like that, Sweetie."
                        else:

                            mom "Your fingers... So good..."
                            mom "You're such a good boy..."

                    if animcounter == 1:
                        if randomizer() <= 50:
                            mom "Oh, baby..."
                        else:

                            mom "How did you get so good?"

                    if M_mom.get_state() != S_mom_fetch_towel and first_pass and randomizer() <= 50 and animcounter == 2:
                        $ first_pass = False
                        player_name "You're so wet {b}[mom_name]{/b}."
                        player_name "What were you thinking about before I came into the kitchen?"
                        mom "...You..."

                    elif M_mom.get_state() != S_mom_fetch_towel and first_pass and animcounter == 2:
                        $ first_pass = False
                        player_name "Do you like having your son finger you on the dining room table?"
                        mom "Oh, baby...I...I..."
                        mom "I do..."
                        mom "Your Momma is a naughty girl..."

                    if animcounter == 3:
                        if randomizer() <= 50:
                            mom "I'm... I'm...almost!"
                        else:

                            mom "Oh!!!"
                            mom "That's the spot, Sweetie!"
                            mom "Ahh!!"

                    $ animcounter += 1

            call screen mom_finger_options

        label mom_finger_cum:
            hide screen mom_finger_options
            if M_mom.get_state() == S_mom_fetch_towel:
                mom "Oh!"
                mom "Sweetie!"
            else:

                player_name "Ready for me to stop teasing you?"
                mom "Yes, you naughty boy!"
                mom "I want to cum!"
                $ M_mom.set('sex speed', .100)
                if M_mom.is_set("sex flip"):
                    show mom 194f_195f_196f at left
                    if M_mom.is_set("robe on"):
                        show mom_robe 194bf_195bf_196bf
                else:

                    show mom 194_195_196 at right
                    if M_mom.is_set("robe on"):
                        show mom_robe 194b_195b_196b
                pause
                pause
                mom "Oh!!!!"
                mom "Yes!!!"

            if M_mom.is_set("sex flip"):
                show player finger 193bf zorder 3
                show mom 197f
                if M_mom.is_set("robe on"):
                    show mom_robe 197bf
            else:

                show player finger 193b zorder 3
                show mom 197
                if M_mom.is_set("robe on"):
                    show mom_robe 197b
            with flash
            mom "AHHH!"
            pause

            if M_mom.get_state() == S_mom_fetch_towel:
                show mom 197ff at left
                show player 11f at Position (xpos=600)
                with dissolve
                mom "Sweetie?"
                show mom 197cf
                show player 12f
                player_name "Yea-"
                show player 11f
                show mom 197df
                mom "Oh, no... no no no... NO!"
                mom "What am I doing..."
                show mom 197ff
                mom "What did I just..."
                show mom 197cf
                show player 10f
                player_name "What's wrong, {b}[mom_name]{/b}?"
                show player 11f
                show mom 197ff
                mom "Sweetie, I'm sorry."
                show mom 197df
                mom "I...I've had to much to drink."
                mom "I need to go to bed."
                show mom 197ff
                mom "I'm so sorry."
                show mom 197df
                mom "I-"
                hide mom with fastdissolve
                show player 10 at center with dissolve
                player_name "{b}[mom_name]{/b}?"
                show player 10
                player_name "I was really close..."
                show player 5
                pause
                show player 24
                player_name "I hope she's okay..."
                pause
                show player 25
                player_name "I should get some sleep and talk to her tomorrow."
                hide player with dissolve
                $ M_mom.trigger(T_mom_gave_towel)
                $ unlock_ui()
                $ location_count = "Dining Room"
            else:

                show player 13 zorder 0 at Position (xoffset=-118)
                show mom 184d
                if M_mom.is_set("robe on"):
                    show mom_robe 184f
                with dissolve

                if randomizer() <= 50:
                    mom "Oh, baby, that was wonderful."
                    show mom 184c
                    show player 14 at Position (xoffset=-118)
                    player_name "Thanks {b}[mom_name]{/b}."
                else:

                    mom "Oh! That was awesome. I've still got the shivers!"
                    mom "I bet that cock of yours is hard as a rock."
                    show mom 184c
                    show player 14 at Position (xoffset=-118)
                    player_name "Yeah, it was fun making you cum."
                show player 13 at Position (xoffset=-118)
                show mom 184d
                mom "If you want mommy to take care of that for you, just let me know."
        $ gTimer.tick()
    hide player
    hide mom
    hide mom_robe
    with dissolve
    $ callScreen(location_count)

label mom_midnight_swim:
    scene home_diningroom_cs01 with fade
    show text "As I approached the door I could feel my heart pounding in my chest...\nWhat was happening outside at this hour of the night, I thought...\nI reached to pull aside the patio door...\n...and peered into our moonlit backyard." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide home_diningroom_cs01
    with dissolve

    scene home_backyard_pool_c
    show mom 214
    mom "Ha ha ha! What are you doing?"
    show mom 212
    dia "What you're to big to hug your sister?"
    show mom 214
    dia "Ha ha ha!"
    mom "Ha ha ha!"
    show mom 211
    dia "You know, sometimes I forget your boobs are as big as mine!"
    show mom 213
    mom "I don't know about that! I think yours are bigger!"
    mom "Although, it's probably all to do with your little side business."
    show mom 212
    dia "Maybe, you should try it sometime..."
    show mom 215
    dia "The feeling alone sends shivers down my spine..."
    show mom 213
    mom "You're such a pervert!"
    show mom 211
    dia "Oh yeah? And you're not?"
    show mom 214
    mom "Ha ha ha!"
    dia "Ha ha ha!"
    show mom 212b_215b
    pause
    pause
    show mom 213
    mom "Let me go already!"
    mom "Before I pee myself!"
    mom "You're tickling me!"
    show mom 212
    dia "So? We're in the water!"
    show mom 213
    mom "Yeah, but it's my pool!"
    show mom 212
    dia "Whatever, Sis."
    show mom 200
    show aunt 170
    with dissolve
    pause
    show aunt 171
    dia "This is fun."
    dia "I haven't skinny dipped in a long time."
    show aunt 176
    dia "Not since we tag teamed your hubbie and my first husband down at pebble beach."
    show aunt 175
    show mom 201
    mom "Oh, that was fun..."
    show mom 198
    show aunt 170
    pause
    show mom 199
    mom "God, I miss sex..."
    show mom 198
    show aunt 173
    dia "Tell me about it."
    show aunt 172
    dia "Not one of my cukes compares to the feel of a real cock."
    show aunt 174
    dia "But don't worry. Now that your single, maybe we can get the ol' band back to together?"
    show aunt 175
    show mom 199
    mom "I don't know, {b}Diane{/b}..."
    show mom 198
    show aunt 176
    dia "Oh don't hold back on me."
    dia "Remember the wild and kinky times we used to have?"
    show aunt 175
    show mom 199
    mom "I do..."
    mom "But..."
    show mom 198
    show aunt 176
    dia "But what?"
    show aunt 175
    pause
    show mom 199
    mom "I... I may have done something wrong..."
    show mom 198
    show aunt 171
    dia "What happened?!"
    show aunt 170
    show mom 199
    mom "It's something quite...taboo..."
    show mom 198
    show aunt 171
    dia "Tell me! Tell me!"
    show aunt 170
    show mom 199
    mom "I can't! It's sooo wrong!"
    show mom 198
    show aunt 171
    dia "You have to tell me now!"
    show aunt 170
    mom "..."
    show aunt 174
    dia "Come on, Sis. You know me."
    show aunt 170
    show mom 201
    mom "I do and I'm sure you'd be fine with it."
    show mom 199
    mom "But I'm not."
    show mom 201
    mom "Not entirely..."
    show mom 198
    pause
    show aunt 171
    dia "Just spit it out, already!"
    show aunt 170
    pause
    show mom 199
    mom "I may do something bad with..."
    mom "...With {b}[firstname]{/b}."
    show mom 198
    show aunt 171
    dia "No way!"
    dia "Like what?"
    show aunt 170
    show mom 199
    mom "I don't know..."
    mom "I think I want to go all the way."
    show mom 198
    show aunt 176
    dia "!!!"
    show aunt 175
    show mom 199
    mom "I mean...it's all I think about lately."
    show mom 198
    show aunt 176
    dia "You really are a bad girl...and I like it."
    dia "I think you should do it."
    show aunt 175
    show mom 201
    mom "Of course you do."
    mom "But it's not your son."
    show mom 199
    mom "I'm his mother."
    mom "It's not something that should even cross a good mothers mind."
    show mom 198
    show aunt 174
    dia "Now you stop it."
    dia "You're a good mother."
    dia "And you're both grown adults."
    show aunt 176
    dia "Just be sure to fill me in on the juicy details after you jump his bone."
    show aunt 175
    show mom 201
    mom "Don't be so vulgar."
    mom "Gosh. I'm so horny now."
    show mom 200
    show aunt 173
    dia "You and me both."
    show aunt 175
    show mom 201
    mom "Don't you be eyeing my boy now."
    show mom 200
    show aunt 176
    dia "And don't you hoard him!"
    show aunt 175
    pause
    show mom 199
    mom "I can't believe I told you..."
    show mom 201
    mom "You and your wine..."
    show mom 200
    show aunt 172
    dia "Ha ha ha..."
    dia "Don't try and blame the wine, girl."
    show aunt 170
    pause
    show aunt 173
    dia "I'm so drunk..."
    dia "...And I have all this work I have to do tomorrow!!"
    show aunt 174
    dia "I should get going..."
    show aunt 170
    show mom 199
    mom "Just stay a little while longer!"
    show mom 198
    show aunt 176
    dia "I'm not falling for your tricks."
    show mom 200
    dia "Besides... Shouldn't you check up on your son?"
    show aunt 173
    dia "You know... If he's not sleeping, you could lay with-"
    show aunt 175
    show mom 201
    mom "Oh, stop it already and get your butt home."
    mom "I knew I shouldn't have told you."
    show mom 200
    show aunt 172
    dia "Ha ha ha!"
    show aunt 171
    dia "This was fun. We should do this again!"
    show aunt 177 with dissolve
    pause
    show mom 201
    mom "It was! Night, {b}Diane{/b}."
    show mom 202
    show aunt 178
    with dissolve
    dia "Woah!"
    dia "I'm...a bit...tipsy on dry land!"
    mom "Careful!"
    dia "You should be more careful!"
    dia "Look who has both the towels!"
    show aunt 179 with dissolve
    dia "Night, Sis! Have fun getting to home naked!"
    mom "Hey! {b}Diane{/b}!"
    hide aunt with dissolve
    pause
    show mom 199 with dissolve
    mom "That dumby..."
    mom "I'm not the one who lives across town..."
    show mom 198
    pause
    show mom 199
    mom "I should get back inside..."
    mom "I'm getting cold and she ran off with the towels."
    scene black with fade
    hide mom
    pause 1

    scene home_diningroom_n_c
    show player 26f with dissolve
    player_name "I should see if {b}[mom_name]{/b} needs help."
    hide player with dissolve

    scene backyard_n_c with fade
    show mom 208f at left
    show player 434f at right
    with dissolve
    mom "That crazy girl. I cant believe she left me-"
    show player 435f
    player_name "{b}[mom_name]{/b}?"
    show player 434f
    show mom 203 with dissolve
    mom "!!!"
    show player 13f
    show mom 204
    mom "Sweetie!"
    mom "Wha...what are you doing out here?"
    show mom 205
    show player 14f
    player_name "I heard some noises out in the backyard."
    player_name "I thought I should check it out."
    show player 13f
    show mom 204
    mom "Oh... I'm sorry that I woke you up."
    show mom 205
    show player 26f
    player_name "No, it's fine."
    show player 14f
    player_name "I was just worried someone was breaking into our yard."
    show player 13f
    show mom 204
    mom "No, you're aunt and I were...just relaxing."
    show mom 206
    mom "You didn't-"
    show mom 205
    show player 29f with dissolve
    player_name "I must have missed her. I just came down."
    show player 13f with dissolve
    show mom 204
    mom "...Good..."
    show mom 205
    pause
    show player 434f
    show mom 206
    mom "{b}*Brrr*{/b}"
    mom "I...I'm a bit cold."
    show mom 205
    show player 14f
    player_name "Need me to get you something?"
    show player 13f
    show mom 204
    mom "Could you get your momma a {b}towel from the bathroom?{/b}"
    mom "I'm...a bit wet..."
    show mom 205
    show player 14f
    player_name "Of course! I'll be right back!"
    show player 10f
    player_name "Don't... Don't go anywhere!"
    hide player
    hide mom
    with dissolve
    $ M_mom.trigger(T_mom_midnight_swim)
    $ callScreen(location_count)