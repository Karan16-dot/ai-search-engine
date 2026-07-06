import logging
from pathlib import Path

# Create logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logger = logging.getLogger("ai_search_engine")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File Handler
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setFormatter(formatter)

# Prevent duplicate handlers
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)