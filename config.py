ESC_KEY = '\x1b'

SAMPLE_VID_BUNNY_LONG = r"samples\videos\SampleVideo_1280x720_30mb.mp4"
SAMPLE_VID_BUNNY_SHORT = r"samples\videos\SampleVideo_1280x720_1mb.mp4"
SAMPLE_VID_EARTH = r"samples\videos\earth_1280_10MG.mp4"
SAMPLE_VID_SURFER = r"samples\videos\Surfer.mp4"

MAIN_SCREEN_MO_BIRTH = r"media\main_screen_mouse_overs\Birth_MO.mp4"
MAIN_SCREEN_MO_CARE = r"media\main_screen_mouse_overs\Care_MO.mp4"
MAIN_SCREEN_MO_INDEPENDENT = r"media\main_screen_mouse_overs\Independent_MO.mp4"
MAIN_SCREEN_MO_PREG = r"media\main_screen_mouse_overs\Preg_MO.mp4"
MAIN_SCREEN_MO_SEP = r"media\main_screen_mouse_overs\Sep_MO.mp4"
MAIN_SCREEN_MO_SONG = r"media\main_screen_mouse_overs\Song_MO.mp4"

MAIN_SCREEN_TRANS_BIRTH = r"media\main_screen_transitions\Main_to_Birth.mp4"
MAIN_SCREEN_TRANS_CARE = r"media\main_screen_transitions\Main_to_Care.mp4"
MAIN_SCREEN_TRANS_INDEPENDENT = r"media\main_screen_transitions\Main_to_Independent.mp4"
MAIN_SCREEN_TRANS_PREG = r"media\main_screen_transitions\Main_to_Preg.mp4"
MAIN_SCREEN_TRANS_SEP = r"media\main_screen_transitions\Main_to_Sep.mp4"
MAIN_SCREEN_TRANS_SONG = r"media\main_screen_transitions\Song_MO.mp4"

BIRTH_TRANS_MAIN_SCREEN = r"media\main_screen_transitions\Birth_to_Main.mp4"
CARE_TRANS_MAIN_SCREEN = r"media\main_screen_transitions\Care_to_Main.mp4"
INDEPENDENT_TRANS_MAIN_SCREEN = r"media\main_screen_transitions\Independent_to_Main.mp4"
PREG_TRANS_MAIN_SCREEN = r"media\main_screen_transitions\Preg_to_Main.mp4"
SEP_TRANS_MAIN_SCREEN = r"media\main_screen_transitions\Sep_to_Main.mp4"
# SONG_TRANS_MAIN_SCREEN = r"media\main_screen_transitions\Song_MO.mp4"

MAIN_SCREEN_STATIC = r"media\static_screens\Main_Screen.tif"
INNER_SCREEN_STATIC_BIRTH = r"media\static_screens\Birth.mp4"
INNER_SCREEN_STATIC_CARE = r"media\static_screens\Care.mp4"
INNER_SCREEN_STATIC_INDEPENDENT = r"media\static_screens\Independent.mp4"
INNER_SCREEN_STATIC_PREG = r"media\static_screens\Preg.mp4"
INNER_SCREEN_STATIC_SEP = r"media\static_screens\Sep.mp4"
#INNER_SCREEN_SONG = r"media\static_screens\Song.tif"

