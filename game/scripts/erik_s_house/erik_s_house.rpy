default erik_mail = []
default poker_drunk = False
default erik_drunk = False

label erik_house_dialogue:
    $ location_count = "Erik's House"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if gTimer.is_morning():
        if not erik.known(erik_intro):
            scene erikhouse
            show player 2 at left with dissolve
            show erik 1 at right with dissolve
            player_name "Hey, {b}Erik{/b}!"
            show erik 5 at right
            show player 1 at left
            eri "Hey, {b}[firstname]{/b} ..."
            show player 10 at left
            show erik 1 at right
            player_name "You look really tired... You alright?"
            show erik 3 at right
            show player 5 at left
            eri "Well, I was on the computer all night playing this new game that came out..."
            show erik 2 at right
            show player 5 at left
            eri "...and I just hate going to school."
            show erik 3 at right
            eri "I wish I could just stay at home all the time."
            show player 10 at left
            show erik 1 at right
            player_name "Yeah, I hear ya..."
            show erik 3 at right
            show player 24 at left
            eri "Sorry to hear about your {b}Dad{/b}, by the way... I hope you and your family are doing okay."
            show player 25 at left
            show erik 1 at right
            player_name "We'll be alright... Thanks for asking..."
            player_name "We should really get going before we're late for class."
            hide player 25 at left with dissolve
            hide erik 1 at right with dissolve

            show unlock13 at truecenter
            $ renpy.pause()
            hide unlock13 with dissolve
            $ loc_school_unlocked = True
            $ erik.add_event(erik_intro)
            hide erikhouse

        elif erik.started(erik_intro):
            scene erikhouse
            show player 11 at left
            show erik 5 at right
            eri "Shouldn't we be going to {b}school{/b}?"
            show erik 1 at right
            show player 14 at left
            player_name "Oh, Yeah. You're right..."
            hide player 14 at left
            hide erik 1 at right
            hide erikhouse

        elif erik.over(erik_intro) and not gTimer.is_weekend():
            scene erikhouse
            show player 12 with dissolve
            player_name "( There's no one here... )"
            show player 35
            player_name "( {b}Erik{/b} probably left for {b}school{/b} already. )"
            hide player 35 with dissolve
            hide erikhouse
        $ callScreen(location_count)
    else:

        if not mrsj.known(mrsj_intro) and gTimer.is_afternoon():
            scene erikhouse
            show player 1 at left with dissolve
            show erikmom 2 at right with dissolve
            erimom "Hi, {b}[firstname]{/b}!"
            show erikmom 1 at right
            show player 14 at left
            player_name "Hi, {b}Mrs. Johnson{/b}! Just dropping by to see {b}Erik{/b}!"
            show erikmom 4 at right
            show player 1 at left
            eri "Hey, {b}[firstname]{/b}!"
            show erikmom 5 at right
            show player 11 at left
            erimom "There's my little pumpkin!"
            show erikmom 6 at right
            eri "{b}Mom{/b}! I told you not to call me that..."
            show erikmom 7 at right
            show player 5 at left
            erimom "By the way, {b}Erik{/b} told me about your father..."
            erimom "I'm so sorry to hear. Let us know if you ever need anything, okay?"
            show erikmom 8 at right
            show player 10 at left
            player_name "Yes, {b}Mrs. Johnson{/b}."
            show erikmom 7 at right
            show player 13 at left
            erimom "Okay! I'll let you two at it! I have to get to my yoga class."
            show erikmom 8 at right
            show player 1 at left
            erimom "Take good care of my boy, {b}[firstname]{/b}!"
            erimom "He's lucky to have you as a friend."
            erimom "Bye guys!"
            show erikmom 6 at right
            eri "Bye, {b}Mom{/b}."
            hide erikmom 6 at right with dissolve
            show erik 1 at right with dissolve
            show player 14 at left
            player_name "Dude... Your mom is fit!"
            show erik 3 at right
            show player 1 at left
            eri "Um... Yeah... I guess..."
            show erik 1 at right
            show player 26 at left
            player_name "Like... For her age, I mean... Man, she's in GOOD shape..."
            show erik 5 at right
            show player 1 at left
            eri "I don't know... She does hang out at the {b}Gym{/b} a lot."
            eri "She's a yoga instructor down at the {b}Gym{/b}."
            show erik 1 at right
            show player 14 at left
            player_name "So, you want to hangout... or?"
            show erik 3 at right
            show player 11 at left
            eri "I can't right now. I have... I downloaded this new game and-"
            show erik 1 at right
            show player 12 at left
            player_name "It's fine, {b}Erik{/b}. I'll see you tomorrow or something."
            show player 36 at left
            show erik 7 at right
            eri "Cool. See ya later..."
            hide player 36 at left with dissolve
            hide erik 7 at right with dissolve
            hide erikhouse
            $ mrsj.add_event(mrsj_intro)
    $ callScreen(location_count)

