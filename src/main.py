"""このモジュールは、スクリーンショットを撮影し、スレッドに送信するmain関数部分です。"""

import os
import time

from init_logger import init_logger
from judge_image_diff import judge_image_difference
from screenshot import execute_screenshot
from slack_client import send_image_to_thread

DIR_PATH = "./images"  # スクリーンショットが保存されているディレクトリのパス

logger = init_logger()


def main() -> None:
    """1. スクリーンショットを撮影する
    2. スクリーンショットを2つ取得する
    3. 2つのスクリーンショットを比較する
    4. 2つのスクリーンショットが同じ場合は、最新のスクリーンショットを削除する
    5. 2つのスクリーンショットが異なる場合は、最新のスクリーンショットをスレッドに送信する
    6. 1に戻る
    """
    while True:
        execute_screenshot()
        time.sleep(2)
        latest_screenshot, second_latest_screenshot = _get_latest_screenshot()
        if latest_screenshot is None or second_latest_screenshot is None:
            continue
        if judge_image_difference(latest_screenshot, second_latest_screenshot):
            logger.info("The images are the same.")
            _delete_screenshot(latest_screenshot)
        else:
            logger.info("The images are different.")
            send_image_to_thread(latest_screenshot)


def _get_latest_screenshot() -> tuple[str, str] | tuple[None, None]:
    screenshots = os.listdir(
        DIR_PATH,
    )  # ディレクトリ内のスクリーンショットのリストを取得
    screenshots = [
        f for f in screenshots if f.endswith(".png")
    ]  # ".png"で終わるスクリーンショットのみを抽出
    screenshots = sorted(screenshots)  # スクリーンショット名を日付順にソート

    if len(screenshots) >= 2:
        latest_screenshot = screenshots[-1]  # 最新のスクリーンショットを取得
        second_latest_screenshot = screenshots[-2]  # 1つ前のスクリーンショットを取得
        HEADER = "./images/"
        return HEADER + latest_screenshot, HEADER + second_latest_screenshot
    # if文が処理されなかった場合は、スクリーンショットが2つ以上存在しない
    logger.info("There are not enough screenshots in the directory.")
    return None, None


def _delete_screenshot(screenshot_path) -> None:
    os.remove(screenshot_path)


if __name__ == "__main__":
    main()
