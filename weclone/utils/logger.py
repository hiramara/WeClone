"""Logging configuration for WeClone.

Provides a centralized logger setup with colored console output
and optional file logging for the WeClone application.
"""

import logging
import sys
from pathlib import Path
from typing import Optional


LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ColoredFormatter(logging.Formatter):
    """Custom formatter that adds ANSI color codes to log level names."""

    COLORS = {
        logging.DEBUG: "\033[36m",    # Cyan
        logging.INFO: "\033[32m",     # Green
        logging.WARNING: "\033[33m",  # Yellow
        logging.ERROR: "\033[31m",    # Red
        logging.CRITICAL: "\033[35m", # Magenta
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelno, self.RESET)
        record.levelname = f"{color}{record.levelname}{self.RESET}"
        return super().format(record)


def get_logger(
    name: str,
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    use_color: bool = True,
) -> logging.Logger:
    """Create and configure a logger instance.

    Args:
        name: The name for the logger, typically __name__ of the calling module.
        level: Logging level (default: logging.INFO).
        log_file: Optional path to a log file. If provided, logs are also written to disk.
        use_color: Whether to use colored output in the console (default: True).

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)

    # Avoid adding duplicate handlers if logger already configured
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    if use_color and sys.stdout.isatty():
        formatter: logging.Formatter = ColoredFormatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    else:
        formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Optional file handler
    if log_file is not None:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(
            logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
        )
        logger.addHandler(file_handler)

    # Prevent log messages from propagating to the root logger
    logger.propagate = False

    return logger


# Module-level default logger for WeClone
logger = get_logger("weclone")
