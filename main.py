import time
import cv2  # dependency

from config import ESC_KEY, ALL_VIDEOS, VIDEO_TO_STATIC_IMAGE, \
    CLICK_LOCATIONS, MOUSE_OVER_LOCATIONS, \
    current_video_file, next_video_file, after_click, current_screen


def check_bounds(x, y, locations, frame_width, frame_height):
    # check if valid
    if (not (0 < x < frame_width)) or (not (0 < y < frame_height)):
        return None

    for name, values in locations.items():
        # left-top x,y
        x1, y1 = values[0]
        # right-bottom x,y
        x2, y2 = values[1]
        # print("location: {}, {}\ntop-left: {}, {}\nright-bottom: {}, {}".format(x, y, x1, y1, x2, y2))
        if (x1 < x < x2) and (y1 < y < y2):
            return name

    return None


# mouse callback function

def mouse_callback(event, x, y, flags, param):
    global next_video_file, after_click
    frame_width = param[0]
    frame_height = param[1]
    print("Mouse locations: {}, {}".format(x, y))

    if event == cv2.EVENT_LBUTTONDOWN:
        result = check_bounds(x, y, CLICK_LOCATIONS[current_screen], frame_width, frame_height)
        if result:
            print("Mouse locations: {}, {}".format(x, y))
            print("Result: {}".format(result))
            next_video_file = result
            after_click = True

    if event == cv2.EVENT_MOUSEMOVE:
        result = check_bounds(x, y, MOUSE_OVER_LOCATIONS[current_screen], frame_width, frame_height)
        if result and not after_click:
            print("Mouse locations: {}, {}".format(x, y))
            print("Result: {}".format(result))
            next_video_file = result


def play_video(video_files: dict, frames_per_second=25, quit_key=ESC_KEY, fullscreen=True):
    """main function"""

    # set as global for mouse callback function
    global current_video_file, next_video_file, after_click, current_screen

    # load main video first
    cap = cv2.VideoCapture(video_files[current_video_file])

    if fullscreen:
        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    else:
        cv2.namedWindow("window")

    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    cv2.setMouseCallback("window", mouse_callback, [frame_width, frame_height])

    _, _, window_x, window_y = cv2.getWindowImageRect("window")
    print(window_x, window_y)
    print(cv2.getWindowImageRect("window"))

    while cap.isOpened():
        ret, frame = cap.read()

        # it true, video hasn't reach end
        if ret:
            cv2.imshow('window', frame)

            # change video if different animation is marked by cursor
            if current_video_file != next_video_file:
                current_video_file = next_video_file
                cap = cv2.VideoCapture(video_files[current_video_file])

        # else, end of video
        else:
            # print("END OF VIDEO")
            # print("current:{} \nnext: {}".format(current_video_file, next_video_file))
            after_click = False

            if current_video_file == next_video_file:  # play video in loop
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

                if current_video_file in VIDEO_TO_STATIC_IMAGE:
                    next_video_file = VIDEO_TO_STATIC_IMAGE[current_video_file]
                    for screen_name in MOUSE_OVER_LOCATIONS:
                        if "_" + screen_name in next_video_file:
                            current_screen = screen_name
                            current_video_file = next_video_file

                            print("NEW SCREEN: {}".format(current_screen))

                cap = cv2.VideoCapture(video_files[current_video_file])

            else:  # play different video

                current_video_file = next_video_file

                # if current video is a transition - switch to static image at the end of video
                # and change the screen value
                # if current_video_file in VIDEO_TO_STATIC_IMAGE:
                #     next_video_file = VIDEO_TO_STATIC_IMAGE[current_video_file]
                #     for screen_name in MOUSE_OVER_LOCATIONS:
                #         if "_" + screen_name in next_video_file:
                #             current_screen = screen_name
                #             print("NEW SCREEN: {}".format(current_screen))

                # cap = cv2.VideoCapture(video_files[current_video_file])

        # if quit key was pressed, exit video (default: ESC key)
        if cv2.waitKey(frames_per_second) & 0xFF == ord(quit_key):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Starting program...")
    time.sleep(0.3)

    play_video(ALL_VIDEOS, fullscreen=True)
    print("\nProgram terminated")
