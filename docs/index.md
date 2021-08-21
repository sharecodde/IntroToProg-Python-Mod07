# Error and Exception Handling and Pickling in Python
* B Gilbertson 
* August 24, 2021 
* Assignment 07

## Introduction 
In this assignment I will discuss my approach to learning and applying the knowledge I gained about error handling, pickling, and    developing GitHub web pages. This assignment includes a summary of helpful resources found on the web and provides a script that applies error handling and pickling.  The script allows the user to document results of a trout species survey.  The program allows the user to add, and view trout species and the number of fish observed in a trout survey. The program also has provisions to utilize pickling functions to store and retrieve the trout survey data.

## Researching exception handling and pickling in Python
In addition to reading the assigned material and class notes,  I also researched several websites to learn more about error and exception handling and pickling in Python. To help find quality websites on the topic, I first researched websites that we have previously utilized in the Foundations of Programming class, and then expanded my search to other sites.  Below is an annotated summary of the sites I found most useful at explaining the subjects along with my rationale for why I drew that conclusion. 

### Researching web resources for exception handling 
While there are many resources on the web, the following resources  were particularly useful for learning about error and exception handling.

“Exception Handling” :  https://www.learnpython.org/en/Exception_Handling (external link).
This site includes definitions,  examples  and simple exercises for exception handling, including a simplified example of try/except block. The site was a good introduction to the topic of error handling, without being overwhelming with detail.

 “Python Exceptions: An introduction”: https://realpython.com/python-exceptions/ (external link). Summary and demonstrations of how to handle exceptions in both text and video format.  This is a good advanced-beginner resources for error handling.
 
“Errors and Exceptions”: https://docs.python.org/3/tutorial/errors.html#handling-exceptions (external link). Excellent resource for step by step description of how try/except blocks work as well as other error handling information. This is a good detailed reference site with a great deal of information all in one place. 

### Researching web resources for pickling 
While there are many resources on the web, the following resources  were particularly useful for learning about pickling. 

 “Python Pickling”: https://www.tutorialspoint.com/python-pickling (external link). Provides a succinct definition and examples of pickling. The site was a good introduction to the topic of pickling, without being overwhelming with detail.
 
“ Python Pickle Module for saving objects (serialization)”: https://www.youtube.com/watch?v=2Tw39kZIbhs (External link). Easy to follow simple youtube example of pickling.

“The Python Pickle Method: How to Persist Objects in Python”: https://realpython.com/python-pickle-module/  (External link). Provides additional information on how pickling fits in to serialization and deserializtion and why you would want to do this. Easy to understand description and examples both in text and video format. This is a good advanced-beginner resources for pickling. A membership is needed to review some material.

## Script that demonstrates structured error handling and pickling
In preparation to write a Python script for this assignment, I created a new project in PyCharm that used Documents/_PythonClass/Assignment07 as its location and a title of  “Assignment07.py”.   The script incorporates both error handling and pickling. It allows the user to document results of a trout species survey.  The program allows the user to add, and view trout species and the number of fish observed in a trout survey. I first developed the error handling portions of the script and then added the pickling method. 

### Header and variables
I included a script header as well as a brief description of the code (Figure 1).  I identified the variables that I would use in the script .
```
#----------------------------------------------------------------------------  #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# BGilbertson, 8.11.2021,Added header
# BGilbertson, 8.12.2021,Added menu print, enter choice, read data and save data code
# BGilbertson, 8.13.2021,Added enter new task code
# BGilbertson, 8.14.2021,Added remove task and put the code pieces together
# BGilbertson, 8.15.2021,More code testing, commenting, and finalizing
# ---------------------------------------------------------------------------- #
# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
strCopyOriginal = "ToDoFileCopy.txt" #Captures the original text file that is used for menu option "4"
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of a processing functions
```
#### Figure 1. Showing the header of the script and variable identification

