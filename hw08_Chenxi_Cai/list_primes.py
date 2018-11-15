from prime_generator import PrimeGenerator


def main():
    """print all primes in range"""
    prime = PrimeGenerator()
    max_range = int(input("Please enter the larget number:\n"))
    prime_list = prime.primes_to_max(max_range)
    print("Prime are:\n", prime_list)


main()
