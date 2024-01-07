import json
from logging import getLogger, config

with open("./log_config.json", "r") as f:
    log_conf = json.load(f)

config.dictConfig(log_conf)
# logger = getLogger("app")
