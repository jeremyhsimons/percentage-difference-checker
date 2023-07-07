# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd party imports
import pandas as pd
import openpyxl
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OUTPUT_TABLE = {
    "Excel table row number" : [],
    "Question name" : [],
    "Crossbreak subgroup" : [],
    "National average for question (%)" : [],
    "Proportion for subgroup (%)": [],
    "Significant difference (%)": []
}

def get_threshold():
    """
    A function that collects the threshold for a significant difference
    (from the national average) and stores it in the 
    THRESHOLD global variable.
    """
    threshold_input = input("PLEASE ENTER THE THRESHOLD FOR SIGNIFICANT DIFFERENCE HERE: \n")
    threshold_float = float(threshold_input) / 100
    return threshold_float


def scan_data(threshold):
    """
    A function that loops through all rows of the data
    and for each row and ensuring that only valid data
    is sent to the checking function
    """
    df = pd.read_excel('poll-data.xlsx', sheet_name="Full Results")
    for index in range(len(df)):
        national_average = (df.iloc[index, 2])
        if isinstance(national_average, float):
            i = 3
            while i <= 31:
                data = df.iloc[index, i]
                if isinstance(data, float):
                    check_data(df, index, i, data, national_average, threshold)
                else:
                    pass
                i += 1
        else:
            pass


def check_data(df, index, i, data, national_average, threshold):
    """
    A function that compares each value against the national
    average and threshold to see if it is significantly 
    greater or less than expected.
    """
    if data > national_average + threshold:
        # print(f"{index} outlier, greater than")
        add_to_output(df, index, i, data, national_average, threshold)
    elif data < national_average - threshold:
        # print(f"{index} outlier, less than")
        add_to_output(df, index, i, data, national_average, threshold)


def add_to_output(df, index, i, data, national_average, threshold):
    """
    A function that records the key metadata for each value
    that exceeds the threshold in either direction, and adds it
    to the OUTPUT_TABLE global variable.
    """
    OUTPUT_TABLE["Excel table row number"].append(index)
    OUTPUT_TABLE["Question name"].append(df.iloc[index, 1])
    OUTPUT_TABLE["Crossbreak subgroup"].append(df.iloc[4, i])
    OUTPUT_TABLE["National average for question (%)"].append(national_average * 100)
    OUTPUT_TABLE["Proportion for subgroup (%)"].append(data * 100)
    OUTPUT_TABLE["Significant difference (%)"].append(data - national_average * 100)


def main():
    threshold = get_threshold()
    print(f"You have selected the threshold of: {threshold * 100}% difference.")
    input("Press 'Enter' to run the checker with this threshold.")
    scan_data(threshold)

main()

output = pd.DataFrame(OUTPUT_TABLE)
output.to_excel("output_table.xlsx")
print(output)
