# Title: very hungry and dumb bot
# Author: Jimmy Cao 
# Date: March 4, 2024
import time 

# Greet the user 
print("hello there, unknown user! 👋")
print()


print()
time.sleep(1)
user_name = input("Whats your name?")
print()

time.sleep(1)
print(f"It's really nice to meet you {user_name}!")
print()
user_reply = input(f"Wanna go out to eat {user_name}?")


# if user responds yes to going out to eat
if user_reply.strip("!.,?/").lower() == "yes" or user_reply.strip("!.,?/").lower() == "sure":
    time.sleep(1)
    print("Okay! Lets go then!")
    time.sleep(1)
    print("Lets go eat BBQ!")
    time.sleep(2)

    user_reply = input("Would you like barbecue sauce with your chicken wings?")
    if user_reply.strip("!.,?/").lower() == "yes" or user_reply.strip("!.,?/").lower() == "sure":
        time.sleep(1)
        print("Here you go")

    elif user_reply.strip("!.,?/").lower() == "no":
         time.sleep(1)
         print("Okay no problem")
         time.sleep(2)
         
    print("I am so full now after eating")
    time.sleep(1)
    def main():
        dollars = dollars_to_float(input("How much was the meal? "))
        time.sleep(1)
        percent = percent_to_float(input("What percentage should we tip? "))
        tip = dollars * percent
        time.sleep(1)
        print(f"We should leave a ${round(tip, 2)} tip")


    def dollars_to_float(d: str):
         return float(d)


    def percent_to_float(p):
         return float(p) / 100 
    


    main()
    time.sleep(1)
    print(f"It was fun hanging out with you! Goodbye {user_name}")


# if user responds no to going out to eat 
elif user_reply.strip("!.,?/").lower() == "no":
     time.sleep(1)
     print("Okay fine")
     time.sleep(1)
     print("I'm still hungry though")
     time.sleep(1)

     user_input = int(input("How many bags of chips do we have?"))

     time.sleep(1)

     user_input2 = int(input("How many bags of chips do you want to eat?"))

     total = (user_input - user_input2)

     if total == 0:
          time.sleep(1)

          print ("What? You're not giving me any?")
          print("I hate you goodbye")

     if total < 10:
          time.sleep(1)
          print ("That's not even enough food for a child, I need more!")
          print("*slams the door and leaves*")

     if total > 10:
           time.sleep(1)
           print ("Okay I will eat all of it, I am so hungry")
           print("Thanks for the food, goodbye!")


# if user responds with anything else to going out to eat 
else:
     time.sleep(1)
     print("What? I dont't understand, please try again")