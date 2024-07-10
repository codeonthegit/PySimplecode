class Cal:

    def __init__(self, a, b):    #same program Lab0014 with constructor
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

object_ref = Cal(3, 4)
output = object_ref.sum()
print(output)

print(Cal(3, 4).sum())  # reduce the code in one line

