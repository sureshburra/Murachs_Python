import numpy as np
 
# Create a random number generator instance
rng = np.random.default_rng()
 
def geometric_random_sample(p, size):
    # PMF of Geometric Distribution: P(X=k) = (1-p)^(k-1) * p
    def pmf(k):
        return (1 - p)**(k - 1) * p
 
    # CDF of Geometric Distribution: F(k) = 1 - (1-p)^k
    def cdf(k):
        return 1 - (1 - p)**k
 
    # Generate 'size' uniform random numbers between 0 and 1
    U = rng.uniform(0, 1, size)
 
    generated_sample = []
    for u in U:
        k = 1
        # Find smallest k such that u <= F(k)
        while u > cdf(k):
            k += 1
        generated_sample.append(k)
 
    return generated_sample
 
# Parameters for geometric distribution
p = 0.3
size = 10
 
# Generate sample
generated_sample = geometric_random_sample(p, size)
print(f"Generated sample from the geometric distribution: {generated_sample}")