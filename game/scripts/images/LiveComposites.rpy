
image school = ConditionSwitch(
    "datetime.date.today().month == 12 and (datetime.date.today().day >= 15 and datetime.date.today().day <= 30)", "backgrounds/location_school_christmas_blur.jpg",
    "(datetime.date.today().month == 10 and datetime.date.today().day > 25) and (datetime.date.today().month == 11 and datetime.date.today().day < 2)", "backgrounds/location_school_halloween_blur.jpg",
    "True", "backgrounds/location_school_blur.jpg",
    )
image school_night = ConditionSwitch(
    "datetime.date.today().month == 12 and (datetime.date.today().day >= 15 and datetime.date.today().day <= 30)", "backgrounds/location_school_christmas_night_blur.jpg",
    "(datetime.date.today().month == 10 and datetime.date.today().day > 25) and (datetime.date.today().month == 11 and datetime.date.today().day < 2)", "backgrounds/location_school_halloween_night_blur.jpg",
    "True", "backgrounds/location_school_night_blur.jpg",
    )
image graveyard = ConditionSwitch(
    "(datetime.date.today().month == 10 and datetime.date.today().day > 25) and (datetime.date.today().month == 11 and datetime.date.today().day < 2)", "backgrounds/location_church_graveyard_halloween_blur.jpg",
    "True", "backgrounds/location_church_graveyard_blur.jpg",
    )
image graveyard_night = ConditionSwitch(
    "(datetime.date.today().month == 10 and datetime.date.today().day > 25) and (datetime.date.today().month == 11 and datetime.date.today().day < 2)", "backgrounds/location_church_graveyard_halloween_night_blur.jpg",
    "True", "backgrounds/location_church_graveyard_night_blur.jpg",
    )


image card_2 = ConditionSwitch(
    "not erik.known(erik_crown_card) or erik.completed(erik_crown_card)", "objects/item_card2.png",
    "erik.started(erik_crown_card)", "objects/item_card2_quest.png",
    "True", Null(),
    )
image card_2b = ConditionSwitch(
    "not erik.known(erik_crown_card) or erik.completed(erik_crown_card)", "objects/item_card2b.png",
    "erik.started(erik_crown_card)", "objects/item_card2b_quest.png",
    "True", Null(),
    )
image game_1 = ConditionSwitch(
    "not erik.completed(erik_favor) or erik.known(erik_favor_2)", "objects/item_game1.png",
    "erik.completed(erik_favor) and not erik.known(erik_favor_2)", "objects/item_game1_quest.png",
    "True", Null(),
    )
image game_1b = ConditionSwitch(
    "not erik.completed(erik_favor) or erik.known(erik_favor_2)", "objects/item_game1b.png",
    "erik.completed(erik_favor) and not erik.known(erik_favor_2)", "objects/item_game1b_quest.png",
    "True", Null(),
    )
image game_2 = ConditionSwitch(
    "not erik.known(erik_vr) or erik.completed(erik_vr)", "objects/item_game2.png",
    "erik.started(erik_vr)", "objects/item_game2_quest.png",
    "True", Null(),
    )
image game_2b = ConditionSwitch(
    "not erik.known(erik_vr) or erik.completed(erik_vr)", "objects/item_game2b.png",
    "erik.started(erik_vr)", "objects/item_game2b_quest.png",
    "True", Null(),
    )
image cosplay_1 = ConditionSwitch(
    "not June.known(june_cosplay) or June.completed(june_cosplay)", "objects/item_cosplay1.png",
    "June.started(june_cosplay)", "objects/item_cosplay1_quest.png",
    "True", Null(),
    )
image cosplay_1b = ConditionSwitch(
    "not June.known(june_cosplay) or June.completed(june_cosplay)", "objects/item_cosplay1b.png",
    "June.started(june_cosplay)", "objects/item_cosplay1b_quest.png",
    "True", Null(),
    )
image sex_6 = ConditionSwitch(
    "True", "objects/item_sex6.png",
    "False", "objects/item_sex6_quest.png",
    "True", Null(),
    )
