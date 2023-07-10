# percentage-difference-checker

## Introduction
This is a python tool that takes input from the user to specify the threshold for a significant difference from the national average response in Public First's Poll for Google UK. With this user data, the program checks all crossbreaks for all questions and collects responses that are significantly higher or lower than the national average, and saves this information in an excel sheet called output_table.xlsx

The tool is currently a command-line based project which requires a virtual environment such as a code editor to operate. There is, however, a lot of scope for this program to be developed into a full-stack, web-hosted application with an interactive front end. Currently, though, this tool requires a small amount of setup to use.

New users should follow the steps shown in the user manual below to set up an easy-to-use code editor, and to set up Python on their machine.

## Project goals

* To take and store input data from a user.
* To check all crossbreaks against the national average for each question.
* To record each significant difference and output it in a human-readable format.

## User Manual

### Setup for running the program locally.

1. Download the latest version of python and install it on your PC.
2. Download and install Visual Studio Code (Microsoft's free code editor).
3. Create a new folder on your desktop, and place three files inside of it: checker.py, the polling data excel file, and an empty excel file.
4. Make sure the polling data file is renamed 'poll_data', or the program will not work.
5. Make sure the empty excel file is renamed 'output_table', or the program will not work.
6. Once your folder is set, right click on the checker.py file and open with Visual Studio Code.
7. Once the editor has loaded, select the file icon in the top left corner of the screen, click on open folder, and select the new folder you created.
8. Ensure that the version of python VSCode is using matches the version you have installed on your PC.
9. If there is no terminal at the bottom of the screen select the terminal on the top toolbar and click on new terminal.
10. In the terminal, run the following 2 commands to install the 3rd party dependencies into the code: pip3 install pandas, pip3 install openpyxl
11. To run the program, type 'python3 checker.py' into the terminal and hit 'enter'. If that does not work try the command 'python checker.py'. Basic instructions for running python files from a terminal can be found [here](https://learn.microsoft.com/en-us/windows/python/beginners).

### Using the program for the Google UK poll data

1. Run the checker.py file by typing 'python3 checker.py' in the terminal and hitting 'enter'
2. When prompted, type a number (the threshold for significant difference) into the terminal (e.g. 25).
3. If you type invalid data here, the program will exit and you will have to start again from step 1 of this section of the manual.
4. You should then get a prompt to tell you that the program will check all data for a 25% difference from the national averages of the poll data.
5. Hit 'enter' on your keyboard to run the checking function. There may be a few seconds' wait while the calculations are completed.
6. A truncated table of the collated data points that exceed the significant difference threshold (either above or below) will be displayed in the terminal.
7. Open the folder where you placed the three files. Open 'output_table.xlsx'
8. The data posted to the terminal should also appear here and may now be copied elsewhere for editing.
9. OPTIONAL: re-run the program using these steps, but this time enter a different threshold. The output_table.xlsx file should now be re-written with the new set of results.
10. Beware, the output table in the folder on your desktop must always remain where it is in order to work. It is recommended that any result sets you want to save for future use should be copied and saved to a different directory on your PC.

### Using the program for future Public First polls

This program is designed on the assumption that all polling data tables produced by Public First have the same format in terms of rows and columns. Therefore it should be possible to re-use this tool for any future poll that Public First carries out. If this is ever not the case, the following instructions will help a non-programmer to adapt the program for future polling data.

1. Open the checker.py file in Visual Studio Code.
1. Scroll down to line 43 and find the variable named 'national_average'. This is currently hard-coded to the 'total' column in the polling data excel file. This is the third column at the moment. If the 'total' column is ever not the third, set the national_average variable to equal ```df.iloc[index, (excel_col_number - 1)]```, where excel_col_number = the column in excel where total values are stored.
1. After this set i to equal the column value + 1, and change the default value of 31 to match 1 less than the number of total columns in the excel file.
1. Repeeat step 2 on line 76: ```OUTPUT_TABLE["Question name"].append(df.iloc[index, (excel_col_number - 1)])``` where excel_col_number = the column where questions/response options are stored.
1. Repeat step 2 on line 77: ```OUTPUT_TABLE["Crossbreak subgroup"].append(df.iloc[(excel_row_number - 2), i])``` where excel_row_number = the row where the crossbreak categories are listed. On the google poll file, this is currently row 6


## Ideas for future development

* A function that can record the original question/the base for each subset of options that poll respondents can select and record it in a new column in the output_table.xlsx file.
* Use a library such as Streamlit (Python) to create a frontend dashboard and formatted table for the program user.

## Credits / 3rd party and opensource code used
Two 3rd party Python libraries were used to develop this project for Public First:
* [Pandas](https://pandas.pydata.org/) for modelling and manipulating the polling data provided by Public First
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) for reading and writing to excel files.