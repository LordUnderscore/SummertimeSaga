default temp_list = []
default chico_random = 0
default chad_random = 0
default tyrone_random = 0
init python:
    class Rap:
        def __init__(self, line, rhymes, answer):
            self.line = line
            self.rhymes = rhymes
            self.answer = answer


    style.rapbattle = Style(style.button)
    style.rapbattle_text = Style(style.text)
    style.button["rapbattle"].idle_background = "buttons/rap_ui_button01.png"
    style.button["rapbattle"].hover_background = "buttons/rap_ui_button01b.png"
    style.button["rapbattle"].xsize = 277
    style.button["rapbattle"].ysize = 69

    style.text["rapbattle_text"].background = Frame("buttons/rap_ui_button01.png", 277,79)
    style.text["rapbattle_text"].size = 22
    style.text["rapbattle_text"].color = ("#ffffff")
    style.text["rapbattle_text"].pos = (50,23)

    style.time_bar.left_bar = "buttons/bar_full.png"
    style.time_bar.right_bar = "buttons/bar_empty.png"


screen rapbattle:
    add "backgrounds/minigame05b.jpg"
    add "buttons/rap_ui_mc.png" pos 400,250
    text temp_list[player_point].line size 22 pos 520,280
    $ rap_index = 0
    $ a = 570
    for Rap in temp_list[player_point].rhymes:
        $ b = 380 + rap_index*60
        textbutton temp_list[player_point].rhymes[rap_index] style style.button["rapbattle"] text_style style.text["rapbattle_text"] pos a,b action If(temp_list[player_point].rhymes[rap_index] == temp_list[player_point].answer, Jump("end_phase"), [Hide("rapbattle"), Jump("rapbattle_lose")])
        $ rap_index += 1
    timer 0.02 repeat True action If(time_count > 0, SetVariable("time_count", time_count - 0.01), [Hide("rapbattle"), Jump("rapbattle_lose")])
    bar value time_count range timer_range pos 260,685 xmaximum 513 ymaximum 33 style "time_bar"

