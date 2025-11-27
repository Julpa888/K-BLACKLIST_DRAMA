import os
import sys

while True:
    try:
        user_input = input("Enter a directory path (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            sys.exit(0)

        if not os.path.isdir(user_input):
            print("The provided path is not a valid directory. Please try again.")
            continue

        files = os.listdir(user_input)
        if not files:
            print("The directory is empty.")
        else:
            print("Files in the directory:")
            for file in files:
                print(file)
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")