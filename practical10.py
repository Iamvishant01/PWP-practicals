def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")
text = "Hello World!"
count_upper_lower(text)

# 2
import random
import math

random_float = 5 + (random.random() * (50 - 5))

print(f"Random float between 5 and 50: {random_float}")
