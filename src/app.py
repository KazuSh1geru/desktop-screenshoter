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

if __name__ == '__main__':
    # img1_path = 'images/230405_100556_image.png'
    # img1_path = 'images/230405_101254_image.png'
    # img2_path = 'images/230405_101243_image.png'

    # if judge_image_difference(img1_path, img2_path):
    #     print('The images are the same.')
    # else:
    #     print('The images are different.')

    while True:
        screenshot()
        time.sleep(2)
        latest_file, second_latest_file = get_latest_file()
        if judge_image_difference(latest_file, second_latest_file):
            print('The images are the same.')
        else:
            print('The images are different.')
            send_image_to_thread(True, latest_file)