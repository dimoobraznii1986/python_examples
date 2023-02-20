import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the point in the walk.
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15,9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    # Remove the axis
    ax.get_xaxaxis().set_visible(False)
    ax.get_yaxaxis().set_visible(False)

    keep_running = input("Make another walk? (y,n):")
    if keep_running == 'n':
        break