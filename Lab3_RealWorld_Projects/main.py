# Lab 3 RealWorld Projects

# IMPORT

import access_control
import signal_shutdown
import media_engine

# STUDENT CONFIG

SEED_NUM = 2
FAVORITE_ARTIST = "THE RIDLEYS"
CONTROL_NUM = max(1, SEED_NUM)


# MISSION 1: AUTHORIZATION
print("=" * 50)
print("MISSION 1: AUTHORIZATION PROTOCOL")
print("=" * 50)

decision = access_control.authorize(CONTROL_NUM, FAVORITE_ARTIST)
print("Final Authorization Decision:", decision)

# MISSION 2: RECURSIVE SHUTDOWN
print("\n" + "=" * 50)
print("MISSION 2: RECURSIVE SIGNAL SHUTDOWN")
print("=" * 50)

initial_power = CONTROL_NUM + len(FAVORITE_ARTIST)
print("Initial Signal Strength:", initial_power)

total_calls = signal_shutdown.signal_shutdown(initial_power)
print("Total Recursive Calls:", total_calls)

# MISSION 3: STREAMING ANALYTICS
print("\n" + "=" * 50)
print("MISSION 3: STREAMING MEDIA ENGINE")
print("=" * 50)

limit = CONTROL_NUM + len(FAVORITE_ARTIST)
print("Stream Limit:", limit)

media_engine.play_count_stream(limit)
