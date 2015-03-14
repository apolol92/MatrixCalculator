import numpy as np
from decimal import *


# This Class convert the specific matrix-forms(str -> float matrix..)
class MatrixFormer:
	
    @staticmethod
    def str_to_matrix(str_input):
        rows = str(str_input).split(sep='\n')
        first = True
        for r in rows:
            cols = str(r).split(sep=' ')
            if(cols[0]!=''):
                if first:
                    #print(cols)
                    narr = np.array(cols, float)
                    first = False
                else:
                    #print(cols)
                    narr = np.vstack([narr, np.array(cols, float)])
        matrix_values = np.matrix(narr)
        return matrix_values.copy()

    @staticmethod
    def matrix_to_str(m):
        s = ""
        i = 0
        while i < m.values.shape[0]:
            d = 0
            while d < m.values.shape[1]:
                if(d != m.values.shape[1]-1):
		    #Set the precision:
                    s += '{0:.3f}'.format(m.values[i,d]) + " "
                    #s += str(m.values[i,d])+ " "
                else:
		    #Set the precision(also here):
                    s += '{0:.3f}'.format(m.values[i,d]) + "\n"
                    #s += str(m.values[i,d])+ "\n"
                d+=1
            i+=1
        return s

# This is the Matrix-Container Class. We only work with this Container
class Matrix:

    def __init__(self, str_input='0 0\n0 0\n'):
        self.values = MatrixFormer.str_to_matrix(str_input)

    def calc_inverse(self):
        result_matrix = Matrix()
        result_matrix.values = np.linalg.inv(self.values)
        return result_matrix

    def transpose(self):
        result_matrix = Matrix()
        result_matrix.values = self.values .transpose()
        return result_matrix

    def calc_eigenvectors(self):
        result_matrix = Matrix()
        result_matrix.values = np.linalg.eig(self.values)[1]
        return result_matrix

    def calc_LES(self):
        result_matrix = Matrix()
        row_length = self.values.shape[0]
        col_length = self.values.shape[1]
        a = self.values[:,0:col_length-1]
        b = self.values[:,col_length-1]
        result_matrix.values = np.linalg.solve(a, b)
        return result_matrix

    def calc_power(self, n):
        result_matrix = Matrix()
        result_matrix.values = np.linalg.matrix_power(self.values, n)
        return result_matrix

    def calc_determinant(self):
        return np.linalg.det(self.values)

    def calc_eigenvalues(self):
        return np.linalg.eig(self.values)[0]

    def add(self, m2):
        m3 = Matrix()
        m3.values = self.values + m2.values
        return m3

    def subtract(self, m2):
        m3 = Matrix()
        m3.values = self.values - m2.values
        return m3

    def product(self, m2):
        m3 = Matrix()
        m3.values = self.values * m2.values
        return m3

    def toString(self):
        return MatrixFormer.matrix_to_str(self)

