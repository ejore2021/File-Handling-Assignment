# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: This is the first line.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python File Handling\n")
        print("File created and initial content written successfully.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading process completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appended line\n")
        file.write("Line 5: 67890\n")
        file.write("Line 6: Additional content\n")
        print("\nAdditional content appended successfully.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File appending process completed.")
