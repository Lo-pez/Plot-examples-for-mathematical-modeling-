import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3]
plt.rcParams["figure.autolayout"] = True

def T(p):
   return -(p*p) + 3*p + 1

def t(p):
   return -2*p*p + 4*p + 1

x = np.linspace(0, 1, 100)

# x axis goes from min() to max() + 1, in this case 0 to 3+1 in 0.1 intervals
plt.xticks(np.arange(0, 4, 0.1))

plt.plot(x, T(x), color='red', label='T=1+3p-p^2')
plt.plot(x, t(x), color='blue', linestyle='dashed', label='t=1+4p-2p^2')
plt.axhline(y=2, color='green', linestyle='dashed')

plt.title('Graph of t(p)-T(p)')
plt.legend(loc='upper left')

plt.xlabel('p', color='#1C2833')
plt.ylabel('# of tests', color='#1C2833')

x = 0.382
y = 2

plt.plot(x, y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")


plt.show()
