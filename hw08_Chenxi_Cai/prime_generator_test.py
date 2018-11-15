"""PyTest test suite"""
from prime_generator import PrimeGenerator


def test_primes_to_max():
    """test the output of our primes generator"""
    prime = PrimeGenerator()
    assert 2 not in prime.prime_list
    prime_list = prime.primes_to_max(43)
    assert 31 in prime_list
    assert 23 in prime_list