image sex_6b = ConditionSwitch(
    "True", "objects/item_sex6b.png",
    "False", "objects/item_sex6b_quest.png",
    "True", Null(),
    )
image sex_17 = ConditionSwitch(
    "M_mia.get_state != S_mia_helen_outfit_request", "objects/item_sex17.png",
    "M_mia.get_state == S_mia_helen_outfit_request", "objects/item_sex17_quest.png",
    "True", Null(),
    )
image sex_17b = ConditionSwitch(
    "M_mia.get_state != S_mia_helen_outfit_request", "objects/item_sex17b.png",
    "M_mia.get_state == S_mia_helen_outfit_request", "objects/item_sex17b_quest.png",
    "True", Null(),
    )


image sis_computer_bg = LiveComposite(
    (1024,768),
    (0,0), "backgrounds/computer_sis_02.jpg",
    (105,603), "buttons/computer_button_02.png",
    (105,140), "buttons/computer_icon_01.png",
    (105,250), "buttons/computer_icon_02.png",
    (105,360), "buttons/computer_icon_03.png",
    (105,470), "buttons/computer_icon_04.png",
    (215,140), "buttons/computer_icon_05.png",
    (215,250), "buttons/computer_icon_06.png",
    (215,360), "buttons/computer_icon_22.png",
    )
image sis_computer_nude = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_03.png",
    (270,150), "buttons/computer_pic_03.png",
    )
image sis_computer_family = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_01.png",
    (270,150), "buttons/computer_pic_05.png",
    )
image sis_computer_swimsuit = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_02.png",
    (270,150), "buttons/computer_pic_01.png",
    )
image sis_computer_igor = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_01.png",
    (270,150), "buttons/computer_pic_04.png",
    )
image sis_computer_summertime = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_08.png",
    )
image sis_computer_webcam = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_06.png",
    (719,495), "buttons/computer_button_04.png",
    )
image sis_computer_toylist = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_04.png",
    )
image sis_computer_livecrush = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_05.png",
    )
image sis_computer_email = LiveComposite(
    (1024,768),
    (135,150), "buttons/computer_window_11.png",
    (235,251), "buttons/computer_email_01.png",
    (235,291), "buttons/computer_email_02.png",
    (235,331), "buttons/computer_email_03_read.png",
    (235,371), "buttons/computer_email_04_read.png",
    (235,411), "buttons/computer_email_05_read.png",
    (235,451), "buttons/computer_email_06_read.png",
    )
image player_computer_bg_day = LiveComposite(
    (1024,768),
    (0,0), "backgrounds/computer_player_02.jpg",
    (105,603), "buttons/computer_button_02.png",
    (105,140), "buttons/computer_icon_01.png",
    (105,250), "buttons/computer_icon_02.png",
    (105,360), "buttons/computer_icon_03.png",
    (105,470), "buttons/computer_icon_04.png",
    (215,140), "buttons/computer_icon_13.png",
    (215,250), "buttons/computer_icon_14.png",
    (215,360), "buttons/computer_icon_23.png",
    )
image player_computer_bg_night = LiveComposite(
    (1024,768),
    (0,0), "backgrounds/computer_player_02_night.jpg",
    (105,603), "buttons/computer_button_02.png",
    (105,140), "buttons/computer_icon_01.png",
    (105,250), "buttons/computer_icon_02.png",
    (105,360), "buttons/computer_icon_03.png",
    (105,470), "buttons/computer_icon_04.png",
    (215,140), "buttons/computer_icon_13.png",
    (215,250), "buttons/computer_icon_14.png",
    (215,360), "buttons/computer_icon_23.png",
    )
image player_computer_webscreen_connected = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_09.png",
    (370,380), "buttons/computer_icon_20.png",
    (500,380), "buttons/computer_icon_21.png",
    (623,380), "buttons/computer_icon_21.png",
    )
image player_computer_webscreen_disconnected = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_09.png",
    (304,302), "buttons/computer_window_10.png",
    )
image player_computer_webscreen_connecting = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_09b.png",
    (490,350), Transform("webcam_loading_circle"),
    )
image player_computer_egay_search = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_12.png",
    )
