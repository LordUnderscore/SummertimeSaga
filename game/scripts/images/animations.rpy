
image cloud_animation:
    contains:
        xalign 0.0
        "backgrounds/menu_cloud_large.png"
        linear 90.0 xpos -1.0
        repeat
    contains:
        subpixel True
        xalign 0.0
        xoffset 125.0
        yoffset 110.0
        "backgrounds/menu_cloud_small.png"
        linear 175.0 xpos -1.0
        repeat


image webcam_loading_circle:
    "buttons/loading_circle.png"
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 1 rotate 360
    repeat


image player 155_156 = Animation("characters/player/char_player_155.png", .35, "characters/player/char_player_156.png", .35)
image location_mombed 2_3 = Animation("backgrounds/location_mombed02.jpg", .4, "backgrounds/location_mombed03.jpg", .4)
image playersex 86_85:
    Transform("playersex 86")
    pause .4
    Transform("playersex 85")
    pause .4
    repeat
image playersex 96_97:
    Transform("playersex 96")
    pause .4
    Transform("playersex 97")
    pause .4
    repeat
image playersex 134_135_136_137:
    Transform("playersex 134")
    pause M_sis.get('sex speed')
    Transform("playersex 135")
    pause M_sis.get('sex speed')
    Transform("playersex 136")
    pause M_sis.get('sex speed')
    Transform("playersex 137")
    pause M_sis.get('sex speed')
    repeat
image player 239_240:
    Transform("player 239")
    pause .4
    Transform("player 240")
    pause .4
    repeat
image player 239_240f:
    Transform("player 239f")
    pause .4
    Transform("player 240f")
    pause .4
    repeat


image mom_peek_sequence 2_3 = Animation("backgrounds/location_mompeak02.jpg", .4, "backgrounds/location_mompeak03.jpg", .4)
image dreammom 1_2 = Animation("backgrounds/dream_mom_01.jpg", .4, "backgrounds/dream_mom_02.jpg", .4)
image mom 80_79 = Animation("characters/mom/char_mom_80.png", .5, "characters/mom/char_mom_79.png", .5)
image moms 7_8 = Animation("characters/mom/char_mom_sex_07.png", .4, "characters/mom/char_mom_sex_08.png", .4)
image moms 13_14 = Animation("characters/mom/char_mom_sex_13.png", .4, "characters/mom/char_mom_sex_14.png", .4)
image moms 16_17 = Animation("characters/mom/char_mom_sex_16.png", .45, "characters/mom/char_mom_sex_17.png", .45)
image moms 37_36 = Animation("characters/mom/char_mom_sex_37.png", .45, "characters/mom/char_mom_sex_36.png", .45)
image moms 41_76 = Animation("characters/mom/char_mom_sex_41.png", .5, "characters/mom/char_mom_sex_76.png", .5)
image moms 49_50:
    Image("characters/mom/char_mom_49.png")
    pause .4
    Image("characters/mom/char_mom_50.png", xoffset = 5)
    pause .4
    repeat
image moms 52_53_52_51 = Animation("characters/mom/char_mom_sex_52.png", .4, "characters/mom/char_mom_sex_53.png", .4, "characters/mom/char_mom_sex_52.png", .4, "characters/mom/char_mom_sex_51.png", .4)
image moms 56_55 = Animation("characters/mom/char_mom_sex_56.png", .35, "characters/mom/char_mom_sex_55.png", .35)

image moms 59_60_61:
    Transform("moms 59")
    pause M_mom.get('sex speed')
    Transform("moms 60")
    pause M_mom.get('sex speed')
    Transform("moms 61")
    pause M_mom.get('sex speed')
    repeat

image moms 65_66_64:
    Transform("moms 65")
    pause M_mom.get('sex speed')*2/4
    Transform("moms 66")
    pause M_mom.get('sex speed')
    Transform("moms 64")
    pause M_mom.get('sex speed')
    repeat

image moms 68_67 = Animation("characters/mom/char_mom_sex_68.png", .4, "characters/mom/char_mom_sex_67.png", .4)
image moms 72_71 = Animation("characters/mom/char_mom_sex_72.png", .4, "characters/mom/char_mom_sex_71.png", .4)
image moms 73_74 = Animation("characters/mom/char_mom_sex_73.png", .4, "characters/mom/char_mom_sex_74.png", .4)
image moms 81_82 = Animation("characters/mom/char_mom_sex_81.png", .5, "characters/mom/char_mom_sex_82.png", .5)
image moms 85_86 = Animation("characters/mom/char_mom_sex_85.png", .5, "characters/mom/char_mom_sex_86.png", .5)
image moms 88_89:
    Image("characters/mom/char_mom_sex_88.png", xoffset = 0)
    pause .5
    Image("characters/mom/char_mom_sex_89.png", xoffset = -2)
    pause .5
    repeat
