# Methods - String Methods
# Author: Jimmy Cao 
# 21 February 2024

# Ask the user what the weather is, if they say rainy, say bring an umbrella 
user_reply = input("What is the weather today?")

if user_reply.strip("!.,?/").lower() == "rainy":
    print("Bring an umbrella")
else: 
    print("Sorry I didn't understand")