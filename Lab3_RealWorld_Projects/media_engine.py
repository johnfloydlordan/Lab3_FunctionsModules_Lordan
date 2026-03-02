# media_engine.py

def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper


def even_square_stream(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2


@monitor
def play_count_stream(limit):
    total_plays = 0
    records = 0

    for value in even_square_stream(limit):
        print("Play Count:", value)
        total_plays += value
        records += 1

    print("Total Plays:", total_plays)
    print("Number of Records Processed:", records)

    return total_plays