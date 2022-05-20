import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9, 12, 15, 20]
heur = [134, 55, 36, 33, 30, 28, 27, 27]
greedy = [161, 74, 49, 45, 38, 36, 35, 34]
greedyPerRoute = [204, 86, 59, 51, 42, 37, 34, 31]


plt.plot(x, heur, label='Int. Prog.')
plt.plot(x,greedy, label='Greedy')
plt.plot(x,greedyPerRoute, label='Greedy Per Route')
plt.xlabel('Miles on Full Charge')
plt.ylabel('Batteries Needed')

plt.legend(loc='upper left')

plt.show()


## EXPONETIAL OR GAUSSIAN FOR BATTERY PRICES
