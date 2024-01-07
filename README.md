# desktop_screenshoter

スクショ業務に悩める全ての人へ

# 手順
- .envファイルにbot_token, thread_ts, channel_idを記述
- SnapBotアプリをチャンネルに招待する

環境構築
```
$ make setup
```

送りたいスレッドの準備 .env　ファイルの編集
```
$ make env


記入例に沿って編集
# https://sample.slack.com/archives/<チャンネルID>/p1681263649282189?thread_ts=<スレッドID>&cid=<チャンネルID>
# https://sample.slack.com/archives/C01D50TQJR5/p1681263649282189?thread_ts=1681263621.082189&cid=C01D50TQJR5
```



スクリーンショットの実行
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