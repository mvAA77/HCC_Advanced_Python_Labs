### Tanya Kadiyala
### CMSY-257-300
### Lab 1
### Problem 2: Weekly Pay with Overtime

print("Welcome to the Weekly Pay Calculator!")
user_wage = input("Please enter your hourly wage: ")
user_regular = input("Please enter your total number of regular hours: ")
user_overtime = input("Please enter your total number of overtime hours: ")

wage = float(user_wage)
regular  = float(user_regular)
overtime = float(user_overtime)

regular_earning = (wage * regular)
overtime_earning = (1.5 * wage * overtime)

total = regular_earning + overtime_earning

print("Your total weekly pay is " + str(total))