import math
import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt

 # create function
def dydt(y, t):
	return math.exp(y) - math.exp(-y) 

t = np.linspace( 0, 0.5, 20) # vector of time
y0 = 10 # start value
y = odeint (dydt, y0, t) # solve eq.
y = np.array(y).flatten() 
plt.plot( t, y,'-sr', linewidth=3) # graphic
plt.show() # display