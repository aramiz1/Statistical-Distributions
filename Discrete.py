# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:36:31 2017

@author: Areeb Ramiz

This is the discrete module for the program. Calculates all the discrete
distributions and displays them to the user.
"""

# import functions
import parser
import math
import fractions
from multiprocessing.connection import FAILURE

# Calculate a discrete distribution
def regularDiscrete():
    
    # Gives a disclaimer to the user. Unfortunately, it was exceedingly
    # complicated to make this program able to calculate formulas with
    # +- operands because the eval() function has strange behavior
    # with them which gives incorrect answers due to them being taken
    # as a String from the input() function.
    print("NOTE: This particular function only accepts non-polynomial " +
          "formulas such as '3/4 * x^3'.")
    
    # Get the formula from the user
    formula = (input("What is the formula? (Only use x as a variable)"))

    # If the formula contains the exponential symbol, make it python compatible
    if "^" in formula:
        formula = formula.replace("^", "**")

    # Conver the string formula the user inputted into an evaluable formula
    code = parser.expr(formula).compile()

    # Get the value of variable of the formula from the user, input it into the
    # equation to calculate the probability at one element value
    getX = (input("What is the value of x? (Find the probability of one single desired element). "))
    x = float(getX)
    probability = (eval(code))

    # Get how many elements are present in the equation from the user, make
    # variables to get ready to  calculate the properties of the distribution.
    elements = int(input("How many elements are there? "))
    mean = 0
    variance = 0
    inputList = []
    elementList = []

    # Use a loop to get each element from the user
    for z in range(0, elements):

        # Get elements from user
        meanLoopInput = (input("What is element " + str(z + 1) + "? "))

        # If a fraction is enetered, convert it to a decimal
        toFloat = float(fractions.Fraction(meanLoopInput))

        # Assign the user input to x because the formula they entered requires
        # them to use x as their variable. Evaluate the formula based on input,
        # summate the mean and add it to an array for use when calculating the
        # variance
        x = toFloat
        p = (eval(code))
        elementList.append(float(meanLoopInput))
        inputList.append(p)

    # Calculate the mean
    for m in range(0, elements):
        x = elementList[m]
        ans = eval(code)
        mean = mean + (elementList[m] * ans)

    # Use a for loop to summate the variance based on the array created and
    #  that stores the value of each user input evaluated at the
    # formula they entered initially
    for y in range(0, elements):
        variance = variance + ((inputList[y] - mean)**2)

    # Calculate the variance and standard deviation.
    variance = variance * (1 / elements)
    stanDev = math.sqrt(variance)

    # Print properties
    print("\nProbability: " + str(probability))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Calculate a uniform discrete distribution
def uniformDiscrete():
    coefficient = input("What is f(x)? ")
    toDecimal = float(fractions.Fraction(coefficient))

    # Get how many elements are present in the equation from the user, make
    # variables to get ready to  calculate the properties of the distribution.
    elements = int(input("How many elements are there? "))
    mean = 0
    variance = 0
    elementList = []

    # Use a loop to get each element from the user and calculate the mean
    for z in range(0, elements):

        # Get elements from user
        meanLoopInput = (input("What is element " + str(z + 1) + "? "))

        # If a fraction is enetered, convert it to a decimal
        toFloat = float(fractions.Fraction(meanLoopInput))

        # Summate the mean, add each user inputted element to an array to
        # use later to calculate the variance.
        mean = mean + (toFloat * toDecimal)
        elementList.append(float(meanLoopInput))
        
    # Use a loop to calculate the variance 
    for v in range(0,elements):
        variance = variance + (((elementList[v] - mean)**2) * toDecimal)
    
    # Print properties
    print("\nExpected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(math.sqrt(variance)))
    
# Calculate a bernoulli distribution
def bernoulliDiscrete():

    # Get input from user
    probability = (input("What is the probability of success? "))

    # Bernoulli distribution has a very simple property where the sum of the
    # success and failure equals 1.
    failure = 1 - float(probability)

    # Find and calculate the mean, variance and standard deviation.
    mean = float(probability)
    variance = mean * failure
    stanDev = math.sqrt(variance)

    # Print properties
    print("\nProbability of failure: " + str(failure))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Calculate a binomial distribution
def binomialDiscrete():

    # Get inputs on number of trials done, probability of success per trial,
    # and the number of desired successful trials from the user.
    trials = input("How many trials were done? ")
    probabilityForOne = input("What is the probability of success per trial? ")
    trialSuccess = input("How many successful trials are desired? ")

    # Split the formula for calculating the probability into three parts,
    # find each part individually then multiply them all together to find the
    # exact decimal.
    combos = getCombination(int(trialSuccess), int(trials))
    successPower = float(probabilityForOne)**int(trialSuccess)
    failurePower = (1 - float(probabilityForOne)
                    )**(int(trials) - int(trialSuccess))
    probabilityForAll = combos * successPower * failurePower

    # Find and calculate the mean, variance and standard deviation.
    mean = int(trials) * float(probabilityForOne)
    variance = (mean) * (1 - float(probabilityForOne))
    stanDev = math.sqrt(variance)

    # Print properties
    print("\nProbability: " + str(probabilityForAll))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Calculate a negative binomial distribution
def negBinomialDiscrete():

    # Get the probability of success per trial, number of successes desired,
    # and trial number of a certain success from the user
    probabilityForOne = input("What is the probability of success per trial? ")
    numSuccesses = input("How many successes do you want to observe? ")
    trialNumber = input("On which trial do you hope to " +
                        " observe success #" + str(numSuccesses) + "?")

    # Split the formula for calculating the probability of a negative binomial
    # distribution into smaller parts them combine them together to find the
    # final answer
    combos = getCombination(int(numSuccesses) - 1, int(trialNumber) - 1)

    successPower = float(probabilityForOne)**int(numSuccesses)

    failurePower = (1 - float(probabilityForOne)
                    )**(int(trialNumber) - int(numSuccesses))

    probabilityForAll = combos * successPower * failurePower

    # Find and calculate the mean, variance and standard deviation.
    mean = int(numSuccesses) / float(probabilityForOne)

    variance = (int(numSuccesses) * (1 - float(probabilityForOne))
                ) / (float(probabilityForOne)**2)

    stanDev = math.sqrt(variance)

    # Print properties
    print("\nProbability: " + str(probabilityForAll))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Calculate a geometric distribution
def geometricDiscrete():

    # Get the probability of success per trial, expected trial number of first
    # success from the user
    probSuccess = input("What is the probability of success per trial? ")
    trialNumber = input(
        "On which trial do you expect the first success to occur? ")

    # Calculate the probabiltiy using the geometric distribution formula based
    # on the user inputs
    probability = float(probSuccess) * \
        ((1 - float(probSuccess))**(int(trialNumber) - 1))

    # Calculate the mean, variance and standard deviation.
    mean = 1 / float(probSuccess)

    variance = (1 - float(probSuccess)) / ((float(probSuccess))**2)
    stanDev = math.sqrt(variance)

    # Also calculating the probablity mass function of this distribution
    # because it is commonly used and asked for in most problems relating to
    # the geometric distribution
    probSummation = 0

    # Loop to summate the total probability mass function of the distribution
    for x in range(1, int(trialNumber)):
        probSummation = probSummation + (1 - float(probSuccess)) * \
            ((float(probSuccess))**(int(x) - 1))

    # Print properties
    print("\nProbability of first success occurring on trial #" +
          str(trialNumber) + ": " + str(probability))
    print("Probability at least " + str(int(trialNumber) - 1) +
          " trials occurring before the first success: " + str(probSummation))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Calculate a poisson distribution
def poissonDiscrete():

    # Get the value of lambda, number of successes expected from the user.
    getLambda = input("What is the value of lambda? ")
    successes = input("How many successes are expected to occur? ")

    # Get factorial of #successes
    getFact = fact(int(successes))

    # Calculate the probability
    ExactProb = math.exp(-1 * float(getLambda)) * \
        (float(getLambda)**int(successes)) / getFact

    # Also calculating the probablity mass function of this distribution
    # because it is commonly used and asked for in most problems relating to
    # the poisson distribution
    probSummation = 0

    for x in range(0, int(successes) + 1):
        probSummation = probSummation + math.exp(-1 * float(getLambda)) * \
            (float(getLambda)**int(x)) / getFact

    # Calculate standard deviation (no calculations are required for the mean
    # and variance for this particular distribution).
    stanDev = math.sqrt(float(getLambda))

    # Print properties
    print("\nProbability of exactly " + str(successes) +
          "  successes: " + str(ExactProb))
    print("Probability of at least " + str(successes) +
          " successes occurring: " + str(probSummation))
    print("Expected Value: " + str(getLambda))
    print("Variance: " + str(getLambda))
    print("Standard Deviation: " + str(stanDev))

# Calculate the combinatinon of two numbers
def getCombination(r, n):

    nMinusR = n - r
    n = fact(n)
    r = fact(r)
    denominatorSubtraction = fact(nMinusR)

    result = n / (r * denominatorSubtraction)
    return result

# Calculate the factorial of a number
def fact(f):

    if(f == 0):
        return 1

    result = 1
    for a in range(f, 1, -1):
        result = result * a

    return result
