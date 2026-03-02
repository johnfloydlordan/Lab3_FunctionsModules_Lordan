# access_control.py

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper


def compute_access_level(control, artist):
    return control * 3 + len(artist)


def validate_access(level, threshold):
    return level >= threshold


@audit_log
def authorize(control, artist):
    access_level = compute_access_level(control, artist)
    threshold = control + 5

    if validate_access(access_level, threshold):
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"