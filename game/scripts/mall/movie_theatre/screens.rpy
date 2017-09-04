screen movieoptions:
    frame:
        background None
        has hbox
        vbox:
            imagebutton:
                focus_mask True
                pos (17,181)
                idle "images/buttons/movie_option_01.png"
                hover "images/buttons/movie_option_01b.png"
                action [Hide("movie_theatre"), Jump("after_movie_pick_dialogue")]

            imagebutton:
                focus_mask True
                pos (359,-190)
                idle "images/buttons/movie_option_02.png"
                hover "images/buttons/movie_option_02b.png"
                action [Hide("movie_theatre"), Jump("after_movie_pick_dialogue")]

            imagebutton:
                focus_mask True
                pos (739,-592)
                idle "images/buttons/movie_option_03.png"
                hover "images/buttons/movie_option_03b.png"
                action [Hide("movie_theatre"), Jump("after_movie_pick_dialogue")]