label rapbattle_listing:
    if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap.ogg"):
        $ playMusic("<loop 108.292 to 180.658>audio/music_rap.ogg")

    $ chico1 = Rap(line = "Chico, why are you such a bitch?\nYour busted lip gonna need a ____.", rhymes = ["stitch", "patch", "kiss"], answer = "stitch")
    $ chico2 = Rap(line = "You sure your name's not Rick?\nCuz, right now you're being a ____.", rhymes = ["dick", "penis", "ass"], answer = "dick")
    $ chico_list = [chico1, chico2]
    $ chico3 = Rap(line = "You want a command? I'll give you three.\nYou shall have no other gods\nbefore ____.", rhymes = ["me", "Kao", "Jesus"], answer = "me")
    $ chico4 = Rap(line = "Bow before me and respect my flow.\nI give the commands now,\nthis is my ____.", rhymes = ["show", "rap", "life"], answer = "show")
    $ chico_list2 = [chico3, chico4]
    $ chico5 = Rap(line = "Besides Eve, all I see here is posers.\nYou may have started this flow,\nbut I'll be the ____.", rhymes = ["closer", "better", "Jesus"], answer = "closer")
    $ chico6 = Rap(line = "And really man? One of your kin?\nI could pull better raps from\nthe garbage ____.", rhymes = ["bag", "truck", "bin"], answer = "bin")
    $ chico_list3 = [chico5, chico6]
    $ chico7 = Rap(line = "Hey yo, Chico, you really wanna rap?\nYou talkin like you got feathers in ____.", rhymes = ["yo cap", "yo hair", "yo ass"], answer = "yo cap")
    $ chico8 = Rap(line = "Yo, your rhymes are so whack;\nAll you need is a ____.", rhymes = ["new shtick", "laugh track", "mom's spaghetti"], answer = "laugh track")
    $ chico_list4 = [chico7, chico8]

    $ chad_time = 6.0
    $ chad1 = Rap(line = "It's real nice to meet you Chad and I am\nglad that I did, Because you flows are\nweak, and you're built like a ____.", rhymes = ["kid", "woman", "elephant"], answer = "kid")
    $ chad2 = Rap(line = "I might be in your class, but you will\nlearn from me. I am going to fix your art,\nand I'll even do it for ____.", rhymes = ["free", "a massage", "everyone"], answer = "free")
    $ chad3 = Rap(line = "There is nothing you can teach me,\nyou ain't mastered shit. You can have\nthis seat now, I think it's time YOU ____.", rhymes = ["sit", "go away", "fuckoff"], answer = "sit")
    $ chad4 = Rap(line = "Your prose is weak, and your\ncomposition isn't worth mention, Your\nflows are a failure and that nets you ____.", rhymes = ["detention", "autism", "applause"], answer = "detention")
    $ chad_list = [chad1, chad2, chad3, chad4]
    $ chad5 = Rap(line = "This tired rap again? Alright Chad,\nlet's make it wild, You like this school\nthing huh? Well come on then, ____.", rhymes = ["child", "dude", "loser"], answer = "child")
    $ chad6 = Rap(line = "I'm not here to impress you, but trust\nme, i'll leave an impression, you wont be\nable to walk after i'm done with this ____.", rhymes = ["session", "shit", "line"], answer = "session")
    $ chad7 = Rap(line = "You are a pretty boy, so yeah, let's talk\nabout you, and about how I am\ndestroying you and that pansy ass ____.", rhymes = ["hairdo", "style", "face"], answer = "hairdo")
    $ chad8 = Rap(line = "You wanna spit science about the heat\nof convection? I roasted you\nand it gave your boys' an ____.", rhymes = ["erection", "autism", "goosebumps"], answer = "erection")
    $ chad_list2 = [chad5, chad6, chad7, chad8]
    $ chad9 = Rap(line = "Let's not talk about skin, as thin as\nyours is, I'm all up in your hood,\nand you know it's my ____.", rhymes = ["biz", "woman", "elephant"], answer = "biz")
    $ chad10 = Rap(line = "Yeah, I wear sandals, because sneakers\nwould melt, My fire's hotter than yours,\nwhen I take off my ____.", rhymes = ["belt", "pants", "wig"], answer = "belt")
    $ chad11 = Rap(line = "I give a shit about your wit, mine's as\nsharp as a blade, When I am done with\nyour ass, I'll hit up the mall and get ____.", rhymes = ["laid", "drunk", "thrown out"], answer = "laid")
    $ chad12 = Rap(line = "So it's been fun in your class, shame\nyour raps were bad, I graduated this\nschool, it's over, Goodbye ____.", rhymes = ["Chad", "everyone", "waifus"], answer = "Chad")
    $ chad_list3 = [chad9, chad10, chad11, chad12]

    $ tyrone_time = 6.0
    $ tyrone1 = Rap(line = "Don't talk about my family, i'll fuckin\ncut you. I got a sword at the house,\nsharp as a ____.", rhymes = ["Ginsu", "Jutsu", "Windu"], answer = "Ginsu")
    $ tyrone2 = Rap(line = "But nothings as sharp as this rap's\ngroove, like a knife in your heart,\njust can't ____.", rhymes = ["remove", "behoove", "disprove"], answer = "remove")
    $ tyrone3 = Rap(line = "You ignited in me a murderous intent,\nI need to calm down before I am ____.", rhymes = ["spent", "bent", "pent"], answer = "spent")
    $ tyrone4 = Rap(line = "Let me get some of that brownie, guy,\nI need relief too, so don't\nBogart the ____.", rhymes = ["high", "side", "stride"], answer = "high")
    $ tyrone5 = Rap(line = "You're the only Rasta that I've ever\nmet, the gayest one too, if I had to ____.", rhymes = ["bet", "fret", "sweat"], answer = "bet")
    $ tyrone6 = Rap(line = "You're not in the streets you punk ass\nmark, I've been all around,\nyou ain't left this ____.", rhymes = ["park", "dark", "spark"], answer = "park")
    $ tyrone7 = Rap(line = "And yeah, I remember how I came to be,\nI smacked two bitches,\nyou about to be ____.", rhymes = ["three", "free", "thee"], answer = "three")
    $ tyrone8 = Rap(line = "I don't need to finish, I defused your\nbomb, replaced it with my\nown burning ____.", rhymes = ["napalm", "palm", "psalm"], answer = "napalm")
    $ tyrone_list = [tyrone1, tyrone2, tyrone3, tyrone4, tyrone5, tyrone6, tyrone7, tyrone8]
    $ tyrone9 = Rap(line = "I told you once before and I'll tell\nyou again, leave my family out\nof this before I turn wrath past ____.", rhymes = ["ten", "ballpen", "glen"], answer = "ten")
    $ tyrone10 = Rap(line = "I'll turn the heat to eleven when I'm\nbustin on you, I'm Mr. T. in this\nmatch and I pity you, ____.", rhymes = ["foo", "r2d2", "too"], answer = "foo")
    $ tyrone11 = Rap(line = "You fancy yourself a dragon? Bitch,\nthat's cute. You got the weight of a\nlizard in a cheap ass ____.", rhymes = ["suit", "route", "loot"], answer = "suit")
    $ tyrone12 = Rap(line = "I'm a real dragon slayer, and pussy\nslayer to boot, I got a harem in my lair,\nwhat you got? ____?", rhymes = ["Fruit", "cute", "mute"], answer = "Fruit")
    $ tyrone13 = Rap(line = "You couldn't roast me, even if you\nhad MY fire, You going to lose this battle\nnow that you provoked my ____.", rhymes = ["ire", "gyr", "squire"], answer = "ire")
    $ tyrone14 = Rap(line = "You think you'd beaten me when I\nstart to bleed? This is an underdog\nstory, that's the motivation I ____.", rhymes = ["need", "bead", "deed"], answer = "need")
    $ tyrone15 = Rap(line = "I got the impact like a bullet to\nthe brain, you front on me?\nYou must be ____.", rhymes = ["insane", "krain", "inane"], answer = "insane")
    $ tyrone16 = Rap(line = "I seen through you and I know what\nyou are. Go own home boy, take yo\nRasta ass ____.", rhymes = ["far", "bar", "car"], answer = "far")
    $ tyrone_list2 = [tyrone9, tyrone10, tyrone11, tyrone12, tyrone13, tyrone14, tyrone15, tyrone16]
    $ tyrone17 = Rap(line = "Hold up, let me start the battle this\ntime. It's a preemptive strike,\nkicking your ass with ____.", rhymes = ["rhyme", "grime", "dime"], answer = "rhyme")
    $ tyrone18 = Rap(line = "I beat your boys, you the last on the\nlist, Chico was commanded,\nand Chad was ____.", rhymes = ["dissmissed", "hissed", "pissed"], answer = "dissmissed")
    $ tyrone19 = Rap(line = "I'd say I already killed you, but you\nstill breathin, and that's about to\nbe corrected, you dank ass ____.", rhymes = ["heathen", "freeman", "semen"], answer = "heathen")
    $ tyrone20 = Rap(line = "I've heard your raps and listened to\nyou rip, It's time to put you to bed\nwith a saline ____.", rhymes = ["drip", "clip", "rip"], answer = "drip")
    $ tyrone21 = Rap(line = "I'd look you in the eye, but I can't\nsee through the smoke, you thought you\nspit fire, but yo ass is a ____.", rhymes = ["joke", "bloke", "croak"], answer = "joke")
    $ tyrone22 = Rap(line = "I got ice in my veins, I'm vicious\nand cold. I'll end you right here, you\nwon't have a chance to get ____.", rhymes = ["old", "bold", "cold"], answer = "old")
    $ tyrone23 = Rap(line = "Remember my words when I put your\nass down, you asked for this in the\nbeginning when you called me a ____.", rhymes = ["clown", "down", "frown"], answer = "clown")
    $ tyrone24 = Rap(line = "Who's laughing now, bitch? You don't\nlook so good, I'm here now,\nI showed you, This is MY ____.", rhymes = ["hood", "wood", "stood"], answer = "hood")
    $ tyrone_list3 = [tyrone17, tyrone18, tyrone19, tyrone20, tyrone21, tyrone22, tyrone23, tyrone24]
    $ tyrone25 = Rap(line = "I'm a stop you right there, it's clear\nthat your done. Your straight outta raps,\nand I gotta ____.", rhymes = ["ton", "phone", "none"], answer = "ton")
    $ tyrone26 = Rap(line = "So i'll take your boat, and sail the\nrap sea. Undefeated and undisputed,\nbest ____.", rhymes = ["MC", "DC", "PC"], answer = "MC")
    $ tyrone27 = Rap(line = "I've defeated your crew and now you\nbow, Look at me, bitch,\nI'm the Captain ____.", rhymes = ["now", "cow", "dove"], answer = "now")
    $ tyrone_list4 = [tyrone25, tyrone26, tyrone27]

    $ player_point = 0

    if rap_opponent == "chico":
        jump chico01
    elif rap_opponent == "chad":
        jump chad01
    elif rap_opponent == "tyrone":
        jump tyrone01

