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


def compute_sub_quartile(data, p, t):
	"""return the value representing the quartile"""
	if t == 0.25:
		v = (data[math.trunc(p)] * 3 + data[math.trunc(p) + 1] * 1) / (4)
	elif t == 0.50:
		v = (data[math.trunc(p)] + data[math.trunc(p) + 1]) / (2)
	elif t == 0.75:
		v = (data[math.trunc(p)] * 1 + data[math.trunc(p) + 1] * 3) / (4)
	elif t == 0:
		v = data[math.trunc(p)]
	# print(f"data[{math.trunc(p)}]={data[math.trunc(p)]} - data[{math.trunc(p) + 1}]={data[math.trunc(p) + 1]}")
	return v

def compute_quartiles(data, n):
	"""compute quartiles of data"""
	quartile = []
	# print(data)
	sorted_data = data.copy()
	sorted_data.sort_values(ascending=True, inplace=True)
	sorted_list = sorted_data.tolist()
	p = (n + 3) / 4
	t = p - math.trunc(p)
	# print(f"1 n={n} => p={p} t={t}")
	v = compute_sub_quartile(sorted_list, math.trunc(p) -1, t)
	quartile.append(v)
	
	# 2nd quartile (50) 
	p = (n + 1) / 2
	t = p - math.trunc(p)
	# print(f"2 n={n} => p={p} t={t}")
	v = compute_sub_quartile(sorted_list, math.trunc(p) -1, t)
	quartile.append(v)

	# 3rd quartile (75)
	p = (3 * n + 1) / 4
	t = p - math.trunc(p)
	# print(f"3 n={n} => p={p} t={t}")
	v = compute_sub_quartile(sorted_list, math.trunc(p) -1, t)
	quartile.append(v)

	return quartile


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
	quartile = compute_quartiles(data[col], nb)
	# print(f"{col}: nb={nb}, mean={mean}, min={min} max={max}, std={std}, quartiles={quartile}")
	info = [nb, mean, std, min, quartile[0], quartile[1], quartile[2], max]

	return info

def main():
	"""main function of the program"""
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Wrong number of arguments")
		filename = sys.argv[1]
		# print(f"args= {filename}")
		datas = pd.read_csv(filename)
		# print(datas)
		col = get_all_columns(datas)
		# print(col)
		info = {'': ['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']}
		info = pd.DataFrame(info)
		for elem in col:
			tmp = get_info_col('', datas, elem)
			info[elem] = tmp
			# break
		# info.set_index('', inplace=True)

		# print(f"{info}")
		print(info.to_string(index=False))

	except AssertionError as error:
		print(f"{AssertionError.__name__}: {error}")
	except FileNotFoundError as error:
		print(f"FileNotFoundError: {error}")
	except Exception as error:
		print(f"Error: {error}")
	return


if __name__ == "__main__":
	main()