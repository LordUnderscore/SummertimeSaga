label church_graveyard_dialogue:
    $ location_count = "Church Graveyard"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 2>audio/ambience_graveyard.ogg"):
            $ playSound("<loop 2>audio/ambience_graveyard.ogg")
    $ callScreen(location_count)

label right_tombstone:
    scene location_church_graveyard_tombstone01
    if M_aqua.get_state() == S_aqua_graveyard_search:
        player_name "The name on this tomb stone is Ben Dover!"
        player_name "This has to be the one."
        player_name "But now that I've found it, I'm not sure what I'm supposed to be looking for?"
        player_name "Hmm..."
        player_name "Maybe there's a {b}clue{/b} somewhere?"
        player_name "This engraving stands out..."
        player_name "Maybe I should look for a large {b}bell{/b} somewhere in town?"
        $ M_aqua.trigger(T_aqua_tomb_engraving)
    else:

        pause
    $ callScreen(location_count)