clean:
	rm -r images/*

lint:
	zsh validate.sh

setup:
	python -m venv .venv
	. .venv/bin/activate && \
		pip install -r requirements.txt
