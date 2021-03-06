init python:
    class ComicItem:
        def __init__(self, item, name = "", image = "", popup = "", idle = "", hover = "", price = 0, category = "", purchased = False):
            self.name = name
            self.image = image
            self.popup = popup
            self.idle = idle
            self.hover = hover
            self.price = price
            self.category = category
            self.item = item
            self.purchased = purchased


    class ComicStore (object) :
        def __init__(self):
            self.items = []

default comic_first_visit = True

label comic_store_dialogue:
    $ location_count = "Comic Store"
    if June.started(june_cosplay) and orcette_cosplay not in inventory.items:
        scene comic_b
        show player 14
        with dissolve
        player_name "Looks like they have some costumes hanging on the wall."
        player_name "I should have a look at them..."
        player_name "... maybe they have those orc cosplay pieces."
        hide player with dissolve
    elif erik.started(erik_vr):
        scene comic_b
        if game02 in inventory.items and virtualsaga in inventory.items:
            show player 14 with dissolve
            player_name "( I think that's all {b}Erik{/b} wanted. )"
            player_name "( Let's get back to him... )"
        else:
            show player 35 with dissolve
            player_name "( They must have the things {b}Erik{/b} wanted in here somewhere. )"
            show player 12 with dissolve
            player_name "( Maybe in those shelves by the counter? )"
        hide player with dissolve
    elif comic_first_visit == True:
        scene comic_b
        show player 1 at left
        show tatia 3 at right
        with dissolve
        tati "Hi!"
        show tatia 2
        tati "First time visiting {b}Cosmic Cumics{/b}?"
        show tatia 1
        show player 29
        player_name "Umm... Yeah! I didn't know this place existed..."
        show tatia 2
        show player 1
        tati "Yeah we just opened recently!"
        show tatia 1
        show player 2
        player_name "Oh, cool!"
        player_name "You guys sell video games, too?"
        show tatia 3
        show player 1
        tati "Of course."
        show tatia 2
        tati "We sell a variety of products ranging from {b}video games{/b},{b}comic books{/b}, {b}figurines{/b}, {b}posters{/b} and {b}collectibles{/b}!"
        show tatia 1
        show player 2
        player_name "Oh. So... nerd stuff..."
        show tatia 3
        show player 1
        tati "Yup!"
        tati "Have a look around, and let me know if you need help with anything!"
        $ comic_first_visit = False
        hide tatia
        hide player
        hide comic_b with None
    $ callScreen(location_count)

label tatiana_dialogue:
    scene comic_c
    show xtra 17 zorder 2
    show tatia 2 zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    tati "What's up?"
    label comic_tatiana_menu:
        show tatia 1
        menu:
            "You seem familiar.":
                show tatia 1
                show player 4
                player_name "I feel like I've seen you somewhere."
                show tatia 3
                show player 1
                tati "Right. Well, you've probably seen me on the internet..."
                show tatia 2
                tati "I do a lot of {b}video game streams{/b} and I post them on my {b}YT channel{/b}."
                show tatia 4
                tati "I usually go by the name of {b}PureRuby87{/b}."
                show tatia 5
                show player 17
                player_name "Oh, right! My friend {b}Erik{/b} loves your stuff!"
                show player 21
                player_name "He keeps talking about your videos and your {b}huge{/b}... err... fan base!"
                show tatia 3
                show player 1
                tati "Aww... You guys are so sweet."
                show tatia 2
                tati "Is there anything else you want to talk about?"
                jump comic_tatiana_menu
            "Any suggestions?":

                show tatia 1
                show player 2
                player_name "Do you have any suggestions? New products that you would recommend?"
                show player 1
                tati "Hmmm..."
                show tatia 2
                tati "Well, I really love {b}cosplay{/b}!"
                show tatia 4
                tati "I like to wear {b}sexy outfits{/b}. Actually, we have a new line of costumes that just came in!"
                show tatia 5
                show player 21
                player_name "Oh, yeah? Sounds interesting..."
                show tatia 4
                show player 1
                tati "It's sometimes hard to fit my... umm... forms into them."
                tati "They make them so tight, you know?"
                show tatia 3
                tati "But guys usually don't seem to mind!"
                show tatia 5
                show player 29
                player_name "Haha. I see."
                show player 2
                player_name "Thanks, I'll have a look."
                jump comic_tatiana_menu
            "I found what I need.":

                show tatia 1
                show player 2
                player_name "Yeah, I think I have everything I need. Thanks!"
                show tatia 2
                show player 1
                tati "Great! Thanks for shopping at {b}Cosmic Cumics{/b}..."
                show tatia 3
                show player 13
                tati "And tell your friends about us!"
    hide tatia
    hide player
    hide xtra
    hide comic_c
    $ callScreen(location_count)