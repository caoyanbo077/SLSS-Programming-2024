# Functions
# Jimmy Cao 
# 26 February, 2024

# create a function called say hello 
# When you call it, it prints hello

def say_hello():
    print("hello!")


say_hello()
say_hello()

# Create a function called say_hello params
# The parameter we pass in 
# THe person that were greeting

def say_hello_params(name):
    print(f"Hello {name.capitalize()}!")

say_hello()
say_hello_params("Jeffery")

say_hello_params("thomas")

# Create a function that takes a number 
# It will tell you how big that number is 

def how_big(num):
    if num < 0:
        return "very small"
    if num < 10:
        return "pretty small"
    if num < 100:
        return "big"
    if num < 1000: 
        return "very big"
    
def adder(x: int,y: int) -> int:
    return x + y 

result = adder(100, 2)
print(result)

print (how_big(100))

result = how_big(100)
print(result)
