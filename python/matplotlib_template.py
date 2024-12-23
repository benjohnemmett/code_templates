from matplotlib import pyplot as plt

def plot(x_data, y_data, title="Title"):
    plt.plot(x_data, y_data, linestyle="-", marker=".", color="green", label="Some Data")
    plt.xlabel("X Data")
    plt.ylabel("Y Data")
    plt.title(title)
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.show()

if __name__ == "__main__":
    N = 100
    X = [x for x in range(N)]
    Y = [abs(x - 50) for x in X]

    print(f"Plotting {N} points")
    plot(X, Y)