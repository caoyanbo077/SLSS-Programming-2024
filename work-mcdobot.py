# McDoBot
# Author: Jimmy Cao 
# 21 February 2024

# Ask the user if they want fries with their meal
user_reply = input("Would you like fries with your meal?")

# If user responds yes, tell them that would be an extra $20
if user_reply.strip("!.,?/").lower() == "yes":
    print("That would be an extra $20")

# if user responds no, print "okay"
elif user_reply.strip("!.,?/").lower() == "no":
    print("Okay")

# For anything else, reply with answer not valid
else: 
    print(f"Sorry,{user_reply} is not a valid answer.")