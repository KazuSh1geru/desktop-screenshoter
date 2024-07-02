"""このモジュールは、Slackに画像を送信するための関数を提供します。"""

import os

from dotenv import load_dotenv
from init_logger import init_logger

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError, SlackClientError

load_dotenv()

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
logger = init_logger()


def send_image_to_thread(image_path) -> None:
    """与えられた判定結果と画像を使用して、スレッドに画像を送信する関数。
    判定結果がTrueの場合は、画像をスレッドに送信します。
    """
    try:
        client = _get_slack_client()
        channel_id, thread_ts = _get_target_info()
        # _: resultを出力できる
        _ = client.files_upload_v2(
            channel=channel_id,
            thread_ts=thread_ts,
            file=image_path,
            initial_comment="SNAP :camera:",
        )
        # Log the result
        logger.info(f"Screenshot uploaded: {image_path}")
    except SlackApiError as e:
        logger.info(f"Error: {e}")
    except Exception:
        raise


def _get_slack_client() -> WebClient:
    bot_token = os.getenv("SLACK_BOT_TOKEN")
    if bot_token is None:
        raise SlackClientError("SLACK_BOT_TOKEN is not set in .env file")
    return WebClient(token=bot_token)


def _get_target_info() -> tuple[str, str]:
    channel_id = os.getenv("CHANNEL_ID")
    thread_ts = os.getenv("THREAD_TS")
    if channel_id is None or thread_ts is None:
        raise Exception("CHANNEL_ID or THREAD_TS is not set in .env file")
    return channel_id, thread_ts
