### Tanya Kadiyala
### CMSY-257-300
### Lab 4
### Problem 1

def is_palindrome_stack(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    stack = []
    for ch in cleaned:
        stack.append(ch)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return cleaned == reversed_str


if __name__ == "__main__":
    print("Palindrome Checker Tests:")
    for t in ["noon", "RaceCar", "Was it a car or a cat I saw?", "python"]:
        print(f"{t} → {is_palindrome_stack(t)}")
