import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
from tqdm import tqdm
from time import time
from typing import Any


def time_decorator(func):
    """compute performance in s"""
    def inner(*args: Any, **kwds: Any):
        """inner function of perf function"""
        """eliminate args"""
        init = time()
        result = func(*args)
        end = time()
        total = end - init
        print(f"==>Function {func.__name__} took : {total}s")
        return result
    return inner


def get_col(data):
	a = np.array(data)
	a = a.reshape(a.shape[0], 1)

	f_min = min(data)
	f_max = max(data)
	for i in range(0, len(a)):
		a[i] = (a[i] - f_min) / (f_max - f_min)

	a = np.nan_to_num(a, nan=0.5)
	return a

def get_datas(data, columns):
	"""get datas in forms of matrices"""
	# get y
	houses = ['Hufflepuff', 'Ravenclaw', 'Gryffindor', 'Slytherin']
	houses_students = list(data['Hogwarts House'])
	for i in range(0, len(houses_students)):
		if houses_students[i] == 'Hufflepuff':
			houses_students[i] = 0
		elif houses_students[i] == 'Ravenclaw':
			houses_students[i] = 1
		elif houses_students[i] == 'Gryffindor':
			houses_students[i] = 2
		elif houses_students[i] == 'Slytherin':
			houses_students[i] = 3
	# print(houses_students)
	y = np.array(houses_students)
	y = y.reshape(y.shape[0], 1)
	# print(f"shape y = {y.shape}")
	# print(y)

	# get x
	a = get_col(data[columns[0]])
	b = get_col(data[columns[1]])
	# c = get_col(data[columns[2]])
	
	x = np.hstack((a, b, np.ones((a.shape[0], 1))))
	# print(f"shape x = {x.shape}")
	# print(x)

	# initialise thetas avec des valeurs randoms
	# thetas_init = np.random.randn(4, 1)
	thetas_init = np.array([0, 0, 0])
	thetas_init = thetas_init.reshape(thetas_init.shape[0], 1)
	# print(f"shape thetas_init = {thetas_init.shape}")
	# print(thetas_init)
	return x, y, thetas_init


def model(X, theta):
	"""modele lineaire"""
	return X.dot(theta)


def cost_function(X, y, theta):
	"""fonction cout"""
	m = len(y)
	return 1/(2 * m) * np.sum((model(X, theta) - y) ** 2)


def grad(X, y, theta):
	"""calcul le gradient"""
	m = len(y)
	return 1 / m * X.T.dot(model(X, theta) - y)


# @time_decorator
def gradient_descent(X, y, theta, learning_rate, n_iterations):
	"""calcule la descente de gradient"""
	cost_history = np.zeros(n_iterations)

	for i in tqdm(range(0, n_iterations)):
		theta = theta - learning_rate * grad(X, y, theta)
		cost_history[i] = cost_function(X, y, theta) 
		# if (i % 500 == 0):
		# 	print(f"here {i} : theta={theta}")
	return theta, cost_history


def train_all(data, columns):
	"""train model"""


def theta_reel_one(data, theta):
	"""do the job for one theta"""
	f_min = data.min()
	f_max = data.max()
	theta = theta * (f_max - f_min) + f_min
	return theta


def thetas_reel(x, thetas):
	"""return the thetas without standardisation"""
	thetas[0] = theta_reel_one(x[0], thetas[0])
	thetas[1] = theta_reel_one(x[1], thetas[1])
	thetas[2] = theta_reel_one(x[2], thetas[2])
	return thetas


@time_decorator
def main():
	"""main function of the program"""
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Wrong number of arguments")
		filename = sys.argv[1]
		datas = pd.read_csv(filename)
		selected_colums = ['Astronomy', 'Ancient Runes'] #Herbology
		x, y, theta = get_datas(datas, selected_colums)
		theta_final = np.array([])
		print(x)
		y_tmp = y.flatten()

		y_show = np.array([])
		cost_history = np.array([])
		# print(y_tmp)

		
		# theta_final = theta_final.reshape(4, 4)

		nb_iter = 4000

		for i in range(0, 4):
			y_train = np.where(y == i, 1, 0)
			# print(y_train)
			theta_train, cost_tmp = gradient_descent(x, y_train, theta, 0.01, nb_iter)
			# print(theta_train)
			theta_train = theta_train.T
			cost_tmp = cost_tmp.reshape(cost_tmp.shape[0], 1)
			# cost_tmp = cost_tmp.T
			# print(cost_history)
			# print(f"shape cost_tmp = {cost_tmp.shape}")
			# print(theta_train)
			
			if theta_final.size == 0:
				theta_final = theta_train
				y_show = y_train
				cost_history = cost_tmp
			else:
				theta_final = np.vstack([theta_final, theta_train])
				y_show = np.hstack([y_show, y_train])
				cost_history = np.hstack([cost_history, cost_tmp])
			# print(f"shape theta_final = {theta_final.shape}")
			# print(theta_final)
		# print(f"shape theta_final = {theta_final.shape}")
		print(theta_final)

		fig, axes = plt.subplots(nrows=4, ncols=2)
		# print(y_show)
		row = 0
		axes[0,0].scatter(x[:,0], x[:,1], c=y_show[:,row])
		axes[0,0].plot([x / 1000 for x in range(0,1000)], [theta_final[row][0] * ((x/1000)*(x/1000)) + theta_final[row][1] * x/1000 + theta_final[row][2] for x in range(0,1000)])

		row = 1
		axes[0,1].scatter(x[:,0], x[:,1], c=y_show[:,row])
		axes[0,1].plot([x / 1000 for x in range(0,1000)], [theta_final[row][0] * ((x/1000)*(x/1000)) + theta_final[row][1] * x/1000 + theta_final[row][2] for x in range(0,1000)])

		row = 2
		axes[1,0].scatter(x[:,0], x[:,1], c=y_show[:,row])
		axes[1,0].plot([x / 1000 for x in range(0,1000)], [theta_final[row][0] * ((x/1000)*(x/1000)) + theta_final[row][1] * x/1000 + theta_final[row][2] for x in range(0,1000)])

		row = 3
		axes[1,1].scatter(x[:,0], x[:,1], c=y_show[:,row])
		axes[1,1].plot([x / 1000 for x in range(0,1000)], [theta_final[row][0] * ((x/1000)*(x/1000)) + theta_final[row][1] * x/1000 + theta_final[row][2] for x in range(0,1000)])

		print(f"cost history: shape={cost_history.shape}")
		axes[2,0].plot(list(range(0,nb_iter)), cost_history[:,0])
		axes[2,1].plot(list(range(0,nb_iter)), cost_history[:,1])
		axes[3,0].plot(list(range(0,nb_iter)), cost_history[:,2])
		axes[3,1].plot(list(range(0,nb_iter)), cost_history[:,3])
		plt.show()
		
		# retour aux valeurs sans standardisation
		theta_final = thetas_reel(x, theta_final)
		print(f"real thetas")
		print(theta_final)
		
	except AssertionError as error:
		print(f"{AssertionError.__name__}: {error}")
	except FileNotFoundError as error:
		print(f"FileNotFoundError: {error}")
	except Exception as error:
		print(f"Error: {error}")
	return


if __name__ == "__main__":
	main()