label mias_upstairs:
    $ location_count = "Mia's House Upstairs"
    if M_mia.get_state() in [S_mia_consult, S_mia_impress_harold, S_mia_parent_unblock, S_mia_strip_aftermath, S_mia_midnight_call] and gTimer.is_dark():
        scene mia_house_upstairs_n_b
        show player 1 at left
        show helen 2 at right
        with dissolve
        helen "What are you doing?"
        show helen 1
        show player 22
        player_name "!!!" with vpunch
        show helen 1
        show player 10
        player_name "I, err-"
        show player 5
        show helen 2
        helen "Are you trying to see {b}Mia{/b}?"
        show player 10
        show helen 1
        player_name "But, I didn't mean-"
        show player 5
        show helen 2
        helen "You have no business here, young man."
        show helen 3
        helen "Stay away from my daughter. Understood?"
        show player 10
        show helen 1
        player_name "Yes, ma'am..."
        $ location_count = "Mia's House"

    elif M_mia.get_state() in [S_mia_midnight_help, S_mia_locked_room]:
        scene mia_house_upstairs_n_b
        show player 11 with dissolve
        "*Muffled voices*"
        show player 30
        player_name "Huh?"
        player_name "( I hear voices coming from that {b}room on the left{/b}... )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_unexpected_visit:
        scene mia_house_upstairs_b
        show player 30 with dissolve
        player_name "Huh?"
        show player 10
        player_name "( I hear voices coming from {b}Helen's{/b} bedroom... )"
        player_name "( ...{b}Mia{/b} must be in there with her mom. )"
        hide player with dissolve
        hide player with dissolve

    elif M_helen.get_state() == S_helen_aftersex_mia_suspicious:
        scene mia_house_upstairs_n_b
        show mia 44f at right
        show player 22 at left
        with dissolve
        player_name "!!!" with hpunch
        show mia 43f
        mia "{b}[firstname]{/b}?"
        show mia 44f
        show player 29 with dissolve
        player_name "Oh... Uh... Hi!"
        show player 3
        show mia 43f
        mia "I didn't know you were here."
        show mia 44f
        show player 12 with dissolve
        player_name "Oh..."
        show player 11
        show mia 43f
        mia "And what were you doing in my mom's bedroom?"
        show mia 44f
        show player 10
        player_name "Ummm... Yeah... She..."
        player_name "...Just wanted to have a word with me about...uhhh...bible study stuff."
        show player 5
        show mia 43f
        mia "Really? Since when did you start taking an interest in church?"
        show mia 44f
        show player 29 with dissolve
        player_name "Oh... Uh... Yeah. I've been getting more involved a little while back."
        player_name "Hey! Want to hang out? I just finished...talking...with your mom."
        show player 3
        show mia 46f
        mia "I don't really feel like it."
        mia "I think I'm just going to sit in my room for a bit."
        show mia 45f
        show player 29
        player_name "Okay..."
        player_name "I guess I'll head back home then."
        show player 3
        show mia 46f
        mia "Sounds good."
        hide mia
        show player 24
        with dissolve
        player_name "...Bye..."
        hide player with dissolve
        $ gTimer.tick()
        $ unlock_ui()
        $ M_helen.trigger(T_mia_stay_alone)
    $ callScreen(location_count)

label helens_locked_room_block:
    scene expression gTimer.image("mia_house_upstairs{}_b")
    player_name "( The door is locked. )"
    if M_mia.get_state() == S_mia_midnight_help:
        player_name "( I have to find a {b}key{/b}... )"
    $ callScreen(location_count)