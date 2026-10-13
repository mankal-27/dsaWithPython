
import random
import string

target = "motherofall".upper()
alphabet = string.ascii_uppercase
max_attempts = 100_000

for attempt in range(1, max_attempts + 1):
    generated = "".join(
        random.choice(alphabet)
        for _ in range(len(target))
    )

    if generated == target:
        print("Found:", generated)
        print("Attempts:", attempt)
        break
else:
    print("Target not found.")
    print("Attempts:", max_attempts)
