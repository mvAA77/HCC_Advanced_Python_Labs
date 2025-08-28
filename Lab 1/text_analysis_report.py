### Tanya Kadiyala
### CMSY-257-300
### Lab 1
### Problem 3: Text Analysis Report

flag = True
while flag == True:
    try:
        in = input("Enter The Path and Name of the Text File: ")
        text_file = open(in, 'r')
        flag = False
    except OSError:
        print("Error: file(s) not found or could not be opened")
        print("Please re-enter\n")


