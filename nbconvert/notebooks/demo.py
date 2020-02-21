#%% [markdown]
# # This *was* a notebook
# ## This is _still_ also a markdown cell

#%%
# This is a code cell
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#%%
get_ipython().run_line_magic('matplotlib', 'inline')


#%%
# It has its pros and cons
length = 1000
data = [str(x) for x in np.random.randint(5000,size=(length,))]
domain = list(range(length))
n=5
print(f'First {n} values of {len(data)}: {data[:n]}')


#%%
plt.xkcd()
plt.figure(figsize=(15,10),facecolor='white')
# plt.style.use('ggplot')
plt.title('This was random.')
plt.scatter(domain, data)
plt.show()


#%%