image moms 93_94:
    Image("characters/mom/char_mom_sex_93.png", xoffset = 0)
    pause .4
    Image("characters/mom/char_mom_sex_94.png", xoffset = -2)
    pause .4
    repeat
image moms 97_98:
    Transform("moms 97")
    pause .4
    Transform("moms 98", xoffset = -2)
    pause .4
    repeat

image moms 103_104_105_104:
    Transform("moms 103")
    pause M_mom.get('sex speed')*3/4
    Transform("moms 104")
    pause M_mom.get('sex speed')*1/4
    Transform("moms 105")
    pause M_mom.get('sex speed')*1/4
    Transform("moms 104")
    pause M_mom.get('sex speed')*2/4
    repeat

image moms 113_114:
    Image("characters/mom/char_mom_sex_113.png", xoffset = 0)
    pause .4
    Image("characters/mom/char_mom_sex_114.png", xoffset = 4)
    pause .4
    repeat

image moms 126_127_128:
    Transform("moms 126")
    pause M_mom.get('sex speed')
    Transform("moms 127")
    pause M_mom.get('sex speed')
    Transform("moms 128")
    pause M_mom.get('sex speed')
    repeat

image moms_xray 56_55_54:
    contains:
        subpixel True
        "characters/mom/char_mom_sex_61.png"
        pause M_mom.get('sex speed')
        "characters/mom/char_mom_sex_60.png"
        pause M_mom.get('sex speed')
        "characters/mom/char_mom_sex_59.png"
        pause M_mom.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_56.png", xoffset = 276, yoffset = 464)
        pause M_mom.get('sex speed')
        Image("characters/player/char_player_sex_55.png", xoffset = 262, yoffset = 475)
        pause M_mom.get('sex speed')
        Image("characters/player/char_player_sex_54.png", xoffset = 267, yoffset = 487)
        pause M_mom.get('sex speed')
        repeat

image moms_xray 58_59_57:
    contains:
        subpixel True
        "characters/mom/char_mom_sex_65.png"
        pause M_mom.get('sex speed')*2/4
        Image("characters/mom/char_mom_sex_66.png", yoffset = -11)
        pause M_mom.get('sex speed')
        Image("characters/mom/char_mom_sex_64.png", yoffset = 48)
        pause M_mom.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_58.png", xoffset = 347, yoffset = 255)
        pause M_mom.get('sex speed')*2/4
        Image("characters/player/char_player_sex_59.png", xoffset = 378, yoffset = 234)
        pause M_mom.get('sex speed')
        Image("characters/player/char_player_sex_57.png", xoffset = 263, yoffset = 278)
        pause M_mom.get('sex speed')
        repeat
image moms_xray 65_66_67_66:
    contains:
        subpixel True
        "characters/mom/char_mom_sex_103.png"
        pause M_mom.get('sex speed')*3/4
        Image("characters/mom/char_mom_sex_104.png", yoffset = -7)
        pause M_mom.get('sex speed')*1/4
        Image("characters/mom/char_mom_sex_105.png", yoffset = -7)
        pause M_mom.get('sex speed')*1/4
        Image("characters/mom/char_mom_sex_104.png", yoffset = -7)
        pause M_mom.get('sex speed')*2/4
        repeat
    contains:
        Image("characters/player/char_player_sex_65.png", xoffset = 367, yoffset = 240)
        pause M_mom.get('sex speed')*3/4
        Image("characters/player/char_player_sex_66.png", xoffset = 414, yoffset = 224)
        pause M_mom.get('sex speed')*1/4
        Image("characters/player/char_player_sex_67.png", xoffset = 434, yoffset = 230)
        pause M_mom.get('sex speed')*1/4
        Image("characters/player/char_player_sex_66.png", xoffset = 414, yoffset = 224)
        pause M_mom.get('sex speed')*2/4
        repeat


image shower 05d_05e = Animation("backgrounds/location_shower_05d.jpg", .3, "backgrounds/location_shower_05e.jpg", .3)
image sis 69_68:
    Transform("sis 69")
    pause .4
    Transform("sis 68")
    pause .4
    repeat
image sis 74_83:
    Transform("sis 74")
    pause sis_sybian_speed
    Transform("sis 83", xoffset = 2)
    pause sis_sybian_speed
    repeat
