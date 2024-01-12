import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

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
	print(f"shape y = {y.shape}")
	print(y)

	# get x
	a = get_col(data[columns[0]])
	b = get_col(data[columns[1]])
	c = get_col(data[columns[2]])
	
	x = np.hstack((a, b, c, np.ones((a.shape[0], 1))))
	print(f"shape x = {x.shape}")
	print(x)

	# initialise thetas avec des valeurs randoms
	thetas_init = np.random.randn(4, 1)
	print(f"shape thetas_init = {thetas_init.shape}")
	print(thetas_init)
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


def gradient_descent(X, y, theta, learning_rate, n_iterations):
	"""calcule la descente de gradient"""
	for i in range(0, n_iterations):
		theta = theta - learning_rate * grad(X, y, theta)
	return theta


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


def main():
	"""main function of the program"""
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Wrong number of arguments")
		filename = sys.argv[1]
		datas = pd.read_csv(filename)
		selected_colums = ['Astronomy', 'Ancient Runes', 'Herbology']
		x, y, theta = get_datas(datas, selected_colums)
		theta_final = gradient_descent(x, y, theta, 0.01, 1000)
		print(f"shape theta_final = {theta_final.shape}")
		print(theta_final)
		
		# retour aux valeurs sans standardisation
		theta_final = thetas_reel(x, theta_final)
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