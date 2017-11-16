AVERAGE = 1
MEDIAN = 2
MODE = 3
MINIMUM = 4
MAXIMUM = 5
QUIT = 6

print("This Program takes a set of five or fewer numbers and gives you an Average, Median, Mode, Min, or Max.")
Given_Range_1 = int(input("Enter the first number: "))
Given_Range_2 = int(input("Enter the second number: "))
Given_Range_3 = int(input("Enter the third number: "))
Given_Range_4 = int(input("Enter the fourth number: "))
Given_Range_5 = int(input("Enter the fifth number: "))
        
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
    
    import statistics
    print(statistics.mean([Given_Range_1,Given_Range_2,Given_Range_3,Given_Range_4,Given_Range_5]))
    
def hand_median(MEDIAN):
    
    import statistics
    print(statistics.median([Given_Range_1,Given_Range_2,Given_Range_3,Given_Range_4,Given_Range_5]))
    
def hand_mode(MODE):
    
    import statistics
    print(statistics.mode([Given_Range_1,Given_Range_2,Given_Range_3,Given_Range_4,Given_Range_5]))
    
def hand_minimum(MINIMUM):
   
    minimum_value = min(Given_Range_1,Given_Range_2,Given_Range_3,Given_Range_4,Given_Range_5)
    print(minimum_value)
    
def hand_maximum(MAXIMUM):
    
    maximum_value = max(Given_Range_1,Given_Range_2,Given_Range_3,Given_Range_4,Given_Range_5)
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