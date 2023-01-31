import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def T(G):
    return 1/G + p_values[0]*G

p_values = [0.25, 0.20, 0.15, 0.10, 0.05, 0.03, 0.01, 0.005, 0.001, 0.0005, 0.0001]
p_val = 0
g_values = []

while p_values:      
    res = optimize.minimize(T, p_val, method='Nelder-Mead', tol=1e-6)
    g_values.append(res.x[0])
    p_values.pop(0)

p_values = [0.25, 0.20, 0.15, 0.10, 0.05, 0.03, 0.01, 0.005, 0.001, 0.0005, 0.0001]

df = pd.DataFrame({"x": p_values, "y": g_values})
print(df)

plt.scatter(p_values, g_values)
plt.title('Log-Log re-expression to linearize data')

plt.xlabel('ln(probability of testing positive)', color='#1C2833')
plt.ylabel('ln(Best group size)', color='#1C2833')

plt.yscale('log')
plt.xscale('log')



plt.show()





# print(p_values)
# print(g_values)