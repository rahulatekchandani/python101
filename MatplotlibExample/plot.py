import matplotlib.pyplot as plt

def straight_graph(x_values,y_values):
    # plotting co-ordinates
    plt.plot(x_values, y_values, c='red', linewidth=3)

    # Set chart titles and label axes
    plt.title("Print straight line graph",fontsize =20)
    plt.xlabel("X axis", fontsize = 10)
    plt.ylabel("Y axis", fontsize = 10)
    plt.tick_params(axis='both')
    plt.show()

def scatter_graph(x_values, y_values):
    # plotting co-ordinates
    plt.scatter(x_values, y_values, c='red', s=50)

    # Set chart titles and label axes
    plt.title("Print scatter line graph", fontsize=20)
    plt.xlabel("X axis", fontsize = 10)
    plt.ylabel("Y axis", fontsize = 10)
    plt.show()

x_values = list(range(1,10))
y_values = [x**2 for x in x_values]
straight_graph(x_values, y_values)
scatter_graph(x_values, y_values)