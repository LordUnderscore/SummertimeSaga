default trailer_interior_first_visit = True

label trailer_park_dialogue:
    $ location_count = "Trailer Park"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label trailer_interior_dialogue:
    $ location_count = "Trailer Interior"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")
    if trailer_interior_first_visit:
        $ trailer_interior_first_visit = False
        scene expression gTimer.image("trailer_interior{}")
        show player 10 with dissolve
        player_name "Is this where {b}Roxxy{/b} lives?"
        player_name "There's trash all over the place..."
        hide player with dissolve
    $ callScreen(location_count)

label trailer_bedroom_dialogue:
    $ location_count = "Trailer Bedroom"
    $ callScreen(location_count)

label roxmom_dialogue:
    scene expression gTimer.image("trailer_interior_c{}")
    if not crystal.known(crystal_intro):
        show player 11 at left
        show roxmom 2 at right
        with dissolve
        crys "Well, well!"
        crys "Who do we have here?"
        show roxmom 1
        show player 10
        player_name "Huh?"
        show player 5
        show roxmom 3 with dissolve
        crys "Which boyfriend are you? {b}Dexter{/b}?"
        show roxmom 1 with dissolve
        show player 12
        player_name "I'm not {b}Dexter{/b}..."
        show player 11
        show roxmom 4 with dissolve
        crys "*Gulp*"
        show roxmom 3 with dissolve
        crys "You're a friend of my daughter?"
        show roxmom 1 with dissolve
        show player 10
        player_name "I suppose you could say that."
        show player 5
        show roxmom 2
        crys "She usually doesn't have guy friends."
        show player 11
        crys "She likes men for something a little...more. Just like her mother!"
        show roxmom 1
        show player 22
        player_name "..."
        show roxmom 2
        crys "So what do you want, young man?"
        show player 5
        $ crystal.add_event(crystal_intro)
        $ crystal_intro.finish()
    else:

        show player 5 at left
        show roxmom 3 at right
        with dissolve
        crys "It's my little girl's boyfriend again."
        show roxmom 1 with dissolve
        show player 10
        player_name "I told you we're not-"
        show player 5
        show roxmom 2
        crys "Whatever you say, young man."
        show roxmom 4 with dissolve
        crys "*Gulp*"
        show roxmom 2 with dissolve
        crys "So what do you want?"
    show roxmom 1
    menu roxmom_dialogue_repeat:
        "Where's Roxxy?":
            show player 10
            player_name "Do you know where I could find {b}Roxxy{/b}?"
            show player 5
            show roxmom 3 with dissolve
            crys "Hah! You think I babysit my daughter?"
            show roxmom 1 with dissolve
            show player 10
            player_name "Hmm..."
            show player 5
            show roxmom 2
            crys "She's always out doing stuff..."
            crys "...But, usually she's at {b}school{/b} or at {b}the mall{/b}."
            show roxmom 1
            show player 14
            player_name "Oh, I see. Thanks!"
            show player 13
            show roxmom 2
            crys "Anything else?"
            show roxmom 1
            jump roxmom_dialogue_repeat
        "Roxxy's dad.":

            show player 10
            player_name "Where's {b}Roxxy's...father{/b}?"
            show player 11
            show roxmom 2
            crys "Hah! She don't have no father!"
            crys "I raised her myself."
            show roxmom 1
            show player 10
            player_name "I see."
            show player 11
            show roxmom 2
            crys "To tell you the truth, I don't remember which one it was..."
            show roxmom 4 with dissolve
            crys "*Gulp*"
            show roxmom 2 with dissolve
            crys "...So her daddy could be anyone, for all I know."
            show roxmom 1
            show player 22
            player_name "!!!"
            show roxmom 2
            crys "Anything else you'd like to talk about?"
            show player 5
            show roxmom 1
            jump roxmom_dialogue_repeat
        "Nothing.":

            show player 10
            player_name "Oh, nothing."
            player_name "I was just passing by..."
            show player 11
            show roxmom 2
            crys "Well I got a visitor coming soon, so why don't you move along."
            show roxmom 1
            show player 10
            player_name "I'm sorry. I'll get going then."
            player_name "Bye!"
            hide player
            hide roxmom
            with dissolve
    $ callScreen(location_count)