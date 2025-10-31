### Tanya Kadiyala
### CMSY-257-300
### Lab 7
### Problem 1

from pathlib import Path

def count_files(directory_path):
    path = Path(directory_path)
    if not path.exists() or not path.is_dir():
        return 0
    
    file_count = 0
    try:
        for item in path.iterdir():
            if item.is_file():
                file_count += 1
            elif item.is_dir():
                file_count += count_files(item)
    except PermissionError:
        pass
    
    return file_count

def main():
    directory = input("Please type your entire directory path here: ")
    total_files = count_files(directory)
    print(f"Your chosen directory contains {total_files} files.")

if __name__ == "__main__":
    main()