# You have a list of valid column values
# I need to read a data table, grab the first row which is the column names
# And then check if at least one or more of those columns is in my valid column list 
# And I want to do it in JavaScript and python 

def check_at_least_one_valid_column(valid_cols, column_names):
	for valid_col in valid_cols:
		if valid_col in column_names:
			return True
	return False

def check_at_least_one_valid_column(valid_cols, column_names):
	return any(valid_col for valid_col in valid_cols if valid_col in column_names)



valid_columns_arr_1 = ['cat_breed', 'fur_color', 'eye_color', 'is_shorthair', 'meow_octave']
input_header_row_1 = ['cat_name', 'fur_color', 'owner_name']
print('Running check_at_least_one_valid_column... (expecting true')
print('Here is the input columns we are checking: ' + str(input_header_row_1))
print('Here is the list of valid columns: ' + str(valid_columns_arr_1))
print(check_at_least_one_valid_column(valid_columns_arr_1, input_header_row_1))
print('\n')

valid_columns_arr_2 = ['cat_breed', 'fur_color', 'eye_color', 'is_shorthair', 'meow_octave']
input_header_row_2 = ['cat_name', 'owner_name']
print('Running check_at_least_one_valid_column... (expecting false)')
print('Here is the input columns we are checking: ' + str(input_header_row_2))
print('Here is the list of valid columns: ' + str(valid_columns_arr_2))
print(check_at_least_one_valid_column(valid_columns_arr_2, input_header_row_2))