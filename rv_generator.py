# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:57:14 2022

@author: Andres Munoz
"""

import numpy as np


class RVGenerator:
    """
        Method to generate random variables from different probability distributions.
    """

    def __init__(self):
        """
            Class initialization
        """

        pass

    def exponential(self, lambda_: float = 1., seed: int = 1234, size: int=1) -> np.array:
        """ 
            Function to generate a list of pseudo-random variables from an exponential distribution.
            This function employs the inverse transform method to generate a random variable from an exponential probability distribution using an uniform random variable.

        :param lambda_: Float indicating the exponential distribution parameter value.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        # Retrieving a set of pseudo-random variable from a uniform distribution

        U = self.uniform(seed=seed, size=size)

        # Computing a set of random variables from an exponential probability distribution using the inverse transform method

        return -(1/lambda_)*np.log(1-U)

    def gaussian(self, mu: float = 0., sigma: float = 1., seed_1: int = 1234, seed_2: int = 5678, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables from a normal/gaussian probability distribution.
            This function employs the Box-Muller transform method to generate the normal random variables from uniform random variables.

        :param mu: Mean of the normal probability distribution from which the pseudo-random variables will be generated.
        :param sigma: Standard deviation of the normal probability distribution from which the pseudo-random variables will be generated.
        :param seed_1: First start value for the LCG, providing deterministic uniform values for specific seed values.
        :param seed_2: Second start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """ 

        # Retrieving two pseudo-random variable from a uniform distribution

        U1 = self.uniform(seed=seed_1, size=size)

        U2 = self.uniform(seed=seed_2, size=size)

        # Calculating the pseudo-random variable from a normal distribution using the uniform pseudo-random variable

        Z = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)

        # Adjusting the calculated value to the provided statistical moments of the normal probability distribution

        return Z*sigma + mu

    @staticmethod
    def lcg(mult: int = 16807, modulus: int = (2**31) - 1, seed: int = 1234, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables following a Linear Congruential Generator (LCG).

        :param mult: Multiplier for the LCG.
        :param modulus: Modulus for the LCG.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        # Initializing the output

        U = np.zeros(size)

        # Calculating the initial pseudo-random value

        X = (seed*mult + 1) % modulus

        # Assigning the initial value to the output

        U[0] = X / modulus

        # Iterating to obtain all the required pseudo-random variables

        for idx in range(1, size, 1):

            # Recalculating the pseudo-random variable

            X = (X*mult + 1) % modulus

            # Assigning to the output

            U[idx] = X / modulus

        return U

    def uniform(self, minim: float = 0., maxim: float = 1., seed: int = 1234, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables from a uniform probability distribution.

        :param minim: Number indicating the minimum value to be extracted from the uniform probability distribution.
        :param maxim: Number indicating the maximum value to be extracted from the uniform probability distribution.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        return minim + (maxim - minim) * self.lcg(
            seed=seed,
            size=size
        )

    def weibull(self, lambda_: float = 1., k: float = 1.5, seed: int = 1234, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables from a Weibull probability distribution.

        :param lambda_: Value for the scale parameter of the desired Weibull probability distribution.
        :param beta: Value for the shape parameter of the desired Weibull probability distribution.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """
        
        # Retrieving a set of pseudo-random variable from a uniform distribution

        U = self.uniform(seed=seed, size=size)

        # Computing a set of random variables from a Weibull probability distribution using the inverse transform method

        return (1/lambda_)*(-np.log(1 - U))**(1/k)
