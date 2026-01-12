import os, sys

FILE_PATH = "/Users/dev/PyCharmMiscProject/TestFile/test1.txt"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('==== Menu ===')
    print('1: Read File')
    print('2: Write/Create File')
    print('3: Delete File')
    print('4: Exit program')

    try:
        choice = int(input("Enter your choice what you want to perform: "))
    except ValueError:
        print("Please enter a valid number")
        input("Press Enter to continue...")
        continue

    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == 1:
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                print(file.read())
        else:
            print("File doesn't exist")

    elif choice == 2:
        mode = input("Which mode you want? Append(a) / Overwrite(w): ")

        if mode.lower() == 'a':
            with open(FILE_PATH, "a") as file:
                file.write(input("Write here: ") + "\n")

        elif mode.lower() == 'w':
            with open(FILE_PATH, "w") as file:
                file.write(input("Write here: ") + "\n")

        else:
            print("Invalid mode selected")

    elif choice == 3:
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
            print("File deleted successfully")
        else:
            print("File doesn't exist")

    elif choice == 4:
        sys.exit(0)

    else:
        print("Invalid choice")

    input("\nPress Enter to continue...")
