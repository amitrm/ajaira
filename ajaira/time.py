from datetime import datetime

def time_now():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")