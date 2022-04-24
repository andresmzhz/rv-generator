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

    seed = 12345

    # Set the path where the output graphics will be saved to -- change as needed

    path_out = "figs"

    # Initiating the required class

    rvg = RVGenerator(seed=seed)

    # Uniform distribution

    # figure = TheArtist(latex=False, n_rows = 1, n_cols = 1)

    # figure.plot_hist(rvg.uniform(size=n_rv), 100, 0, 0, color='black', edgecolor='black')
    # figure.savefig(fname=os.path.join(path_out, "uniform"), fig_format='png')

    # Normal distribution

    figure = TheArtist(latex=False, n_rows = 1, n_cols = 1)

    figure.plot_hist(rvg.gaussian(mu=5, sigma=10, size=n_rv), 1000, 0, 0, color='black', edgecolor='black')
    figure.savefig(fname=os.path.join(path_out, "normal"), fig_format='png')

    # Exponential distribution

    # figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    # figure.plot_hist(rvg.exponential(size=n_rv), 100, 0, 0, color='black', edgecolor='black')
    # figure.savefig(fname=os.path.join(path_out, "exponential"), fig_format='png')

    # Weibull distribution

    figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    figure.plot_hist(rvg.weibull(lambda_=1, alpha_=2, size=n_rv), 100, 0, 0, color='black', edgecolor='black')
    figure.savefig(fname=os.path.join(path_out, "weibull"), fig_format='png')

    ## Poisson distribution

    # figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    # figure.plot_hist(rvg.poisson(size=n_rv), 100, 0, 0, color='black', edgecolor='black')
    # figure.savefig(fname=os.path.join(path_out, "poisson"), fig_format='png')

    # # Binomial distribution

    # figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    # figure.plot_hist(rvg.binomial(size=n_rv), 100, 0, 0, color='black', edgecolor='black')
    # figure.savefig(fname=os.path.join(path_out, "binomial"), fig_format='png')

    # # Geometric distribution

    # figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    # figure.plot_hist(rvg.geometric(size=n_rv), 50, 0, 0, color='black', edgecolor='black')
    # figure.savefig(fname=os.path.join(path_out, "geometric"), fig_format='png')

    # # Bernoulli distribution

    # figure = TheArtist(latex=False, n_rows=1, n_cols=1)

    # figure.plot_hist(rvg.bernoulli(size=n_rv), 100, 0, 0, color='black', edgecolor='black')
    # figure.savefig(fname=os.path.join(path_out, "bernoulli"), fig_format='png')

    return


if __name__ == "__main__":

    # Main execution logic

    main()