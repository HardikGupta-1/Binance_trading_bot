from loguru import logger

logger.add(
    "bot.log",
    rotation="1 MB",
    level="INFO",
    format="{time} | {level} | {message}"
)

def get_logger():
    return logger
