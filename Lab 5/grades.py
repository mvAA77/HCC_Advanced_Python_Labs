### Tanya Kadiyala
### CMSY-257-300
### Lab 5
### Problem 2

def load_scores(filename):
    scores = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        scores.append(int(line))
                    except ValueError:
                        print(f"Warning: Skipping non-integer value: {line}")
        return scores
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def calculate_median(scores):
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    
    if n == 0:
        return 0
    elif n % 2 == 1:
        return sorted_scores[n // 2]
    else:
        mid = n // 2
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2

def analyze_grades(scores):
    if not scores:
        return None, None, None, None, []
    
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    median = calculate_median(scores)
    
    above_avg = [score for score in scores if score > average]
    
    return highest, lowest, average, median, above_avg

def write_sorted_scores(scores, filename="grades_out.txt"):
    try:
        with open(filename, 'w') as f:
            for score in sorted(scores):
                f.write(f"{score}\n")
        print(f"Sorted scores written to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    print("=== Student Grades Analyzer ===")
    filename = input("Enter scores filename: ")
    
    scores = load_scores(filename)
    
    if not scores:
        print("No valid scores to analyze.")
        return
    
    highest, lowest, average, median, above_avg = analyze_grades(scores)
    
    print("\n--- Grade Statistics ---")
    print(f"Number of scores: {len(scores)}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Average score: {average:.2f}")
    print(f"Median score: {median}")
    print(f"Scores above average: {len(above_avg)}")
    print(f"Above average scores: {above_avg}")
    
    write_sorted_scores(scores)

if __name__ == "__main__":
    main()