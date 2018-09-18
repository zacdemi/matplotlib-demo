import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [111,100,81,62,80,84,73,103,93]

fig, ax = plt.subplots()

ax.plot(x,y)

plt.show()

# ------unpacking----------
# >>> plt.subplots()
# (<Figure size 640x480 with 1 Axes>, <matplotlib.axes._subplots.AxesSubplot object at 0x117fcc2e8>)

# >>> a, b = (1,2)
# >>> a 
# 1
# >>> b 
# 2
