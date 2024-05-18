import numpy as np
from scipy.stats import poisson 
import matplotlib.pyplot as plt
 

K = eval(input("Input the number of occurence:"))
u = eval(input ("Input the mean:"))

v = np.arange(0, u)

S=poisson.pmf(k=K, mu=u)

plt.bar(v, S, alpha=0.5, align='center')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.title('Poisson Distribution (lambda={})'.format(K))
plt.show()