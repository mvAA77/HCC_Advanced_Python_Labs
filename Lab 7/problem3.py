### Tanya Kadiyala
### CMSY-257-300
### Lab 7
### Problem 3

def recursive_list_sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + recursive_list_sum(numbers[1:])

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("List of numbers:")
    print(numbers)
    
    result = recursive_list_sum(numbers)
    print(f"Sum of all the numbers in the list: {result}")

if __name__ == "__main__":
    main()