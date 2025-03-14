from datetime import datetime
import sys

def log(message, *args, **kwargs):
    formatted_message = " ".join(map(str, args))
    print(f"[{datetime.now()}] {message} {formatted_message}")

def log_kfk(msg):
    print(f"[{datetime.now()}] {msg}", flush=True)
    sys.stdout.flush()

def value(n):
    return ", ".join(["%s"] * n)