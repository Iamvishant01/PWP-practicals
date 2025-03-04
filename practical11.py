def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

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

number = 7
print(f"{number} is prime:" , is_prime(number))


num = 5
print(f"Factorial of {num}:", factorial(num))


text = "Hello World!"
count_upper_lower(text)