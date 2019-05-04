
ESC_KEY = '\x1b'

SAMPLE_VID_BUNNY_LONG = r"samples\videos\SampleVideo_1280x720_30mb.mp4"
SAMPLE_VID_BUNNY_SHORT = r"samples\videos\SampleVideo_1280x720_1mb.mp4"
SAMPLE_VID_EARTH = r"samples/videos/earth_1280_10MG.mp4"
SAMPLE_VID_SURFER = r"samples/videos/Surfer.mp4"


ALL_VIDEOS = {
    'surfer': SAMPLE_VID_SURFER,
    'earth': SAMPLE_VID_EARTH,
    'bunny': SAMPLE_VID_BUNNY_SHORT
}


# keys: names
# values: left-top (x,y), right-bottom (x,y)
CLICK_LOCATIONS = {
    'bunny': [(0, 0), (1280, 720)]
}

HOVER_LOCATIONS = {
    'surfer': [(0, 0), (100, 100)],
    'bunny': [(1000, 600), (1280, 720)]
}

current_video_file = 'surfer'
next_video_file = 'surfer'
after_click = False

