# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:57:14 2022

@author: Andres Munoz
"""

import math
import time
import numpy as np


class RVGenerator:
    """
        Method to generate random variables from different probability distributions.
    """

    def __init__(self, seed: int = time.time()):
        """
            Class initialization
        """

        self.seed = int(seed) if not type(seed) == int else seed

    def bernoulli(self, p: float = 0.5, seed: int = 0, size: int = 1) -> np.array:
        """ 
            Function to generate a list of pseudo-random variables from a Bernoulli distribution.

        :param p: Probability for success in the experiment.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        U = self.uniform(seed=seed if seed else self.seed, size=size)

        return (U <= p).astype(int)

    def binomial(self, p: float = 0.5, n: int = 50, seed: int = 0, size: int = 1) -> np.array:
        """ 
            Function to generate a list of pseudo-random variables from a binomial distribution.

        :param p: Probability for success in the experiment.
        :param n: Number of independent experiments.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        out = []

        UU = self.uniform(seed=seed if seed else self.seed, size=n*size)

        for m in range(size):

            U = UU[m*n:(m+1)*n]

            out.append(np.sum((U <= p).astype(int)))

        return np.array(out)

    def exponential(self, lambda_: float = 1., seed: int = 0, size: int=1) -> np.array:
        """ 
            Function to generate a list of pseudo-random variables from an exponential distribution.
            This function employs the inverse transform method to generate a random variable from an exponential probability distribution using an uniform random variable.

        :param lambda_: Float indicating the exponential distribution parameter value.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        U = self.uniform(seed=seed if seed else self.seed, size=size)

        return -(1/lambda_)*np.log(1-U)

    def gaussian(self, mu: float = 0., sigma: float = 1., seed_1: int = 0, seed_2: int = 0, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables from a normal/gaussian probability distribution.
            This function employs the Box-Muller transform method to generate the normal random variables from uniform random variables.

        :param mu: Mean of the normal probability distribution from which the pseudo-random variables will be generated.
        :param sigma: Standard deviation of the normal probability distribution from which the pseudo-random variables will be generated.
        :param seed_1: First start value for the LCG, providing deterministic uniform values for specific seed values.
        :param seed_2: Second start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """ 

        U1 = self.uniform(seed=seed_1 if seed_1 else self.seed, size=size)

        U2 = self.uniform(seed=seed_2 if seed_2 else int(self.seed/2*100+1), size=size)

        Z = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)

        return Z*sigma + mu

    def geometric(self, p: float = 0.5, seed: int = 0, size: int = 1) -> np.array:
        """ 
            Function to generate a list of pseudo-random variables from a geometric distribution.

        :param p: Probability for success in the experiment.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        U = self.uniform(seed=seed if seed else self.seed, size=size)

        return np.array([math.ceil(i) for i in np.log(U)/np.log(1-p)])

    @staticmethod
    def lcg(mult: int = 16807, modulus: int = (2**31) - 1, seed: int = 0, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables following a Linear Congruential Generator (LCG).

        :param mult: Multiplier for the LCG.
        :param modulus: Modulus for the LCG.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        # Initializing the output

        U = np.zeros(size)

        # Initial state

        ss = seed if seed else self.seed

        # Calculating the initial pseudo-random value

        X = (ss*mult + 1) % modulus

        # Assigning the initial value to the output

        U[0] = X / modulus

        # Iterating to obtain all the required pseudo-random variables

        for idx in range(1, size, 1):

            # Recalculating the pseudo-random variable

            X = (X*mult + 1) % modulus

            # Assigning to the output

            U[idx] = X / modulus

        return U

    def poisson(self, lambda_: float = 5., size: int = 1) -> np.array:
        """ 
            Function to generate a list of pseudo-random variables from a Poisson distribution.
            This function employs the method by Knuth to generate random Poisson-distributed numbers by employing uniform random variables.

        :param lambda_: Float indicating the expected number of times that an event is expected to happen in a certain interval.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        out = []

        UU = self.uniform(seed=self.seed, size=(int(5*lambda_)+1)*size)

        L = np.exp(-lambda_)

        for m in range(size):

            k, i, P = 0, 0, 1

            U = UU[m*(int(5*lambda_)+1):(m+1)*(int(5*lambda_)+1)]

            while P >= L:

                P = U[i] * P

                k+=1
                i+=1

            out.append(k)

        return np.array(out)

    def set_seed(self, seed: int = 0):
        """
            Function to set the initial state for the pseudo-random uniform number generation.

        :param seed: Initial state.
        """

        if seed and type(seed) == int:

            self.seed = seed

    def uniform(self, minim: float = 0., maxim: float = 1., seed: int = 0, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables from a uniform probability distribution.

        :param minim: Number indicating the minimum value to be extracted from the uniform probability distribution.
        :param maxim: Number indicating the maximum value to be extracted from the uniform probability distribution.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        return minim + (maxim - minim) * self.lcg(seed=seed if seed else self.seed, size=size)

    def weibull(self, lambda_: float = 1., alpha_: float = 1.5, seed: int = 1234, size: int = 1) -> np.array:
        """
            Function to generate a list of pseudo-random variables from a Weibull probability distribution.

        :param lambda_: Value for the scale parameter of the desired Weibull probability distribution.
        :param alpha_: Value for the shape parameter of the desired Weibull probability distribution.
        :param seed: Start value for the LCG, providing deterministic uniform values for specific seed values.
        :param size: Number of pseudo-random variables to be retrieved.
        """

        U = self.uniform(seed=seed if seed else self.seed, size=size)

        return (1/lambda_)*(-np.log(1 - U))**(1/alpha_)
