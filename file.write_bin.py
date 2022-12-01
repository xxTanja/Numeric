from file_read_csv import m
import _pickle


my_out_file = 'matrix_out.dat'
with open(my_out_file, 'wb') as f:
    _pickle.dump(m, f)

