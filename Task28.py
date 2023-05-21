from bitarray import bitarray
from random import randint


class BloomFilter:
    def __init__(self):
        self.arr = bitarray()
        self.a = (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

    def show_arr(self):
        print(self.arr)

    def _hash(self, m, data):
        res = 0
        for i in range(4):
            res += self.a[i] * data[i]

        return res % m


import random
import math


class GPTBloomFilter:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.m = math.ceil((n * math.log(p)) / math.log(1 / (pow(2, math.log(2)))))
        self.k = math.ceil((self.m / n) * math.log(2))
        self.bitset = [False] * self.m
        self.hash_functions = [self._generate_hash_function() for _ in range(self.k)]

    def add(self, ip_address):
        for hash_function in self.hash_functions:
            index = hash_function(ip_address) % self.m
            self.bitset[index] = True

    def contains(self, ip_address):
        for hash_function in self.hash_functions:
            index = hash_function(ip_address) % self.m
            if not self.bitset[index]:
                return False
        return True

    def _generate_hash_function(self):
        a = random.randint(1, self.m - 1)
        b = random.randint(0, self.m - 1)
        return lambda x: (a * hash(x) + b) % self.m


def generate_random_ip_addresses(n):
    ip_addresses = []
    for i in range(n):
        octets = [str(random.randint(0, 255)) for _ in range(4)]
        ip_address = '.'.join(octets)
        ip_addresses.append(ip_address)
    return ip_addresses


def test(n):
    sol = GPTBloomFilter(n, 0.5)
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

test(100)
