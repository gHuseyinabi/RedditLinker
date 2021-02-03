from config import config

log_stream = open(config.get("logFile") if "logFile" in config else "default.log", "w")


def log(string, **kwargs):
    open(config.get("logFile") if "logFile" in config else "default.log", "w").write(string, **kwargs)