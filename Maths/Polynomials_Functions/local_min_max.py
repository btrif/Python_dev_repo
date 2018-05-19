#  Created by Bogdan Trif on 11-02-2018 , 8:14 PM.
import numpy as np
import matplotlib.pyplot as plt


n_samples = 30
Y = np.random.rand(n_samples)
print(Y)


def find_local_min_max(dataset):
    min_and_max = np.diff(np.sign(np.diff(dataset))).nonzero()[0] + 1 # local min+max

    minimum = (np.diff(np.sign(np.diff(dataset))) > 0).nonzero()[0] + 1 # local min
    maximum = (np.diff(np.sign(np.diff(dataset))) < 0).nonzero()[0] + 1 # local max
    print('\nmin & max : ', min_and_max)
    print('min : ', minimum)
    print('max : ', maximum)
    return minimum, maximum



def plotSamples(dataset):
    fig = plt.figure(1, figsize=(10,3))
    ax = plt.subplot(111)
    t = np.arange(len(dataset))

    Min, Max = find_local_min_max(dataset)

    # graphical output...


    plt.plot(t[Min], dataset[Min], "yo", label="min")
    plt.plot(t[Max], dataset[Max], "ko", label="max")

    plt.plot(t, dataset, "c-.")
    plt.legend()
    plt.grid(which ='both')
    plt.show()




plotSamples(Y)
find_local_min_max(Y)