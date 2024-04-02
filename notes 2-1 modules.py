# Lists and Modules
# Author: Jimmy Cao 
# March 8 2024

import random 

def coin_flip():
    # return heads or tails or other 
    # Heads is any number 0 to 0.499999999
    # Tails is any number from 0.5 to 0.5 to 0.99999991
    # Other is any number greater than 0.9999991
    roll = random.random()
    
    if roll < 0.5:
        return "Heads"
    elif roll <0.999991:
        return "Tails"
    else:
        return "other"
    
def main():
    for _ in range (1000):
    
        print(coin_flip())
    if coin_flip() == heads: 
        heads = heads + 1
    elif coin_flip() == "tails":
        tails += 1
    elseother += 1
main()

