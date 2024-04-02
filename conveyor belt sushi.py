# Cupcake Party
# Author: Jimmy Cao 
# February 23, 2024

Small = int(input("How many small boxes of cupcake?"))
Reg = int(input("How many reular boxes of cupcake?"))

total = (Small * 3 + Reg * 8) - 28

if total > 0:
    print (f"There is {total} cupcakes left over")

if total < 0:
    print ("There are not enough cupcakes for the class")