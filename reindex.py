#%%
import pandas as pd
# %%
data = [['John', 50, 'Austin', 70],
        ['Cataline', 45 , 'San Francisco', 80],
        ['Matt', 30, 'Boston' , 95]]



# %%
idx = ['x', 'y', 'z']
#%%
df = pd.DataFrame(data, index=idx)
# %%
df
