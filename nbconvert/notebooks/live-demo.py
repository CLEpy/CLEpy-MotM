## ==============================================
##   This file was generated live during MotM
##                from demo.py
## ==============================================

#%% [markdown]
# # This is a notebook
# ## This is also a markdown cell

#%%
# This is a code cell
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#%%
# I'm using this code cell for a setting
# This one's called a "magic." That's neat.
get_ipython().run_line_magic('matplotlib', 'inline')


#%%
# It has its pros and cons
length = 1000
data = [str(x) for x in np.random.randint(5000,size=(length,))]
domain = list(range(length))
n=5
print(f'First {n} values of {len(data)}: {data[:n]}')


#%%
# But here's a plot
plt.xkcd()
plt.figure(figsize=(15,10),facecolor='white')
plt.title('This was random.')
plt.scatter(domain, data)
plt.show()


#%%



