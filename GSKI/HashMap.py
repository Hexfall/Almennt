class MyHashableKey():
    def __init__(self, int_value, string_value):
        self.int = int_value
        self.str = string_value
    
    def __eq__(self, other):
        return self.int == other.int and self.str == other.str
    
    def __hash__(self):
        primes = [2]
        num = 3
        while len(primes) < len(self.str) + 1:
            for i in primes:
                if num % i == 0:
                    break
            else:
                primes.append(num)
            num += 2
        numbers = [self.int] + [ord(i) for i in self.str]
        return sum([primes[i]**numbers[i] for i in range(len(numbers))])