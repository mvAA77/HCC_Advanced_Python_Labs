### Tanya Kadiyala
### CMSY-257-300
### Lab 5
### Problem 1

def word_wrap(input_file, output_file, width):

    try:
        with open(input_file, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    
    words = text.split()
    
    if not words:
        print("Input file is empty.")
        return
    
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + (len(current_line) if current_line else 0) > width:
            if current_line:
                lines.append(current_line)
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)
    
    if current_line:
        lines.append(current_line)
    
    try:
        with open(output_file, 'w') as f:
            for line in lines:
                f.write(' '.join(line) + '\n')
        print(f"Wrapped text written to {output_file}")
    except Exception as e:
        print(f"Error writing to output file: {e}")
    
    return lines

def main():
    print("=== Word Wrap Formatter ===")
    infile = input("Enter input filename: ")
    outfile = input("Enter output filename: ")
    width = int(input("Enter line width: "))
    
    wrapped_lines = word_wrap(infile, outfile, width)
    
    if wrapped_lines:
        print("\nFirst 3 lines of wrapped text:")
        for i, line in enumerate(wrapped_lines[:3]):
            print(f"Line {i+1}: {' '.join(line)}")
        if len(wrapped_lines) > 3:
            print("...")

if __name__ == "__main__":
    main()