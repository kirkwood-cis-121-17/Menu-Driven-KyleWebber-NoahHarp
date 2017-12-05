AVERAGE = 1
MEDIAN = 2
MODE = 3
MINIMUM = 4
MAXIMUM = 5
QUIT = 6

def main():
    
    choice = 0
    
    while choice != QUIT:
        display_menu()
        choice = int(input("Enter your desired choice: "))
        output = handle_choice(choice)
        
def display_menu():
    print("MENU")
    print("1) Calculate Average/Mean")
    print("2) Calculate Median")
    print("3) Calculate Mode")
    print("4) Calculate Minimum")
    print("5) Calculate Maximum")
    print("6) Quit")
    
def hand_average(AVERAGE):
    
    import Average
    
def hand_median(MEDIAN):
    
    import Median
    
def hand_mode(MODE):
    
    import Mode
    
def hand_minimum(MINIMUM):
    
    import Minimum
    
def hand_maximum(MAXIMUM):
    
    import Maximum

def handle_choice(choice):
    
    if choice == AVERAGE:
        return hand_average(AVERAGE)
    elif choice == MEDIAN:
        return hand_median(MEDIAN)
    elif choice == MODE:
        return hand_mode(MODE)
    elif choice == MINIMUM:
        return hand_minimum(MINIMUM)
    elif choice == MAXIMUM:
        return hand_maximum(MAXIMUM)
    elif choice == QUIT:
        print("Exiting the program... Have a nice day!")
    else:
        print("E R R O R, invalid selection. Please try again.")
    
main()