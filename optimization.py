import numpy as np
from scipy.optimize import minimize

def run_optimization(coeffs, total_budget, bounds, initial_guess):
    """
    coeffs: dict  {"tv_spend": 0.02, "search_spend": 0.08, ...}
    total_budget:  35000
    bounds: لیست تاپل مثل [(5000,20000), (3000,12000), ...]
    initial_guess: 
    """
    channels = list(coeffs.keys())
    coef_arr = np.array([coeffs[ch] for ch in channels])

    # maximize sales -> minimize -sales
    def objective(x):
        return -(coef_arr @ x)

    constraints = ({
        "type": "eq",
        "fun": lambda x: np.sum(x) - total_budget
    })

    result = minimize(
        objective,
        x0=np.array(initial_guess),
        bounds=bounds,
        constraints=constraints
    )

    return channels, result.x, result
