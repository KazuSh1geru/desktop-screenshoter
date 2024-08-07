"""このモジュールは画像の差分有無を判定するモジュールです。"""

import os
import cv2
import numpy as np
from init_logger import init_logger

THRESHOLD = float(os.getenv("THRESHOLD", 8))

logger = init_logger()


def judge_image_difference(img1_path, img2_path):
    """画像の差分有無を判定する関数

    Args:
        img1_path (string): 比較対象の画像1
        img2_path (string): 比較対象の画像2

    Returns:
        boolean: 差分有無
    """
    diff = _image_difference(img1_path, img2_path)
    logger.info(diff)

    return _judge_diff(diff, threshold=THRESHOLD)


def _image_difference(img1_path, img2_path):
    # 画像読み込み
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # 画像をグレースケールに変換
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 特徴量抽出器の生成
    orb = cv2.ORB_create()

    # 特徴量の検出と記述子の計算
    _, des1 = orb.detectAndCompute(img1_gray, None)
    _, des2 = orb.detectAndCompute(img2_gray, None)

    # 特徴量のマッチング
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # マッチングされた特徴点の距離の平均値を計算
    dist_sum = 0
    for match in matches:
        dist_sum += match.distance
    dist_avg = dist_sum / len(matches)

    # 2つの画像の距離を計算
    diff = np.abs(dist_avg)

    return diff


def _judge_diff(diff, threshold=THRESHOLD) -> bool:
    return diff < threshold
