# AutoGuesser 0.2
# by Hugh Cowley
# https://github.com/hughcowley
#
# This program selects a random number N between 0 and 100
# then guesses a number x between 0 and 100
# if x is [higher/lower] than N, make a new guess [lower/higher] than x
# repeat until x = N
# return the number of guesses needed to reach x = N
# repeat 1000 times and return average number of guesses needed

from random import randint

def one_guess():
    """
    Pick random number N between 0 and 100
    Pick another random number x between 0 and 100
    Evaluate whether x is [equal to/greater than/less than] N
    If x != N, make a new guess between x and N
    Return number of guesses needed for x == N
    """
    # initialise parameters
    N = randint(1, 100)
    x = randint(1, 100)
    g = 1

    # loop until correct guess
    while x != N:
        if x > N:
            g += 1
            x = randint(N, x)
        else:
            g+= 1
            x = randint(x, N)

    # return number of guesses
    return g


def main():
    """
    Run one_guess function 1000 times and return average number of guesses needed
    """
    gs = []
    for y in range(1000):
        g = one_guess()
        gs.append(g)

    avg = sum(gs) / 1000

    print(f"On average: {avg:.5f} guesses taken.")

    input("Press the Enter key to exit.")

if __name__ == '__main__':
    main()