image player_computer_egay_purchased = LiveComposite(
    (1024,768),
    (270,150), "buttons/computer_window_15.png",
    )

image player_computer_bg = ConditionSwitch(
    "not gTimer.is_dark()", "player_computer_bg_day",
    "gTimer.is_dark()", "player_computer_bg_night",
    "True", Null(),
    )





image player_computer_webscreen = ConditionSwitch(
    "connected == True", "player_computer_webscreen_connected",
    "connected == False", "player_computer_webscreen_disconnected",
    "True", Null(),
    )


image pink_channel_login = LiveComposite(
    (1024,768),
    (0,0), "backgrounds/location_tv.jpg",
    (86,107), "buttons/tv_channel_08.png", 
    )


image hospital_cabinet_filled = LiveComposite(
    (1024,768),
    (0,0), "backgrounds/location_hospital_cabinet.jpg",
    (98,173), "objects/object_pharmacy_01.png",
    (486,207), "objects/object_pharmacy_02.png",
    (770,226), "objects/object_pharmacy_03.png",
    (148,469), "objects/object_pharmacy_04.png",
    (331,502), "objects/object_pharmacy_05.png",
    (596,466), "objects/object_pharmacy_06.png",
    (732,457), "objects/object_pharmacy_07.png",
    )


image moms_59x = LiveComposite(
    (711,752),
    (0,0), "characters/mom/char_mom_sex_59.png",
    (267,487), "characters/player/char_player_sex_54.png", 
    )
image moms_60x = LiveComposite(
    (700,751),
    (0,0), "characters/mom/char_mom_sex_60.png",
    (262,475), "characters/player/char_player_sex_55.png",  
    )
image moms_60xc = LiveComposite(
    (700,751),
    (0,0), "characters/mom/char_mom_sex_60.png",
    (262,475), "characters/player/char_player_sex_64.png",  
    )
image moms_61x = LiveComposite(
    (695,751),
    (0,0), "characters/mom/char_mom_sex_61.png",
    (276,464), "characters/player/char_player_sex_56.png", 
    )
image moms_64x = LiveComposite(
    (952,639),
    (0,0), "characters/mom/char_mom_sex_64.png",
    (263,230), "characters/player/char_player_sex_57.png", 
    )
image moms_65x = LiveComposite(
    (952,687),
    (0,0), "characters/mom/char_mom_sex_65.png",
    (347,255), "characters/player/char_player_sex_58.png", 
    )
image moms_66x = LiveComposite(
    (952,698),
    (0,0), "characters/mom/char_mom_sex_66.png",
    (378,245), "characters/player/char_player_sex_59.png", 
    )
image moms_67x = LiveComposite(
    (1024,698),
    (0,0), "characters/mom/char_mom_sex_67.png",
    (378,245), "characters/player/char_player_sex_59.png", 
    )
image moms_68x = LiveComposite(
    (1024,698),
    (0,0), "characters/mom/char_mom_sex_68.png",
    (378,245), "characters/player/char_player_sex_59.png", 
    )
image moms_69x = LiveComposite(
    (947,761),
    (0,0), "characters/mom/char_mom_sex_69.png",
    (263,352), "characters/player/char_player_sex_57.png", 
    )
image moms_69xc = LiveComposite(
    (947,761),
    (0,0), "characters/mom/char_mom_sex_69.png",
    (268,352), "characters/player/char_player_sex_60.png", 
    )
image moms_97x = LiveComposite(
    (655,744),
    (0,0), "characters/mom/char_mom_sex_97.png",
    (160,305), "characters/player/char_player_sex_61.png", 
    )
image moms_98x = LiveComposite(
    (651,744),
    (0,0), "characters/mom/char_mom_sex_98.png",
    (160,305), "characters/player/char_player_sex_62.png", 
    )
image moms_99x = LiveComposite(
    (647,727),
    (0,0), "characters/mom/char_mom_sex_99.png",
    (158,286), "characters/player/char_player_sex_63.png", 
    )
