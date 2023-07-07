# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd party imports
import pandas as pd
import openpyxl
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

THRESHOLD = 0

def get_threshold():
    """
    A function that collects the threshold for a significant difference
    (from the national average) and stores it in the 
    THRESHOLD global variable.
    """
    threshold_input = input("PLEASE ENTER THE THRESHOLD FOR SIGNIFICANT DIFFERENCE HERE: \n")
    threshold = int(threshold_input) / 100
    return threshold


def main():
    THRESHOLD = get_threshold()
    print(f"You have selected the threshold of: {THRESHOLD * 100}% difference.")

main()

df = pd.read_excel('poll-data.xlsx', sheet_name="Full Results")

# print(df.head(20))