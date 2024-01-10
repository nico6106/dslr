import pandas as pd
import matplotlib.pyplot as plt
import sys
import math


def get_all_columns(data):
	"""return all columns where we have numerical values"""
	data_col = []
	for col in data.columns:
		# print(f"{col} = {data[col].dtype}")
		if data[col].dtype == float:
			data_col.append(col)
	return data_col


def plot_all_hists(datas, all_columns, houses):
	"""plat all histograms to see the bests"""
	nb_col = 5
	nb_row = math.trunc(len(all_columns) / nb_col) + 1
	fig, axes = plt.subplots(nrows=nb_row, ncols=nb_col)
	i = 0
	j = 0

	for col in all_columns:
		for house in houses:
			data = datas[datas['Hogwarts House'] == house]
			data[col].hist(ax=axes[i, j])
			axes[i, j].set_title(f'{col}')
		j = j + 1
		if j == nb_col:
			j = 0
			i = i + 1
	plt.subplots_adjust(top=0.95, bottom=0.05)
	plt.show()


def plot_one_hists(datas, col, houses):
	"""plot only one histogram"""

	for house in houses:
		data = datas[datas['Hogwarts House'] == house]
		plt.hist(data[col])
		plt.title(f'{col}')
		plt.legend(houses, loc='upper right');

	plt.show()


def main():
	"""main function of the program"""
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Wrong number of arguments")
		filename = sys.argv[1]
		datas = pd.read_csv(filename)
		all_columns = get_all_columns(datas)
		houses = ['Hufflepuff', 'Ravenclaw', 'Gryffindor', 'Slytherin']
		plot_all_hists(datas, all_columns, houses)
		plot_one_hists(datas, 'Care of Magical Creatures', houses)
		
	except AssertionError as error:
		print(f"{AssertionError.__name__}: {error}")
	except FileNotFoundError as error:
		print(f"FileNotFoundError: {error}")
	except Exception as error:
		print(f"Error: {error}")
	return


if __name__ == "__main__":
	main()