image moms_103x = LiveComposite(
    (901,502),
    (0,0), "characters/mom/char_mom_sex_103.png",
    (367,240), "characters/player/char_player_sex_65.png", 
    )
image moms_104x = LiveComposite(
    (902,509),
    (0,0), "characters/mom/char_mom_sex_104.png",
    (414,231), "characters/player/char_player_sex_66.png", 
    )
image moms_105x = LiveComposite(
    (903,509),
    (0,0), "characters/mom/char_mom_sex_105.png",
    (434,237), "characters/player/char_player_sex_67.png", 
    )
image moms_105xc = LiveComposite(
    (903,509),
    (0,0), "characters/mom/char_mom_sex_105.png",
    (414,231), "characters/player/char_player_sex_68.png", 
    )
image moms_106c = LiveComposite(
    (905,627),
    (0,0), "characters/mom/char_mom_sex_106.png",
    (374,307), "characters/player/char_player_sex_69.png", 
    )















image moms_129x = LiveComposite(
    (536,626),
    (0,0), "characters/mom/char_mom_sex_129.png",
    (185,321), "characters/player/char_player_sex_79.png", 
    )

image moms 59 = ConditionSwitch(
    "xray == True", "moms_59x",
    "xray == False", "characters/mom/char_mom_sex_59.png",
    "True", Null(),
    )
image moms 60 = ConditionSwitch(
    "xray == True and cum == True", "moms_60xc",
    "xray == True", "moms_60x",
    "xray == False", "characters/mom/char_mom_sex_60.png",
    "True", Null(),
    )
image moms 61 = ConditionSwitch(
    "xray == True", "moms_61x",
    "xray == False", "characters/mom/char_mom_sex_61.png",
    "True", Null(),
    )
image moms 64 = ConditionSwitch( 
    "xray == True", "moms_64x",
    "xray == False", "characters/mom/char_mom_sex_64.png",
    "True", Null(),
    )
image moms 65 = ConditionSwitch( 
    "xray == True", "moms_65x",
    "xray == False", "characters/mom/char_mom_sex_65.png",
    "True", Null(),
    )
image moms 66 = ConditionSwitch( 
    "xray == True", "moms_66x",
    "xray == False", "characters/mom/char_mom_sex_66.png",
    "True", Null(),
    )
image moms 67 = ConditionSwitch( 
    "xray == True", "moms_67x",
    "xray == False", "characters/mom/char_mom_sex_67.png",
    "True", Null(),
    )
image moms 68 = ConditionSwitch( 
    "xray == True", "moms_68x",
    "xray == False", "characters/mom/char_mom_sex_68.png",
    "True", Null(),
    )
image moms 69 = ConditionSwitch( 
    "xray == True and cum == True", "moms_69xc",
    "xray == True", "moms_69x",
    "xray == False", "characters/mom/char_mom_sex_69.png",
    "True", Null(),
    )
image moms 97 = ConditionSwitch( 
    "xray == True", "moms_97x",
    "xray == False", "characters/mom/char_mom_sex_97.png",
    "True", Null(),
    )
image moms 98 = ConditionSwitch(
    "xray == True", "moms_98x",
    "xray == False", "characters/mom/char_mom_sex_98.png",
    "True", Null(),
    )
image moms 99 = ConditionSwitch(
    "xray == True", "moms_99x",
    "xray == False", "characters/mom/char_mom_sex_99.png",
    "True", Null(),
    )
image moms 103 = ConditionSwitch( 
    "xray == True", "moms_103x",
    "xray == False", "characters/mom/char_mom_sex_103.png",
    "True", Null(),
    )
image moms 104 = ConditionSwitch( 
    "xray == True", "moms_104x",
    "xray == False", "characters/mom/char_mom_sex_104.png",
    "True", Null(),
    )
image moms 105 = ConditionSwitch( 
    "xray == True and cum == True", "moms_105xc",
    "xray == True", "moms_105x",
    "xray == False", "characters/mom/char_mom_sex_105.png",
    "True", Null(),
    )
image moms 106 = ConditionSwitch( 
    "cum == True", "moms_106c",
    "cum == False", "characters/mom/char_mom_sex_106.png",
    "True", Null(),
    )















