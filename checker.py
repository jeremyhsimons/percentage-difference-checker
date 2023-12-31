# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd PARTY IMPORTS
import pandas as pd
import openpyxl

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GLOBAL VARIABLES

# df stands for dataframe
df = pd.read_excel('poll_data.xlsx', sheet_name="Full Results")
df2 = pd.read_excel('poll_data.xlsx', sheet_name="Contents")

TOTAL_CELL = []

TABLES_CELL = []

QUESTIONS = []

OUTPUT_TABLE = {
    "Excel table row number" : [],
    "Question": [],
    "Question option" : [],
    "Crossbreak subgroup" : [],
    "National average for question (%)" : [],
    "Proportion for subgroup (%)": [],
    "Threshold for significant difference (%)": [],
    "Significant difference (%)": []
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SCRIPT LOGIC

def get_threshold():
    """
    A function that collects the threshold for a significant difference
    (from the national average) and stores it in the 
    THRESHOLD global variable.
    """
    threshold_input = input(
        "PLEASE ENTER THE THRESHOLD FOR SIGNIFICANT DIFFERENCE HERE: \n"
        )
    try:
        if not isinstance(float(threshold_input), float):
            raise ValueError(
                "Please enter a valid number"
            )
        else:
            threshold_float = float(threshold_input) / 100
            return threshold_float  
    except ValueError as e:
        print(f"Invalid response: {e}")
        return False


def find_total_cell():
    """
    A function that loops through rows and columns 
    and returns the index for each.
    """
    for index in range(len(df)):
        row = df.iloc[index]
        j = 0
        while j < row.shape[0]:
            if df.iloc[index, j] == 'Total':
                return [index, j]
            else:
                j += 1


def find_individual_tables():
    """
    A function to scan the 'contents' sheet and return the coords
    of the cell named 'Individual Tables'.
    """
    for index in range(len(df2)):
        row = df2.iloc[index]
        k = 0
        while k < row.shape[0]:
            if df2.iloc[index, k] == 'Individual Tables':
                return [index, k]
            else:
                k += 1


def store_questions():
    """
    A function to loop through the question rows and store
    them in a list of dictionaries called QUESTIONS.
    """
    for row in range(len(df2)):
        question_dict = {
            'question': '',
            'number': '',
            'base': '',
        }
        question = df2.iloc[row, TABLES_CELL[1]]
        if isinstance(question, str) and question != 'Individual Tables':
            question_dict['question'] = question
            number = df2.iloc[row, TABLES_CELL[1] + 1]
            question_dict['number'] = number
            base = df2.iloc[row, TABLES_CELL[1] + 2]
            question_dict['base'] = base
            QUESTIONS.append(question_dict)
        else:
            pass


def scan_data(threshold):
    """
    A function that loops through all rows of the data
    and for each row and ensuring that only valid data
    is sent to the checking function
    """
    for row in range(len(df)):
        national_average = (df.iloc[row, TOTAL_CELL[1]])
        if isinstance(national_average, float):
            i = TOTAL_CELL[1] + 1
            while i <= df.iloc[row].shape[0] - 1:
                data = df.iloc[row, i]
                if isinstance(data, float):
                    check_data(df, row, i, data, national_average, threshold)
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
        add_to_output(df, index, i, data, national_average, threshold)
    elif data < national_average - threshold:
        add_to_output(df, index, i, data, national_average, threshold)


def check_question_number(index):
    """
    A function to check the data excel row number against the 
    question numbers to assess which question 
    the data belongs to.
    """
    h = 0
    while h < (len(QUESTIONS)):
        if QUESTIONS[h]["number"] != 'nan':
            if float(QUESTIONS[h]["number"]) > index + 2:
                return f"{QUESTIONS[h-1]['question']}, {QUESTIONS[h-1]['base']}"
            elif index + 2 > float(QUESTIONS[-1]["number"]):
                return f"{QUESTIONS[-1]['question']}, {QUESTIONS[-1]['base']}"
            else:
                pass
        h += 1



def add_to_output(df, index, i, data, national_average, threshold):
    """
    A function that records the key metadata for each value
    that exceeds the threshold in either direction, and adds it
    to the OUTPUT_TABLE global variable.
    """
    OUTPUT_TABLE["Excel table row number"].append(index + 2)
    question = check_question_number(index)
    OUTPUT_TABLE["Question"].append(question)
    OUTPUT_TABLE["Question option"].append(df.iloc[index, 1])
    OUTPUT_TABLE["Crossbreak subgroup"].append(df.iloc[TOTAL_CELL[0], i])
    OUTPUT_TABLE["National average for question (%)"].append(national_average * 100)
    OUTPUT_TABLE["Proportion for subgroup (%)"].append(data * 100)
    OUTPUT_TABLE["Threshold for significant difference (%)"].append(threshold * 100)
    OUTPUT_TABLE["Significant difference (%)"].append((data - national_average) * 100)


def main():
    """
    A function to control the logic flow of all other functions.
    """
    threshold = get_threshold()
    if not threshold:
        print("-- EXITING PROGRAM --")
        return
    print(f"You have selected the threshold of: {threshold * 100}% difference.")
    input("Press 'Enter' to run the checker with this threshold.")
    total_cell = find_total_cell()
    TOTAL_CELL.append(total_cell[0])
    TOTAL_CELL.append(total_cell[1])
    tables_cell = find_individual_tables()
    TABLES_CELL.append(tables_cell[0])
    TABLES_CELL.append(tables_cell[1])
    store_questions()
    scan_data(threshold)
    output = pd.DataFrame(OUTPUT_TABLE, index=None)
    output.to_excel("output_table.xlsx", index=False)
    print(output)

main()
