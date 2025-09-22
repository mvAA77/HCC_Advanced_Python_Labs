### Tanya Kadiyala
### CMSY-257-300
### Lab 1
### Problem 3: Text Analysis Report
import string

flag = True
while flag == True:
    try:
        user_input = input("Enter The Path and Name of the Text File: ")
        text_file = open(user_input, 'r')
        flag = False
    except OSError:
        print("Error: file(s) not found or could not be opened")
        print("Please re-enter\n")

# Initialize counters
total_lines = 0
total_words = 0
total_chars_no_whitespace = 0
word_count = {}
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Define punctuation to remove
punctuation = string.punctuation

# Process each line in the file
for line in text_file:
    total_lines += 1
    
    # Remove trailing whitespace and normalize to lowercase
    line = line.rstrip().lower()
    
    # Count characters excluding whitespace
    total_chars_no_whitespace += len(line.replace(" ", ""))
    
    # Remove punctuation
    for char in punctuation:
        line = line.replace(char, ' ')
    
    # Split into words
    words = line.split()
    total_words += len(words)
    
    # Count words and vowels
    for word in words:
        # Update word frequency
        word_count[word] = word_count.get(word, 0) + 1
        
        # Count vowels in this word
        for char in word:
            if char in vowel_counts:
                vowel_counts[char] += 1

text_file.close()

# Calculate unique words
unique_words = len(word_count)

# Get top 10 most frequent words (sort by frequency descending, then alphabetically ascending)
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
top_10_words = sorted_words[:10]

# Print the analytics report
print("\n" + "="*50)
print("TEXT ANALYSIS REPORT")
print("="*50)
print(f"Total lines: {total_lines}")
print(f"Total words: {total_words}")
print(f"Total characters (excluding whitespace): {total_chars_no_whitespace}")
print(f"Number of unique words: {unique_words}")
print("\nTop 10 most frequent words:")
for word, count in top_10_words:
    print(f"  {word} → {count}")
print("\nVowel counts:")
for vowel, count in vowel_counts.items():
    print(f"  {vowel.upper()}: {count}")
print("="*50)

