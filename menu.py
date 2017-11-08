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
    given_range = int(input("Enter the first number: "))
    given_range_0 = int(input("Enter the second number: "))
    given_range_1 = int(input("Enter the third number: "))
    given_range_2 = int(input("Enter the fourth number: "))
    given_range_3 = int(input("Enter the fifth number: "))
    import statistics
    print(statistics.mean([given_range,given_range_0,given_range_1,given_range_2,given_range_3]))
    
def hand_median(MEDIAN):
    given_range1 = int(input("Enter the first number: "))
    given_range1_0 = int(input("Enter the second number: "))
    given_range1_1 = int(input("Enter the third number: "))
    given_range1_2 = int(input("Enter the fourth number: "))
    given_range1_3 = int(input("Enter the fifth number: "))
    import statistics
    print(statistics.median([given_range1,given_range1_0,given_range1_1,given_range1_2,given_range1_3]))
    
def hand_mode(MODE):
    given_range2 = int(input("Enter the first number: "))
    given_range2_0 = int(input("Enter the second number: "))
    given_range2_1 = int(input("Enter the third number: "))
    given_range2_2 = int(input("Enter the fourth number: "))
    given_range2_3 = int(input("Enter the fifth number: "))
    import statistics
    print(statistics.mode([given_range2,given_range2_0,given_range2_1,given_range2_2,given_range2_3]))
    
def hand_minimum(MINIMUM):
    given_range3 = int(input("Enter the first number: "))
    given_range3_0 = int(input("Enter the second number: "))
    given_range3_1 = int(input("Enter the third number: "))
    given_range3_2 = int(input("Enter the fourth number: "))
    given_range3_3 = int(input("Enter the fifth number: "))
    minimum_value = min(given_range3,given_range3_0,given_range3_1,given_range3_2,given_range3_3)
    print(minimum_value)
    
def hand_maximum(MAXIMUM):
    given_range4 = int(input("Enter the first number: "))
    given_range4_0 = int(input("Enter the second number: "))
    given_range4_1 = int(input("Enter the third number: "))
    given_range4_2 = int(input("Enter the fourth number: "))
    given_range4_3 = int(input("Enter the fifth number: "))
    maximum_value = max(given_range4,given_range4_0,given_range4_1,given_range4_2,given_range4_3)
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