ALL_VIDEOS = {
    'surfer': SAMPLE_VID_SURFER,
    'earth': SAMPLE_VID_EARTH,
    'bunny': SAMPLE_VID_BUNNY_SHORT,

    'main_MO_birth': MAIN_SCREEN_MO_BIRTH,
    'main_MO_care': MAIN_SCREEN_MO_CARE,
    'main_MO_independent': MAIN_SCREEN_MO_INDEPENDENT,
    'main_MO_preg': MAIN_SCREEN_MO_PREG,
    'main_MO_sep': MAIN_SCREEN_MO_SEP,
    'main_MO_song': MAIN_SCREEN_MO_SONG,

    'main_trans_birth': MAIN_SCREEN_TRANS_BIRTH,
    'main_trans_care': MAIN_SCREEN_TRANS_CARE,
    'main_trans_independent': MAIN_SCREEN_TRANS_INDEPENDENT,
    'main_trans_preg': MAIN_SCREEN_TRANS_PREG,
    'main_trans_sep': MAIN_SCREEN_TRANS_SEP,
    'main_trans_song': MAIN_SCREEN_TRANS_SONG,

    'birth_trans_main': BIRTH_TRANS_MAIN_SCREEN,
    'care_trans_main': CARE_TRANS_MAIN_SCREEN,
    'independent_trans_main': INDEPENDENT_TRANS_MAIN_SCREEN,
    'preg_trans_main': PREG_TRANS_MAIN_SCREEN,
    'sep_trans_main': SEP_TRANS_MAIN_SCREEN,
    # 'song_trans_main': SONG_TRANS_MAIN_SCREEN,

    'static_main': MAIN_SCREEN_STATIC,
    'inner_static_birth': INNER_SCREEN_STATIC_BIRTH,
    'inner_static_care': INNER_SCREEN_STATIC_CARE,
    'inner_static_independent': INNER_SCREEN_STATIC_INDEPENDENT,
    'inner_static_preg': INNER_SCREEN_STATIC_PREG,
    'inner_static_sep': INNER_SCREEN_STATIC_SEP
    # 'inner_static_song': INNER_SCREEN_STATIC_SONG,

}

# keys: names
# values: left-top (x,y), right-bottom (x,y)
CLICK_LOCATIONS = {
    'main': {
        'main_trans_birth': [(1053, 410), (1567, 1080)],
        'main_trans_care': [(215, 115), (605, 714)],
        'main_trans_independent': [(3186, 1786), (3599, 2057)],
        'main_trans_preg': [(1967, 117), (2838, 729)],
        'main_trans_sep': [(242, 1708), (1296, 2047)],
        'main_trans_song': [(973, 1090), (1384, 1395)]
    },
    'care': { # TODO: should replace all below to care_trans_main
        'care_trans_main': [(1816, 977), (1886, 1039)]
    },
    'birth': {
        'birth_trans_main': [(1816, 977), (1886, 1039)]
    },
    'independent': {
        'independent_trans_main': [(1816, 977), (1886, 1039)]
    },
    'preg': {
        'preg_trans_main': [(1816, 977), (1886, 1039)]
    },
    'sep': {
        'sep_trans_main': [(1816, 977), (1886, 1039)]
    },
    'song': {
        'song_trans_main': [(1816, 977), (1886, 1039)]
    }
}

MOUSE_OVER_LOCATIONS = {
    'main': {
        'main_MO_birth': [(1053, 410), (1567, 1080)],
        'main_MO_care': [(215, 115), (605, 714)],
        'main_MO_independent': [(3186, 1786), (3599, 2057)],
        'main_MO_preg': [(1967, 117), (2838, 729)],
        'main_MO_sep': [(242, 1708), (1296, 2047)],
        'main_MO_song': [(973, 1090), (1384, 1395)]
    },

    'care': {},
    'birth': {},
    'independent': {},
    'preg': {},
    'sep': {},
    'song': {}

}

VIDEO_TO_STATIC_IMAGE = {
    'main_trans_birth': 'inner_static_birth',
    'main_trans_care': 'inner_static_care',
    'main_trans_independent': 'inner_static_independent',
    'main_trans_preg': 'inner_static_preg',
    'main_trans_sep': 'inner_static_sep',
    'main_trans_song': 'inner_static_song',

    'birth_trans_main': 'static_main',
    'care_trans_main': 'static_main',
    'independent_trans_main': 'static_main',
    'preg_trans_main': 'static_main',
    'sep_trans_main': 'static_main',
    'song_trans_main': 'static_main'
}

current_video_file = 'static_main'
next_video_file = 'static_main'
current_screen = 'main'
after_click = False
