# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:05:05 2017

@author: Areeb Ramiz

This is the continuous module for the program. Calculates all the continuous
distributions and displays them to the user.
"""
# import functions
import math
import fractions
from scipy.integrate import quad
import scipy

# Message instructing the user on how to properly input their formulas or range
def message():

    print("If you need to use infinity for any bounds, please type " +
        "'inf' or '-inf'. Also please convert all fractions to decimal form.")


# Calculate a uniform continous distribution
def uniformContinuous():

    # Get the range calculated to/from for the integral.
    a = input("What is the value of a? ")
    b = input("What is the value of b? ")

    # If an entered range is infinity, adjusts the ranges value
    # for integration to its mathematical function.
    if(b == "inf"):
        b = math.inf
    else:
        if(a == "-inf"):
            a = -math.inf

    # Calculate the coefficent, integral from the inputted range and
    # multiply them together to find the final answer.
    coefficient = 1/(float(b) - float(a))
    ans, err = quad(returnUniformContinuousFormula, float(a), float(b))
    ans = ans * coefficient

    # Calculate the mean, variance and standard deviation.
    mean = (float(a) + float(b))/2
    variance = ((float(a) + float(b))**2)/12
    stanDev = math.sqrt(variance)

    # Print properties
    print("Probability: " + str(ans))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Return the uniform continuous formula to integrate.
def returnUniformContinuousFormula(x):

    return x

### Separate the continuous method from the exponential methods ###

# Global variable that must be stored to build the formula in the
# returnExponentialFormula function.
exponentialCoeff = 0

# Calculate an exponential distribution.
def exponentialContinuous():

    # Get the mean, lower and upper time bound from the user.
    mean = input("What is the mean? ")
    getLowTime = input("What is the lower time bound? ")
    getUpTime = input("What is the upper time bound? ")

    # Set the values of a,b, which is what the formula will be integrated
    # to/from. They are being separately declared in the case that one of the
    # entered bounds above is infinity to preserve their original values.
    a = float(getLowTime)
    b = float(getUpTime)

    # If an entered range is infinity, adjusts the ranges value
    # for integration to its mathematical function.
    if(getUpTime == "inf"):
        b = math.inf
    else:
        if(getLowTime == "-inf"):
            a = -math.inf

    # Calculate the coefficient, assign it to a global variable in order for
    # it to be used to build the returnExponentialFormula method
    # that will be returned and integrated to this method
    # to find the probability between a and b.

    coefficient = 1/float(mean)
    global exponentialCoeff
    exponentialCoeff = coefficient

    # Calculate the variance and standard deviation
    variance = 1/(float(mean)**2)
    stanDev = math.sqrt(variance)

    # Calculate the probability
    ans, err = quad(returnExponentialFormula, float(a), float(b))

    # Print properties
    print("Probability: " + str(ans))
    print("Expected Value: " + str(coefficient))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Build and return the exponential formula that will be integrated
# to calculate the probability.
def returnExponentialFormula(x):
    return exponentialCoeff*math.e**(-1*exponentialCoeff*x)

### Separate the exponential methods from the gamma methods ###

# Global variables that must be stored to build the formula in the
# returnGammaFormula function.
passA = 0
passB = 0

def gammaContinuous():

    # Get what is being integrated to/from,
    # what is the maximum bound and minimum bound from the user.
    a = input("What is a? ")
    B = input("What is B? ")
    getLowerBound = input("What is the lower bound? ")
    getUpperBound = input("What is the upper bound? ")

    lowerBound = getLowerBound
    upperBound = getUpperBound

    # If an entered range is infinity, adjusts the ranges value
    # for integration to its mathematical function.
    if(getUpperBound == "inf"):
        upperBound = math.inf
    else:
        if(getLowerBound == "-inf"):
            lowerBound = -math.inf

    # Raise B*a to build the coefficient.
    BtoA = float(B)**float(a)

    # Certain values of the gamma symbol function (also used in beta distributions)
    # in statistics have special properties. This if-else
    # statement checks if those numbers are present
    # and if so updates their value accordingly.
    gamma = 0

    if(a == ".5"):
        gamma = math.sqrt(math.pi)
    else:
        if(a == "1"):
            gamma = 1
        gamma = fact(int(a)-1)

    # Assign a,b to global variables in order for them to be accessable to
    # build the gamma formula in the returnGammaFormula method
    # that will be returned and integrated to this method
    # to find the probability between a and b.
    global passA
    global passB
    passA = float(a)-1
    passB = B

    # Find the coefficient
    coefficient = BtoA/gamma

    # Integrate to calculate the probability, multiply it by the coefficient
    ans, err = quad(returnGammaFormula, float(lowerBound), float(upperBound))
    ans = ans * coefficient

    # Calculate the mean, variance and standard deviation.
    mean = float(a)/float(B)
    variance = float(a)/(float(B)**2)
    stanDev = math.sqrt(variance)

    # Print properties
    print("Probability: " + str(ans))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Certain values of the gamma symbol function in statistics
# have special properties. This method checks if those numbers are present and
# if so updates their value accordingly.
def returnGammaFormula(x):

    aToFloat = float(passA)
    bToFloat = float(passB)

    return (x**aToFloat)*math.e**(-1*bToFloat*x)

### Separate the exponential methods from the gamma methods ###

# Global variable that must be stored to build the formula in the
# returnBetaFormula function. It is confusing to have 'gamma' in thier
# names when it is being used for the beta dstribution but the actual
# function ((a number - 1)!) uses the gamma symbol to denote it.
passGammaA = 0
passGammaB = 0

def betaContinuous():

    a = input("What is a? ")
    B = input("What is B? ")
    getLowerBound = input("What is the lower bound? ")
    getUpperBound = input("What is the upper bound? ")

    lowerBound = getLowerBound
    upperBound = getUpperBound

    # If an entered range is infinity, adjusts the ranges value
    # for integration to its mathematical function.
    if(getUpperBound == "inf"):
        upperBound = math.inf
    else:
        if(getLowerBound == "-inf"):
            lowerBound = -math.inf

    # Certain values of the gamma symbol function
    # (also used in beta distributions) in statistics have special properties.
    # This checks if those numbers are present and if so
    # updates their value accordingly.
    Agamma = checkBetaInput(int(a)-1)
    Bgamma = checkBetaInput(int(B)-1)

    # Calculate the gammas of a, B, a + B and use them
    # to build the coefficient.
    Agamma = fact(int(a)-1)
    Bgamma = fact(int(B)-1)

    toSumGamma = (int(a)+int(B))-1

    sumGamma = checkBetaInput(toSumGamma)
    sumGamma = fact(toSumGamma)

    coefficient = 1 / ((Agamma*Bgamma)/sumGamma)

    # Assign a,b to global variables in order for them to be accessable to
    # build the gamma formula in the returnBetaFormula method
    # that will be returned and integrated to this method
    # to find the probability between a and b. Subtract 1 here so it slightly
    # simplifies the expression when the formula is being built.
    global passGammaA
    global passGammaB
    passGammaA = float(a)-1
    passGammaB = float(B)-1

    # Integrate to calculate the probability, multiply it by the coefficient
    ans, err = quad(returnBetaFormula, float(lowerBound), float(upperBound))
    ans = ans * coefficient

    # Calculate the mean, variance and standard deviation. Assign a,B as floats
    # to variables to simplify the expressions.
    aFloat = float(a)
    bFloat = float(B)

    mean = aFloat / (aFloat + bFloat)
    variance = (aFloat*bFloat)/(((aFloat+bFloat)**2) * (aFloat+bFloat+1))
    stanDev = math.sqrt(variance)

    # Print properties
    print("Probability: " + str(ans))
    print("Expected Value: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(stanDev))

# Certain values of the gamma symbol function (also used in beta distributions)
# in statistics have special properties. This method checks if those numbers
# are present and if so updates their value accordingly.
def checkBetaInput(num):

        if(num == ".5"):
            num = math.sqrt(math.pi)
            return num
        else:
            if(num == "1"):
                num = 1
                return num

        return num + 1

# Return the beta formula for the quad function from scipy to use and integrate
def returnBetaFormula(x):

    return (x**passGammaA)*((1-x)**passGammaB)

# Calculate a normal distribution
def normalContinuous():

    # Get the mean, standard deviation and sample size from the user
    mean = input("What is the mean? ")
    sigma = input("What is sigma? (Standard Deviation) ")
    size = input("What is the sample size? ")

    # Calculate and print the range using the scipy function for normal
    # distributions.
    ans = scipy.random.normal(float(mean), float(sigma), int(size))
    print(ans)

# Calculate the combination of two numbers
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
