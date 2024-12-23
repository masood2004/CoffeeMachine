import sys
import time


def bouncing_ball_animation(duration):
    ball_path = ["  o  ", " o   ", "o    ",
                 " o   ", "  o  ", "   o ", "    o", "   o "]
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in ball_path:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\rDone!    \n")
