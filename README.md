# desktop_screenshoter

スクショ業務に悩める全ての人へ

# 手順
- .envファイルにbot_token, thread_ts, channel_idを記述
- SnapBotアプリをチャンネルに招待する

環境構築
```
$ make setup
```

スクリーンショットの実行
```
$ python src/app.py
```
止めるときは「Ctrl + Cキーを押す」
→ これにより、実行中のプロセスが強制的に中断されます。


# TIPS

簡易的なlint

```
$ make lint
```