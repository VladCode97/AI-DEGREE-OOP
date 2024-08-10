import random

def estimate_pi(num_simulations):
    inside_circle = 0

    for _ in range(num_simulations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_simulations) * 4

num_simulations = 1000000
pi_estimate = estimate_pi(num_simulations)
print(f"Estimated value of π: {pi_estimate}")
