default attic_first_visit = True
default fishing_rod_taken = False
default ring_taken = False
default cheerleader_outfit_taken = False

label attic_dialogue:
    $ location_count = "Attic"
    if attic_first_visit:
        $ attic_first_visit = False
        scene home_attic_cs with fade
        show text "Using the key and stool, I was able to get into our attic.\nI had never been up there before.\nI was filled with excitement wondering what treasures [mom_name] and dad had stashed away." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        with dissolve
    $ callScreen(location_count)

label ring:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_ring.png" with dissolve
    player_name "( That looks like an expensive ring! )"
    player_name "( What was it doing all the way up there? )"
    hide expression "objects/closeup_ring.png" with dissolve
    show expression "boxes/popup_ring.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_ring.png" with dissolve
    jump attic_dialogue

label cheerleader_outfit:
    scene expression gTimer.image("attic{}")




    show expression "boxes/popup_item_outfit1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_outfit1.png" with dissolve
    jump attic_dialogue

label fishing_rod:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_rod.png" with dissolve
    player_name "That's {b}Dad{/b}'s old {b}fishing rod{/b}!!"
    player_name "( I remember when we used to go fishing by the {b}pier{/b}, when I was little. )"
    player_name "{b}*Sigh*{/b}"
    player_name "I miss {b}Dad{/b}..."
    hide expression "objects/closeup_rod.png" with dissolve
    show expression "boxes/popup_item_rod1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_rod1.png" with dissolve
    jump attic_dialogue

label painting:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_painting01.png" with dissolve
    player_name "{b}[mom_name]{/b} used to love painting farm animals..."
    hide expression "objects/closeup_painting01.png" with dissolve
    jump attic_dialogue

label globe:
    scene location_home_attic_globe
    pause
    $ callScreen(location_count)