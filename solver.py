import os
from time import sleep
import countdown
import itertools
from functools import reduce
from Equation import Equation
from utils import operators, operationHash, factorial, progressBar

# Main solver function. Takes two inputs:
# - NUMBERS: Starts as the 6 generated numbers.
# - TARGET: the TARGET number.


def solver(NUMBERS, TARGET, seqSolutions=True):
    NUMBERS = sorted(NUMBERS, reverse=True)

    # 1. Find all possible unordered pairs of the NUMBERS.
    #         For example, with NUMBERS = [6,3,2],
    #        possible pairs are (6,3), (6,2), (3,2),
    #        but (3,6) is not valid as it is the same as (6,3).
    #
    #        For n items, there are (n * (n-1) / 2) pairs.

    # Remove pair so branches don't reuse the numbers
    for pair in itertools.combinations(NUMBERS, 2):
        [NUMBERS.remove(element) for element in pair]

        # 2. Find the output of all operations on each pair.
        #        For example, in (6,3):
        #             6 + 3 -> 9
        #             6 - 3 -> 3
        #             6 * 3 -> 18
        #             6 / 3 -> 2

        for operator in operators:

            # Encode the current equation
            newNumber = Equation(pair[0], operator, pair[1])

            # If current equation produces a valid solution
            # and no permutations of it have been used yet,
            # essentially "return" this equation.
            #
            # NB: yield is used to minimize overall space complexity

            if newNumber == TARGET:
                if newNumber.isUsed() == 1:
                    yield ""
                    continue
                if seqSolutions:
                    yield reduce(lambda x, y: x+", "+y, newNumber.display())

                else:
                    yield f"{newNumber} = {TARGET}"

                continue

            # "Return" the empty string to signal maximal depth reached
            if len(NUMBERS) == 0:
                yield ""
                continue

            # 3. Create branch at each output, replacing the pair
            #   of numbers used with the product of those numbers
            #   using "operator".

            yield from solver(newNumber >> NUMBERS, TARGET)

        # Replace pair as all brances have computed
        for element in pair:
            NUMBERS.append(element)


def main(NUMBERS, TARGET):

    n = len(NUMBERS)

    progress = 0
    solutionsGiven = 0
    SOL_SPACE_SIZE = n*(factorial(n-1)**2)*(2**(n-1))  # See attached PDF

    countdown.spinner(NUMBERS, TARGET)

    INDENT = "\t\t\t"

    with open("solutions.txt", "w") as file:
        solution_generator = solver(NUMBERS, TARGET)

        for solution in solution_generator:
            progress += 1

            if solution != "":

                if solutionsGiven <= 100:
                    file.write(solution+"\n")
                    solutionsGiven += 1
                progressFractional = progress/SOL_SPACE_SIZE

                countdown.spinner(NUMBERS, TARGET)
                progressBar(INDENT, progressFractional, solution)
        #   Uncomment line below to see number of operations that ran.
        #   This number is exactly equal to the solution
        #   space calculated!
        # file.write(str(progress))

    with open("solutions.txt", "r") as file:

        solutions = file.readlines()

        if solutions == []:
            print("This problem is impossible!")
            return

        [print(line) for line in solutions[:100]]


if __name__ == "__main__":
    NUMBERS = [50, 3, 1, 25, 9, 7]
    TARGET = 871
    solutions = solver(NUMBERS, TARGET)
    for solution in solutions:
        if solution != "":
            print(solution)
