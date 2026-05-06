import matplotlib.pyplot as plt

def isolation_forest_plot(labels = "lonely", estimates = [0.5], lower_ci = [0.2], upper_ci = [0.8], title="Isolation Forest"):
    fig, ax = plt.subplots()

    # Compute error bars
    xerr = [
        [estimates[i] - lower_ci[i] for i in range(len(estimates))],
        [upper_ci[i] - estimates[i] for i in range(len(estimates))]
    ]

    # Plot
    ax.errorbar(estimates, labels, xerr=xerr, fmt='o')

    # Reference line
    ax.axvline(x=0, linestyle='--')

    # Labels and title
    ax.set_title(title)
    ax.set_xlabel("Effect Size")

    plt.show()


isolation_forest_plot()