label chico01:
    $ time_count = 3.5
    $ timer_range = 3.5
    scene rapbattle01bg
    show rapbattle_npc at Position(xpos = 350, ypos = 750)
    if pStats.chr() > 3:
        $ chico_random = renpy.random.randint(1,4)
    if pStats.chr() == 0 or chico_random == 1:
        show text " {size=17}You think you can stand up to me\nwhite bread?\nEven before you start, you're already dead!{/size}" at Position(xpos = 320, ypos = 675)
        $ renpy.pause()
        hide text
        show text "{size=17}You so bland you like plain ol' toast;\nLemme show you how the western ESE roast!{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list4
    elif pStats.chr() == 1 or chico_random == 2:
        show text " {size=17}You back, but you should have ran,\nabout to get whipped by the latino man.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}This is our park, and your ass is banned,\nYou best leave now, and that's a command.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list2
    elif pStats.chr() == 2 or chico_random == 3:
        show text " {size=17}You feeling yourself, with a couple of wins?\nStep up hard and be recognized as kin.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}So drop some bars and rock this beat,\nor take your ass home and beat your meat.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list3
    elif pStats.chr() == 3 or chico_random == 4:
        show text " {size=17}Look at this fool, he's shaken.\nI know this fool mistaken,{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}For ever thinking he could step to me,\nMust have bumped his head at three.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label chad01:
    $ time_count = 5.0
    $ timer_range = 5.0
    scene rapbattle02bg
    show rapbattle_npc at Position(xpos = 350, ypos = 750)
    if pStats.chr() > 6:
        $ chad_random = renpy.random.randint(1,3)
    if pStats.chr() == 4 or chad_random == 1:
        show text " {size=17}I know we just met and I hate to be rude,\nBut Chico should have ended you man,\nyou shouldn't be here dude.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}But welcome to my class,\nschool's about to start,\nTake a seat boy, you'll wanna copy this art.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}You might learn something rapping against\na man who mastered, trust me, you'll\nneed refined flows, because you a ugly bastard.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Class is over and there is nothing left for\nyou here, I blew my rap load in your face,\nand it's dripping from your ear.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chad_list
    elif pStats.chr() == 5 or chad_random == 2:
        show text " {size=17}You're back again and the bell's about to ring,\nSchool is in session let's do this thing.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}I was almost impressed last time, but you still\nwack as hell. You been jacking it alone?\nYour shorts sticky as hair gel.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}But enough about you, let's talk about me,\nI'm the chillest around but\nI'm gonna bring the heat.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Like a flash in the pan,\nthis battle's already done\nI've cooked you dude, give up. I've won.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chad_list2
    elif pStats.chr() == 6 or chad_random == 3:
        show text " {size=17}My skin is light, but my heart is dark,\nYou in my hood boy, I run this park. {/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Stepped to me in shorts and sandals,\nI got the fire raps, too hot to handle.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}I been had that wicked wit, Make you dumb\non stupid shit, Think you gonna go and hit,\nbut I seen cum where you sit.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}You thought you passed, but you only missed,\nSchool’s out for summer\nand your ass is dismissed.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chad_list3
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label tyrone01:
    $ time_count = 8.0
    $ timer_range = 8.0
    scene rapbattle03bg
    show rapbattle_npc at Position(xpos = 350, ypos = 750)
    if pStats.chr() > 9:
        $ tyrone_random = renpy.random.randint(1,3)
    if pStats.chr() == 7 or tyrone_random == 1:
        show text " {size=17}Don't front, don't fret, I'm comin' with force\njumping in windows and kicking in doors{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Be like the police up in here serving,\nwarrants on yo ass that you deserving.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}I'm the baddest Rasta that you'll ever see,\nit was a mistake when you started fuckin' with me.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}I'm a heat up this beat and start up the coal,\ncook this little MC like a casserole. {/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text " {size=17}While I'm in the kitchen I'll make a brownie,\nneed relief from this fool tryin' to clown me.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Back to the streets and onto my block,\nI'm hood from my head to the tip my cock.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}And never forget how you made it to me,\nbarely scraping through with each victory.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Now that I finished and dropped this bomb,\nI'll drop by your crib and fuck your mom.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = tyrone_list
    elif pStats.chr() == 8 or tyrone_random == 2:
        show text " {size=17}Back in the spot, time to start again,\nhang up the mic bitch, you know imma win.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}My raps are fast and mind is faster,\nYou step to me, you step to a master.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}I am the final boss of this little quest of yours,\nI got hellfire rain and it's about to downpour.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}I spit heat from my mouth like Chinese dragon,\nI'll roast you alive boy and sip the flagon.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text " {size=17}Light up the toke from the heat of your ashes,\npuff puff pass and hand off to the masses.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}A crowd will gather as we put you in the dirt,\nI'll comfort your moms when her feelings are hurt.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Take her back to my place and dick her deep, mister,\nthrow her ass away and go after your sister.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Morale of the story is I'll kill you fool,\nlyrically unmatched, when your blood starts to pool.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = tyrone_list2
    elif pStats.chr() == 9 or tyrone_random == 3:
        $ temp_list = tyrone_list3
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label tyrone02:
    show text " {size=17}I thought you had enough last time you here,\nthis time I'll finish you like a blast to the ear.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text "{size=17}You see, I been in this park much longer than you,\nfought up from the bottom and earned this crew.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text "{size=17}You think you can come here rocking my boat?\nI'll kick you overboard and see if you float.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text "{size=17}I can't believe you got here spittin' your cheese,\nyou won't get past me, I'll drop you with ease.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text " {size=17}So now it's time to put you in your place,\nI'm tired of you boy, can't stand your fuckin' face.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    $ temp_list = tyrone_list4
    $ player_point = 0
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle  

