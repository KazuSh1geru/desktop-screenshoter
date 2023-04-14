import os
import time
from judge_image_diff import judge_image_difference
from screenshot import screenshot
from slack_client import send_image_to_thread


dir_path = "./images"  # ファイルが保存されているディレクトリのパス


def get_latest_file():
    files = os.listdir(dir_path)  # ディレクトリ内のファイルのリストを取得
    files = [f for f in files if f.endswith(".png")]  # ".png"で終わるファイルのみを抽出
    files = sorted(files)  # ファイル名を日付順にソート

    if len(files) >= 2:
        latest_file = files[-1]  # 最新のファイルを取得
        second_latest_file = files[-2]  # 1つ前のファイルを取得
        HEADER = "./images/"
        return HEADER + latest_file, HEADER + second_latest_file
    else:
        print("There are not enough files in the directory.")
        return None, None


def delete_file(file_path):
    os.remove(file_path)


if __name__ == "__main__":
    while True:
        screenshot()
        time.sleep(2)
        latest_file, second_latest_file = get_latest_file()
        if latest_file is None or second_latest_file is None:
            continue
        if judge_image_difference(latest_file, second_latest_file):
            print("The images are the same.")
            delete_file(latest_file)
        else:
            print("The images are different.")
            send_image_to_thread(True, latest_file)
