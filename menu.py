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
        choice = int(input("Enter your D E S I R E D choice: "))
        output = handle_choice(choice)
        print(output)
        
def display_menu():
    print("MENU")
    print("1) Calculate Average/Mean")
    print("2) Calculate Median")
    print("3) Calculate Mode")
    print("4) Calculate Minimum")
    print("5) Calculate Maximum")
    print("6) Quit")
    
def hand_average(AVERAGE):
    given_range = str(input("Enter the desired string of numbers, with commas in between them. (Example - 1,2,3,4): "))
    import statistics
    print(statistics.mean([given_range]))
    
def hand_median(MEDIAN):
    given_range1 = int(input("Enter the desired string of numbers, with commas in between them. (Example - 1,2,3,4): "))
    import statistics
    print(statistics.median([given_range1]))
    
def hand_mode(MODE):
    given_range2 = int(input("Enter the desired string of numbers, with commas in between them. (Example - 1,2,3,4): "))
    import statistics
    print(statistics.mode([given_range2]))
    
def hand_minimum(MINIMUM):
    given_range3 = int(input("Enter the desired string of numbers, with commas in between them. (Example - 1,2,3,4): "))
    minimum_value = min(given_range3)
    print(minimum_value)
    
def hand_maximum(MAXIMUM):
    given_range4 = int(input("Enter the desired string of numbers, with commas in between them. (Example - 1,2,3,4): "))
    maximum_value = max(given_range4)
    print(maximum_value)

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