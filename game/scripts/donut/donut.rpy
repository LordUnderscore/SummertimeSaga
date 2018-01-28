label donut_shop_dialogue:
    $ location_count = "Donut Shop"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label donut_interior_dialogue:
    $ location_count = "Donut Shop Interior"
    $ callScreen(location_count)

label beth_dialogue:
    scene donut_c
    show beth 2 zorder 1 at right
    show xtra 27 zorder 2 at center
    show player 1 zorder 3 at left
    with dissolve
    beth "Howdy, mister!"
    show player 14
    show beth 1
    player_name "Hi."
    show player 1
    show beth 2
    beth "Looking to buy some sweet holes, are ya?"
    show beth 1
    menu:
        "I don't know." if not M_mia.is_set("buy donuts"):
            show player 14
            player_name "Hmm... I'm not sure what I need to buy yet."
            show player 1
            show beth 2
            beth "You don't know?"
            show player 14
            show beth 1
            player_name "Well, I'm buying these for someone as a gift but I'm not sure what he likes."
            show player 1
            show beth 2
            beth "I can't help ya if you don't know what ya'd like!"
            show player 14
            show beth 1
            player_name "I'll come back later when I know the ingredients."

        "<>I want donuts! (50$)" if inventory.money < 50 and M_mia.is_set("buy donuts"):
            $ pass

        "I want donuts! (50$)" if inventory.money >= 50 and M_mia.is_set("buy donuts"):
            show player 14 at left
            show beth 1 at right
            player_name "I'd like to buy a small box, please."
            show player 1
            show beth 2
            beth "Sure thing!"
            beth "What kind of glaze and topping would you like on them?"
            call screen donut_minigame
        "No, thanks.":

            show beth 1 at right
            show player 14 at left
            player_name "I'm fine, thanks!"
            player_name "Perhaps another time..."
            show player 1
            show beth 2
            beth "Sure thing, see ya!"
    hide player
    hide xtra
    hide beth
    with dissolve
    $ callScreen(location_count)

label donut_buy_dialogue:
    show beth 2
    beth "Here ya go."
    show unlock51 at truecenter with dissolve
    pause
    hide unlock51 with dissolve
    show player 17
    show beth 1
    player_name "Thank you."
    show player 1
    show beth 2
    beth "Enjoy the sweet holes!"
    hide player
    hide xtra
    hide beth
    with dissolve
    $ callScreen(location_count)

label donut_locked:
    show player 10 with dissolve
    player_name "( I should come back during the day while they are open. )"
    $ callScreen(location_count)