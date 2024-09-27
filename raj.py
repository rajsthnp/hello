class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def multiply(self):
        return self.a*self.b



    @staticmethod
    def sub(a,b):
        return a-b

a=Math
print(a.add(2,3))
print(a.sub(3,4))
b=Math(1,2)
print(b.multiply())

