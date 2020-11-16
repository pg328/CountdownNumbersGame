# Dictionary of all valid operators.
operators = {
    "+": "+",
    "-": "-",
    # "-2": "-",
    "*": "*",
    "/": "/",
    # "/2": "/"
}

# Dictionary where keys are operators and values
#   are corresponding lambda functions
operationHash = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    # "-2": (lambda a, b: b - a)
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: 0 if b == 0 else a / b),
    # "/2": (lambda a, b: 0 if a == 0 else b / a),
}


def factorial(n):
    if n == 1:
        return 1
    return n*(factorial(n-1))


def progressBar(INDENT, progressFraction, solution):
    print("\n"+INDENT+"Solution: "+solution)

    print(INDENT+" ------------------------------ ")
    print(INDENT+"|"+("|"*int(30*progressFraction)) +
          (" "*(29-int(30*progressFraction)))+"|")
    print(INDENT+" ------------------------------ ")
