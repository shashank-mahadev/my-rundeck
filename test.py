import random
import string
import time

while True:
    # Generate random text (50 characters)
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=50))

    # Append to test.txt
    with open("test.txt", "a") as f:
        f.write(data + "\n")

    print("Written:", data)

    # Wait 1 second
    time.sleep(1)
