""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression


def display_digits():
    digits = load_digits()
    print(digits.DESCR)
    fig = plt.figure()
    for i in range(10):
        subplot = fig.add_subplot(5, 2, i+1)
        subplot.matshow(np.reshape(digits.data[i], (8, 8)), cmap='gray')

    plt.show()


def train_model():
    data = load_digits()
    num_trials = 100
    train_percentages = range(5, 95, 5)
    test_accuracies = np.zeros(len(train_percentages))


    for i in range(len(train_percentages)):
        accuracy_of_trials = []

        for j in range(num_trials):
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
            train_size=train_percentages[i]*.01)
            model = LogisticRegression(C=10**-10)
            model.fit(X_train, y_train)

            accuracy_of_trials.append(model.score(X_train, y_train) * 100)

        average_accuracy = np.average(accuracy_of_trials)
        print(str(train_percentages[i]) + ": " + str(average_accuracy))
        test_accuracies[i] = average_accuracy

    fig = plt.figure()
    plt.plot(train_percentages, test_accuracies)
    plt.xlabel('Percentage of Data Used for Training')
    plt.ylabel('Accuracy on Test Set')
    plt.show()


if __name__ == "__main__":
    # display_digits()
    train_model()