image sis 93_94:
    Transform("sis 93")
    pause .6
    Transform("sis 94")
    pause .6
    repeat
image sis 95_94:
    Transform("sis 95")
    pause .6
    Transform("sis 94")
    pause .6
    repeat
image sis 99_100_101:
    Transform("sis 99")
    pause .4
    Transform("sis 100")
    pause .4
    Transform("sis 101")
    pause .4
    repeat
image sis 117_118_119_116:
    Transform("sis 117")
    pause .4
    Transform("sis 118", xoffset = 6)
    pause .4
    Transform("sis 119", xoffset = 8)
    pause .4
    Transform("sis 116", xoffset = 4)
    pause .4
    repeat
image sis 124_125_126_123:
    Transform("sis 124")
    pause .4
    Transform("sis 125")
    pause .4
    Transform("sis 126")
    pause .4
    Transform("sis 123")
    pause .4
    repeat
image sis 145_146_147_148:
    Transform("sis 145")
    pause .4
    Transform("sis 146")
    pause .4
    Transform("sis 147")
    pause .4
    Transform("sis 148")
    pause .4
    repeat
image sissex 2_3_1_4:
    Transform("sissex 2")
    pause .4
    Transform("sissex 3")
    pause .4
    Transform("sissex 1")
    pause .4
    Transform("sissex 4")
    pause .4
    repeat
image sissex 23_24_25_22:
    Transform("sissex 23")
    pause .4
    Transform("sissex 24")
    pause .4
    Transform("sissex 25")
    pause .4
    Transform("sissex 22")
    pause .4
    repeat
image sissex 28_29_30_31:
    Transform("sissex 28")
    pause .4
    Transform("sissex 29")
    pause .4
    Transform("sissex 30")
    pause .4
    Transform("sissex 31")
    pause .4
    repeat
image sissex 36_37_38_35:
    Transform("sissex 36", xoffset = -8)
    pause .4
    Transform("sissex 37", xoffset = 45)
    pause .4
    Transform("sissex 38", xoffset = 51)
    pause .4
    Transform("sissex 35")
    pause .4
    repeat
image sissex 49_84:
    Transform("sissex 49")
    pause .4
    Transform("sissex 84")
    pause .4
    repeat
image sissex 54_55:
    Transform("sissex 54")
    pause .6
    Transform("sissex 55")
    pause .6
    repeat
image sissex 60_59:
    Transform("sissex 60")
    pause .6
    Transform("sissex 59")
    pause .6
    repeat
image sissex 62_64:
    Transform("sissex 62")
    pause .4
    Transform("sissex 63", xoffset = 2)
    pause .4
    repeat
image sissex 78_79:
    Transform("sissex 78")
    pause .4
    Transform("sissex 79", xoffset = 7)
    pause .4
    repeat
image sissex 79_78:
    Transform("sissex 79")
    pause .4
    Transform("sissex 78", xoffset = -7)
    pause .4
    repeat
image sissex 42_43_44_41:
    Transform("sissex 42", xoffset = 2)
    pause .4
    Transform("sissex 43", xoffset = 3)
    pause .4
    Transform("sissex 44", xoffset = 2)
    pause .4
    Transform("sissex 41")
    pause .4
    repeat
image sissex 92_93_94_95:
    Transform("sissex 92")
    pause .4
    Transform("sissex 93", xoffset = 23)
    pause .4
    Transform("sissex 94", xoffset = 2)
    pause .4
    Transform("sissex 95")
    pause .4
    repeat

image sissex 98_99_100_101:
    Transform("sissex 98")
    pause M_sis.get('sex speed')
    Transform("sissex 99", xoffset = 7)
    pause M_sis.get('sex speed')
    Transform("sissex 100", xoffset = -14)
    pause M_sis.get('sex speed')
    Transform("sissex 101", xoffset = -35)
    pause M_sis.get('sex speed')
    repeat

image sissex 102_103:
    Transform("white")
    pause .1
    Transform("sissex 102")
    pause .6
    Transform("sissex 103", xoffset = -5)
    pause .4
    repeat
image sissex 114b_115b:
    Transform("sissex 114b")
    pause .6
    Transform("sissex 115b")
    pause .6
    repeat

image sissex 117_118_119_120_121:
    Transform("sissex 117")
    pause M_sis.get('sex speed')
    Transform("sissex 118", xoffset = 2)
    pause M_sis.get('sex speed')
    Transform("sissex 119", xoffset = 23)
    pause M_sis.get('sex speed')
    Transform("sissex 120", xoffset = 29)
    pause M_sis.get('sex speed')
    Transform("sissex 121", xoffset = 14)
    pause M_sis.get('sex speed')
    repeat

