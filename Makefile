.PHONY: clean
clean:
	rm -r images/*

.PHONY: ci
ci: install

.PHONY: install
install:
	poetry install

.PHONY: format
format:
	poetry run black src
	poetry run ruff check src --fix-only --unsafe-fixes

.PHONY: screenshot
screenshot:
	poetry run python src/main.py

.PHONY: lint
lint:
	# Python
	poetry run black src --check
	poetry run ruff check src