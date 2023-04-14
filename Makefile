clean:
	rm -r images/*

lint:
	zsh validate.sh

setup:
	python -m venv .venv
	. .venv/bin/activate && \
		pip install -r requirements.txt


SLACK_BOT_TOKEN := xoxb-<kusagiに確認>
CHANNEL_ID := C01...  # チャンネルID
THREAD_TS := 16812xxxxx.082xxx # スレッドID

.env:
	touch $@
	@echo "SLACK_BOT_TOKEN=$(SLACK_BOT_TOKEN)\nCHANNEL_ID=$(CHANNEL_ID)\nTHREAD_TS=$(THREAD_TS)" > $@
	@echo ".env file has been created"

.PHONY: env
env: .env
