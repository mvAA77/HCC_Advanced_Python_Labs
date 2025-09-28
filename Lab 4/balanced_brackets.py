### Tanya Kadiyala
### CMSY-257-300
### Lab 4
### Problem 4


def balanced_brackets(s: str) -> str:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != matching[ch]:
                return "Not Balanced"
            stack.pop()
    return "Balanced" if not stack else "Not Balanced"


if __name__ == "__main__":
    print("Balanced Brackets Tests:")
    for s in ["([])", "([{}])", "([)]", "("]:
        print(f"{s} → {balanced_brackets(s)}")
