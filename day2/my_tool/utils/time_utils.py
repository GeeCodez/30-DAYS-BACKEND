from datetime import datetime

def timestamp():
    """
    Return the current timestamp as a formatted string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def timestamp_filename(prefix="log"):
    """
    Return a safe filename with timestamp.
    Example: log_2025-01-01_12-30-59.txt
    """
    raw =datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{prefix}_{raw}.txt"