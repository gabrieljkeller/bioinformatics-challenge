import matplotlib.pyplot as plt


def plot_amino_acids(counter):
    # First plot: counts
    plt.bar(counter.keys(), counter.values())
    plt.xlabel("Animo Acid")
    plt.ylabel("Frequency")
    plt.title("Amino Acid Frequency")
    plt.xticks(rotation=90)  # doesn't fit otherwise
    plt.subplots_adjust(top=0.93, bottom=0.15, right=0.93)  # (unfortunately) hard-coded values to fit the axis labels
    plt.show()

    # Second plot: relative frequencies (histogram)
    value_sum = sum(counter.values())
    for i in counter.keys():
        counter[i] = counter[i] / value_sum

    plt.bar(counter.keys(), counter.values())
    plt.xlabel("Animo Acid")
    plt.ylabel("Relative Frequency (%)")
    plt.title("Amino Acid % Relative Frequency")
    plt.xticks(rotation=90)
    plt.subplots_adjust(top=0.93, bottom=0.15)
    plt.show()