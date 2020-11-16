""" NUMBERS GAME --  COUNTDOWN """
import os
import solver
from time import sleep
import random


def title_bar():
    # Display a title bar.
    os.system('clear')
    print(("\t"*3)+"***********************************")
    print(("\t"*3)+"***  NUMBERS GAME -- COUNTDOWN  ***")
    print(("\t"*3)+"***********************************\n\n\n")

# Extra padding for formatting


def addWhiteSpace():
    print("\n"*8)

# Displays the 6 chosen numbers in boxes


def display(disp_list):
    whitespace = "\t\t   "
    if len(disp_list) <= 4:
        whitespace += "\t"

    whitespace += " " * \
        (3-len([num for num in disp_list if (num >= 10 and num < 100)]))

    print(whitespace, end='')
    print(" ", end="")
    for i in disp_list:
        if i >= 10 and i < 100:
            if i == disp_list[-1]:
                print("------", end="")
            else:
                print("-------", end="")
        else:
            if i == disp_list[-1]:
                print("-----", end="")
            else:
                print("------", end="")
    print("")
    print(whitespace, end="")
    if disp_list == []:
        print("  ", end="")
    else:
        print("| ", end="")
    for i in disp_list:
        if i < 10:
            buffer = " "
            buffer2 = " "
        elif i < 100:
            buffer = " "
            buffer2 = " "
        else:
            buffer = ""
            buffer2 = ""

        print(buffer+str(i)+buffer2+" |", end=" ")

    print("")
    print(whitespace, end="")
    print(" ", end="")
    for i in disp_list:
        if i >= 10 and i < 100:
            if i == disp_list[-1]:
                print("------", end="")
            else:
                print("-------", end="")
        else:
            if i == disp_list[-1]:
                print("-----", end="")
            else:
                print("------", end="")
    print()


# Whitespace wrapping for the spinner
spinner_container = {
    "beforeSpinner": ("\t"*4)+(" "*4)+("-"*7)+"\n"+("\t"*4)+"   |  ",
    "afterSpinner": ("  |"+"\n")+("\t"*4)+(" "*4)+("-"*7)+"\n"+"\n"*5
}

# Responsible for the slowing random number generator animation


def spinner(num_list, r_num):
    title_bar()
    print(spinner_container["beforeSpinner"]
          + str(r_num) +
          spinner_container["afterSpinner"])
    display(num_list)

# Defines behaviour for when timer runs out


def timeOut(num_list, target, solution_generator):

    has_Quit = input(
        "\n\n\t\t\tEnter to play again, S to solve, \n\tD to find a solution that you missed, or any other key to quit. ").lower()

    if has_Quit == "":
        main()
        return

    if has_Quit == "d":
        answer = ""
        while answer == "":
            answer = next(solution_generator)
        print(answer)
        timeOut(num_list, target, solution_generator)
        return

    if has_Quit == "s":
        solver.main(num_list, target)
        timeOut(num_list, target, solution_generator)
        return

    os.system('clear')


def main():
    title_bar()
    addWhiteSpace()

    # Remove a random item from list A to NUMBERS
    def useList(A):
        NUMBERS.append(
            A.pop(
                A.index(
                    random.choice(A)
                )
            )
        )

    # Creates a list of time intervals for rng animation to use
    TIME_LIST = (0.005*(1.1**(n)) for n in range(45))
    # Creates empty list of time intervals
    TIME_LIST = [0]
    # Sets length of countdown in seconds
    COUNTDOWN_LENGTH = 0
    TARGET_NUM_LIST = list(range(101, 1000))
    LARGE = list(range(25, 100, 25))+[100]
    SMALL = list(range(1, 10))*2
    NUMBERS = []
    ERROR_MESSAGE = ""

    while len(NUMBERS) < 6:

        title_bar()
        addWhiteSpace()
        display(NUMBERS)
        print(ERROR_MESSAGE)
        print("\n"*6)

        choice = input("Large Number or small Number? (l or s) ")

        if choice == "s" or choice == " ":
            try:
                useList(SMALL)
            except IndexError:
                map(lambda _: useList(LARGE), range(2))
            ERROR_MESSAGE = ""

            continue

        if choice == "l":
            try:
                useList(LARGE)
            except IndexError:
                map(lambda _: useList(SMALL), range(2))
            ERROR_MESSAGE = ""

            continue

        if choice == "q":
            os.system("clear")
            return

        ERROR_MESSAGE = "\n Please make a valid choice!\n\n "

    for interval in TIME_LIST:
        target = random.choice(TARGET_NUM_LIST)
        spinner(NUMBERS, target)
        sleep(interval)

    # Displays a timer

    spinner(NUMBERS, target)
    print("\n\nTime Left: 30")

    for secondsPassed in range(COUNTDOWN_LENGTH):
        sleep(1)
        spinner(NUMBERS, target)
        time_left = str(29-secondsPassed)
        if time_left == "0":
            time_left = "---"
        print("\n\nTime Left: "+time_left)

    solution_generator = solver.solver(NUMBERS, target)

    timeOut(NUMBERS, target, solution_generator)


main() if __name__ == "__main__" else print(
    """   Program Written for Terminal Use! Go to your terminal and enter "python3 countdown.py"!       """)