image sissex 123_124_125_126_127:
    Transform("sissex 123")
    pause M_sis.get('sex speed')
    Transform("sissex 124")
    pause M_sis.get('sex speed')
    Transform("sissex 125")
    pause M_sis.get('sex speed')
    Transform("sissex 126")
    pause M_sis.get('sex speed')
    Transform("sissex 127")
    pause M_sis.get('sex speed')
    repeat

image sissex 129b_128:
    Transform("sissex 129b")
    pause .6
    Transform("white")
    pause .1
    Transform("sissex 128")
    pause .4
    repeat
image sissex 139_140_141_142 = Animation("characters/sis/char_sis_sex_139.png", .4, "characters/sis/char_sis_sex_140.png", .4, "characters/sis/char_sis_sex_141.png", .3, "characters/sis/char_sis_sex_142.png", .2)
image sissex 139b_140b_141b_142b = Animation("characters/sis/char_sis_sex_139b.png", .4, "characters/sis/char_sis_sex_140b.png", .4, "characters/sis/char_sis_sex_141b.png", .3, "characters/sis/char_sis_sex_142b.png", .2)


image auntsex 30_6 = im.Composite((835, 768), (0, 0), "characters/aunt/char_aunt_sex_30.png", (43, 349), "characters/player/char_player_sex_06.png")
image auntsex 31_9 = im.Composite((835, 768), (44, 0), "characters/aunt/char_aunt_sex_31.png", (200, 400), "characters/player/char_player_sex_09.png")


image aunt_masturbate 1_2 = Animation("backgrounds/location_diane_kitchen_vegies01.jpg", .4, "backgrounds/location_diane_kitchen_vegies01b.jpg", .4)
image aunt 77_78_76 = Animation("characters/aunt/char_aunt_77.png", .35, "characters/aunt/char_aunt_78.png", .35, "characters/aunt/char_aunt_76.png", .35)
image aunt 83_82 = Animation("characters/aunt/char_aunt_83.png", .3, "characters/aunt/char_aunt_82.png", .3)
image auntsex 11_12 = Animation("characters/aunt/char_aunt_sex_11.png", .4, "characters/aunt/char_aunt_sex_12.png", .4)
image auntsex 19_20 = Animation("characters/aunt/char_aunt_sex_19.png", .4, "characters/aunt/char_aunt_sex_20.png", .4)
image auntsex 26_27:
    Image("characters/aunt/char_aunt_sex_26.png", xoffset = 0)
    pause M_aunt.get('sex speed')
    Image("characters/aunt/char_aunt_sex_27.png", xoffset = 16)
    pause M_aunt.get('sex speed')
    repeat
image auntsex 30_31:
    Image("characters/aunt/char_aunt_sex_30.png", xoffset = 0)
    pause M_aunt.get('sex speed')
    Image("characters/aunt/char_aunt_sex_31.png", xoffset = 16)
    pause M_aunt.get('sex speed')
    repeat
image auntsex 32_33 = Animation("characters/aunt/char_aunt_sex_32.png", .4, "characters/aunt/char_aunt_sex_33.png", .4)
image auntsex 38_40:
    "characters/aunt/char_aunt_sex_38.png"
    pause M_aunt.get('sex speed')
    Image("characters/aunt/char_aunt_sex_40.png", xoffset = 3)
    pause M_aunt.get('sex speed')
    repeat
image auntsex 50_52:
    "characters/aunt/char_aunt_sex_50.png"
    pause M_aunt.get('sex speed')
    Image("characters/aunt/char_aunt_sex_52.png", xoffset = 5)
    pause M_aunt.get('sex speed')
    repeat
image auntsex 54_55:
    "characters/aunt/char_aunt_sex_54.png"
    pause M_aunt.get('sex speed')*5/4
    "characters/aunt/char_aunt_sex_55.png"
    pause M_aunt.get('sex speed')*5/4
    repeat
image auntsex 58_59_58_57:
    Transform("aunts 58", xoffset = -2)
    pause M_aunt.get('sex speed')*3/4
    Transform("aunts 59", xoffset = 1)
    pause M_aunt.get('sex speed')*2.5/4
    Transform("aunts 58", xoffset = -2)
    pause M_aunt.get('sex speed')*3.5/4
    Transform("aunts 57")
    pause M_aunt.get('sex speed')
    repeat
image auntsex 61_60:
    Image("characters/aunt/char_aunt_sex_61.png", xoffset = -45)
    pause M_aunt.get('sex speed')*5/4
    Image("characters/aunt/char_aunt_sex_60.png", xoffset = -45)
    pause M_aunt.get('sex speed')*5/4
    repeat
