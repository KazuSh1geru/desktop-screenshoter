import os
import time
from judge_image_diff import judge_image_difference
from screenshot import execute_screenshot
from slack_client import send_image_to_thread


dir_path = "./images"  # スクリーンショットが保存されているディレクトリのパス

def main():
    while True:
        execute_screenshot()
        time.sleep(2)
        latest_screenshot, second_latest_screenshot = _get_latest_screenshot()
        if latest_screenshot is None or second_latest_screenshot is None:
            continue
        if judge_image_difference(latest_screenshot, second_latest_screenshot):
            print("The images are the same.")
            _delete_screenshot(latest_screenshot)
        else:
            print("The images are different.")
            send_image_to_thread(latest_screenshot)


def _get_latest_screenshot():
    screenshots = os.listdir(dir_path)  # ディレクトリ内のスクリーンショットのリストを取得
    screenshots = [f for f in screenshots if f.endswith(".png")]  # ".png"で終わるスクリーンショットのみを抽出
    screenshots = sorted(screenshots)  # スクリーンショット名を日付順にソート

    if len(screenshots) >= 2:
        latest_screenshot = screenshots[-1]  # 最新のスクリーンショットを取得
        second_latest_screenshot = screenshots[-2]  # 1つ前のスクリーンショットを取得
        HEADER = "./images/"
        return HEADER + latest_screenshot, HEADER + second_latest_screenshot
    else:
        print("There are not enough screenshots in the directory.")
        return None, None


def _delete_screenshot(screenshot_path):
    os.remove(screenshot_path)


if __name__ == "__main__":
    main()