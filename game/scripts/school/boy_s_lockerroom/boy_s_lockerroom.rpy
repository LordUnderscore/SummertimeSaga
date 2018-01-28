label locker_room_dialogue:
    $ location_count = "Boy's Lockerroom"
    if not gTimer.is_dark():
        if player.over(intense_gymercise) and not roxxy.known(roxxy_shower):
            scene locker_empty_b with None
            show roxxy 17 at right
            show becca 1 at Position(xpos=315)
            show missy 1 at left
            with dissolve
            rox "Anyway, so I'm like, \"no way I'm studying for this stupid exam!\""
            show roxxy 16
            show missy 2
            show becca 3
            missy "Totally! I HATE studying!"
            show roxxy 17
            show missy 1
            show becca 1
            rox "Ugh! I need to find a way to get past those assignments first!"
            show roxxy 16
            show becca 2
            becca "You haven't done those yet?!"
            show roxxy 17
            show becca 1
            rox "Oh, shut up! I'll find a way!"
            rox "{b}Mrs. Bissette{/b} has been on my case about them, though..."
            show roxxy 16
            show missy 2
            show becca 3
            missy "Yeah, {b}Mrs. Bissette{/b} is the worst."
            show missy 1
            show becca 2
            becca "Yeah, too bad you don't have a penis, {b}Roxxy{/b}. I hear she loves trading dick for good grades."
            show roxxy 17
            show missy 3
            show becca 1
            rox "The real problem is exams."
            rox "I can't afford to fail any more of them."
            show roxxy 16
            show missy 2
            show becca 3
            missy "Can't your boyfriend help you?"
            show roxxy 17
            show missy 3
            show becca 1
            rox "Like, help how?! All {b}Dexter{/b} is good at, is basketball and lifting weights..."
            show roxxy 16
            show missy 1
            show becca 2
            becca "Maybe he can beat up one of the nerds around school, and get you what you want?"
            show roxxy 17
            show becca 1
            rox "When is he NOT doing that..."
            show roxxy 16
            show missy 2
            show becca 3
            missy "Right."
            show roxxy 17
            show missy 1
            show becca 1
            rox "I can't fail these exams, or I'm going to look like an idiot in front of everyone!"
            rox "I need to get my hands on a copy the exams, somehow..."
            show roxxy 16
            show becca 2
            becca "How are you going to do that?"
            show roxxy 17
            show missy 3
            show becca 1
            rox "I'll find a way."
            show becca 2
            show roxxy 18 at Position(xoffset=-19) with fastdissolve
            becca "I hope so, they're coming up soon..."
            show becca 1
            show roxxy 19 at Position(xoffset=-49) with fastdissolve
            rox "Anyway!"
            show roxxy 20 at Position(xoffset=-69) with fastdissolve
            rox "I have to take a shower."
            rox "You two keep an eye out, so no one comes in while I'm in there."
            show becca 2
            show roxxy 21 at Position(xoffset=-27) with fastdissolve
            becca "How long are you gonna take?"
            show missy 2
            show becca 3
            missy "Yeah! We have to get to class soon!"
            show missy 1
            show becca 1
            show roxxy 22 with fastdissolve
            rox "Shut up and guard the showers!"
            show missy 3
            show roxxy 24 with fastdissolve
            rox "I don't want any creeps coming in while I'm in there."
            show roxxy 23
            becca "..."
            show missy 2
            missy "Sure, {b}Roxxy{/b}..."
            hide missy
            hide roxxy
            hide becca
            with dissolve
            pause
            show jersey 11 with dissolve
            player_name "( It looks like no one's here yet! )"
            show jersey 13
            player_name "( Just how I like it... )"
            show jersey 18
            player_name "( I'll be able to get a warm shower before the water gets cold! )"
            hide jersey with dissolve
            $ roxxy.add_event(roxxy_shower)

        elif locker_room_count == 0:
            scene locker
            show combo 1 at left with dissolve
            player_name "See?"
            player_name "It's not too bad: There's only a few people in here!"
            show combo 2 at left
            show annie 3 at right with dissolve
            ann "I hope you two remember the rules in regards to being late!"
            ann "If you're not in uniform and in the Courtyard in one min-"
            show combo 3 at left
            show annie 1 at right
            player_name "It's okay, {b}Annie{/b}... We get it."
            player_name "We'll be outside in just a moment..."
            show combo 4 at left
            show annie 3 at right
            ann "As the Student Union President and official hallway monitor..."
            ann "...it is my {b}duty{/b} to write infractions to anyone breaking school guidelines!"
            show combo 5 at left
            show annie 1 at right
            player_name "Look..."
            player_name "{b}Judith{/b} is not very comfortable in the guy's Locker Room."
            player_name "She's going to need some extra time to get ready, okay?"
            show combo 4 at left
            show annie 5 at right
            ann "Is that right, {b}Judith{/b}?"
            show combo 6 at left
            show annie 6 at right
            jud "Well..."
            jud "Y...Yes..."
            show combo 4 at left
            show annie 5 at right
            ann "What's the matter?"
            ann "Just a little bit insecure around the boys?"
            ann "...Or are you inciting disorder and disobeying the rules?"
            show combo 6 at left
            show annie 6 at right
            jud "It's not..."
            jud "It's just that..."
            show combo 7 at left
            jud "...I'm not... wearing a bra!"
            show annie 5 at right
            ann "Oh, I see... Coming up with excuses to skip class, are we?"
            show combo 4 at left
            show annie 3 at right
            ann "Your lack of obedience is alarming, and I will not allow it!"
            show annie 4 at right
            ann "Get dressed immediately, or I'm sending you both to detention!!"
            show annie 6 at right
            show combo 8 at left
            window hide
            pause
            show combo 9 at left
            window hide
            pause
            show combo 10 at left
            window hide
            pause
            show combo 11 at left
            player_name "..."
            show combo 12 at left
            window hide
            pause
            show combo 13 at left
            window hide
            pause
            show annie 9 at right
            show combo 14 at left
            window hide
            pause
            show annie 10 at right
            show combo 15 at left
            window hide
            pause
            show annie 11 at right
            show combo 16 at left with hpunch
            player_name "Shit..."
            jud "Oh, my..."
            show combo 18 at left
            show annie 8 at right
            ann "This..."
            ann "This is... improper... and shameful!!"
            show combo 17 at left
            show annie 1 at right
            player_name "I'm... so sorry..."
            show combo 18 at left
            show annie 2 at right with hpunch
            ann "Put your uniforms on and get your asses to class, {b}NOW{/b}!!!"
            show combo 19 at left
            show annie 7 at right
            ann "I will have to report this incident to {b}Principal Smith{/b}, along with your infractions for being late..."
            show combo 20 at left
            ann "...Now, move it!!"
            hide combo 20 at left with dissolve
            hide annie 7 at right with dissolve
            $ wearing_jersey_count = 2
            $ courtyard_door_count = 1
            $ locker_room_count = 1
            $ stairs_count = 1
            $ classroom_door_count = 1
    else:
        if webcam_quest:
            scene locker_night
            show player 14 at left with dissolve
            show erik 1 at right with dissolve
            player_name "Okay, this is the place!"
            show player 1
            show erik 5
            eri "The lockeroom??"
            show erik 1
            show player 35
            player_name "Yah... But I need to find a {b}hidden spot{/b}..."
            player_name "...There has to be a place in this room where I could {b}hide{/b} something small..."
            hide erik 1
            hide player 35
    $ callScreen(location_count)