label door18_locked_dialogue:
    if location_count == "Erik's House":
        scene erikhouse
    elif location_count == "Erik's Backyard":
        scene eriks_backyard_b
    show player 11 at left
    show erik 5 at right
    eri "Umm... Why are we going in my house?"
    eri "Shouldn't we be going to {b}school{/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "Oh, yeah! You're right..."
    hide player 14 at left
    hide erik 1 at right
    $ callScreen(location_count)

label unfinished_dialogue4:
    scene erikhouse
    show player 14
    player_name "You can't do anything in here yet, because the game is still in early development!"
    show player 26
    player_name "But soon, you will be able to visit {b}Erik{/b}... And talk to his mom!"
    show player 17
    player_name "Come back when the next game update is released!"
    hide player 17 with dissolve
    $ callScreen(location_count)

label erik_gf_stolen:
    if location_count == "Erik's House":
        scene expression gTimer.image("erikhouse{}")
    elif location_count == "Erik's Backyard":
        scene expression gTimer.image("eriks_backyard{}_b")
    show player 10
    with dissolve
    player_name "I shouldn't make this any more awkward..."
    player_name "I'll wait until tomorrow to talk to them."
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_thief_block:
    scene erikhouse_night
    show player 2 with dissolve
    player_name "I should go catch that {b}burglar{/b} first."
    hide player 2 with dissolve
    $ callScreen(location_count)

label closed_erik:
    if not gTimer.is_dark():
        if location_count == "Erik's House":
            scene erikhouse
        elif location_count == "Erik's Backyard":
            scene eriks_backyard_b
        show player 12 with dissolve
        player_name "( There's no one here... )"
        show player 35
        player_name "{b}Erik{/b} probably left for {b}school{/b} already."
    else:

        if location_count == "Erik's House":
            scene erikhouse_night
        elif location_count == "Erik's Backyard":
            scene eriks_backyard_n_b
        show player 2 with dissolve
        player_name "( {b}Erik{/b} is probably asleep. I should come back tomorrow. )"
        hide player 2 with dissolve
    $ callScreen(location_count)

label closed_erik_weekend:
    if location_count == "Erik's House":
        scene erikhouse
    elif location_count == "Erik's Backyard":
        scene eriks_backyard_b
    show player 12 with dissolve
    player_name "( There's no one here. )"
    show player 35
    player_name "( {b}Erik{/b} probably went out with his mom somewhere. )"
    hide player 35 with dissolve
    $ callScreen(location_count)

label erik_mailbox:
    scene expression gTimer.image("erik_mailbox{}")
    if m_magazine in erik_mail:
        show expression "objects/object_mailbox_item01_closeup.png" with dissolve
        player_name "( Huh. A magazine. I wonder who it could be for... )"
        player_name "( Milfness? Well, I know it's for {b}Mrs. Johnson{/b}. I didn't know she subscribed to these, though... )"
        player_name "( I better put this back. )"
        hide expression "objects/object_mailbox_item01_closeup.png" with dissolve

    elif m_dad_letter in erik_mail:
        player_name "( I didn't know they recieved letters. I wonder who it's addressed to... )"
        player_name "( It's for {b}Erik{/b}. )"
        menu:
            "Leave it alone.":
                call screen erik_mailbox
            "Open it.":

                show expression "objects/object_mailbox_item03_closeup.png" at Position(xpos = 565, ypos = 768) with dissolve
                player_name "( A letter from his Dad?! )"
                player_name "( I didn't know he was still trying to contact him... )"
                player_name "I better put this back."
                hide expression "objects/object_mailbox_item03_closeup.png" with dissolve
                call screen erik_mailbox
        $ erik_mailbox_items.remove(dad_letter)
    elif m_pizza_pamphlet in erik_mail:
        player_name "( This looks like junk mail. )"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( Tony's Pizza. I haven't been to that place in a while. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        if not loc_pizza_unlocked:
            show expression "boxes/popup_pizza.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_pizza.png" with dissolve
            $ loc_pizza_unlocked = True

    elif m_newspaper in erik_mail:
        player_name "( Local news. This should be interesting... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( The thief is still on the loose? You would've thought they would've caught him by now. )"
        player_name "( I better put this back. )"
        hide expression "objects/object_newspaper.png" with dissolve
    call screen erik_mailbox

label erik_house:
    $ location_count = "Erik's House"
    $ callScreen(location_count)