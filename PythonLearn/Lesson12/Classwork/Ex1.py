class Factorial:
    def __init__(self, n):
        self.n = n
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.result *= self.n
        self.n -= 1
        return self.result
