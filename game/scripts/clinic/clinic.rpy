label hospital_dialogue:
    $ location_count = "Hospital"
    $ callScreen(location_count)

label roz_dialogue:
    scene hospital_desk
    show roz 1 at left
    if datetime.date.today().month == 12 and (datetime.date.today().day >= 15 and datetime.date.today().day <= 30):
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 14f at right
    with dissolve
    player_name "Hi!"
    show player 13f
    show roz 2
    roz "Yes?"
    roz "What can I do for you?"
    show roz 1
    if not Roz.known(roz_intro):
        $ Roz.add_event(roz_intro)
        $ roz_intro.finish()
    menu roz_dialogue_repeat:
        "1st floor?":
            show player 12f
            player_name "What can I find on the 1st floor?"
            show player 5f
            roz "..."
            show roz 2
            roz "It's the lobby."
            show roz 1
            show player 10f
            player_name "Oh... Is there anything else?"
            show player 5f
            show roz 3 with dissolve
            roz "Do you see anything else?"
            show roz 1 with dissolve
            show player 24f
            player_name "I guess not..."
            show player 25f
            show roz 2
            roz "Anything else I can do?"
            show roz 1
            show player 13f
            jump roz_dialogue_repeat
        "2nd floor?":

            show player 12f
            player_name "What can I find on the 2nd floor?"
            show player 5f
            show roz 2
            roz "We have sick rooms, and a storage room on the 2nd floor."
            show roz 1
            show player 12f
            player_name "Oh. I see."
            show player 5f
            show roz 2
            roz "Anything else I can do?"
            show roz 1
            show player 13f
            jump roz_dialogue_repeat
        "Schedule.":

            show player 12f
            player_name "Is there always someone at the reception?"
            show player 5f
            show roz 2
            roz "Yes."
            roz "I'm always here."
            show roz 1
            show player 12f
            player_name "You never leave your desk?"
            show player 5f
            show roz 2
            roz "Why do you ask?"
            show roz 1
            show player 10f
            player_name "Err... Just wondering?"
            show player 5f
            show roz 2
            roz "I only leave my desk in case of an emergency."
            show player 11f
            roz "If I don't get a {b}phone call{/b}, I don't leave."
            show roz 1 with dissolve
            show player 14f
            player_name "Oh. I see."
            show player 13f
            show roz 2
            roz "Anything else I can do?"
            show roz 1
            jump roz_dialogue_repeat

        "Ancestry." if M_aqua.get_state() == S_aqua_boatsmith_search and M_roz.get_state() == S_roz_start:
            show player 14f
            show roz 1
            player_name "Roz! I need to ask you something."
            show player 11f
            show roz 2
            roz "Hmm, yes?"
            show roz 1
            show player 10f
            player_name "I'm trying to find the gravesite of someone who died in this town, a long time ago."
            show player 29f
            player_name "I think he was some kind of Boatsmith."
            player_name "Do you have any ideas on the best way to go about finding it?"
            show player 3f
            show roz 2
            roz "I might have an idea or two."
            show roz 1
            roz "..."
            show player 11f
            player_name "..."
            show player 12f
            player_name "Could you tell me?"
            show player 11f
            show roz 2
            roz "... I probably could."
            show roz 1
            roz "..."
            show player 16f
            player_name "..."
            show player 30f
            player_name "*sigh* Will you please tell me?"
            show player 16f
            show roz 2
            roz "What's this fella's name?"
            show player 29f
            show roz 1
            player_name "... That's the problem. I don't know his name."
            show player 11f
            show roz 2
            roz "Hmm..."
            roz "Well that makes things difficult, doesn't it?"
            show player 25f
            show roz 1
            player_name "... Yeah."

            show player 24f
            show roz 2
            roz "Hmm..."
            roz "It's possible you could find him in the old {b}Obituary Records{/b}."
            show player 11f
            roz "I seem to recall more than a few folk had their professions listed in there."
            show player 10f
            show roz 1
            player_name "Really?! That sounds promising!"
            show player 11f
            show roz 2
            roz "Problem is, it's gonna be a big hassle. Me diggin' that old thing up."
            show player 29f
            show roz 1
            player_name "Oh?"
            show player 3f
            show roz 2
            roz "Maybe you could do something to make it worth my while?"
            show player 29f
            show roz 1
            player_name "O-Of course!"
            show player 2f
            player_name "You let me take a look at those records and I'll do anything you want!"
            show player 1f
            show roz 2
            roz "Hmm... Anything?"
            show player 2f
            show roz 1
            player_name "Anything!"
            show player 1f
            roz "..."
            show roz 2
            roz "Alright. I tell ya what. Take this pass key up to the {b}2nd floor storage{/b}."
            roz "You'll find an ugly box sitting there on the shelf, stands out like a sore thumb, you can't miss it."
            show player 2f
            show roz 1
            player_name "Ugly box, got it."
            show player 1f
            show roz 2
            roz "You go get me that box and bring it back here while I dig up those records."
            show player 2f
            show roz 1
            player_name "That sounds easy enough! I'll be back in a flash!"
            hide player with dissolve

            show roz 2
            roz "Heh, sure you will kid. Sure you will."
            hide roz
            hide roz_desk
            with dissolve
            $ M_roz.trigger(T_roz_favour)
            $ M_roz.set("fun time", True)

        "Go on break." if M_roz.get_state() == S_roz_end and not M_roz.is_set("fun time"):
            show player 14f
            show roz 1
            player_name "I was wondering if you wanted to... Ya know, take your break?"
            show player 13f
            show roz 2
            roz "Ahh..."
            roz "Can't get enough of ole' Roz, eh Kiddo?"
            show roz 1
            player_name "..."
            show roz 2
            roz "Don't you worry, message recieved."
            roz "You head on up to storage and I'll be along shortly..."
            roz "...just need a moment to freshen up."
            show roz 1
            player_name "..."
            show player 14f
            player_name "S-Sure, I'll be up there waiting."
            show player 13f
            hide player with dissolve
            show roz 2
            roz "That's a good boy..."
            hide player
            hide roz
            hide roz_desk
            with dissolve
            $ M_roz.set("fun time", True)
        "Nothing.":

            show player 14f
            player_name "No, I think that's all!"
            show player 13f
            show roz 2
            roz "Bye."
            hide player
            hide roz
            hide roz_desk
            with dissolve
    $ callScreen(location_count)