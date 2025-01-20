def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def add_prime_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        if is_prime(i):
            total_sum += i
    return total_sum

n = int(input("Enter the value of n: "))

result = add_prime_numbers(n)
print(f"The sum of all prime numbers from 1 to {n} is: {result}")