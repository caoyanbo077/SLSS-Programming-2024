# Chatbot
# Jimmy Cao 
# March 8 2024

import random 

user_input = input("Hello there, what is your name?")

print(f"It's nice to meet you {user_input}")

user_response = input("How is your day so far")

# Create a list of possible response, then randomly choose a response, then were going to print that response 

positive_possible_responses = ["Im really happy for you!", "That's really good news!", "That's awesome!"]
if user_response == "good":
    chosen_response = random.choice(positive_possible_responses)
    print(chosen_response)

    

elif user_response == "bad":
    print("Aww, I hope your day will get better soon!")


print("goodbye, user!")

random.random()