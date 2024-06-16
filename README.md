# desktop-screenshoter

スクショ業務に悩める全ての人へ

# 手順
- .envファイルにbot_token, thread_ts, channel_idを記述
- SnapBotアプリをチャンネルに招待する

## 環境構築

### 1. パッケージの準備
下記コマンドを実行する。
```
$ make setup
```

### 2. 環境変数の設定

送りたいスレッドの準備 .env　ファイルの編集
```
$ nano .env
```

下記のように、環境変数を記入する。
```
SLACK_BOT_TOKEN=xoxb-... # Bot User OAuth Access Token
CHANNEL_ID=C01...  # チャンネルID
THREAD_TS=16812xxxxx.082xxx # スレッドID
```

### 3. チャンネルID と スレッドIDを取得する
送信したいチャンネルにスレッドを立ち上げ、メッセージのURLを取得する。
URLを参照することで、チャンネルID と スレッドIDを取得することができる。
チャンネルID と スレッドIDの構成は下記のようになっている。
```
https://sample.slack.com/archives/<チャンネルID>/p1681263649282189?thread_ts=<スレッドID>&cid=<チャンネルID>

https://sample.slack.com/archives/C01D50TQJR5/p1681263649282189?thread_ts=1681263621.082189&cid=C01D50TQJR5
```


# スクリーンショットの実行
```
$ python src/main.py
```
止めるときは「Ctrl + Cキーを押す」
→ これにより、実行中のプロセスが強制的に中断されます。


# TIPS

imagesの削除
```
$ make clean
```

簡易的なlint
```
$ make lint
```
