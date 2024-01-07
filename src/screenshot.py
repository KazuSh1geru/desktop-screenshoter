"""
screencapture ./images/$(date "+%y%m%d_%H%M%S")_image.png

# 背景しか写らないので、-Rオプションをつける
# -x: 消音
screencapture -o -R0,0,1650,1080 ./images/$(date "+%y%m%d_%H%M%S")_image.png
# Select Display ID
screencapture -l <display_id> screen.png
"""

import os
from subprocess import run
from datetime import datetime
from logging import getLogger
import pyautogui

logger = getLogger(__name__)


def execute_screenshot() -> None:
    """スクリーンショットを実行"""
    os.makedirs("images", exist_ok=True)
    try:
        # スクリーンショットを取得
        # logger.info("execute screenshot")
        _screenshot()
    except Exception as e:
        logger.debug("screenshot error: ", e)


def _screenshot() -> None:
    screenshot = pyautogui.screenshot()
    # ファイル名を生成
    filename = _get_filename()
    # 画像を保存
    screenshot.save(filename)
    logger.info(f"screenshot saved: {filename}")


def _screenshot_with_macos() -> None:
    filename = _get_filename()
    run(["screencapture", "-x", "-o", "-m", filename])


def _get_filename() -> str:
    return "./images/{}_image.png".format(datetime.now().strftime("%y%m%d_%H%M%S"))
