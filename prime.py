def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Write prime numbers to output.txt
with open("output.txt", "w") as f:
    for num in range(1, 101):
        if is_prime(num):
            f.write(f"{num}\n")

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Automatically generate and display primes without waiting for user input
n = 10  # Set a fixed number of primes to generate
print(f"First {n} prime numbers: {generate_primes(n)}")