screen locker_room:

    if not gTimer.is_dark():
        if roxxy.started(roxxy_shower):
            add "backgrounds/location_locker_room_empty.jpg"
        else:
            add "backgrounds/location_locker_room.jpg"
    else:
        add "backgrounds/location_locker_room_night.jpg"

    if roxxy.started(roxxy_shower):
        if not gTimer.is_dark():
            imagebutton:
                focus_mask True
                pos (25,274)
                idle "images/objects/object_door_17_girls.png"
                hover "images/objects/object_door_17b_girls.png"
                action Hide("locker_room"), Jump("roxxy_shower_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (25,274)
            idle gTimer.image("objects/object_door_17{}.png")
            hover gTimer.image("objects/object_door_17b{}.png")
            if not gTimer.is_dark():
                action If(
                    shower_door_count == 0,
                    [Hide("locker_room"), Jump("door17_locked_dialogue")],
                    [Hide("locker_room"), Jump("lockershowers_dialogue")]
                )
            else:
                action Hide("locker_room"), Jump("denied_access_locker")

    if gTimer.is_evening() and quest11 in quest_list and not webcam_planted:
        imagebutton:
            focus_mask True
            pos (520,160)
            idle "objects/object_airvent_01.png"
            hover "objects/object_airvent_01b.png"
            action Hide("locker_room"), Jump("airvent_webcam_quest")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover "boxes/auto_option_02b.png"
        action Hide("locker_room"), Jump("left_hall_dialogue")

label airvent_webcam_quest:
    scene locker_night
    show player 34 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Hmm..."
    show player 43
    show erik 13
    player_name "Up there!"
    show erik 14
    eri "The air vent?"
    show erik 1
    show player 14
    player_name "Yeah! It's perfect!"
    player_name "It has a view of the entire room..."
    player_name "...just stand right under it."
    show player 17
    player_name "I'll climb on your shoulders to reach it!"
    show player 1
    show erik 3
    eri "Okay..."
    hide erik
    show player 128 at center
    with dissolve
    player_name "Alright, stay still!"
    hide player
    hide erik
    scene locker_closeup
    show player 129
    with dissolve
    player_name "Stay still!"
    show player 130
    player_name "It's almost done..."
    show player 131
    player_name "..."
    player_name "There!"
    hide player
    $ inventory.items.remove(supersaga_webcam)
    scene locker_night
    show player 43 at left
    show erik 1 at right
    with dissolve
    player_name "Alright! Let's get out of here..."
    show player 11
    show erik 5
    eri "Should I know what this is about?"
    $ erik_helped_with_camera = True
    menu:
        "Can't tell you.":
            show erik 3 at right
            show player 10 at left
            player_name "It's probably better if you don't know..."
            player_name "...It's nothing that bad, anyway..."
            show player 21
            player_name "...And it will help with my {b}homework{/b}!!"
            show player 13
            eri "Okay, then..."
            show erik 5
            eri "...Can we leave now?"
            show erik 1
            show player 14
            player_name "Yeah, let's go."
            hide erik 1 with dissolve
            hide player 14 with dissolve
        "Hidden webcam.":

            show player 24 at left
            show erik 1 at right
            player_name "{b}*Sigh*{/b}..."
            player_name "It's the {b}librarian.{/b}"
            show player 25
            player_name "She won't order the {b}textbooks{/b} I need..."
            player_name "...Unless I do this for her."
            show player 5
            show erik 5
            eri "What? Why?"
            show erik 1
            show player 10
            player_name "It seems like the {b}library{/b} ran out of budget to get new books."
            player_name "Anyway, it's done now. Let's just go..."
            show player 13
            show erik 4
            eri "Okay. Thanks for letting me know about it."
            hide player 13 with dissolve
            hide erik 1 with dissolve
    $ gTimer.tick()
    $ webcam_planted = True
    $ ui_lock_count = 0
    jump map_dialogue

label roxxy_shower_dialogue:
    scene locker_empty_b with None
    show jersey 11 at left
    show becca 2f at Position(xpos=715)
    show missy 1f at right
    with dissolve
    becca "Uhmm... What are you doing?"
    show becca 3f
    show missy 2f
    missy "No one is allowed in the shower."
    show missy 1f
    show becca 1f
    show jersey 10
    player_name "I just finished gym class! I NEED to take a shower."
    show becca 2f
    show jersey 11
    becca "Uhmm... No. You don't."
    show becca 1f
    show jersey 12
    player_name "Yes, I do! I have class soon, and I'm all sweaty!"
    player_name "This is the guys locker room!"
    show missy 2f
    show becca 3f
    show jersey 11
    missy "Like, it's occupied."
    show missy 1f
    show becca 2f
    becca "Can't you see?"
    show missy 3f
    show becca 1f
    show jersey 12
    player_name "I'm surprised you even know the meaning of \"occupied.\""
    show becca 4f
    show missy 1f
    show jersey 13
    becca "Haha!"
    show jersey 11
    show missy 4f
    show becca 3f
    missy "Don't laugh at me, you dumb slut!"
    show missy 1f
    player_name "..."
    show becca 2f
    becca "You're still here?"
    show missy 2f
    show becca 1f
    missy "What do you want?"
    show missy 1f
    $ ui_lock_count = 0
    menu:
        "Nevermind.":
            show becca 1f
            show missy 1f
            show jersey 12
            player_name "Fine!!"
            player_name "I'll go shower at home..."
            show becca 2f
            show missy 3f
            show jersey 11
            becca "Go cry in the hall, you wuss!"
            becca "None of the other nerds will mind if you smell, anyway!"
            becca "You'll fit right with in them!"
            show becca 1f
            player_name "..."
            show jersey 12
            player_name "You really shouldn't talk about people like that."
            show becca 3f
            show missy 2f
            show jersey 11
            missy "Whatever, loser."
            show becca 2f
            show missy 1f
            becca "Just go away."
            hide missy
            hide becca
            hide jersey
            with dissolve

        "Please?" if pStats.chr() < 5:
            show becca 1f
            show missy 1f
            show jersey 10
            player_name "[chr_warn]... Pretty please?"
            show jersey 13
            pause
            show missy 2f
            show becca 3f
            show jersey 11
            missy "[chr_warn]Like, that was pathetic!"
            show missy 3f
            show becca 2f
            becca "[chr_warn]Yeah, you aren't getting through."
            show missy 1f
            show becca 1f
            show jersey 10
            player_name "[chr_warn]But I really need a shower!"
            show missy 3f
            show becca 2f
            show jersey 12
            becca "[chr_warn]Go wash off in the water fountain!"
            show missy 1f
            show becca 1f
            show jersey 12
            player_name "[chr_warn]It's not a water fountain, it's a bubbler!"
            show missy 3f
            show becca 2f
            show jersey 11
            becca "[chr_warn]Whatever! You stink!!"
            show missy 2f
            show becca 3f
            missy "[chr_warn]Get out of our face! Like, now!"
            show missy 1f
            show becca 1f
            show jersey 10
            player_name "[chr_warn]Oh come on! Please, I smell really bad!"
            show missy 3f
            show becca 2f
            show jersey 11
            becca "[chr_warn]Haha! Of course you do! You always will!"
            show missy 2f
            show becca 1f
            missy "[chr_warn]Move along..."
            hide missy
            hide becca
            hide jersey
            with dissolve

        "Please?" if pStats.chr() >= 5:
            show becca 1f
            show missy 1f
            show jersey 10 at Position (xpos=200) with fastdissolve
            player_name "Please! I smell so bad..."
            show becca 2f
            show jersey 11
            becca "Eew! don't come any closer!"
            show becca 1f
            show missy 2f
            missy "Like, stay away!"
            show becca 2f
            show missy 3f
            becca "We don't want your stink rubbing off on us!"
            show becca 1f
            show missy 1f
            show jersey 12
            player_name "Then I suggest you let me shower!"
            show becca 2f
            show missy 3f
            show jersey 11
            becca "We can't! {b}Roxxy{/b}'s in there!"
            show missy 1f
            show becca 1f
            show jersey 12
            player_name "If you don't let me in, I'll get {b}Annie{/b} and you can deal with {b}Mrs. Smith{/b} instead..."
            show missy 2f
            show becca 3f
            show jersey 13
            missy "No! Don't!"
            show becca 2f
            show missy 3f
            becca "I... I can't stand the smell any longer!"
            becca "Let's, like, get outta here!"
            hide becca
            hide missy
            with dissolve
            show jersey 17
            player_name "There..."
            player_name "Time for a nice warm shower!"
            hide jersey with dissolve
            scene lockershowers with fade
            player_name "..."
            show jersey 11 at left
            show roxxy 25 at right
            with dissolve
            rox "!!!"
            show roxxy 26
            show jersey 22
            rox "What the fuck are doing in here?!" with hpunch
            show roxxy 25
            show jersey 23
            player_name "Uhh..."
            show roxxy 26
            show jersey 11
            rox "Get out!"
            show roxxy 25
            show jersey 10
            player_name "I won't take long!! I just need-"
            show roxxy 26
            show jersey 22
            rox "NO!! Get OUT of here!" with hpunch
            show roxxy 25
            hide jersey with fastdissolve
            pause
            show roxxy 26
            rox "I can't believe they let him in!"
            rox "Ughh!!!"
            rox "{b}[firstname]{/b}, you are soooooo dead!"
            scene locker_empty_b with None
            show player 11 with dissolve
            player_name "( Wow... )"
            player_name "( Can't believe I just saw {b}Roxxy{/b} naked!! )"
            show player 13
            player_name "( She has a really nice body. )"
            show player 11
            player_name "( I hope {b}Dexter{/b} doesn't find out about this... )"
            hide player with dissolve
            $ roxxy_shower.finish()
            $ roxxy_shower_lock = True
            $ location_count = "School Left Hallway"
    $ callScreen(location_count)

label denied_access_locker:
    scene locker_night
    show erik 1f at Position (xpos = 550, ypos = 768)
    show player 34 at Position (xpos = 370, ypos = 768)
    player_name "Hmm..."
    show player 113
    player_name "( We should find {b}another way{/b}. )"
    hide player 113
    hide erik 1f
    $ callScreen(location_count)

label door17_locked_dialogue:
    scene locker
    show jersey 10 at left
    player_name "( I should go to the {b}Field{/b} for my {b}Athletics{/b} class... )"
    $ callScreen(location_count)