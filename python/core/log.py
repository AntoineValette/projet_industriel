from datetime import datetime

def log(message):
    """Simple fonction de logging."""
    print(f"[{datetime.now()}] {message}")

def value(n):
    return ", ".join(["%s"] * n)