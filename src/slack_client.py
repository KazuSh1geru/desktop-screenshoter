import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# SLACK_BOT_TOKENとTHREAD_URLには、Slack APIのトークンとスレッドのURLを指定します
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
thread_url = os.environ["THREAD_URL"]

def send_image_to_thread(is_true, image_path):
    """
    与えられた判定結果と画像を使用して、スレッドに画像を送信する関数。
    判定結果がTrueの場合は、画像をスレッドに送信します。
    """
    if is_true:
        try:
            response = client.conversations_list(types="private_channel")
            for channel in response["channels"]:
                if channel["name"] == "bot-test":
                    conversation_id = channel["id"]
                    break
            with open(image_path, "rb") as f:
                response = client.files_upload(
                    channels=conversation_id,
                    file=f,
                    initial_comment="True です！",
                    thread_ts=thread_url
                )
                print(f"スレッドに画像を送信しました: {response['file']['url_private']}")
        except SlackApiError as e:
            print(f"Error: {e}")
    else:
        print("判定結果はFalseです。何もしません。")

if __name__ == "__main__":
    # 例: 判定結果がTrueで、画像のパスが"/path/to/image.jpg"の場合
    send_image_to_thread(True, "/path/to/image.jpg")
