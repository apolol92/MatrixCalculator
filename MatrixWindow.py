from tkinter import *
from MatrixController import *
from Matrix import *


BUTTON_EIGENVECTORS_TEXT = 'v'
BUTTON_INVERSE_TEXT = 'INV'
BUTTON_TRANSPOSE_TEXT = 'TRANS'
BUTTON_LINEAR_EQUATION_SYSTEM_TEXT = 'LES'
BUTTON_DETERMINANT_TEXT = 'DET'
BUTTON_EIGENVALUES_TEXT = 'λ'
BUTTON_ADD_TEXT = '+'
BUTTON_SUBTRACT_TEXT = '-'
BUTTON_PRODUCT_TEXT = 'x'
BUTTON_EQUAL = '='
BUTTON_POWER_TEXT = 'up'
LABEL_MATRIX_TEXT = 'Matrix:'
TEXT_SCALAR_FUNCTION_OUTPUT = 'Scalar-Output: '

class MatrixWindow:

    def __init__(self, index = 1, str_input = "23 42 1337\n17 5 1\n25 6 19\n", old_mat = None, operation = "no"):
        '''
        This is the constructor from MatrixWindow.
        It creates the User-Interface.

        :param index:
        :param str_input: Matrix in string-format. Default-Value is an example for starters
        :param old_mat: Only for operations like addition, subtraction, etc.. Gives the new window the last matrix
        :param operation: Tells the new window which operation is currently running
        :return: Nothing
        '''
        self.window = Tk()
        self.index = index
        self.old_matrix = old_mat
        self.operation = operation
        self.window.title('Matrix Calculator - Matrix '+ str(self.index))
        #Create Frames for window
        self.frame_top = Frame(self.window, width=150)
        self.frame_matrix = Frame(self.window, width=100, height=100)
        self.frame_matrix_functions = Frame(self.window, width=50, height=50)
        self.frame_matrix_operations = Frame(self.window, width=50, height=50)
        self.frame_matrix_scalar_functions = Frame(self.window, width=150, height=50)
        self.frame_matrix_scalar_function_output = Frame(self.window, width=150, height=50)

        #Create Widgets
        self.label_matrix = Label(self.frame_top, text=LABEL_MATRIX_TEXT)
        self.text_matrix = Text(self.frame_matrix, width=40, height=15)
        if(self.old_matrix != None):
            self.text_matrix.insert(INSERT, "")
        else:
            self.text_matrix.insert(INSERT, str_input)
        self.entry_power = Entry(self.frame_matrix_functions, width=5)
        self.button_power = Button(self.frame_matrix_functions, text=BUTTON_POWER_TEXT, command=self.button_power_click)
        self.button_eigenvectors = Button(self.frame_matrix_functions, text=BUTTON_EIGENVECTORS_TEXT)
        self.button_inverse = Button(self.frame_matrix_functions, text=BUTTON_INVERSE_TEXT, command=self.button_inverse_click)
        self.button_transpose = Button(self.frame_matrix_functions, text=BUTTON_TRANSPOSE_TEXT, command=self.button_transpose_click)
        self.button_linear_equation_system = Button(self.frame_matrix_functions, text=BUTTON_LINEAR_EQUATION_SYSTEM_TEXT, command=self.button_les_click)
        if(self.old_matrix == None):
            self.button_add = Button(self.frame_matrix_operations, text=BUTTON_ADD_TEXT, command=self.button_add_click)
            self.button_subtract = Button(self.frame_matrix_operations, text=BUTTON_SUBTRACT_TEXT, command=self.button_subtract_click)
            self.button_product = Button(self.frame_matrix_operations, text=BUTTON_PRODUCT_TEXT, command=self.button_product_click)
        else:
            self.button_equal = Button(self.frame_matrix_operations, text=BUTTON_EQUAL, command=self.button_equal_click)
        self.button_determinant = Button(self.frame_matrix_scalar_functions, text=BUTTON_DETERMINANT_TEXT, command=self.button_determinant_click)
        self.button_eigenvalues = Button(self.frame_matrix_scalar_functions, text=BUTTON_EIGENVALUES_TEXT, command=self.button_eigenvalues_click)
        self.text_scalar_output = Text(self.frame_matrix_scalar_function_output,width=40, height=4)
        self.text_scalar_output.config(state=DISABLED)


        #Add Widgets to Frames
        self.label_matrix.pack(side=LEFT)
        self.text_matrix.pack()
        self.entry_power.grid(row=0, column=0, sticky=W)
        self.button_power.grid(row=0, column=1, sticky=W+E+N+S)
        self.button_inverse.grid(row=1, column=0, columnspan=2, sticky=W+E+N+S)
        self.button_transpose.grid(row=2, column=0, columnspan=2, sticky=W+E+N+S)
        self.button_linear_equation_system.grid(row=3, column=0, columnspan=2, sticky=W+E+N+S)
        if(self.old_matrix==None):
            self.button_add.grid(row=0, column=0, sticky=W+E+N+S)
            self.button_subtract.grid(row=0, column=1, sticky=W+E+N+S)
            self.button_product.grid(row=1, column=0, sticky=W+E+N+S)
        if(self.old_matrix!=None):
            self.button_equal.grid(row=1, column=1, sticky=W+E+N+S)
        self.button_determinant.grid(row=0, column=0, sticky=W+E+N+S)
        self.button_eigenvalues.grid(row=0, column=1, sticky=W+E+N+S)
        self.text_scalar_output.grid(row=0, column=0, sticky=W)

        #Add Frames to window
        self.frame_top.grid(row=0, column=0, sticky=W)
        self.frame_matrix.grid(row=1, rowspan=5, column=0, columnspan=5)
        self.frame_matrix_functions.grid(row=1, column=5, columnspan=2, rowspan=4, sticky=W+E+N+S)
        self.frame_matrix_operations.grid(row=4, column=5, columnspan=4, rowspan=1)
        self.frame_matrix_scalar_functions.grid(row=7, column=0, sticky=W)
        self.frame_matrix_scalar_function_output.grid(row=7, sticky=W)
        self.frame_matrix_scalar_function_output.grid(row=8, sticky=W)

        #loop window
        self.window.mainloop()

    #Click-Events:

    def button_power_click(self):
        mat_str_input = self.text_matrix.get("1.0",END)
        if(MatrixController.square_check(self.text_matrix.get("1.0",END))==True and str(self.entry_power.get()).isdigit()):
            power = int(self.entry_power.get())
            mat = Matrix(self.text_matrix.get("1.0",END))
            MatrixWindow(self.index+1, mat.calc_power(power).toString())

    def button_inverse_click(self):
        if(MatrixController.square_check(self.text_matrix.get("1.0",END))==True):
            mat = Matrix(self.text_matrix.get("1.0",END))
            MatrixWindow(self.index+1, mat.calc_inverse().toString())

    def button_transpose_click(self):
        mat_str_input = self.text_matrix.get("1.0",END)
        mat = Matrix(self.text_matrix.get("1.0",END))
        MatrixWindow(self.index+1, mat.transpose().toString())

    def button_les_click(self):
        if(MatrixController.les_check(self.text_matrix.get("1.0",END))==True):
            mat_str_input = self.text_matrix.get("1.0",END)
            mat = Matrix(self.text_matrix.get("1.0",END))
            MatrixWindow(self.index+1, mat.calc_LES().toString())
        else:
            self.text_scalar_output.config(state=NORMAL)
            self.text_scalar_output.delete("1.0",END)
            self.text_scalar_output.config(state=DISABLED)

    def button_determinant_click(self):
        mat_str_input = self.text_matrix.get("1.0",END)
        if(MatrixController.square_check(self.text_matrix.get("1.0",END))==True):
            mat = Matrix(self.text_matrix.get("1.0",END))
            determinant = mat.calc_determinant()
            self.text_scalar_output.config(state=NORMAL)
            self.text_scalar_output.delete("1.0",END)
            self.text_scalar_output.insert(INSERT, "Determinant: " + '{0:.3f}'.format(determinant))
            self.text_scalar_output.config(state=DISABLED)
        else:
            self.text_scalar_output.config(state=NORMAL)
            self.text_scalar_output.delete("1.0",END)
            self.text_scalar_output.config(state=DISABLED)

    def button_eigenvalues_click(self):
        mat_str_input = self.text_matrix.get("1.0",END)
        if(MatrixController.square_check(self.text_matrix.get("1.0",END))==True):
            mat = Matrix(self.text_matrix.get("1.0",END))
            eigenvalues = mat.calc_eigenvalues()
            str_eigenvalues = ""
            i = 1
            for v in eigenvalues:
                str_eigenvalues += "λ"+str(i)+" = "+'{0:.3f}'.format(v)+ "\n"
                i+=1
            self.text_scalar_output.config(state=NORMAL)
            self.text_scalar_output.delete("1.0",END)
            self.text_scalar_output.insert(INSERT, str_eigenvalues)
            self.text_scalar_output.config(state=DISABLED)

    def button_add_click(self):
        if MatrixController.is_matrix(self.text_matrix.get("1.0",END)):
            MatrixWindow(self.index+1, old_mat = Matrix(self.text_matrix.get("1.0",END)), operation="add")
    def button_subtract_click(self):
        if MatrixController.is_matrix(self.text_matrix.get("1.0",END)):
            MatrixWindow(self.index+1, old_mat = Matrix(self.text_matrix.get("1.0",END)), operation="subtract")
    def button_product_click(self):
        if MatrixController.is_matrix(self.text_matrix.get("1.0",END)):
            MatrixWindow(self.index+1, old_mat = Matrix(self.text_matrix.get("1.0",END)), operation="multiply")

    def button_equal_click(self):
        if(self.operation=="add" and MatrixController.is_matrix(self.text_matrix.get("1.0",END))):
            m3 = self.old_matrix.add(Matrix(self.text_matrix.get("1.0", END)))
            MatrixWindow(self.index+1, str_input=m3.toString())
        elif(self.operation=="subtract" and MatrixController.is_matrix(self.text_matrix.get("1.0",END))):
            m3 = self.old_matrix.subtract(Matrix(self.text_matrix.get("1.0", END)))
            MatrixWindow(self.index+1, str_input=m3.toString())
        elif(self.operation=="multiply" and MatrixController.is_matrix(self.text_matrix.get("1.0",END))):
            m3 = self.old_matrix.product(Matrix(self.text_matrix.get("1.0", END)))
            MatrixWindow(self.index+1, str_input=m3.toString())