image moms 129 = ConditionSwitch(
    "xray == True", "moms_129x",
    "xray == False", "characters/mom/char_mom_sex_129.png",
    "True", Null(),
    )


image aunts_57x = LiveComposite(
    (711,752),
    (0,0), "characters/aunt/char_aunt_sex_57.png",
    (267,487), "characters/player/char_player_sex_54.png", 
    )

image aunts 57 = ConditionSwitch( 
    
    
    "shed_xray_toggle == False", "characters/aunt/char_aunt_sex_57.png",
    "True", Null(),
    )
image aunts 58 = ConditionSwitch( 
    
    
    "shed_xray_toggle == False", "characters/aunt/char_aunt_sex_58.png",
    "True", Null(),
    )
image aunts 59 = ConditionSwitch( 
    
    
    "shed_xray_toggle == False", "characters/aunt/char_aunt_sex_59.png",
    "True", Null(),
    )


image sissex 77x = LiveComposite(
    (484,737),
    (0,0), "characters/sis/char_sis_sex_77.png",
    (145,305), "characters/sis/char_sis_sex_78x.png"
    )
image sissex 78x = LiveComposite(
    (484,737),
    (0,0), "characters/sis/char_sis_sex_78.png",
    (145,305), "characters/sis/char_sis_sex_78x.png"
    )
image sissex 79x = LiveComposite(
    (470,740),
    (0,0), "characters/sis/char_sis_sex_79.png",
    (131,308), "characters/sis/char_sis_sex_79x.png"
    )
image sissex 79bx = LiveComposite(
    (470,740),
    (0,0), "characters/sis/char_sis_sex_79b.png",
    (131,308), "characters/sis/char_sis_sex_79x.png"
    )
image sissex 80ac = LiveComposite(
    (498,760),
    (0,0), "characters/sis/char_sis_sex_80.png",
    (145,324), "characters/player/char_player_sex_105.png"
    )
image sissex 80bc = LiveComposite(
    (498,760),
    (0,0), "characters/sis/char_sis_sex_80.png",
    (145,324), "characters/player/char_player_sex_106.png"
    )
image sissex 80cc = LiveComposite(
    (498,760),
    (0,0), "characters/sis/char_sis_sex_80.png",
    (145,324), "characters/player/char_player_sex_107.png"
    )
image sissex 97x = LiveComposite(
    (644,563),
    (0,0), "characters/sis/char_sis_sex_97.png",
    (20,279), "characters/player/char_player_sex_110.png"
    )
image sissex 98x = LiveComposite(
    (644,563),
    (0,0), "characters/sis/char_sis_sex_98.png",
    (20,279), "characters/player/char_player_sex_110.png"
    )
image sissex 99x = LiveComposite(
    (630,589),
    (0,0), "characters/sis/char_sis_sex_99.png",
    (6,305), "characters/player/char_player_sex_111.png"
    )
image sissex 100x = LiveComposite(
    (673,582),
    (0,0), "characters/sis/char_sis_sex_100.png",
    (49,298), "characters/player/char_player_sex_112.png"
    )
image sissex 101x = LiveComposite(
    (715,551),
    (0,0), "characters/sis/char_sis_sex_101.png",
    (91,267), "characters/player/char_player_sex_113.png"
    )
image sissex 102x = LiveComposite(
    (635,561),
    (0,0), "characters/sis/char_sis_sex_102.png",
    (11,277), "characters/player/char_player_sex_114.png" 
    )
image sissex 102bx = LiveComposite(
    (635,561),
    (0,0), "characters/sis/char_sis_sex_102b.png",
    (11,277), "characters/player/char_player_sex_114.png" 
    )
image sissex 103x = LiveComposite(
    (644,561),
    (0,0), "characters/sis/char_sis_sex_103.png",
    (20,277), "characters/player/char_player_sex_115.png"
    )
image sissex 117x = LiveComposite(
    (643,573),
    (0,0), "characters/sis/char_sis_sex_117.png",
    (157,238), "characters/sis/char_sis_sex_117x.png"
    )
