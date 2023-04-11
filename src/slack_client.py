import os

import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

channel_id = "C040Z00A15L"
thread_ts = "1681200773.262709"

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token="xoxb-518476454566-5090106341458-IwYn3ipNiI6Os263vz2vSvUy")
logger = logging.getLogger(__name__)


def send_image_to_thread(is_true, image_path):
    """
    与えられた判定結果と画像を使用して、スレッドに画像を送信する関数。
    判定結果がTrueの場合は、画像をスレッドに送信します。
    """
    if is_true:
        try:
            # Call the files.upload method using the WebClient
            # Uploading files requires the `files:write` scope
            client.files_upload_v2(
                channels=channel_id,
                initial_comment="Here's my file :smile:",
                file=image_path,
                thread_ts=thread_ts)
            # Log the result
            # logger.info(result)
        except SlackApiError as e:
            print(f"Error: {e}")
    else:
        print("判定結果はFalseです。何もしません。")

if __name__ == "__main__":
    # 例: 判定結果がTrueで、画像のパスが"images/230405_100556_image.png"の場合
    send_image_to_thread(True, "images/230405_100556_image.png")
