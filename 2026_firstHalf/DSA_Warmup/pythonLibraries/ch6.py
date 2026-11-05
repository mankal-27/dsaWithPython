val = (1,3,5)
print(val)

#(2,9)
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

val1 = Pair(2,9)
val1.second = 3
print(val1.first, val1.second)