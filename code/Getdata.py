# Get a EMG data and plot
# %% 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# %% 
subject = "h0"
session = "0"
position = "p0"
repeat = "r0"
movements = ["eversion","fist","open_hand","pinch_forefinger","pinch_middlefinger","two","varus"]

path = "./../" + subject + "/" + session + "/"
emgFileName = "emg_" + position + "_" + repeat + "_" + movements[0] + ".csv"

data = pd.read_csv(path + emgFileName)

# %%
plt.plot(data)