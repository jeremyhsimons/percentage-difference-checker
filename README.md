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
4. Make sure the polling data excel file is renamed 'poll_data', or the program will not work.
5. Make sure the empty excel file is renamed 'output_table', or the program will not work.
6. Once your folder is set, right click on the checker.py file and open with Visual Studio Code.
7. Once the editor has loaded, select the file icon in the top left corner of the screen, click on open folder, and select the new folder you created.
8. Ensure that the version of python VSCode is using matches the version you have installed on your PC. You can change it on VSCode if needed.
9. If there is no terminal at the bottom of the screen select the terminal on the top toolbar and click on new terminal.
10. In the terminal, run the following 2 commands to install the 3rd party dependencies into the code: 
- <strong>pip3 install pandas</strong> (type this into the terminal, press 'Enter', and wait for the package to install before doing anything else) 
- <strong>pip3 install openpyxl.</strong> 
11. To run the program, type 'python3 checker.py' into the terminal and hit 'Enter'. If that does not work try the command 'python checker.py'. Some more detailed instructions for running python files from a terminal can be found [here](https://learn.microsoft.com/en-us/windows/python/beginners).

### Using the program for the Google UK poll data

1. Run the checker.py file by typing 'python3 checker.py' in the terminal and hitting 'enter'
2. When prompted, type a number (the threshold for significant difference) into the terminal (e.g. 25).
3. If you type invalid data here, the program will exit and you will have to start again from step 1 of this section of the manual.
4. You should then get a prompt to tell you that the program will check all data for a 25% difference from the national averages of the poll data.
5. Hit 'enter' on your keyboard to run the checking function. There may be a few seconds' wait depending on the amount of data to process.
6. A truncated table of the collated data points that exceed the significant difference threshold (either above or below) will be displayed in the terminal.
7. Open the folder where you placed the three files. Open 'output_table.xlsx'
8. The data posted to the terminal should also appear here and may now be copied elsewhere for editing.
9. OPTIONAL: re-run the program using these steps, but this time enter a different threshold. The output_table.xlsx file should now be re-written with the new set of results.
10. Beware, the output table in the folder on your desktop must always remain where it is in order to work. It is recommended that any result sets you want to save for future use should be copied and saved to a different directory on your PC.

### Output table
The output_table.xlsx file should show six columns of information:
1. The table row number from the excel file.
2. The question option
3. The 

### Using the program for future Public First polls

This program is designed to work with the Google polling data provided by Public First, as well as similar excel tables which have a column marked 'Total' within an excel worksheet called 'Full Results'. These two pieces of data from the excel table are the only two hard-coded pieces of information in this python script. If users wish to run the program with worksheets using different names, two lines of code will have to be changed.

Please note that this script will not work on other tables of data. It is only designed to work on the Full Results sheet as displayed in the poll_data.xlsx file.

## Reporting bugs

If, for any reason, the program does not work as described in the steps already outlined. Please contact the developer at jeremy.h.simons@outlook.com for further assistance in setup.

## Ideas for future development (beyond the scope of this initial project)

* Implementation of a function that can record the original question/base for each subset of options that poll respondents can select and record it in a new column in the output_table.xlsx file. This could be done using the contents sheet of the excel file, but it is a more complex problem to solve since 
* Use of a library such as Streamlit (Python) to create a frontend dashboard. This would allow the user to input their threshold in a simple webform and for the program to generate a neatly-formatted table of results, rather than operating everything through the terminal.
* Creation of a backend database using Mongo DB where csv versions of the polling data could be stored, retrieved, updated, and deleted for future use.
* Creation of a full-stack system using the two previous ideas mentioned that allows users (likely data team members from Public First) to select the poll project they want to look at and run automated analyses of the data 

## Credits / 3rd party and opensource code used
Two 3rd party Python libraries were used to develop this project for Public First:
* [Pandas](https://pandas.pydata.org/) for modelling and manipulating the polling data provided by Public First
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) for reading and writing to excel files.