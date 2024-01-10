import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys
import math

def get_all_columns(data):
	"""return all columns where we have numerical values"""
	data_col = []
	for col in data.columns:
		if data[col].dtype == float:
			data_col.append(col)
	return data_col


def pair_plot(datas, all_columns, houses):
	"""pair plot"""
	data = pd.DataFrame()
	# extract infos
	data['Hogwarts House'] = datas['Hogwarts House']
	for col in all_columns:
		# if col == 'Defense Against the Dark Arts': # same as arithmancy
		# 	na = 'na'
		# else:
		data[col] = datas[col]
	# print(data)
	sns.pairplot(data, hue = 'Hogwarts House', diag_kind="hist")
	sns.set(style="ticks", color_codes=True)
	plt.subplots_adjust(top=0.99, bottom=0.05, left=0.07)
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
		pair_plot(datas, all_columns, houses)
	except AssertionError as error:
		print(f"{AssertionError.__name__}: {error}")
	except FileNotFoundError as error:
		print(f"FileNotFoundError: {error}")
	except Exception as error:
		print(f"Error: {error}")
	return


if __name__ == "__main__":
	main()
