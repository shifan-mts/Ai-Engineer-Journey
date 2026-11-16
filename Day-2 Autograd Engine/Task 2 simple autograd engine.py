class Value:
    def __init__(self,data):
        self.data = data
    def __add__(self,other):
        return Value(self.data+other.data)
    def __sub__(self,other):
        return Value(self.data-other.data)
    def __mul__(self,other):
        return Value(self.data*other.data)


a = Value(1.0)
b = Value(0.0)
b = a+a
print(b.data)