image sissex 117bx = LiveComposite(
    (643,573),
    (0,0), "characters/sis/char_sis_sex_117b.png",
    (157,238), "characters/sis/char_sis_sex_117x.png"
    )
image sissex 118x = LiveComposite(
    (645,576),
    (0,0), "characters/sis/char_sis_sex_118.png",
    (157,244), "characters/sis/char_sis_sex_118x.png"
    )
image sissex 118bx = LiveComposite(
    (645,576),
    (0,0), "characters/sis/char_sis_sex_118b.png",
    (157,244), "characters/sis/char_sis_sex_118x.png"
    )
image sissex 119x = LiveComposite(
    (666,579),
    (0,0), "characters/sis/char_sis_sex_119.png",
    (218,233), "characters/sis/char_sis_sex_119x.png"
    )
image sissex 119bx = LiveComposite(
    (666,579),
    (0,0), "characters/sis/char_sis_sex_119b.png",
    (218,233), "characters/sis/char_sis_sex_119x.png"
    )
image sissex 120x = LiveComposite(
    (672,579),
    (0,0), "characters/sis/char_sis_sex_120.png",
    (226,216), "characters/sis/char_sis_sex_120x.png"
    )
image sissex 120bx = LiveComposite(
    (672,579),
    (0,0), "characters/sis/char_sis_sex_120b.png",
    (226,216), "characters/sis/char_sis_sex_120x.png"
    )
image sissex 121x = LiveComposite(
    (657,566),
    (0,0), "characters/sis/char_sis_sex_121.png",
    (181,214), "characters/sis/char_sis_sex_121x.png"
    )
image sissex 121bx = LiveComposite(
    (657,566),
    (0,0), "characters/sis/char_sis_sex_121b.png",
    (181,214), "characters/sis/char_sis_sex_121x.png"
    )
image sissex 122x = LiveComposite(
    (939,667),
    (0,0), "characters/sis/char_sis_sex_122.png",
    (341,238), "characters/sis/char_sis_sex_117x.png"
    )
image sissex 123x = LiveComposite(
    (913,740),
    (0,0), "characters/sis/char_sis_sex_123.png",
    (380,280), "characters/sis/char_sis_sex_123x.png"
    )
image sissex 124x = LiveComposite(
    (928,738),
    (0,0), "characters/sis/char_sis_sex_124.png",
    (395,274), "characters/sis/char_sis_sex_124x.png"
    )
image sissex 125x = LiveComposite(
    (906,740),
    (0,0), "characters/sis/char_sis_sex_125.png",
    (371,266), "characters/sis/char_sis_sex_125x.png"
    )
image sissex 126x = LiveComposite(
    (926,743),
    (0,0), "characters/sis/char_sis_sex_126.png",
    (391,269), "characters/sis/char_sis_sex_126x.png"
    )
image sissex 127x = LiveComposite(
    (915,741),
    (0,0), "characters/sis/char_sis_sex_127.png",
    (386,274), "characters/sis/char_sis_sex_127x.png"
    )
image sissex 128x = LiveComposite(
    (913,740),
    (0,0), "characters/sis/char_sis_sex_128.png",
    (384,276), "characters/sis/char_sis_sex_128x.png"
    )
image sissex 128bx = LiveComposite(
    (913,740),
    (0,0), "characters/sis/char_sis_sex_128.png",
    (379,282), "characters/sis/char_sis_sex_128x.png"
    )
image sissex 129x = LiveComposite(
    (913,740),
    (0,0), "characters/sis/char_sis_sex_129.png",
    (384,275), "characters/sis/char_sis_sex_129x1.png"
    )
image sissex 129bx = LiveComposite(
    (913,740),
    (0,0), "characters/sis/char_sis_sex_129b.png",
    (384,275), "characters/sis/char_sis_sex_129x3.png"
    )
image sissex 129cx = LiveComposite(
    (913,740),
    (0,0), "characters/sis/char_sis_sex_129c.png",
    (384,275), "characters/sis/char_sis_sex_129x2.png"
    )
