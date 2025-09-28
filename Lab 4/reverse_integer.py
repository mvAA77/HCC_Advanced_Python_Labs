### Tanya Kadiyala
### CMSY-257-300
### Lab 4
### Problem 3

def reverse_int_stack(n: int) -> int:
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    stack = []
    for digit in str(n):
        stack.append(digit)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return sign * int(reversed_str)


if __name__ == "__main__":
    print("Reverse Integer Tests:")
    for n in [12345, -9870, 1000, 0]:
        print(f"{n} → {reverse_int_stack(n)}")
