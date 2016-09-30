import numpy as np
import matplotlib.pyplot as plt

base_price = 400000
price_range= 100000
cost       = np.linspace(0,50000,1000)

price = base_price + price_range - np.sqrt(2*price_range*cost)

plt.plot(cost,price)
plt.show()
