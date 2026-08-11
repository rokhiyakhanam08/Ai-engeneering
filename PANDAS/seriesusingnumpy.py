import numpy as np
import pandas as pd

ser = pd.Series(np.linspace(1, 10, 5))#linspace() is used for creating evenly spaced numbers over a specified rnage 
ser = pd.Series(np.random.randn(5))#randn() is used for creating random numbers from a standard normal distribution
print(ser)
