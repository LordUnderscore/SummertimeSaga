default kassy_first_visit = True

label cupid_dialogue:
    $ location_count = "Cupid"
    if M_mom.get_state() == S_mom_cupid_store:
        scene location_mall_cupid_blur
        show player 5 at left
        show mom 165f at Position(xpos=0.5, ypos=1.0)
        with dissolve
        mom "Oh, wow!"
        show mom 166f
        mom "Look at all the pretty things!"
        show mom 165 at Position(xpos=0.75, ypos=1.0) with dissolve
        mom "Isn't it wonderful!?"
        show mom 164
        player_name "..."
        show player 10
        player_name "I dunno {b}[mom_name]{/b}, it seems pretty girly in here..."
        show player 5
        show mom 165
        mom "Well, yeah..."
        show mom 166
        mom "But I AM a girl, Sweetheart."
        show mom 164
        mom "..."
        show mom 165
        mom "Besides, your obviously starting to become interested in girls."
        show mom 167 at right with dissolve
        mom "And if you want to keep one you'll have to start getting acquainted with places like this!"
        show mom 164 at Position(xpos=0.9, ypos=1.0) with dissolve
        show player 10
        player_name "Really?"
        show player 5
        show mom 166
        mom "Hehe, of course!"
        show mom 165
        mom "Why don't you help me pick something out. It'll be good practice for you!"
        show player 10
        show mom 164
        player_name "Practice?"
        show player 5
        show mom 166
        mom "Yeah!"
        show mom 165
        mom "{b}[firstname]{/b}, {b}gift giving{/b} is a very important part of {b}dating{/b}."
        show player 43
        show mom 164
        player_name "Yeah, I know that, {b}[mom_name]{/b}!"
        show player 5
        show mom 165
        mom "Okay, well... Pretend that your dating me."
        show mom 164
        player_name "..."
        show player 12
        player_name "Seriously?"
        show player 11
        show mom 166
        mom "Hehe, Yesss!"
        show mom 165
        mom "What kind of gift do you think I'd like?"
        show player 10
        show mom 164
        player_name "Hmm, I'm not sure."
        show player 11
        show mom 165
        mom "Well take a look around and see if you can find something!"
        mom "I'll be waiting over here."
        show player 10
        show mom 164
        player_name "Alright."
        hide mom with dissolve
        show player 4 at Position(xpos=0.375, ypos=1.0) with dissolve
        player_name "( What would {b}[mom_name]{/b} like? )"
        player_name "( ... )"
        player_name "( A necklace maybe? )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_cupid_arrival)
    $ callScreen(location_count)

label kass_dialogue:
    scene location_mall_cupid_blur
    if kassy_first_visit:
        $ kassy_first_visit = False
        show player 1f at right
        show kass 2 at left
        with dissolve
        Kass "Welcome to {b}Cupid{/b}. My name is {b}Kassy{/b}, is there anything I can help you find today?"
        show player 2f
        show kass 1
        player_name "No thanks, I'm just looking around."
        show player 1f
        show kass 2
        Kass "Alright. Well, let me know if you need any help."
        show player 2f
        show kass 1
        player_name "Will do! Thanks, {b}Kassy{/b}."
        show player 1f
        show kass 2
        Kass "My pleasure!"
    else:

        show player 2f at right
        show kass 1 at left
        with dissolve
        player_name "Hey {b}Kassy{/b}!"
        show player 1f
        show kass 2
        Kass "Hello there, what can I help you with?"
        show player 2f
        show kass 1
        player_name "Nothing right now, just browsing."
        show player 1f
        show kass 2
        Kass "Alright. Well give me a shout if you need something."
        show player 2f
        show kass 1
        player_name "Will do! Thanks, {b}Kassy{/b}."
    hide kass
    hide player
    with dissolve
    $ callScreen(location_count)

label necklace_display:

    if M_mom.get_state() == S_mom_choose_gift:
        scene location_mall_cupid_blur
        show player 4 zorder 0 at left
        player_name "Yeah, a necklace could definitely work."
        player_name "But which one?"
        show player 492
        show xtra 33 zorder 1 at Position(xpos=0.295, ypos=0.749)
        with dissolve
        player_name "Hmm, no... Too childish for {b}[mom_name]{/b}, I think."
        show xtra 32 with dissolve
        player_name "... No. Too gaudy."
        show xtra 31 with dissolve
        player_name "Ooh, this one is nice and it would look great on her."
        show popup_item_necklace1 at truecenter with dissolve
        $ inventory.items.append(pearl_necklace)
        pause
        hide popup_item_necklace1 with dissolve
        player_name "Perfect!"
        player_name "Now let's see if she likes it!"
        hide xtra
        hide player
        with dissolve
        $ M_mom.trigger(T_mom_pick_necklace)
    else:

        show screen popup_unfinished
    $ callScreen(location_count)

