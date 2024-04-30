import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
xpoints = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
ypoints = np.array([36836.6, 39731.9, 40609.1, 40706.5, 40115.5, 39320.9, 37772.5, 33689.2, 27099.7, 30626.3, 53265.6, 52759.4])
plt.plot(xpoints, ypoints)

plt.ylabel("Individuals in families with children in Shelters ")
plt.xlabel("Years ")

image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'templates/line2_graph.svg'

fig.savefig(image_name, format=image_format, dpi=1200)