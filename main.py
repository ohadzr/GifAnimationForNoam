import time
import cv2  # dependency

from config import ESC_KEY, ALL_VIDEOS, current_video_file, next_video_file

# mouse callback function
def mouse_callback(event, x, y, flags, param):
    global next_video_file

    if event == cv2.EVENT_LBUTTONDOWN:
        print('currently playing main, changing to second')
        next_video_file = 'surfer'
        print((x, y))


def play_video(video_files: dict, frames_per_second=25, quit_key=ESC_KEY, fullscreen=True):
    # load main video first

    # set as global for callback function
    global current_video_file, next_video_file

    cap = cv2.VideoCapture(video_files[current_video_file])

    if fullscreen:
        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    else:
        cv2.namedWindow("window")

    cv2.setMouseCallback('window', mouse_callback, [video_files])
    print(cv2.getWindowImageRect('window'))

    while cap.isOpened():
        ret, frame = cap.read()

        # it true, video hasn't reach end
        if ret:
            cv2.imshow('window', frame)

        # else, end of video
        else:
            print('END OF VIDEO')
            print("current:{} \nnext: {}".format(current_video_file, next_video_file))
            if current_video_file == next_video_file:  # play video in loop
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            else:  # play different video
                current_video_file = next_video_file
                cap = cv2.VideoCapture(video_files[current_video_file])

        # if quit key was pressed, exit video (default: ESC key)
        if cv2.waitKey(frames_per_second) & 0xFF == ord(quit_key):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Starting program...")
    time.sleep(0.3)


    # play_video(sample_vid)
    play_video(ALL_VIDEOS, fullscreen=True)
