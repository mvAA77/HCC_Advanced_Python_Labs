### Tanya Kadiyala
### CMSY-257-300
### Lab 7
### Problem 2

def recursive_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

def main():
    try:
        num = int(input("Enter a positive whole number: "))
        if num < 0:
            print("Please enter a positive number.")
        else:
            result = recursive_sum(num)
            print(f"The sum of 1 - {num} is {result}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()