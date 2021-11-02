# %%
import numpy as np
import pandas as pd
import plotly as pl
import plotly.offline as po
import os

po.init_notebook_mode(connected=True)
dirname = os.path.dirname(__file__)
filename = ""
file = os.path.join(dirname, filename)

# CLASES
class Plotter:
    def __init__(self):
        pass
    def print_main_menu(self):
        print("Select the type of data you want to enter (by pressing 1, 2 or 3)")
        print("1. Random data (between 0 and 1) with 100 rows and 5 columns.")
        print("2. Create a customized dataframe")
        print("3. Upload file (csv/json/excel)")
        self.choice = input("Type of data: ")
        return self.choice

    def get_random_data(self):
        self.data = np.random.rand(100, 5)
        return self.data

# FUNCTIONS


# OBJECTS
plotter = Plotter()

# %%
# GLOBAL VARIABLES
customized_columns = []
customized_values = []

running = True
while running:
    plotter.print_main_menu() #TypeError: print_main_menu() missing 1 required positional argument: 'self'

    # RANDOM DATA -----------------------------------------------------------------------------------------
    if plotter.choice == "1":
        plotter.get_random_data()
        df = pd.DataFrame(plotter.data, columns=["a", "b", "c", "d", "e"])
        df.plot()
        running = False
    # -----------------------------------------------------------------------------------------------------

    # CUSTOMIZED DATA -------------------------------------------------------------------------------------
    elif plotter.choice == "2":
        # DETERMINE GRID SIZE
        number_of_columns = input("How many columns do you want?: ")
        number_of_rows = input("How many rows do you want?: ")

        # CREATE A LIST WITH THE NAME OF THE COLUMNS
        for column in range(int(number_of_columns)):
            column_name = input(f"Enter the name of the column number {column+1}: ")
            customized_columns.append(column_name)

        # ASSIGN VALUES TO EACH ROW
        for row in range(int(number_of_rows)):
            for column in range(int(number_of_columns)):
                value = int(input(f"Enter the values for the row number {row+1}: "))
                customized_values.append(value) 
        
        customized_values = np.reshape(customized_values, (int(number_of_rows),int(number_of_columns)))
        df = pd.DataFrame(customized_values, columns=customized_columns)
        print("\nThis is your data")
        print(df)
        df.plot()
        running = False
    # -----------------------------------------------------------------------------------------------------
# %%



# %%

# COMMENTS
# CUSTOMIZE DE NUMBER OF RANDOM NUMBERS IN OPTION 1?
# OPTION 2 IS PLOTTING, NEED TO INCLUDE DIFFERENT TYPE OF PLOTS