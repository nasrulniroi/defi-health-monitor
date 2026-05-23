"""Structured logging configuration."""
import logging
import sys

def setup_logging(level: str = "INFO", json_format: bool = False):
    log_level = getattr(logging, level.upper(), logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    if json_format:
        formatter = logging.Formatter('{"level":"%(levelname)s","name":"%(name)s","message":"%(message)s","time":"%(asctime)s"}')
    else:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(log_level)
    root.handlers.clear()
    root.addHandler(handler)