image auntsex_xray 6_9:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_30.png")
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_31.png", xoffset = 43)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_06.png", xoffset = 376, yoffset = 417)
        pause M_aunt.get('sex speed')
        Image("characters/player/char_player_sex_09.png", xoffset = 392, yoffset = 400)
        pause M_aunt.get('sex speed')
        repeat
image auntsex_xray 6_7:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_26.png")
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_27.png", xoffset = 43)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_06.png", xoffset = 376, yoffset = 417)
        pause M_aunt.get('sex speed')
        Image("characters/player/char_player_sex_07.png", xoffset = 392, yoffset = 400)
        pause M_aunt.get('sex speed')
        repeat
image auntsex_cowoutfit 39_41:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_38.png", xoffset = 86, yoffset = 40)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_40.png", xoffset = 92, yoffset = 40)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/aunt/char_aunt_sex_39.png", xoffset = 267, yoffset = 145)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_41.png", xoffset = 268, yoffset = 144)
        pause M_aunt.get('sex speed')
        repeat
image auntsex_cowoutfit 51_53:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_50.png", xoffset = 77)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_52.png", xoffset = 89)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/aunt/char_aunt_sex_51.png", xoffset = 115)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_53.png", xoffset = 133)
        pause M_aunt.get('sex speed')
        repeat
image auntsex_xray 42_43:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_38.png", xoffset = 86, yoffset = 40)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_40.png", xoffset = 92, yoffset = 40)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_42.png", xoffset = 498, yoffset = 359)
        pause M_aunt.get('sex speed')
        Image("characters/player/char_player_sex_43.png", xoffset = 486, yoffset = 334)
        pause M_aunt.get('sex speed')
        repeat
image auntsex_xray 46_47:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_50.png", xoffset = 77)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_52.png", xoffset = 89)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_46.png", xoffset = 272, yoffset = 270)
        pause M_aunt.get('sex speed')
        Image("characters/player/char_player_sex_47.png", xoffset = 302, yoffset = 290)
        pause M_aunt.get('sex speed')
        repeat
image auntsex_cowoutfit_xray 39_41_42_43:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_38.png", xoffset = 86, yoffset = 40)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_40.png", xoffset = 92, yoffset = 40)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/aunt/char_aunt_sex_39.png", xoffset = 267, yoffset = 145)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_41.png", xoffset = 268, yoffset = 144)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_42.png", xoffset = 498, yoffset = 359)
        pause M_aunt.get('sex speed')
        Image("characters/player/char_player_sex_43.png", xoffset = 486, yoffset = 334)
        pause M_aunt.get('sex speed')
        repeat
image auntsex_cowoutfit_xray 51_53_46_47:
    contains:
        subpixel True
        Image("characters/aunt/char_aunt_sex_50.png", xoffset = 77)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_52.png", xoffset = 89)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/aunt/char_aunt_sex_51.png", xoffset = 115)
        pause M_aunt.get('sex speed')
        Image("characters/aunt/char_aunt_sex_53.png", xoffset = 133)
        pause M_aunt.get('sex speed')
        repeat
    contains:
        Image("characters/player/char_player_sex_46.png", xoffset = 272, yoffset = 270)
        pause M_aunt.get('sex speed')
        Image("characters/player/char_player_sex_47.png", xoffset = 302, yoffset = 290)
        pause M_aunt.get('sex speed')
        repeat


image ivysex 4_3:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_19.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_19.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_04.png", xoffset = 242, yoffset = 169)
        pause ivy_sex_speed
        Image("characters/ivy/char_ivy_sex_03.png", xoffset = 242, yoffset = 169)
        pause ivy_sex_speed
        repeat
image ivysex 6_5:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_19.png", xoffset = -2, yoffset = 439)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_19.png", xoffset = -2, yoffset = 439)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_06.png", xoffset = 249, yoffset = 85)
        pause ivy_sex_speed
        Image("characters/ivy/char_ivy_sex_05.png", xoffset = 249, yoffset = 63)
        pause ivy_sex_speed
        repeat
image ivysex 10_11:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_20.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_21.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_10.png", xoffset = 148, yoffset = 61)
        pause ivy_sex_speed
        Image("characters/ivy/char_ivy_sex_11.png", xoffset = 148, yoffset = 92)
        pause ivy_sex_speed
        repeat
image ivysex 18_19:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_18.png", xoffset = 246, yoffset = 104)
        pause ivy_sex_speed
        Image("characters/ivy/char_ivy_sex_19.png", xoffset = 244, yoffset = 78)
        pause ivy_sex_speed
        repeat
