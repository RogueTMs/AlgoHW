from bitarray import bitarray
from random import randint
import math


class BloomFilter:
    def __init__(self, s, p):
        self.s = s
        self.p = p
        self.n = math.ceil((s * math.log(1 / p, 2)) / math.log(2))
        self.k = math.ceil((self.n / s) * math.log(2))
        self.bitset = bitarray(self.n)
        self.hash_functions = [self._generate_hash_function() for _ in range(self.k)]

    def add(self, ip_address):
        for hash_function in self.hash_functions:
            index = hash_function(ip_address) % self.n
            self.bitset[index] = 1

    def contains(self, ip_address):
        for hash_function in self.hash_functions:
            index = hash_function(ip_address) % self.n
            if not self.bitset[index]:
                return False
        return True

    def _generate_hash_function(self):
        a = randint(1, self.n - 1)
        b = randint(0, self.n - 1)
        return lambda x: (a * hash(x) + b) % self.n


def generate_random_ip_addresses(n):
    ip_addresses = []
    for i in range(n):
        octets = [str(randint(0, 255)) for _ in range(4)]
        ip_address = '.'.join(octets)
        ip_addresses.append(ip_address)
    return ip_addresses


def test(n):
    sol = BloomFilter(n, 0.5)
    ip = generate_random_ip_addresses(2 * n)
    to_blum = ip[:n]
    to_test = ip[n:]
    for data in to_blum:
        sol.add(data)

    errors = 0
    for data in to_test:
        if sol.contains(data):
            errors += 1

    print(errors)

test(1000)
