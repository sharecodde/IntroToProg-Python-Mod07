# Error and Exception Handling and Pickling in Python
 *B Gilbertson*  
 *August 24, 2021*   
 *Assignment 07* 

## Introduction 
In this assignment I will discuss my approach to learning and applying the knowledge I gained about error handling, pickling, and    developing GitHub web pages. This assignment includes a summary of helpful resources found on the web and provides a Python script that incorporates error handling and pickling.  The script allows the user to document results of a trout species survey.  The program allows the user to add, and view trout species and the number of fish observed in a trout survey. The program also has provisions to utilize pickling functions to store and retrieve the trout survey data.

## Researching exception handling and pickling in Python
In addition to reading the assigned material and class notes,  I also researched several websites to learn more about error and exception handling and pickling in Python. To help find quality websites on the topic, I first researched websites that we have previously utilized in the Foundations of Programming class, and then expanded my search to other sites.  Below is an annotated summary of the sites I found most useful at explaining the subjects along with my rationale for why I drew that conclusion. 

### Researching web resources for exception handling 
While there are many resources on the web, the following resources  were particularly useful for learning about error and exception handling.

“Exception Handling”: [External link] (https://www.learnpython.org/en/Exception_Handling) (External link).
This site includes definitions,  examples  and simple exercises for exception handling, including a simplified example of a try/except block. The site was a good introduction to the topic of error handling, without being overwhelming with detail. 


 “Python Exceptions: An introduction”: https://realpython.com/python-exceptions/ (External link). Summary and demonstrations of how to handle exceptions in both text and video format.  This is a good advanced-beginner resource for error handling.
 
“Errors and Exceptions”: https://docs.python.org/3/tutorial/errors.html#handling-exceptions (External link). Excellent resource for step by step description of how try/except blocks work as well as other error handling information. This is a good detailed reference site with a great deal of information all in one place. 

### Researching web resources for pickling 
While there are many resources on the web, the following resources  were particularly useful for learning about pickling. 

 “Python Pickling”: https://www.tutorialspoint.com/python-pickling (External link). Provides a succinct definition and examples of pickling. The site was a good introduction to the topic of pickling, without being overwhelming with detail.
 
“ Python Pickle Module for saving objects (serialization)”: https://www.youtube.com/watch?v=2Tw39kZIbhs (External link). Easy to follow simple youtube example of pickling.

“The Python Pickle Method: How to Persist Objects in Python”: https://realpython.com/python-pickle-module/  (External link). Provides additional information on how pickling fits in to serialization and deserializtion and why you would want to do this. Easy to understand description and examples both in text and video format. This is a good advanced-beginner resources for pickling. A membership is needed to review some material.

## Script that demonstrates structured error handling and pickling
In preparation to write a Python script for this assignment, I created a new project in PyCharm that used Documents/_PythonClass/Assignment07 as its location and a title of  “Assignment07.py”.   The script incorporates both error handling and pickling. It allows the user to document results of a trout species survey.  The program allows the user to add, and view trout species and the number of fish observed in a trout survey. I first developed the error handling portions of the script and then added the pickling method. 

### Header and variables
I included a script header as well as a brief description of the code (Figure 1).  I also identified the variables that I would use in the script .
```
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
```
##### *Figure 1. Showing the header of the script and variable identification*  



### Classes and functions
I then identified an input/output (IO) class and developed a function to present certain information back to the user (Figure 2).  There was opportunity to develop additional functions, however, I concentrated on the exception/error handling and pickling for purposes of this assignment.
```
class IO:
    """ Performs presentation and input/output. A limited number of functions
     have been defined"""
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
```
##### *Figure 2. Showing the IO class and the print_current_Fish function*  

### The main script
I next developed the main part of the script starting with an introduction of the program to the user as well as importing pickle to use later in the script (Figure 3).  
```
# Step 1  --- import pickle for program functionality
import pickle

# Step 2 - Introduce the program, read the initial data from the text file and
# present data to the user
print()
print("~"*70)
print("""This program is part of a trout conservation fishing survey and allows the
angler (aka the person fishing) to track the species of trout and the number
of trout they catch-and-release in a four hour fishing survey window.""")
print("~"*70)
print("\nThe current fish survey data contains the following items:")
print("="*60)
print("Trout species  (number)")
print("."*60)
```
#### *Figure 3. Code that introduces the program to the user*  

The next part of the script loads the data from a file and checks for two errors using a try/except block.  The first error is to check to see if there is any information in the file; this is the IndexError.  The next error is to check to see that a text file exists; this is the FileNotFoundError (Figure 4).
```
try:
    objFile = open(strFileName, "r") # opens a file in read mode "MyFish.txt"
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
```
#### *Figure 4. Showing try/except block to check for errors when loading data from the file*  
 
 
 The next part of the code presents a menu to the user. Once the user selects one of six choices, the menu directs the user to the appropriate part of the program (Figure 5)
```
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

    # Step 5 - Show the current fish in the table
    if (strChoice.strip() == '1'):
        IO.print_current_Fish(lstTable)
```  
#### *Figure 5. Showing the menu that is presented to the user*  


This next part of the script, option 2, allows the user to add a fish species to the trout survey record (Figure 6).  Once the user enters one of four possible trout species, the script checks for a correct entry.  If an input error is made, a message is displayed to the user and they are directed back to the main menu.  The next part of the script asks for the number of fish that were caught during the survey.  The program checks for a numeric entry and offers the user another opportunity to input a numeric entry.  The user will be returned to the main menu if a second entry error is made.  
```
   elif (strChoice.strip() == '2'):
        strFish = str(input("\nEnter one of the following trout species => rainbow, cutthroat, brown, bull: "))
        if strFish.lower() == "rainbow" or strFish.lower() == "cutthroat" or strFish.lower() == "brown"\
                or strFish.lower() == "bull": #checks for a valid entry
            print("-",strFish,"- trout species will be entered into the Trout Survey Record")
        else:
            print("**Trout species not found. Please check your entry**")
            input('Press the [Enter] key to return to the main menu.')
            continue
        strNumber = str(input("Enter the number of " + "-" +strFish + "- trout caught during the survey: "))
        if strNumber.isnumeric():
            dicRow = {"Fish": strFish,"Number": strNumber}
            lstTable.append(dicRow)
            print("The trout species: " + "-" + strFish + "- has will be entered in the survey record and you caught:  " + strNumber)
            input('Press the [Enter] key to return to the main menu.')
        else:
            print("**Please double check your entry and enter a number.**")
            strNumber = str(input("Enter the number of " + strFish + " trout caught during the survey: "))
            if strNumber.isnumeric():
                dicRow = {"Fish": strFish, "Number": strNumber}
                lstTable.append(dicRow)
                print("The trout species: " + strFish + ",  " + "has been entered in the survey record and you caught:  " + strNumber)
            else:
                input('***Hmmm, let\'s try again. Press the [Enter] key to return to the main menu.**')
        continue
```
#### *Figure 6. Option 2, adding a fish to the survey record*  


Menu option 5 utilizes the pickle.dump method to write binary data into a file (Figure 7); this is also known as serializing data.  The script also prints the information that was stored in the file by calling the IO function print_current_Fish.
```
    elif (strChoice.strip() == '4'):
        objFile = open(pickleFile, "wb") #open in write - binary mode
        pickle.dump(lstTable, objFile)
        objFile.close()
        print("The data stored into the file using the \'pickle.dump\' method is: ")
        IO.print_current_Fish(lstTable)
        input('Press the [Enter] key to return to the main menu.')
 ```
#### *Figure 7. Code demonstrating the pickle.dump method*  


Menu option 6 reads the data back from the file using pickle.load (Figure 8).  The data is also displayed back to the user. 
 ```
     elif (strChoice.strip() == '5'):
        objFile = open(pickleFile, "rb")
        objFileData = pickle.load(objFile)
        objFile.close()
        print("The data from \'pickle\' load is:")
        IO.print_current_Fish(objFileData)
        input('Press the [Enter] key to return to the main menu.')
```
#### *Figure 8. Code demonstrating reading data using pickle.load*  


The final portions of the script exit the program, menu choice 6, and print information back to the user (Figure 9).
 ```
     # Step 10 - Exit program
    elif (strChoice.strip() == '6'):
        break
    else: # This code catches incorrect menu choices by the user
       print("Please choose only 1, 2, 3, 4, 5, or 6")

# Step 11 - Display the fish in the list for the user and end the program
print("Here is a summary of your Trout Survey Record.")
IO.print_current_Fish(lstTable)
print("\nThank you for helping conserve trout, presss 'enter' to end the program.")
input()
```
#### *Figure 9. Code demonstrating exiting the program and displaying  a message to the user*  


## Running the script
To run the script, I “right-clicked” in PyCharm and selected the Run command. I followed the prompts to input the user information and the script ran as expected. When the program starts, information is displayed to the user along with an error message if the data file is not found (Figure 10).

<img width="622" alt="Figure 10" src="https://user-images.githubusercontent.com/88258750/130313665-a6283da2-f58b-4f61-b3bd-3ee36f255603.png">. 

![Figure10a](https://user-images.githubusercontent.com/88258750/130335603-d9373ad3-edf7-4ef2-8d34-912cb975e211.png)

#### *Figure 10 . The first part of the script introduces the script and displays a file not found message along with options for the user*   




The next part of the program displays a menu to the user (Figure 11).

 <img width="453" alt="Figure 11" src="https://user-images.githubusercontent.com/88258750/130313896-c09ff42a-dec7-40be-853c-926e02105a6c.png"> 
 
#### *Figure 11. Script run showing menu of options*  



### Menu option 2
When the user selects option 2, they can enter one of four trout species as well as the number of fish caught.  Error messages are displayed for incorrect data entries (Figure 12).

<img width="698" alt="Figure 12" src="https://user-images.githubusercontent.com/88258750/130314003-1ae0f6da-c2e0-4ffa-a241-f794f81b9f3e.png">  

#### *Figure 12. Script run showing option “2”, as well as error messages to the user*  



### Menu option 1
 <img width="450" alt="Figure 13" src="https://user-images.githubusercontent.com/88258750/130314015-733765a6-9715-4aec-ab3a-1804aaa39916.png">  
 
#### *Figure 13. Script run showing option “1”, the current data*   



### Menu option 4
Menu option 4 shows the data that is stored through the pickle method (Figure 14).

<img width="527" alt="Figure 14" src="https://user-images.githubusercontent.com/88258750/130314030-6b955fbe-9642-404a-b64a-155e7d2aca93.png">
 
#### *Figure 14. Script run showing option “4”, the pickle.dump method*  



### Menu option 5
Menu option 5 shows the data retrieved through pickle.load (Figure 15).

<img width="448" alt="Figure 15" src="https://user-images.githubusercontent.com/88258750/130314045-a1ad4aef-6e40-4ac5-b3a0-49e9052acd31.png">  

#### *Figure 15. Script run showing option “5”, pickle load*  



### Menu option 6
Menu option 6 exits the program and displays a message to the user (Figure 16).
<img width="592" alt="Figure 16" src="https://user-images.githubusercontent.com/88258750/130314065-e1f2628d-077c-4876-9de9-5e880163b9c7.png">  
 
#### *Figure 16. Script run showing option “6”, exit the program and show a summary*  



### Checking data files
To confirm that the program was writing to the  data files correctly, the “MyFish.txt” file and the data file from the pickle dump is shown as “MyPickle.txt” (Figure 17). I also opened the OS/Command/Terminal window to confirm the run of my script from there.  

<img width="183" alt="Figure 17A" src="https://user-images.githubusercontent.com/88258750/130314117-8eec4bda-723c-4e1b-8fbd-1f52217b637b.png">
<img width="378" alt="Figure 17" src="https://user-images.githubusercontent.com/88258750/130314090-bc226aab-94c8-4e03-a5c5-e27b86248473.png">

#### *Figure 17. Showing the MyFish.txt and the MyPickle.txt data files*  


## Saving and documenting my work
I saved the Python script into a folder called “Assignment07” and saved my Python script as Assignment07.py within this folder. I also saved documentation of the assignment in this same folder with the title of “Documentation for Assignment07 Gilbertson.docx”. I created a GitHub webpage utilizing “markdown” language and the information provided in the class programming notes; I posted my work on GitHub. I also posted the external link in the Discussion Forum and in this assignment documentation. 

 
## Summary
By working through the material in Module seven, I was able to build my knowledge of  exception and error handling, pickling, posting my work on GitHub and creating a webpage on GitHub utilizing markdown.  I also documented the process I used to complete the assignment and provided screen shots of the program, the run of the program and the text files.  


