"""
screencapture ./images/$(date "+%y%m%d_%H%M%S")_image.png

# 背景しか写らないので、-Rオプションをつける
# -x: 消音
screencapture -o -R0,0,1650,1080 ./images/$(date "+%y%m%d_%H%M%S")_image.png
# Select Display ID
screencapture -l <display_id> screen.png

"""

import os
import subprocess
from datetime import datetime
import pyautogui


def execute_screenshot() -> None:
    """スクリーンショットを実行
    """
    os.makedirs("images", exist_ok=True)
    try:
        # スクリーンショットを取得
        _screenshot()
    except Exception as e:
        print(e)
        print("screenshot error")


def _screenshot() -> None:
    screenshot = pyautogui.screenshot()
    # ファイル名を生成
    filename = _get_filename()
    # 画像を保存
    screenshot.save(filename)


def _screenshot_with_macos() -> None:
    filename = _get_filename()
    subprocess.run(["screencapture", "-x", "-o", "-m", filename])


def _get_filename() -> str:
    return "./images/{}_image.png".format(datetime.now().strftime("%y%m%d_%H%M%S"))
