"""class of prime generator"""


class PrimeGenerator:
    def __init__(self):
        """constructor
        initialize prime list and composite set"""
        self.prime_list = []
        self.composite_set = set()

    def primes_to_max(self, max_value):
        """Given the integer range, return all primes in this range
        Integer -> list"""
        for i in range(2, max_value + 1):
            if i not in self.composite_set:
                self.prime_list.append(i)
                self.composite_set.update(range(i * i, max_value + 1, i))
        return self.prime_list
