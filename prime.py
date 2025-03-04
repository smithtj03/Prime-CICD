# prime.py

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Set the number without needing input()
num = 100  # Change this to whatever you need

primes = []
for i in range(2, num + 1):
    if is_prime(i):
        primes.append(i)

# Write the primes to a file
with open("/home/ec2-user/prime/output.txt", "w") as f:
    for prime in primes:
        f.write(f"{prime}\n")
