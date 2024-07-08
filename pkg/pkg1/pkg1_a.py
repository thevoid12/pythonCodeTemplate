def function_one():
    print("This is function one")
#leave two lines between one func/class and another

def function_two():
    print("This is function two")


class MyClass:
#leave 1 line between class definition and the first method/value
    def method_one(self):
        print("This is method one") # no blank line after after a function definition
#leave 1 line between different methods insidew a class
    def method_two(self):
        print("This is method two")
        #Use single blank lines within functions or methods to separate logical sections of code.
        print("this is a seperate part of method 2")

    def complex_method(self):
        # Initialize variables
        result = 0
        for i in range(10):
            result += i
        # Check the result
        if result > 0:
            print("Result is positive")
        else:
            print("Result is non-positive")


#strings appending. dont use + for more than 1 join. use %s or f string
name="vinod"
n=100
x = 'name: %s; score: %d' % (name, n)
print(x)


# Avoid using the + and += operators to accumulate a string within a loop. In some conditions, 
# accumulating a string with addition can lead to quadratic rather than linear running time. 
# Although common accumulations of this sort may be optimized on CPython, that is an implementation detail. 
# The conditions under which an optimization applies are not easy to predict and may change. 
# Instead, add each substring to a list and ''.join the list after the loop terminates

a=["this","is","test"]
#wrong
b=""
for val in a:
    b+=val
print(b)
#correct
b=""
b=''.join(a)
print(b)
