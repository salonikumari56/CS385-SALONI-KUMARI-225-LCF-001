# Writing to a file
with open("file.txt", "w") as f:
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if not line:  # If the user just presses Enter, exit the loop
            break
        f.write(line + "\n")

print("Data written to file.txt successfully")

# Reading from the file
with open("file.txt", "r") as g:
    print("\nReading the file:\n")
    print(g.read())