label end_phase:
    if rap_opponent == "chico":
        $ time_count = 7
        $ timer_range = 7
    elif rap_opponent == "chad" or rap_opponent == "tyrone":
        $ time_count = 9
        $ timer_range = 9
    $ player_point += 1
    if temp_list == tyrone_list3 and player_point == len(temp_list):
        jump tyrone02
    if player_point == len(temp_list):
        hide screen rapbattle
        if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
            $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")
        if rap_opponent == "chico":
            jump rapbattle_win_chico
        elif rap_opponent == "chad":
            jump rapbattle_win_chad
        elif rap_opponent == "tyrone":
            jump rapbattle_win_tyrone
    else:
        $ renpy.random.shuffle(temp_list[player_point].rhymes)
        call screen rapbattle

label rapbattle_win_chico:
    $ renpy.suspend_rollback(False)
    $ renpy.checkpoint()
    scene park_bench
    show douche 2 at right with dissolve
    show chico 3 with dissolve
    show player 76 at left with dissolve
    chi "You loco, man!"
    show chico 2
    chi "...That was good..."
    show chico 1
    show player 77 at left
    player_name "Thanks!"
    show chico 2
    show player 76 at left
    chi "Aight, man, peace!"
    hide chico
    hide douche
    with dissolve
    $ gTimer.tick()
    if rap_opponent == "chico" and pStats.chr() < 4:
        $ pStats.increase("chr")
        show unlock23 at truecenter with dissolve
        $ renpy.pause()
        hide unlock23 at truecenter with dissolve
    $ rap_opponent = ""
    if eve_park_dialogue == 0:
        jump eve_after_win
    else:
        $ callScreen(location_count)

