# signal_shutdown.py

def log_shutdown(func):
    def wrapper(power):
        print("Authorization Started")
        result = func(power)
        print("Authorization Completed")
        return result
    return wrapper


@log_shutdown
def signal_shutdown(power):
    if power == 0:
        return 0
    else:
        print("Signal Strength:", power)
        return 1 + signal_shutdown(power - 1)