image ivysex_xray 36_37:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_20.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_21.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_10.png", xoffset = 148, yoffset = 61)
        pause ivy_sex_speed
        Image("characters/ivy/char_ivy_sex_11.png", xoffset = 148, yoffset = 92)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/player/char_player_sex_36.png", xoffset = 428, yoffset = 331)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_37.png", xoffset = 422, yoffset = 370)
        pause ivy_sex_speed
        repeat
image ivysex_xray 39_40:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause ivy_sex_speed
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_18.png", xoffset = 246, yoffset = 104)
        pause ivy_sex_speed
        Image("characters/ivy/char_ivy_sex_19.png", xoffset = 244, yoffset = 78)
        pause ivy_sex_speed
        repeat
    contains:
        Image("characters/player/char_player_sex_39.png", xoffset = 410, yoffset = 329)
        pause ivy_sex_speed
        Image("characters/player/char_player_sex_40.png", xoffset = 419, yoffset = 393)
        pause ivy_sex_speed
        repeat


image cassie 26_27:
    "characters/cassie/char_cassie_26.png"
    pause .4
    Image("characters/cassie/char_cassie_27.png", xoffset = 7)
    pause .4
    repeat

image cassie 26_28:
    "characters/cassie/char_cassie_26.png"
    pause .4
    Image("characters/cassie/char_cassie_28.png", xoffset = 12)
    pause .4
    repeat


image judith 25_23 = Animation("characters/judith/char_judith_25.png", .4, "characters/judith/char_judith_23.png", .4)
image judith 31_32 = Animation("characters/judith/char_judith_31.png", .4, "characters/judith/char_judith_32.png", .4)
image judith 36_37_38 = Animation("characters/judith/char_judith_36.png", .4, "characters/judith/char_judith_37.png", .4, "characters/judith/char_judith_38.png", .4)


image windowmianight03a_b = Animation("backgrounds/window_mia_night03a.jpg", .4, "backgrounds/window_mia_night03b.jpg", .4)
image windowerikday04a_b = Animation("backgrounds/window_erik_day04a.jpg", .4, "backgrounds/window_erik_day04b.jpg", .4)
image windowerikday05a_b = Animation("backgrounds/window_erik_day05a.jpg", .4, "backgrounds/window_erik_day05b.jpg", .4)


image library 1_2 = Animation("characters/library/char_library_01.png", .4, "characters/library/char_library_02.png", .4)


image anna 19_20 = Animation("characters/anna/char_anna_19.png", .8, "characters/anna/char_anna_20.png", 1.6)
image anna_slow 31_32 = Animation("characters/anna/char_anna_31.png", .8, "characters/anna/char_anna_32.png", .8)
image anna_fast 31_32 = Animation("characters/anna/char_anna_31.png", .4, "characters/anna/char_anna_32.png", .4)


image erik_house_cs01_01b = Animation("backgrounds/location_erik_house_cutscene01.jpg", .4, "backgrounds/location_erik_house_cutscene01b.jpg", .6)


image erikmomsex 8_9:
    "characters/erikmom/char_erikmom_sex_08.png"
    pause 0.6
    "characters/erikmom/char_erikmom_sex_09.png"
    pause 0.4
    repeat
image erikmomsex 12_13_14_13:
    "characters/erikmom/char_erikmom_sex_12.png"
    pause 0.6
    "characters/erikmom/char_erikmom_sex_13.png"
    pause 0.4
    "characters/erikmom/char_erikmom_sex_14.png"
    pause 0.5
    "characters/erikmom/char_erikmom_sex_13.png"
    pause 0.4
    repeat
image erikmomsex 13_14_13_12:
    "characters/erikmom/char_erikmom_sex_13.png"
    pause 0.4
    "characters/erikmom/char_erikmom_sex_14.png"
    pause 0.5
    "characters/erikmom/char_erikmom_sex_13.png"
    pause 0.4
    "characters/erikmom/char_erikmom_sex_12.png"
    pause 0.6
    repeat
image erikmomsex 12b_13b_14b:
    "characters/erikmom/char_erikmom_sex_12b.png"
    pause 0.6
    "characters/erikmom/char_erikmom_sex_13b.png"
    pause 0.4
    "characters/erikmom/char_erikmom_sex_14b.png"
    pause 0.5
    "characters/erikmom/char_erikmom_sex_13b.png"
    pause 0.4
    repeat
