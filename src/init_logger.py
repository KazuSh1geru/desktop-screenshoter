import json
from logging import Logger, config, getLogger
from pathlib import Path


def init_logger() -> Logger:
    # ログ設定ファイルの読み込み
    with Path("./log_config.json").open("r") as f:
        log_conf = json.load(f)

    config.dictConfig(log_conf)
    logger = getLogger(__name__)
    return logger
