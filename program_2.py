# Author: Michael Beaudet
# Title: Week 5 Program 2
# Date: 2/17/25

import random 

def math_quiz():
    # Get the random numbers
    num1 = random.randint(1, 300)
    num2 = random.randint(1, 300)
    # Add the two numbers and get the user input
    correct_answer = num1 + num2
    user_answer = int(input(f" {num1}\n+{num2}\n----\n"))
    # Display results
    if user_answer == correct_answer:
        print("Congratulations! You are correct")
    else:
        print(f"You are incorrect, the correct answer is {correct_answer}")

math_quiz() 