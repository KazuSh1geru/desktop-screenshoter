"""
screencapture ./images/$(date "+%y%m%d_%H%M%S")_image.png
# Select Display ID
screencapture -l <display_id> screen.png

"""

import os

def screenshot():
    os.makedirs('images', exist_ok=True)
    os.system('screencapture ./images/$(date "+%y%m%d_%H%M%S")_image.png')
