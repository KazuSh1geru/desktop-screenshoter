"""
screencapture ./images/$(date "+%y%m%d_%H%M%S")_image.png

# 背景しか写らないので、-Rオプションをつける
# -x: 消音
screencapture -o -R0,0,1650,1080 ./images/$(date "+%y%m%d_%H%M%S")_image.png
# Select Display ID
screencapture -l <display_id> screen.png

"""

import os
import pyautogui
import subprocess
from datetime import datetime
import platform


def screenshot():
    os.makedirs("images", exist_ok=True)
    if _is_mac_os():
        filename = "./images/{}_image.png".format(
            datetime.now().strftime("%y%m%d_%H%M%S")
        )
        subprocess.run(["screencapture", "-x", "-o", "-m", filename])
    # windowsの場合
    else:
        try:
            # スクリーンショットを取得
            screenshot = pyautogui.screenshot()
            # ファイル名を生成
            filename = (
                "./images/"
                + datetime.datetime.now().strftime("%y%m%d_%H%M%S")
                + "_image.png"
            )
            # 画像を保存
            screenshot.save(filename)
        except Exception as e:
            print(e)
            print("screenshot error")


def _is_mac_os():
    return platform.system() == "Darwin"


if __name__ == "__main__":
    screenshot()
