"""-
This exercise tests out the default values of parameters. Create a program which has a main function and a
sub-function called tester. The main function prompts user for an input "Write something (quit ends): " and sends
this input to the sub-function as a parameter.
Define the sub-function tester so that it has one parameter called "givenstring", which has the default value "Too
-short". If the user input is less than 10 characters, the program uses the default value and if 10 or more,
it prints the user-given input. If the user inputs "quit", the program is terminated. When working correctly,
the program will print out something like this:
"""

def main():
    while True:
        user_input = input("Write something (quit ends): ").lower()
        if user_input == "quit":
            break
        print(tester(user_input))


def tester(givenstring="Too short"):
    if len(givenstring) < 10:
        return "Too short"
    return givenstring


main()