image sissex 134 = LiveComposite(
    (887,653),
    (0,0), "characters/sis/char_sis_sex_134.png",
    (36,80), "characters/sis/char_sis_sex_136.png"
    )
image sissex 134b = LiveComposite(
    (887,653),
    (0,0), "characters/sis/char_sis_sex_134.png",
    (58,37), "characters/sis/char_sis_sex_134b.png",
    (36,80), "characters/sis/char_sis_sex_136.png"
    )
image sissex 134c = LiveComposite(
    (887,653),
    (0,0), "characters/sis/char_sis_sex_134.png",
    (58,37), "characters/sis/char_sis_sex_134b.png",
    (36,137), "characters/sis/char_sis_sex_136b.png"
    )
image sissex 135 = LiveComposite(
    (887,653),
    (0,0), "characters/sis/char_sis_sex_135.png",
    (36,80), "characters/sis/char_sis_sex_136.png"
    )
image sissex 135b = LiveComposite(
    (887,653),
    (0,0), "characters/sis/char_sis_sex_135.png",
    (58,37), "characters/sis/char_sis_sex_135b.png",
    (36,80), "characters/sis/char_sis_sex_136.png"
    )
image sissex 135c = LiveComposite(
    (887,653),
    (0,0), "characters/sis/char_sis_sex_135.png",
    (58,37), "characters/sis/char_sis_sex_135b.png",
    (36,137), "characters/sis/char_sis_sex_136b.png"
    )
image sissex 137b = LiveComposite(
    (1024,627),
    (0,0), "characters/sis/char_sis_sex_137.png",
    (79,280), "characters/sis/char_sis_sex_137b.png"
    )

image sissex 77 = ConditionSwitch(
    "xray == True", "sissex 77x",
    "xray == False", "characters/sis/char_sis_sex_77.png",
    "True",Null(),
    )
image sissex 78 = ConditionSwitch(
    "xray == True", "sissex 78x",
    "xray == False", "characters/sis/char_sis_sex_78.png",
    "True",Null(),
    )
image sissex 79 = ConditionSwitch(
    "xray == True", "sissex 79x",
    "xray == False", "characters/sis/char_sis_sex_79.png",
    "True",Null(),
    )
image sissex 79b = ConditionSwitch(
    "xray == True", "sissex 79bx",
    "xray == False", "characters/sis/char_sis_sex_79b.png",
    "True",Null(),
    )
image sissex 80a = ConditionSwitch(
    "xray == True", "sissex 80ac",
    "xray == False", "sissex 80",
    "True",Null(),
    )
image sissex 80b = ConditionSwitch(
    "xray == True", "sissex 80bc",
    "xray == False", "sissex 80",
    "True",Null(),
    )
image sissex 80c = ConditionSwitch(
    "xray == True", "sissex 80cc",
    "xray == False", "sissex 80",
    "True",Null(),
    )
image sissex 97 = ConditionSwitch(
    "xray == True", "sissex 97x",
    "xray == False", "characters/sis/char_sis_sex_97.png",
    "True",Null(),
    )
image sissex 98 = ConditionSwitch(
    "xray == True", "sissex 98x",
    "xray == False", "characters/sis/char_sis_sex_98.png",
    "True",Null(),
    )
image sissex 99 = ConditionSwitch(
    "xray == True", "sissex 99x",
    "xray == False", "characters/sis/char_sis_sex_99.png",
    "True",Null(),
    )
image sissex 100 = ConditionSwitch(
    "xray == True", "sissex 100x",
    "xray == False", "characters/sis/char_sis_sex_100.png",
    "True",Null(),
    )
image sissex 101 = ConditionSwitch(
    "xray == True", "sissex 101x",
    "xray == False", "characters/sis/char_sis_sex_101.png",
    "True",Null(),
    )
image sissex 102 = ConditionSwitch(
    "xray == True", "sissex 102x",
    "xray == False", "characters/sis/char_sis_sex_102.png",
    "True",Null(),
    )
image sissex 102b = ConditionSwitch(
    "xray == True", "sissex 102bx",
    "xray == False", "characters/sis/char_sis_sex_102.png",
    "True",Null(),
    )
