### Tanya Kadiyala
### CMSY-257-300
### Lab 1
### Problem 4: Sphere Calculations

def main():    
    # Get valid filename
    while True:
        try:
            filename = input("Enter payroll filename: ")
            with open(filename, 'r') as file:
                lines = file.readlines()
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
    
    # Initialize counters
    employees = 0
    total_hours = 0.0
    total_pay = 0.0
    malformed_lines = 0
    
    print("\nName\t\tHours\t\tWage\t\tPay")
    print("-" * 50)
    
    # Process each line
    for line in lines:
        parts = line.strip().split()
        
        # Skip empty lines
        if not parts:
            continue
        
        # Validate line format (should have exactly 3 parts)
        if len(parts) != 3:
            print(f"[Skipped malformed line] {line.strip()}")
            malformed_lines += 1
            continue
        
        last_name, wage_str, hours_str = parts
        
        # Validate numeric values
        try:
            hourly_wage = float(wage_str)
            hours_worked = float(hours_str)
            
            # Validate positive values
            if hourly_wage < 0 or hours_worked < 0:
                print(f"[Skipped malformed line] {line.strip()}")
                malformed_lines += 1
                continue
                
            # Calculate pay (no overtime)
            wages_paid = hourly_wage * hours_worked
            
            # Update totals
            employees += 1
            total_hours += hours_worked
            total_pay += wages_paid
            
            # Format output
            print(f"{last_name}\t\t{hours_worked:.2f}\t\t${hourly_wage:.2f}\t\t${wages_paid:,.2f}")
            
        except ValueError:
            print(f"[Skipped malformed line] {line.strip()}")
            malformed_lines += 1
            continue
    
    # Print summary
    print("\nEmployees:", employees, "Total Hours:", f"{total_hours:.2f}", "Total Pay:", f"${total_pay:,.2f}")
    if malformed_lines > 0:
        print(f"Note: {malformed_lines} malformed line(s) were skipped.")

if __name__ == "__main__":
    main()