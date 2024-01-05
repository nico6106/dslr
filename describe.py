import pandas as pd
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


def compute_std(data, mean, n):
	"""compute std of data"""
	std = 0
	sum = 0
	for elem in data:
		if elem == elem:
			tmp = (elem - mean)
			sum = sum + tmp ** 2
	if n == 0: raise AssertionError("Cannot have only 1 data to compute std")
	std = math.sqrt((sum) / (n - 1))
	# print(f"std={std}, stdPD={data.std()}")
	return std


def get_info_col(info, data, col):
	"""get info for the column"""
	nb = 0
	sum = 0
	max = data[col][0]
	min = data[col][0]
	for elem in data[col]:
		if elem == elem:
			nb = nb + 1
			sum = sum + elem
			if elem > max:
				max = elem
			if elem < min:
				min = elem
	mean = sum / nb
	std = compute_std(data[col], mean, nb)
	print(f"{col}: nb={nb}, mean={mean}, min={min} max={max}, std={std}")

	return info

def main():
	"""main function of the program"""
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Wrong number of arguments")
		filename = sys.argv[1]
		print(f"args= {filename}")
		datas = pd.read_csv(filename)
		print(datas)
		col = get_all_columns(datas)
		print(col)
		info = []
		for elem in col:
			info = get_info_col(info, datas, elem)
	except AssertionError as error:
		print(f"{AssertionError.__name__}: {error}")
	except FileNotFoundError as error:
		print(f"FileNotFoundError: {error}")
	except Exception as error:
		print(f"Error: {error}")
	return


if __name__ == "__main__":
	main()