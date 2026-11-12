# Print number 0 to 4
for i in range(5):
    print(i)

# print items in list
for fruit in ["apple", "bannana"]:
    print(fruit)

#for loop with else
for i in range(5):
    print(i)
else:
    print("Loop Done")

#Nested Loop
for i in range(2):
    for j in range(3):
        print(i, j)

# while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1

# function
def greet(name):
    print(f"Hello {name}!")

greet("Manjunath")

#user defined function
def my_func(c1, c2, c3):
    print(c3 + " is smallest")

my_func(c1="Email", c2="Tobias", c3="Linus")

#Default Arguments
def my_func1(country="India"):
    print(f"I am from {country}")

my_func1()
my_func1("USA")

# *args arbitary arguments
def my_fun2(*kids):
    print(f"The youngest child is {kids[2]}")

my_fun2("Email", "tobias", "linus")

def my_func3(name, age):
    print(f"My name is {name} and my age is {age}")

my_func3("Manjunath", 34)

class Calculator():
    def add(self,num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num2 - num1

    def mul(self, num1, num2):
        return num1 * num2

    def div(self,num1, num2):
        return num1 // num2

new_calculator = Calculator()
print(new_calculator.add(2,5))
print(new_calculator.sub(3,6))
print(new_calculator.mul(2,5))
print(new_calculator.div(10,5))


def checkEvenOdd(num):
    if(num % 2 != 0):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")

checkEvenOdd(19)
checkEvenOdd(10)

for i in range(11):
    print(i)

