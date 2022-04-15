# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:57:14 2022

@author: Andres Munoz
"""

import os
from TheArtist import TheArtist
from rv_generator import RVGenerator


def main():
    """
        Creating graphic examples of the sampled distributions that can be created with the sample random variables.
    """

    # Setting the number of random variables to be retrieved for each example -- change as desired

    n_rv = 10000000

    # Setting the seed for the random number generation -- change as desired

    seed = 12345678
    seed_1 = 87654321

    # Set the path where the output graphics will be saved to -- change as needed

    path_out = "figs"

    # Initiating the required class

    rvg = RVGenerator()

    ## Uniform distribution

    figure = TheArtist(latex=False, n_rows = 1, n_cols = 1)

    figure.plot_hist(rvg.uniform(size=n_rv, seed=seed), 100, 0, 0, color='dodgerblue', edgecolor='black')
    figure.savefig(fname=os.path.join("%s" % path_out, "uniform"))

    ## Normal distribution

    figure = TheArtist(latex=False, n_rows = 1, n_cols = 1)

    figure.plot_hist(rvg.gaussian(size=n_rv, seed_1=seed, seed_2=seed_1), 100, 0, 0, color='dodgerblue', edgecolor='black')
    figure.savefig(fname=os.path.join("%s" % path_out, "normal"))

    ## Exponential distribution

    figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    figure.plot_hist(rvg.exponential(seed=seed, size=n_rv), 50, 0, 0, color='dodgerblue', edgecolor='black')
    figure.savefig(fname=os.path.join("%s" % path_out, "exponential"))

    ## Weibull distribution

    figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    figure.plot_hist(rvg.weibull(seed=seed, size=n_rv), 100, 0, 0, color='dodgerblue', edgecolor='black')
    figure.savefig(fname=os.path.join("%s" % path_out, "weibull"))

    return


if __name__ == "__main__":

    # Main execution logic

    main()