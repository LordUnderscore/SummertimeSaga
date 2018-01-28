label diane_front_yard:
    $ location_count = "Diane's Front Yard"
    $ callScreen(location_count)

label diane_front_yard_night_locked:
    show expression gTimer.image("backgrounds/location_diane_front{}_blur.jpg")
    show player 10 with dissolve
    player_name "{b}Aunt Diane{/b} is probably asleep..."
    hide player with dissolve
    $ callScreen(location_count)