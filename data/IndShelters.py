import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
xpoints = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
ypoints = np.array([28841.4, 30972.1, 33575.7, 35577, 36741.7, 37726.2, 38002.2, 36782.2, 32537, 34804.9, 52264.4, 51343])
plt.plot(xpoints, ypoints)

plt.ylabel("Individuals in Shelters ")
plt.xlabel("Years ")

image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'templates/line_graph.svg'

fig.savefig(image_name, format=image_format, dpi=1200)