label rapbattle_win_chad:
    $ renpy.suspend_rollback(False)
    $ renpy.checkpoint()
    scene park_bench
    show chad 2 at right
    show player 203 at left
    chad "Not bad kid. Not bad at all."
    chad "Maybe I misjudged you a bit."
    show chad 1
    show player 2
    player_name "Thanks. You were good, too."
    $ gTimer.tick()
    if rap_opponent == "chad" and pStats.chr() < 7:
        $ pStats.increase("chr")
        show unlock23 at truecenter with dissolve
        $ renpy.pause()
        hide unlock23 at truecenter with dissolve

    $ rap_opponent = ""
    if eve_park_dialogue == 0:
        jump eve_after_win
    else:
        $ callScreen(location_count)

label rapbattle_win_tyrone:
    $ renpy.suspend_rollback(False)
    $ renpy.checkpoint()
    scene park_bench
    show player 203 at left
    show tyrone 2 at right
    tyrone "Not going to lie that wasn't half bad."
    tyrone "I want to see you around here again aight."
    show player 2
    show tyrone 1
    player_name "Sure I’ll see."
    $ gTimer.tick()
    if rap_opponent == "tyrone" and pStats.chr() < 10:
        $ pStats.increase("chr")
        show unlock23 at truecenter with dissolve
        $ renpy.pause()
        hide unlock23 at truecenter with dissolve
    $ rap_opponent = ""
    if eve_park_dialogue == 0:
        jump eve_after_win
    else:
        $ callScreen(location_count)

