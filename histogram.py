import pandas as pd
import matplotlib as plt
import sys
import math


def main():
	"""main function of the program"""
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Wrong number of arguments")
		filename = sys.argv[1]
		datas = pd.read_csv(filename)
		# print(datas)

	except AssertionError as error:
		print(f"{AssertionError.__name__}: {error}")
	except FileNotFoundError as error:
		print(f"FileNotFoundError: {error}")
	except Exception as error:
		print(f"Error: {error}")
	return


if __name__ == "__main__":
	main()
