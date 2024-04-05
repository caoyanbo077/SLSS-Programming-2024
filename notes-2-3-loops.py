# Loops and Iteration 
# Jimmy Cao 
# April 4 2024

# print something 10 times

for _ in range(10):
    print("something")

# Print out every item in grocery ist 

grocery_list = [
    "dishwater tabs",
    "aluminium foil",
    "blueberry muffins",
    "Banana"

]
# stop when we reach blueberry muffins
for item in grocery_list: 
    print("---")
    print(f"{item}")
    if item == "blueberry muffins":
        break

# Count from zero to 9 
for i in range(10): 
    print(i)
    if i%2 == 0:
        print(f"{i} is an even number")

counter = 0 

while counter < 1000: 
    print(counter)
    counter = counter + 1