label rapbattle_lose:
    if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
        $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")
    $ renpy.suspend_rollback(False)
    $ renpy.checkpoint()
    scene park_bench
    if rap_opponent == "chico":
        show douche 2 at right with dissolve
        show chico 3 with dissolve
        show player 74 at left with dissolve
        chi "Yo! That was some weak lyrics!"
        show chico 1
        show player 75 at left
        player_name "..."
        show chico 4
        chi "Get outta here, foo!"
        hide chico 4
        hide douche
        with dissolve

    elif rap_opponent == "chad":
        show chad 4 at right
        show player 3 at left
        chad "Yo I feel so insulted right now."
        show chad 3
        chad "You had the balls to step up to me, but then come to me with this trash!"
        chad "I better never see your face around here again!"

    elif rap_opponent == "tyrone":
        show player 3 at left
        show tyrone 3 at right
        tyrone "Why'd you even come here?"
        tyrone "Went and wasted my time. Now, I’m pissed"
        tyrone "You need a personal escort or something!? Leave!"
    $ gTimer.tick()
    show unlock24 at truecenter with dissolve
    $ renpy.pause()
    hide unlock24 at truecenter with dissolve
    $ rap_opponent = ""
    if eve_park_dialogue == 0:
        jump eve_after_lose
    else:
        $ callScreen(location_count)