# Generate a random sample from binomial distribution for custom size

 
import numpy as np
from math import comb
 
rng=np.random.default_rng()
 
def binomial_random_sample(n,p,size):
    def pmf(k):
       return comb(n,k)*(p**k)*((1-p)**(n-k))
    def cdf(k):
       return sum(pmf(j) for j in range(k+1))
   
    U=rng.uniform(0,1,size)
    generated_sample=[]
    for u in U:
     k=0
     while u>cdf(k):
       k=k+1
     generated_sample.append(k)
    return generated_sample
n=10
p=0.3
size=10
generated_sample=binomial_random_sample(n,p,size)
print(f"Generated sample from the binomial distribution {generated_sample}") 