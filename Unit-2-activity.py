# Unit 2 activity
# Jimmy Cao
# 04/08/24
# By inputing your grades this semester, this function can find your semester's average percentage and make a comment about your letter grade
def find_average_marks(marks):
    sum_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_marks / total_subjects
    return average_marks
def calculate_grade(average_marks):
    if average_marks >= 100:
        grade = 'UNpossible, how did you get over 100%?'
    elif average_marks >= 86:
        grade = ' Your average letter grade is A, as in average.'
    elif average_marks >= 73:
        grade = 'Your average letter grade is B. So close yet so far...'
    elif average_marks >= 50:
        grade = 'Your average letter grade is C. Work harder brotha.'
    else:
        grade = 'Your average letter grade is a skill issue. Please call 911 you need help.'
    return grade

marks = []

# Ask the user to put in marks
# Repeat forever

print("Hello 👋! I can help you calculate your average percentage and letter grade! Just enter your marks one at a time. When you're finished, please press enter.")
counter = 1

while True:
    # Ask the user to put in their mark
    user_input = input(f"Mark {counter}: ")

    # If mark is nothing, break
    if user_input == "":
        break
    else:
        # Get their input
        # Add that input to the marks list
        marks.append(int(user_input))
    
    counter += 1

average_marks = find_average_marks(marks)
print("Your average percentage is:", average_marks)
grade = calculate_grade(average_marks)
print(grade)