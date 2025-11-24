# Histogram
import matplotlib.pyplot as plt
mu=0
sigma=1
size=1000
 
data=rng.normal(mu,sigma,size)
 
plt.hist(data,bins=30,color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()