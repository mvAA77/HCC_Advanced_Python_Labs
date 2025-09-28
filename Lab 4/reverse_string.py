### Tanya Kadiyala
### CMSY-257-300
### Lab 4
### Problem 2


def reverse_with_stack(s: str) -> str:
    stack = []
    for ch in s:
        stack.append(ch)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str


if __name__ == "__main__":
    print("Reverse String Tests:")
    print(reverse_with_stack("hello"))
    print(reverse_with_stack("CMSY257"))
    print(reverse_with_stack("stack"))
