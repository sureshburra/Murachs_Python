class MathOperations:
    @classmethod
    def add(cls, x, y):
        return x+y

    @staticmethod
    def multiply(x, y):
        return x*y


result1 = MathOperations.add(5, 3)
result2 = MathOperations.multiply(5, 3)
print(result1)
print(result2)
