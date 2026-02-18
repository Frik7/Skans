from skans.core.rng import RandomNumberGenerator, SimpleRng
import numpy as np


def geometric_brownian_motion(
    S0: float,
    mu: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    rng: RandomNumberGenerator | None = SimpleRng,
) -> np.ndarray:
    """
    Geometric Brownian Motion Simulator.

    Parameters
    ----------
    S0 : float
        Initial level.
    mu : float
        Drift rate.
    sigma : float
        Volatility.
    T : float
        Time horizon.
    n_steps : int
        Number of steps.
    n_paths : int
        Number of paths.
    rng : RandomNumberGenerator | None
        Random number generator.

    Returns
    -------
    np.ndarray
        Simulated paths.
    """
    dt = T / n_steps

    paths = S0 * np.exp(
        (mu - 0.5 * sigma**2) * dt + sigma * rng.generate(n_paths, n_steps) * dt**0.5
    )

    return np.hstack((S0, paths))
