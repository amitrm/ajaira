from datetime import datetime

def time_now():
    '''
    Returns the current timestamp for printing or logging.
    '''

    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")