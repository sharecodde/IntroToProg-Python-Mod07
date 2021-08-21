#----------------------------------------------------------------------------  #
# Title: Assignment 07
# Description: Work with error handling utilizing a program that
#               displays a simple menu to the user. Check for user
#               input and provide user messages. Demonstrate pickling
#               through the dump and load methods.
# ChangeLog (Who,When,What):
# BGilbertson, 8.19.2021,Added header and description for Assignment 07
# BGilbertson, 8.20.2021,Added code for error handling
# BGilbertson, 8.21.2021,Added code for pickling
# BGilbertson, 8.22.2021,Added additional comments and code cleanup
# ------------------------------------------------------------------------ #

# --------Data, declare variables and constants
objFile =  []   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
strFileName = "MyFish.txt"  # The name of the data file
pickleFile = "MyPickle.txt" # The name of another data file used with pickling

#-------------Processing --------------------------------------------------#
class Processor:
    """  Performs Processing tasks. No processing functions were defined
     for this script"""

#-----------Presentation Input/output functions ---------------------------#
class IO:
    """ Performs presentation and input/output. A limited number of IO functions
     have been defined for this script"""

    @staticmethod
    def print_current_Fish(list_of_rows):
        """ Shows the current Fish in the list/Table

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("=" * 50)
        print("Trout Species   (Number)")
        print("." * 50)
        for row in lstTable:
            print(row["Fish"] + "   " +"("+ row["Number"]+")")
        print("=" * 50)

####------------Main script -----------------------------------------
# Step 1  --- import pickle for program functionality
import pickle

# Step 2 - Introduce the program, read the initial data from the text file and
# present data to the user
print()
print("~"*75)
print("""This program is part of a trout conservation fishing survey and allows the
angler (aka the person fishing) to track the species of trout and the number
of trout they catch-and-release in a four hour fishing survey window. The survey
includes rainbow, cutthroat, brown and bull trout. """)
print("~"*75)
print("\nThe current fish survey data contains the following items:")
print("="*60)
print("Trout species  (number)")
print("."*60)

# Step 3 ---- load data from the file and check for no-data-in-the-file and no-file errors ---- #
try:
    objFile = open(strFileName, "r") # opens a file in read mode
    for row in objFile:
        lstRow = row.split(",")  # Returns a list!
        dicRow = {"Fish": lstRow[0].strip(), "Number": lstRow[1].strip()} #establish dictionary keys
        lstTable.append(dicRow)
        print(dicRow["Fish"] + "   " + "("+dicRow["Number"]+")")
    objFile.close()
except IndexError as e: #checks if there is any intial data in the file
    print("There are currently no items in the survey record. "
          "\nPlease add information to the survey using option 2 \nin the menu below.\n")
    input('Press the [Enter] key to display the main menu.')
except FileNotFoundError as e: #check to see if there is a file
    print("File not found, please add information to the survey"
          "\nusing option 2 in the menu below.\n")
    input('Press the [Enter] key to display the main menu.')

# Step 4 - Display a menu of choices to the user
print("="*50)
while (True):
    print("""
    Menu of Options
    1) Show current Trout Survey Information
    2) Add a fish species to your Trout Survey Record
    3) Save data to file
    4) Pickle dump
    5) Pickle load
    6) Exit the program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 6] - "))

    # Step 5 - Show the current fish in the table, Menu choice 1
    if (strChoice.strip() == '1'):
        IO.print_current_Fish(lstTable)

    # Step 6 - Add a new fish to the list/Table, Menu choice 2
    elif (strChoice.strip() == '2'):
        # captures user input for a trout species
        strFish = str(input("\nEnter one of the following trout species => rainbow, cutthroat, brown, bull: "))
        if strFish.lower() == "rainbow" or strFish.lower() == "cutthroat" or strFish.lower() == "brown"\
                or strFish.lower() == "bull": #checks for a valid entry
            print("-",strFish,"- trout species will be entered into the Trout Survey Record")
        else: # Displays error message to user for invalid entry
            print("**Trout species not found. Please check your entry**")
            input('Press the [Enter] key to return to the main menu.')
            continue

        # captures user input for number of fish caught
        strNumber = str(input("Enter the number of " + "-" +strFish + "- trout caught during the survey: "))
        if strNumber.isnumeric(): # checks to see that a numeric value was entered
            dicRow = {"Fish": strFish,"Number": strNumber}
            lstTable.append(dicRow)
            print("The trout species: " + "-" + strFish + "- has will be entered in the survey record and you caught:  " + strNumber)
            input('Press the [Enter] key to return to the main menu.')
        else: # displays a message to the user if a non-numeric value was entered
            print("**Please double check your entry and enter a number.**")

            # gives the user another chance to enter a numeric value
            strNumber = str(input("Enter the number of " + strFish + " trout caught during the survey: "))
            if strNumber.isnumeric():
                dicRow = {"Fish": strFish, "Number": strNumber}
                lstTable.append(dicRow)
                print("The trout species: " + strFish + ",  " + "has been entered in the survey record and you caught:  " + strNumber)
            else: #displays a message to the  user if a non-numeric value was entered and sends them to the menu
                input('***Hmmm, let\'s try again. Press the [Enter] key to return to the main menu.**')
        continue

    # Step 7 - Save data to the  file, Menu choice 3
    elif (strChoice.strip() == '3'):
        objFile = open(strFileName, "w")
        for row in lstTable:
            objFile.write(str(row["Fish"]) + "," + str(row["Number"]) + "\n")
        objFile.close()
        print("Your data has been saved")
        continue

    # Step 8  ---- Pickle dump method - Save data to the file, Menu choice 4
    elif (strChoice.strip() == '4'):
        objFile = open(pickleFile, "wb") #open file in binary write mode for pickling, file created if needed
        pickle.dump(lstTable, objFile)
        objFile.close()
        print("The data stored into the file using the \'pickle.dump\' method is: ")
        IO.print_current_Fish(lstTable)
        input('Press the [Enter] key to return to the main menu.')

    # Step 9 reading the data back using the pickle.load method, Menu choice 5
    elif (strChoice.strip() == '5'):
        objFile = open(pickleFile, "rb") # binary reading mode from the final
        objFileData = pickle.load(objFile)
        objFile.close()
        print("The data from \'pickle\' load is:")
        IO.print_current_Fish(objFileData) # Displays the data from the pickle.load
        input('Press the [Enter] key to return to the main menu.')

    # Step 10 - Exit program, Menu choice 6
    elif (strChoice.strip() == '6'):
        break
    else: # This code catches incorrect menu choices by the user
       print("Please choose only 1, 2, 3, 4, 5, or 6")

# Step 11 - Display the fish in the list for the user and end the program
print("Here is a summary of your Trout Survey Record.")
IO.print_current_Fish(lstTable)
print("\nThank you for helping conserve trout, presss 'enter' to end the program.")
input()