image erikmomsex 15_16_17:
    "characters/erikmom/char_erikmom_sex_15.png"
    pause 0.6
    "characters/erikmom/char_erikmom_sex_16.png"
    pause 0.4
    "characters/erikmom/char_erikmom_sex_17.png"
    pause 0.5
    repeat
image erikmomsex 21_22_23_24_25:
    "characters/erikmom/char_erikmom_sex_21.png"
    pause M_erimom.get('sex speed')*2/3
    "characters/erikmom/char_erikmom_sex_22.png"
    pause M_erimom.get('sex speed')
    "characters/erikmom/char_erikmom_sex_23.png"
    pause M_erimom.get('sex speed')
    "characters/erikmom/char_erikmom_sex_24.png"
    pause M_erimom.get('sex speed')*2.5/3
    "characters/erikmom/char_erikmom_sex_25.png"
    pause M_erimom.get('sex speed')*2/3
    repeat
image erikmomsex 28_29_30:
    Transform("characters/erikmom/char_erikmom_sex_28.png", yoffset=42)
    pause M_erimom.get('sex speed')*2/3
    Transform("characters/erikmom/char_erikmom_sex_29.png", yoffset=36)
    pause M_erimom.get('sex speed')
    Transform("characters/erikmom/char_erikmom_sex_30.png", xoffset=-4, yoffset=41)
    pause M_erimom.get('sex speed')
    repeat
image erikmomsex 36_37:
    Transform("characters/erikmom/char_erikmom_sex_36.png", yoffset=70)
    pause M_erimom.get('sex speed')
    Transform("characters/erikmom/char_erikmom_sex_37.png", yoffset=60)
    pause M_erimom.get('sex speed')
    repeat
image erikmomsex 42_43_44_45_46:
    Transform("characters/erikmom/char_erikmom_sex_42.png", xoffset=-14)
    pause M_erimom.get('sex speed')
    Transform("characters/erikmom/char_erikmom_sex_43.png", xoffset=-20)
    pause M_erimom.get('sex speed')*2/3
    Transform("characters/erikmom/char_erikmom_sex_44.png", xoffset=-30)
    pause M_erimom.get('sex speed')*2.5/3
    Transform("characters/erikmom/char_erikmom_sex_45.png", xoffset=-23)
    pause M_erimom.get('sex speed')*2/3
    Transform("characters/erikmom/char_erikmom_sex_46.png", xoffset=-19)
    pause M_erimom.get('sex speed')*2/3
    repeat


image junesex 4b_5b_6b_7b_8b:
    "characters/june/char_june_sex_04b.png"
    pause M_june.get('sex speed')*2/3
    "characters/june/char_june_sex_05b.png"
    pause M_june.get('sex speed')*2.5/3
    "characters/june/char_june_sex_06b.png"
    pause M_june.get('sex speed')*2.5/3
    "characters/june/char_june_sex_07b.png"
    pause M_june.get('sex speed')*2/3
    "characters/june/char_june_sex_08b.png"
    pause M_june.get('sex speed')
    repeat
image junesex 4_5_6_7_8:
    "characters/june/char_june_sex_04.png"
    pause M_june.get('sex speed')*2/3
    "characters/june/char_june_sex_05.png"
    pause M_june.get('sex speed')*2.5/3
    "characters/june/char_june_sex_06.png"
    pause M_june.get('sex speed')*2.5/3
    "characters/june/char_june_sex_07.png"
    pause M_june.get('sex speed')*2/3
    "characters/june/char_june_sex_08.png"
    pause M_june.get('sex speed')
    repeat


image mias 7_8:
    Transform("mias 7")
    pause M_mia.get('sex speed')
    Transform("mias 8")
    pause M_mia.get('sex speed')
    repeat

image mias 7_8_9_10_11:
    Transform("mias 7")
    pause M_mia.get('sex speed')
    Transform("mias 8")
    pause M_mia.get('sex speed')
    Transform("mias 9")
    pause M_mia.get('sex speed')
    Transform("mias 10")
    pause M_mia.get('sex speed')
    Transform("mias 11")
    pause M_mia.get('sex speed')
    repeat

image mias 7b_8b_9b_10b_11b:
    Transform("mias 7b")
    pause M_mia.get('sex speed')
    Transform("mias 8b")
    pause M_mia.get('sex speed')
    Transform("mias 9b")
    pause M_mia.get('sex speed')
    Transform("mias 10b")
    pause M_mia.get('sex speed')
    Transform("mias 11b")
    pause M_mia.get('sex speed')
    repeat

image mias 12_13:
    Transform("mias 12")
    pause .4
    Transform("mias 13")
    pause .2
    repeat

