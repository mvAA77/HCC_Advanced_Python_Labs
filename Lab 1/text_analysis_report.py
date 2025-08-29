### Tanya Kadiyala
### CMSY-257-300
### Lab 1
### Problem 3: Text Analysis Report

flag = True
while flag == True:
    try:
        user_input = input("Enter The Path and Name of the Text File: ")
        text_file = open(user_input, 'r')
        flag = False
    except OSError:
        print("Error: file(s) not found or could not be opened")
        print("Please re-enter\n")

 for line in text_file:
    line = line.rstrip()



