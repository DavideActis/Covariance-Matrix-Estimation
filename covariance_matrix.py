#!/usr/bin/env python3
"""
Covariance Matrix Estimation for Portfolio Risk Analysis

This script simulates multivariate normal asset returns under two different
covariance structures and compares the estimated sample covariance matrices
with the true covariance matrices.

The project illustrates the role of covariance estimation in portfolio risk
measurement, diversification analysis and asset allocation.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


N_OBSERVATIONS = 1000
RANDOM_SEED = 123


def simulate_multivariate_returns(covariance_matrix, n_observations=N_OBSERVATIONS):
    """
    Simulate multivariate normal returns with zero mean.

    Parameters
    ----------
    covariance_matrix : np.ndarray
        True covariance matrix used to generate the data.
    n_observations : int
        Number of simulated observations.

    Returns
    -------
    np.ndarray
        Simulated return matrix with shape (n_observations, n_assets).
    """
    mean_vector = np.zeros(covariance_matrix.shape[0])

    return np.random.multivariate_normal(
        mean=mean_vector,
        cov=covariance_matrix,
        size=n_observations
    )


def estimate_covariance_matrix(returns):
    """
    Estimate the sample covariance matrix from asset returns.
    """
    return np.cov(returns, rowvar=False, bias=False)


def estimate_correlation_matrix(returns):
    """
    Estimate the sample correlation matrix from asset returns.
    """
    return np.corrcoef(returns, rowvar=False)


def estimate_mean_vector(returns):
    """
    Estimate the sample mean vector from asset returns.
    """
    return returns.mean(axis=0)


def plot_heatmap(matrix, title):
    """
    Plot a heatmap of a covariance or correlation matrix.
    """
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        matrix,
        annot=True,
        fmt=".3f",
        cmap="Blues",
        square=True,
        cbar=True
    )
    plt.title(title)
    plt.tight_layout()
    plt.show()


def report_results(name, true_covariance, returns):
    """
    Print summary statistics and compare estimated and true covariance matrices.
    """
    estimated_mean = estimate_mean_vector(returns)
    estimated_covariance = estimate_covariance_matrix(returns)
    estimated_correlation = estimate_correlation_matrix(returns)
    estimation_error = estimated_covariance - true_covariance

    print("\n" + "=" * 70)
    print(f"Results for {name}")
    print("=" * 70)

    print(f"\nShape of simulated returns: {returns.shape}")

    print("\nEstimated mean vector:")
    print(np.round(estimated_mean, 4))

    print("\nEstimated covariance matrix:")
    print(np.round(estimated_covariance, 4))

    print("\nTrue covariance matrix:")
    print(true_covariance)

    print("\nEstimation error:")
    print(np.round(estimation_error, 4))

    print("\nEstimated correlation matrix:")
    print(np.round(estimated_correlation, 4))

    plot_heatmap(
        estimated_covariance,
        f"{name} - Estimated Covariance Matrix"
    )

    plot_heatmap(
        estimated_correlation,
        f"{name} - Estimated Correlation Matrix"
    )


def main():
    """
    Run the covariance matrix estimation experiment.
    """
    np.random.seed(RANDOM_SEED)

    covariance_matrix_1 = np.array([
        [1.0, 0.5, 0.5],
        [0.5, 1.0, 0.5],
        [0.5, 0.5, 1.0]
    ])

    covariance_matrix_2 = np.array([
        [1.0, 0.5, 0.25],
        [0.5, 1.0, 0.5],
        [0.25, 0.5, 1.0]
    ])

    returns_1 = simulate_multivariate_returns(covariance_matrix_1)
    returns_2 = simulate_multivariate_returns(covariance_matrix_2)

    report_results("Covariance Structure 1", covariance_matrix_1, returns_1)
    report_results("Covariance Structure 2", covariance_matrix_2, returns_2)


if __name__ == "__main__":
    main()