label cupid_dressroom:
    $ location_count = "Cupid Dressroom"
    if M_mom.get_state() == S_mom_dressing_room:
        scene location_mall_cupid_blur
        show player 10
        player_name "{b}[mom_name]{/b}, you alright in there?"
        player_name "What's taking so long?"
        show player 11
        mom "Actually Sweetie, could you come in here for a second?"
        player_name "..."
        show player 10
        player_name "You want me to come in there?!"
        show player 11
        mom "Yes, please."
        show player 10
        player_name "... Okay."
        show player 11

        scene location_mall_cupid_closeup_stall

        show mom 169 zorder 1 at Position(xpos=0.65, ypos=1.0)
        show player 10 at Position(xpos=0.35, ypos=1.0)
        show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
        with dissolve
        player_name "What's the matter?"
        show player 11
        show mom 168
        mom "Oh, I got the necklace snagged on something and I can't get it unclasped."
        mom "Could you help?"
        show player 10
        show mom 169
        player_name "S-sure."
        show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
        show mom 178 zorder 1 at Position(xpos=0.60, ypos=1.0)
        hide mneck 1
        with dissolve

        mom "Oh!"
        show mom 177b
        mom "..."
        show mom 178b
        mom "Oh my..."
        show player 228c
        show mom 177b
        player_name "What is it?"

        show mom 178b
        show player 228d
        mom "*Ahem* N-nothing Sweetheart."
        mom "Can you see where it's snagged?"
        show player 228c
        show mom 177b
        player_name "Yup, I see it. Just hold still one second."
        show player 228d
        player_name "..."
        show player 228c
        player_name "Man, you really got it stuck."
        show player 228d
        mom "..."
        show player 228c
        player_name "Almoooost..."
        player_name "Got iiiit..."
        show player 228d
        player_name "..."
        show mom 179
        mom "Hehehe."
        show player 228c
        player_name "What's so funny?"
        show player 228d
        show mom 178
        mom "N-nothing. It's silly."
        show player 228c
        show mom 177
        player_name "Oh c'mon, tell me."
        show player 228d
        show mom 178
        mom "I'm just thinking about that movie we watched the other night."
        show player 228c
        show mom 177
        player_name "That cheesy romance flick?"
        show player 228d
        show mom 178
        mom "Y-yeah."
        show player 228c
        show mom 177
        player_name "What about it?"
        show player 228d
        show mom 178
        mom "There was a scene just like this... Remember?"
        show mom 177
        player_name "..."
        show player 228c
        player_name "Oh yeah!"
        player_name "He helped the girl out with her necklace and then he-"
        show player 227d at Position(xpos=0.35, ypos=1.0) with dissolve
        player_name "*gulp*"
        show player 227c
        player_name "Kissed her."
        show player 227d
        show mom 178
        mom "Uh huh."
        show player 228d at Position(xpos=0.475, ypos=1.0) with dissolve
        mom "Have you kissed a girl yet, [firstname]?"
        show player 228c
        show mom 177
        player_name "... No."
        show player 228d
        mom "..."
        show mom 179
        mom "Well that's okay, Sweetheart! There's nothing wrong with that."
        show mom 177
        player_name "..."
        show mom 178
        mom "Do you wanna try?"
        show player 227c at Position(xpos=0.35, ypos=1.0) with dissolve
        show mom 177
        player_name "Seriously?!"
        show player 227d
        show mom 178
        mom "Well, yeah... I suppo-"
        hide player
        hide mom
        show mom 180b
        with dissolve

        mom "( !!! )"

        show mom 180
        pause
        show mom 181
        mom "Mmm..."
        show mom 182
        pause

        mom "... Wow."
        mom "Sweetie, We can't... I-I mean I shouldn't have..."
        hide mom
        show player 5 at Position(xpos=0.35, ypos=1.0)
        show mom 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
        show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
        with dissolve
        player_name "..."
        mom "..."
        show player 10
        player_name "I'm sorry, {b}[mom_name]{/b}."
        show player 5
        show mom 168
        mom "NO! No... It's me, I shouldn't have let myself..."
        show mom 169b
        mom "..."
        show mom 168
        mom "*Ahem* W-why don't you just see about getting that necklace unstuck."
        show mom 169b
        player_name "..."
        show player 10
        player_name "Y-yeah, sure thing, {b}[mom_name]{/b}."
        show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
        show mom 177 zorder 1 at Position(xpos=0.60, ypos=1.0)
        hide mneck 1
        with dissolve
        pause
        player_name "..."
        pause

        show player 492 zorder 3 at Position(xpos=0.35, ypos=1.0)
        show xtra 31 zorder 4 at Position(xpos=0.4575, ypos=0.749)
        show mom 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
        with dissolve
        player_name "There we go, all fixed."
        show player 493
        mom "..."
        show mom 168
        mom "Thanks Sweetheart."
        mom "Why don't you go put the necklace back in its display case."
        mom "I'll be right behind you."
        show player 492
        show mom 169b
        player_name "Yeah, okay."
        hide player
        hide xtra
        with dissolve
        mom "..."
        show mom 164b with dissolve
        mom "( Oh god... I can't believe I just did that! )"
        mom "( The poor thing is having a hard enough time as it is. )"
        mom "( What in the world was I thinking... )"
        hide mom with dissolve
        $ M_player.set("jerk mom", True)
        $ M_mom.trigger(T_mom_dressing_room_check)
        $ location_count = "Cupid"
        $ unlock_ui()
        $ gTimer.tick()
    $ callScreen(location_count)

