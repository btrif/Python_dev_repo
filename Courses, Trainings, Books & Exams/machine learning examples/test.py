#Number of training samples
from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour

#Plot the data

   #Load the dataset
data = loadtxt('ex1data1.txt', delimiter=',')

X = data[:, 0]
y = data[:, 1]
m = y.size

it = ones(shape=(m, 2))
it[:, 1] = X

theta = zeros(shape=(2, 1))

predictions = it.dot(theta).flatten()

sqErrors = (predictions - y) ** 2

J = (1.0 / (2 * m)) * sqErrors.sum()


def gradient_descent(X, y, theta, alpha, num_iters):
    '''
    Performs gradient descent to learn theta
    by taking num_items gradient steps with learning
    rate alpha
    '''
    m = y.size
    J_history = zeros(shape=(num_iters, 1))

    for i in range(num_iters):

        predictions = X.dot(theta).flatten()

        errors_x1 = (predictions - y) * X[:, 0]
        errors_x2 = (predictions - y) * X[:, 1]

        theta[0][0] = theta[0][0] - alpha * (1.0 / m) * errors_x1.sum()
        theta[1][0] = theta[1][0] - alpha * (1.0 / m) * errors_x2.sum()

        J_history[i, 0] = compute_cost(X, y, theta)

    return theta, J_history
    print("WEEEEEEEEEEEEEL, the number of iterations is:",num_iters)



#Initialize theta parameters
theta = zeros(shape=(2, 1))

#Some gradient descent settings
iterations = 1500
alpha = 0.01

#compute and display initial cost
print ((it, y, theta))


scatter(data[:, 0], data[:, 1], marker='o', c='b')
title('Profits distribution')
xlabel('Population of City in 10,000s')
ylabel('Profit in $10,000s')
#show()