import time
import glob
import cv2  # dependency


# mouse callback function
def mouse_callback(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print((x, y))

def play_video(video_file: str, frame_per_second=25, quit_key='q', fullscreen=True):
    cap = cv2.VideoCapture(video_file)
    if fullscreen:
        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    else:
        cv2.namedWindow("window")

    cv2.setMouseCallback('window', mouse_callback)

    while cap.isOpened():
        ret, frame = cap.read()


        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('frame', gray)
        if ret:
            cv2.imshow('window', frame)
        else:
            print('END OF VIDEO')
            # load video again for loop
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


        if cv2.waitKey(frame_per_second) & 0xFF == ord(quit_key):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Starting program...")
    time.sleep(0.3)

    sample_vid = r"samples\videos\SampleVideo_1280x720_30mb.mp4"  # video file path
    sample_vid_short = r"samples\videos\SampleVideo_1280x720_1mb.mp4"  # video file path
    samples_jpgs = glob.glob(r"samples/*jpg")

    #play_video(sample_vid)
    play_video(sample_vid_short, fullscreen=False)
