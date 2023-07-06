# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd party imports
import pandas as pd
import openpyxl
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

THRESHOLD = get_threshold()

def get_threshold():
    """
    A function that collects the threshold for a significant difference
    (from the national average) and stores it in the 
    THRESHOLD global variable.
    """
    threshold = input("PLEASE ENTER THE THRESHOLD FOR SIGNIFICANT DIFFERENCE HERE: \n")
    return threshold



df = pd.read_excel('poll-data.xlsx', sheet_name="Full Results")

# print(df.head(20))