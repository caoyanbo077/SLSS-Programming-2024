# Text/Emoji Replacer
# Author: Jimmy Cao
# 26 February 2024

# def translate(text: str):
#     text = text.replace("100", "💯").replace("noodles", "🍜")
#     return text

# def main():
#     user_input = input()
#     print(translate(user_input.strip().lower()))
# main()


# Tip Calc
# Author: Jimmy Cao 
# 


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")


def dollars_to_float(d: str):
    # Converts string dollars to a decimal float
    #    Returns the result
    return float(d)


def percent_to_float(p):
    # Converts percent to a decimal float
    #    Returns the result
    return float(p) / 100 


main()