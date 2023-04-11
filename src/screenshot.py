"""
screencapture ./images/$(date "+%y%m%d_%H%M%S")_image.png

# 背景しか写らないので、-Rオプションをつける
# -x: 消音
screencapture -o -R0,0,1650,1080 ./images/$(date "+%y%m%d_%H%M%S")_image.png
# Select Display ID
screencapture -l <display_id> screen.png

"""

import os


def screenshot():
    os.makedirs("images", exist_ok=True)
    os.system(
        'screencapture -x -o -R0,0,1650,1080 ./images/$(date "+%y%m%d_%H%M%S")_image.png'
    )
