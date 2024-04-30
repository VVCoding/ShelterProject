import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
xpoints = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
ypoints = np.array([9950.7, 10585.9, 12092.1, 13148.8, 14087.6, 15471.1, 16426.6, 17592.3, 17267.2, 17519.9, 21224.1, 20860.2])
plt.plot(xpoints, ypoints)

plt.ylabel("Single Adults in Shelters ")
plt.xlabel("Years ")

image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'templates/line1_graph.svg'

fig.savefig(image_name, format=image_format, dpi=1200)