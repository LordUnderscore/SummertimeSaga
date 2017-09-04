label park_bushes_dialogue:
    $ location_count = "Park Bushes"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if erik.started(erik_father_treasure):
        scene expression gTimer.image("park_bushes{}_b")
        show player 4 with dissolve
        player_name "Hmm..."
        show player 12 with dissolve
        player_name "(Looks like a pretty well-hidden spot in here. )"
        show player 14
        player_name "( Maybe {b}Erik{/b}'s dad was telling the truth. )"
        player_name "( Let's look around. )"
        hide player with dissolve
    $ callScreen(location_count)

label park_bushes_bag_dialogue:
    $ location_count = "Park Bushes Bag"
    if erik.started(erik_father_treasure):
        scene park_bag
        show expression "objects/object_key_02.png" at Position(xpos = 540, ypos = 280)
        player_name "Woah!"
        player_name "( So many things are in here! )"
        player_name "( {b}Erik{/b}'s dad must've been collecting these items for a while. )"
        player_name "Hmm..."
        player_name "( That's a strange looking key... )"
        $ erik_father_treasure.finish()
    $ callScreen(location_count, False)