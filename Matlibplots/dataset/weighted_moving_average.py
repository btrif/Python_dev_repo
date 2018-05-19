#  Created by Bogdan Trif on 05-02-2018 , 11:25 AM.
import numpy as np
import matplotlib.pyplot as plt

#first generate some datapoint for a randomly sampled noisy sinewave
x = np.random.random(1000)*10
noise = np.random.normal(scale=0.3,size=len(x))
y = np.sin(x) + noise

#plot the data
plt.plot(x,y,'ro',alpha=0.3,ms=4,label='data')
plt.xlabel('Time')
plt.ylabel('Intensity')

def weighted_moving_average(x,y,step_size=0.05,width=1):
    bin_centers  = np.arange(np.min(x),np.max(x)-0.5*step_size,step_size)+0.5*step_size
    bin_avg = np.zeros(len(bin_centers))

    #We're going to weight with a Gaussian function
    def gaussian(x,amp=1,mean=0,sigma=1):
        return amp*np.exp(-(x-mean)**2/(2*sigma**2))

    for index in range(0,len(bin_centers)):
        bin_center = bin_centers[index]
        weights = gaussian(x,mean=bin_center,sigma=width)
        bin_avg[index] = np.average(y,weights=weights)

    return (bin_centers,bin_avg)

#plot the moving average
bins, average = weighted_moving_average(x,y)
plt.plot(bins, average,label='moving average')

plt.grid(which='both')
plt.show()