"""このモジュールは、Slackに画像を送信するための関数を提供します。"""

import os

from dotenv import load_dotenv
from init_logger import init_logger

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
logger = init_logger()


def send_image_to_thread(image_path) -> None:
    """与えられた判定結果と画像を使用して、スレッドに画像を送信する関数。
    判定結果がTrueの場合は、画像をスレッドに送信します。
    """
    try:
        # _: resultを出力できる
        _ = client.files_upload_v2(
            channel=os.getenv("CHANNEL_ID"),
            thread_ts=os.getenv("THREAD_TS"),
            file=image_path,
            initial_comment="SNAP :camera:",
        )
        # Log the result
        logger.info(f"Screenshot uploaded: {image_path}")
    except SlackApiError as e:
        logger.debug(f"Error: {e}")
