# ---------------------------
# 1. Sieve of Eratosthenes
# ---------------------------
def sieve_of_eratosthenes(limit):
    # Create a boolean list where index represents the number
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for number in range(2, int(limit ** 0.5) + 1):
        if is_prime[number]:
            # Mark multiples as not prime
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    # Generate a list of prime numbers
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes, is_prime

# ---------------------------
# 2. Main program
# ---------------------------
def main():
    LIMIT = 200000
    primes, is_prime_array = sieve_of_eratosthenes(LIMIT)
    print(f"Primes up to {LIMIT} have been calculated.")

    while True:
        try:
            n = int(input("Enter a number to check if it's prime: "))
            if 1 <= n <= LIMIT:
                if is_prime_array[n]:
                    print("prime")
                else:
                    print("not prime")
                break
            else:
                print(f"Please enter a number between 1 and {LIMIT}.")
        except ValueError:
            print("Invalid input. Enter an integer.")

# ---------------------------
# 3. Run the program
# ---------------------------
main()
