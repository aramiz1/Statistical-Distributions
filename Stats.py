# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:57:12 2017


@author: Areeb Ramiz

This is a program I decided to make after completing a mathematical statistics
class at my university. It calculates some of the most common discrete and
continuous distributions as well as providing information about their
mean and variance. My hope is that it can help anyone who needs to calculate
the distributions save a little time and not have to worry about punching in
a large amount of data into a calculator correctly.
"""

# import modules
import Continuous
import Discrete

# Display welcome message, display appropriate menu based on user input
def start():

    startSelection = int(input("\nWelcome! This is a math program " +
                               " that calculates some basic statistical distributions." +
                               "\nPress 1 to see discrete distributions: " +
                               "\nPress 2 to see continuous distributions:\n"))
    if startSelection == 1:
        doDiscrete()
    else:
        if startSelection == 2:
            doContinuous()

# If the user wants to calculate discrete distributions
def doDiscrete():

    # User inputs a number to access the desired distribution method.
    discreteSelection = int(input("\nDiscrete Distributions:" +
                                  "\nPress 1 to calculate a uniform discrete distribution: " +
                                  "\nPress 2 to calculate a discrete distribution: " +
                                  "\nPress 3 to calculate a Bernoulli distribution: " +
                                  "\nPress 4 to calculate a Binomial distribution:" +
                                  "\nPress 5 to calculate a Negative Binomial distribution:" +
                                  "\nPress 6 to calculate a Geometric distribution:" +
                                  "\nPress 7 to calculate a Poisson distribution:" +
                                  "\nPress 8 to go back to the home screen:\n"))

    # Go to appropriate method in the Discrete module based on input for the
    # for the user calculate their distribution.
    if discreteSelection == 1:
        Discrete.uniformDiscrete()
    else:
        if discreteSelection == 2:
            Discrete.regularDiscrete()
        if discreteSelection == 3:
            Discrete.bernoulliDiscrete()
        if discreteSelection == 4:
            Discrete.binomialDiscrete()
        if discreteSelection == 5:
            Discrete.negBinomialDiscrete()
        if discreteSelection == 6:
            Discrete.geometricDiscrete()
        if discreteSelection == 7:
            Discrete.poissonDiscrete()
        if discreteSelection == 8:
            start()

# If the user wants to calculate continuous distributions
def doContinuous():

    # The Continous.message() function tells the user about how to input
    # infinity, as well as decimal they must follow when using the program
    # to work correctly.
    Continuous.message()

    continuousSelection = int(input("\nContinuous Distributions:" +
                                    "\nPress 1 to calculate a uniform continuous distribution: " +
                                    "\nPress 2 to calculate a Exponential distribution: " +
                                    "\nPress 3 to calculate a Gamma distribution:" +
                                    "\nPress 4 to calculate a Beta distribution:" +
                                    "\nPress 5 to calculate a Normal distribution:" +
                                    "\nPress 6 to go back to the home screen:\n"))

    # Go to appropriate method in the Continuous module based on input for the
    # for the user calculate their distribution.
    if continuousSelection == 1:
        Continuous.uniformContinuous()
    else:
        if continuousSelection == 2:
            Continuous.exponentialContinuous()
        if continuousSelection == 3:
            Continuous.gammaContinuous()
        if continuousSelection == 4:
            Continuous.betaContinuous()
        if continuousSelection == 5:
            Continuous.normalContinuous()
        if continuousSelection == 6:
            start()
            
        

# Made a main method to start the program off
if __name__ == "__main__":
    start()
