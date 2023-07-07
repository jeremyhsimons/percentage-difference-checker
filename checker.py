# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd party imports
import pandas as pd
import openpyxl
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def get_threshold():
    """
    A function that collects the threshold for a significant difference
    (from the national average) and stores it in the 
    THRESHOLD global variable.
    """
    threshold_input = input("PLEASE ENTER THE THRESHOLD FOR SIGNIFICANT DIFFERENCE HERE: \n")
    threshold_float = float(threshold_input) / 100
    return threshold_float


def check_data(threshold):
    """
    A function that loops through all rows of the data
    and for each row checks all the float values against
    the national average column.
    """
    print("function call working")
    df = pd.read_excel('poll-data.xlsx', sheet_name="Full Results")
    for index in range(len(df)):
        national_average = (df.iloc[index, 2])
        if isinstance(national_average, float):
            i = 3
            while i <= 31:
                data = df.iloc[index, i]
                if isinstance(data, float):
                    if data > national_average + threshold:
                        print(f"{index} outlier, greater than")
                    elif data < national_average - threshold:
                        print(f"{index} outlier, less than")
                else:
                    pass
                i += 1
        else:
            pass


def main():
    threshold = get_threshold()
    print(f"You have selected the threshold of: {threshold * 100}% difference.")
    input("Press Enter to run the checker with this threshold.")
    check_data(threshold)

main()