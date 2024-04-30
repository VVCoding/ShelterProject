import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
xpoints = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
ypoints = np.array([10504.2, 11335.2, 11884.8, 12610.5, 12687.8, 12572.9, 12167.3, 10833.6, 8866.4, 9855.2, 16302.5, 16184.7])
plt.plot(xpoints, ypoints)

plt.ylabel("Families with Children in Shelter ")
plt.xlabel("Years ")

image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'templates/line3_graph.svg'

fig.savefig(image_name, format=image_format, dpi=1200)