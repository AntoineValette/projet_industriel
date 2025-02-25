from datetime import datetime

def log(message, *args, **kwargs):
    formatted_message = " ".join(map(str, args))
    print(f"[{datetime.now()}] {message} {formatted_message}")

def value(n):
    return ", ".join(["%s"] * n)