def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("/home/ec2-user/prime/output.txt", "w") as f:
    for i in range(1, 100):  # Example range of numbers to check
        if is_prime(i):
            f.write(f"{i} is prime\n")

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    n = int(input("Enter the number of primes to generate: "))
    print(f"First {n} prime numbers: {generate_primes(n)}")
