from Matrix import *
# This Class controls the special matrix-calculations
class MatrixController:
    #Right string-input?
    @staticmethod
    def square_check(str_input):
        print(str_input)
        numpy_matrix = MatrixFormer.str_to_matrix(str_input)
        row_length = numpy_matrix.shape[0]
        col_length = numpy_matrix.shape[1]
        return row_length == col_length and row_length != 0
    #Right linear equation system string-input?
    @staticmethod
    def les_check(str_input):
        numpy_matrix = MatrixFormer.str_to_matrix(str_input)
        row_length = numpy_matrix.shape[0]
        col_length = numpy_matrix.shape[1]
        return col_length-row_length==1

    #Is string-input a matrix?
    @staticmethod
    def is_matrix(str_input):
        try:
            MatrixFormer.str_to_matrix(str_input)
            return True
        except:
            return False

