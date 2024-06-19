import sys
from terminal_interface import terminal_interface
from gui import gui_interface

def main():
    print("Choose interface:")
    print("1. Terminal")
    print("2. GUI")
    choice = input("Enter your choice: ")

    if choice == '1':
        terminal_interface()
    elif choice == '2':
        gui_interface()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()

