from utils import operators, operationHash

# Define class Equation such that it can interact with
#   numbers. In this way, objects of this class can be
#   added to the original numbers list and used as if
#   they were native ints.


class Equation:
    usedEquations = {}

    def __init__(self, arg1, operator, arg2):
        self.argList = sorted([arg1, arg2])
        self.operator = operator
        self.id = hash(str(self))
        self.output = operationHash[self.operator](
            self.argList[0], self.argList[1])

    def isUsed(self):
        if self.id in Equation.usedEquations:
            return 1

        Equation.usedEquations[self.id] = self.output
        return 0

    def __str__(self):
        output1 = str(round(self.argList[0], 2)) if isinstance(
            self.argList[0], float) else str(self.argList[0])
        output2 = round(self.argList[1], 2) if isinstance(
            self.argList[1], float) else str(self.argList[1])

        return f"({output1}{operators[self.operator]}{output2})"

    def __eq__(self, target):

        if isinstance(target, int):
            return self.output == target

    def __rshift__(self, inputList):
        return inputList+[self]

    def __add__(self, other):
        if isinstance(other, int):
            return self.output+other

        return self.output+other.output

    def __radd__(self, other):
        if isinstance(other, int):
            return other+self.output

        return other.output+self.output

    def __sub__(self, other):
        if isinstance(other, int):
            return self.output-other

        return self.output-other.output

    def __rsub__(self, other):
        if isinstance(other, int):
            return other-self.output

        return other.output-self.output

    def __mul__(self, other):
        if isinstance(other, int):
            return self.output*other

        return self.output*other.output

    def __rmul__(self, other):
        if isinstance(other, int):
            return other*self.output

        return other.output*self.output

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.output/other

        return self.output/other.output

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return other/self.output

        return other.output/self.output

    def __lt__(self, other):
        if isinstance(other, int):
            return self.output < other

        return self.output < other.output

    def __gt__(self, other):
        if isinstance(other, int):
            return self.output > other

        return self.output > other.output
