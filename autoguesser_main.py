# AutoGuesser 0.1
# by Hugh Cowley
# https://github.com/hughcowley
#
# This program selects a random number N between 0 and 100
# then guesses a number x between 0 and 100
# if x is [higher/lower] than N, make a new guess [lower/higher] than x
# repeat until x = N
# return the number of guesses needed to reach x = N

from random import randint

def main():
    """Main program function"""

    # initialise parameters
    N = randint(1, 100)
    x = randint(1, 100)
    g = 1

    while x != N:
        if x > N:
            g += 1
            x = randint(N, x)
        else:
            g+= 1
            x = randint(x, N)

    print(f"{g} guesses taken.")

    input("Press the Enter key to exit.")

if __name__ == '__main__':
    main()