label mom_cupid_outing:
    scene location_mall_cupid_blur
    if M_mom.get_state() == S_mom_choose_gift:
        show player 5 at left with dissolve
        show mom 165 at Position(xpos=.75, ypos=1.0) with dissolve
        mom "Did you find something, Sweetheart?"
        show player 10
        show mom 164
        player_name "I'm still looking."
        show player 5
        show mom 166
        mom "Hehe, okay!"
        show mom 165
        mom "Don't look so serious. It's easy! Just find something you think I'll like..."
        show mom 164
        pause
        hide mom with dissolve
        show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
        player_name "( ... )"
        player_name "( Something {b}[mom_name]{/b} would like? )"
        player_name "( A necklace perhaps? )"

    elif M_mom.get_state() == S_mom_show_necklace:
        $ inventory.items.remove(pearl_necklace)
        show player 492 zorder 0 at left
        show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
        with dissolve
        show mom 164 at Position(xpos=0.75, ypos=1.0) with dissolve
        player_name "Okay, {b}[mom_name]{/b}. How about this?"
        hide xtra
        show player 1 with dissolve
        show mom 170 at Position(xpos=0.7, ypos=1.0) with dissolve
        show mom 172
        mom "Oh, [firstname]... It's beautiful!"
        show mom 170
        show player 14
        player_name "You really like it?"
        show player 13
        show mom 171
        mom "I do! You have great taste, Sweetie."
        show mom 170
        show player 14
        player_name "Heh, thanks {b}[mom_name]{/b}!"
        show player 13
        show mom 173 at Position(xpos=0.775, ypos=1.0)
        pause 1
        show mom 174 at Position(xpos=0.7, ypos=1.0)
        pause 1
        show mom 175
        pause 2
        show mom 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
        show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
        pause
        show mom 165
        mom "Well?"
        show player 14
        show mom 164
        player_name "... Hmm?"
        show player 13
        show mom 166
        mom "How do I look?"
        show player 14
        show mom 164
        player_name "You look beautiful, {b}[mom_name]{/b}!"
        show player 13
        show mom 166
        mom "Aww... Thanks, Sweetheart."
        show mom 164
        mom "Hmm..."
        show mom 165
        mom "Where's a mirror when you need one?"
        show mom 164
        player_name "..."
        show player 14
        player_name "There's probably one in the dressing room..."
        show player 13
        show mom 165
        mom "Good thinking, Sweetie!"
        mom "I'll be right back."
        hide mom
        hide mneck
        with dissolve
        show player 14
        player_name "Okay."
        $ M_mom.trigger(T_mom_give_necklace)
    hide player with dissolve
    $ callScreen(location_count)

label mom_cupid_outing_block:
    scene location_mall_cupid_blur
    if M_mom.get_state() == S_mom_choose_gift:
        show player 4 with dissolve
        player_name "Hmm, I should check out the necklace display for something {b}[mom_name]{/b} would like..."
    elif M_mom.get_state() == S_mom_show_necklace:
        show player 4 with dissolve
        player_name "I should take this necklace to {b}[mom_name]{/b} and see if she likes it."
    elif M_mom.get_state() == S_mom_dressing_room:
        show player 14 with dissolve
        player_name "I have to wait for {b}[mom_name]{/b}."
        show player 13
        player_name "..."
        show player 10
        player_name "I wonder what's taking her so long?"
    hide player with dissolve
    $ callScreen(location_count)