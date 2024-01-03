import pandas as pd
import sys


def get_all_columns(data):
	"""return all columns where we have numerical values"""
	data_col = []
	for col in data.columns:
		# print(f"{col} = {data[col].dtype}")
		if data[col].dtype == float:
			data_col.append(col)
	return data_col


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
	print(f"{col}: nb={nb}, mean={mean}, min={min} max={max}")

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