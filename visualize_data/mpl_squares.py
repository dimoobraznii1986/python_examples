#!/Users/dmitryanoshin/.pyenv/shims/python

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1,4,9,16,25]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick lables
ax.tick_params(labelsize=14)


plt.show()


#Figure(640x480)


#AxesSubplot(0.125,0.11;0.775x0.77)