image mias 12b_13b:
    Transform("mias 12b")
    pause .4
    Transform("mias 13b")
    pause .2
    repeat


image helens 1_2 = Animation("characters/helen/char_helen_sex_02.png", .25, "characters/helen/char_helen_sex_01.png", .2)
image helens 4_4b = Animation("characters/helen/char_helen_sex_04.png", .4, "characters/helen/char_helen_sex_04b.png", .2)
image helens 6_7_8_9_10:
    Transform("characters/helen/char_helen_sex_06.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_07.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_08.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_09.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_10.png")
    pause M_helen.get('sex speed')
    repeat
image helens 11_11b = Animation("characters/helen/char_helen_sex_11.png", .2, "characters/helen/char_helen_sex_11b.png", 1)
image helens 15_16_17_18_19:
    Transform("characters/helen/char_helen_sex_15.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_16.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_17.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_18.png")
    pause M_helen.get('sex speed')
    Transform("characters/helen/char_helen_sex_19.png")
    pause M_helen.get('sex speed')
    repeat
image helens 23_24_25_26_27:
    Transform("helens 23")
    pause M_helen.get('sex speed')
    Transform("helens 24")
    pause M_helen.get('sex speed')
    Transform("helens 25")
    pause M_helen.get('sex speed')
    Transform("helens 26")
    pause M_helen.get('sex speed')
    Transform("helens 27")
    pause M_helen.get('sex speed')
    repeat
image h_corset 23_24_25_26_27:
    Transform("h_corset 23b")
    pause M_helen.get('sex speed')
    Transform("h_corset 24b")
    pause M_helen.get('sex speed')
    Transform("h_corset 25b")
    pause M_helen.get('sex speed')
    Transform("h_corset 26b")
    pause M_helen.get('sex speed')
    Transform("h_corset 27b")
    pause M_helen.get('sex speed')
    repeat


image rozs 1_2_3_4_5_6_7:
    Transform("characters/roz/char_roz_sex_01.png")
    pause M_roz.get('sex speed')
    Transform("characters/roz/char_roz_sex_02.png")
    pause M_roz.get('sex speed')
    Transform("characters/roz/char_roz_sex_03.png")
    pause M_roz.get('sex speed')
    Transform("characters/roz/char_roz_sex_04.png")
    pause M_roz.get('sex speed')
    Transform("characters/roz/char_roz_sex_05.png")
    pause M_roz.get('sex speed')
    Transform("characters/roz/char_roz_sex_06.png")
    pause M_roz.get('sex speed')
    Transform("characters/roz/char_roz_sex_07.png")
    pause M_roz.get('sex speed')
    repeat

image rozs 8_9 = Animation("characters/roz/char_roz_sex_08.png", .2, "characters/roz/char_roz_sex_09.png", 1)


image aquas 3_4_5_6_7:
    Transform("characters/aqua/char_aqua_sex_03.png")
    pause M_aqua.get('sex speed')
    Transform("characters/aqua/char_aqua_sex_04.png")
    pause M_aqua.get('sex speed')
    Transform("characters/aqua/char_aqua_sex_05.png")
    pause M_aqua.get('sex speed')
    Transform("characters/aqua/char_aqua_sex_06.png")
    pause M_aqua.get('sex speed')
    Transform("characters/aqua/char_aqua_sex_07.png")
    pause M_aqua.get('sex speed')
    repeat


image ang 22_23_24f = Animation(im.Flip("characters/angelica/char_angelica_22.png", horizontal=True), .3, im.Flip("characters/angelica/char_angelica_23.png", horizontal=True), .3, im.Flip("characters/angelica/char_angelica_24.png", horizontal=True), .3)


image rump_n_cunt 01_02_03_04:
    "characters/mayor/char_mayor_sex_01.png"
    pause 0.2
    "characters/mayor/char_mayor_sex_02.png"
    pause 0.25
    "characters/mayor/char_mayor_sex_03.png"
    pause 0.25
    "characters/mayor/char_mayor_sex_04.png"
    pause 0.2
    repeat
init python:
    class PulseImage(renpy.Displayable):
        def __init__(self,img1,img2,delay=0.1,**kwargs):
            super(PulseImage,self).__init__(**kwargs)
            self._image1 = renpy.displayable(img1)
            self._image2 = renpy.displayable(img2)
            self._toggle = True
            self._delay = delay
        def render(self,width,height,st,at):
            if self._toggle:
                self._toggle = False
                r = renpy.render(self._image1,width,height,st,at)
            else:
                self._toggle = True
                r = renpy.render(self._image2,width,height,st,at)
            renpy.redraw(self,self._delay)
            return r