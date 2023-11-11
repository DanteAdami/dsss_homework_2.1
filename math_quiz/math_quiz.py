import random


def function_random_integer(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_random_sign():
    """
    Select a random sign operation between sum, difference and multiplication
    """
    return random.choice(['+', '-', '*'])


def function_operation(value1, value2, sign):
    """
    Return the operation that is being performed as an expression together, and the result of the 
    expression. 
    """
    expression = f"{value1} {sign} {value2}" #Create the expression putting together the three eleemnts
    
    if sign == '+': #check the sign and perform the according operation
        result = value1 + value2
    elif sign == '-': 
        result = value1 - value2
    else: 
        result = value1 * value2

    return expression, result

def math_quiz():
    """
    Perform a little game. The system will generate some random operations, and the user has to guess the
    result. The game is repeated the number of times of the variable repeats. If the user fails the question, 
    the correct answer is shown. At the end of the game the final result of the user is shown. 
    """

    points = 0 # initialize the points of the user at 0
    repeats = 3 # set the number of iterations of the game

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(repeats):
        
        # Creating the operations by randomly selecting two integers and one sign
        n1 = function_random_integer(1, 10); 
        n2 = function_random_integer(1, 5); 
        o = function_random_sign()

        # get the expression and the result and show the expression to the user
        PROBLEM, ANSWER = function_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        # get the input from the user with their guess. We make sure that the input is an integer
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break # if integer, we break the while loop
            except ValueError:
                # if not integer, we remember to the user the requirement and wait for a new input
                print("Invalid input! The input has to be an integer. Please enter a valid integer.")


        # if the user guesses the correct answer, then they get a point and a message is shown.
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += 1
        else:
            # if the user is wrong, the correct answer is shown
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # at the end of the game, we show the final result. 
    print(f"\nGame over! Your score is: {points}/{repeats}")

if __name__ == "__main__":
    math_quiz()
