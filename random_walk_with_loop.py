import matplotlib.pyplot as plt

from Random_walk import RandomWalk

#Make a random walk as long as the user wants
while True:

    rw = RandomWalk(60_000)
    rw.fill_walk()

    #Plot the walk pattern
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(16,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Oranges,
               edgecolor='none', s=1)

    # Enphasizing the first an last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)

    #turning off the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


    #Asks the user if he wants to do another plot
    valid = input('Want to make another walk? (y/n) ')

    if valid == 'n':
        break

    else:
        pass