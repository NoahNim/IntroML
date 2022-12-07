import pandas as pd

# save filepath to variable for easy access
melbourne_file_path = 'input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame title melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of data in Melbourne data
print(melbourne_data.describe())