image sissex 103 = ConditionSwitch(
    "xray == True", "sissex 103x",
    "xray == False", "characters/sis/char_sis_sex_103.png",
    "True",Null(),
    )
image sissex 117 = ConditionSwitch(
    "xray == True", "sissex 117x",
    "xray == False", "characters/sis/char_sis_sex_117.png",
    "True",Null(),
    )
image sissex 117b = ConditionSwitch(
    "xray == True", "sissex 117bx",
    "xray == False", "characters/sis/char_sis_sex_117b.png",
    "True",Null(),
    )
image sissex 118 = ConditionSwitch(
    "xray == True", "sissex 118x",
    "xray == False", "characters/sis/char_sis_sex_118.png",
    "True",Null(),
    )
image sissex 118b = ConditionSwitch(
    "xray == True", "sissex 118bx",
    "xray == False", "characters/sis/char_sis_sex_118b.png",
    "True",Null(),
    )
image sissex 119 = ConditionSwitch(
    "xray == True", "sissex 119x",
    "xray == False", "characters/sis/char_sis_sex_119.png",
    "True",Null(),
    )
image sissex 119b = ConditionSwitch(
    "xray == True", "sissex 119bx",
    "xray == False", "characters/sis/char_sis_sex_119b.png",
    "True",Null(),
    )
image sissex 120 = ConditionSwitch(
    "xray == True", "sissex 120x",
    "xray == False", "characters/sis/char_sis_sex_120.png",
    "True",Null(),
    )
image sissex 120b = ConditionSwitch(
    "xray == True", "sissex 120bx",
    "xray == False", "characters/sis/char_sis_sex_120b.png",
    "True",Null(),
    )
image sissex 121 = ConditionSwitch(
    "xray == True", "sissex 121x",
    "xray == False", "characters/sis/char_sis_sex_121.png",
    "True",Null(),
    )
image sissex 121b = ConditionSwitch(
    "xray == True", "sissex 121bx",
    "xray == False", "characters/sis/char_sis_sex_121b.png",
    "True",Null(),
    )
image sissex 122 = ConditionSwitch(
    "xray == True", "sissex 122x",
    "xray == False", "characters/sis/char_sis_sex_122.png",
    "True",Null(),
    )
image sissex 123 = ConditionSwitch(
    "xray == True", "sissex 123x",
    "xray == False", "characters/sis/char_sis_sex_123.png",
    "True",Null(),
    )
image sissex 124 = ConditionSwitch(
    "xray == True", "sissex 124x",
    "xray == False", "characters/sis/char_sis_sex_124.png",
    "True",Null(),
    )
image sissex 125 = ConditionSwitch(
    "xray == True", "sissex 125x",
    "xray == False", "characters/sis/char_sis_sex_125.png",
    "True",Null(),
    )
image sissex 126 = ConditionSwitch(
    "xray == True", "sissex 126x",
    "xray == False", "characters/sis/char_sis_sex_126.png",
    "True",Null(),
    )
image sissex 127 = ConditionSwitch(
    "xray == True", "sissex 127x",
    "xray == False", "characters/sis/char_sis_sex_127.png",
    "True",Null(),
    )
image sissex 128 = ConditionSwitch(
    "xray == True", "sissex 128x",
    "xray == False", "characters/sis/char_sis_sex_128.png",
    "True",Null(),
    )
image sissex 128b = ConditionSwitch(
    "xray == True", "sissex 128bx",
    "xray == False", "characters/sis/char_sis_sex_128.png",
    "True",Null(),
    )
image sissex 129 = ConditionSwitch(
    "xray == True", "sissex 129x",
    "xray == False", "characters/sis/char_sis_sex_129.png",
    "True",Null(),
    )
image sissex 129b = ConditionSwitch(
    "xray == True", "sissex 129bx",
    "xray == False", "characters/sis/char_sis_sex_129b.png",
    "True",Null(),
    )
image sissex 129c = ConditionSwitch(
    "xray == True", "sissex 129cx",
    "xray == False", "characters/sis/char_sis_sex_129c.png",
    "True",Null(),
    )