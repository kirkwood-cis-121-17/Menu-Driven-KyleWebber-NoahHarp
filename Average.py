def Average():
    
    Given_Range_1 = int(input("Enter the first number: "))
    Given_Range_2 = int(input("Enter the second number: "))
    Given_Range_3 = int(input("Enter the third number: "))
    Given_Range_4 = int(input("Enter the fourth number: "))
    Given_Range_5 = int(input("Enter the fifth number: "))
    
    import statistics
    print(statistics.mean([Given_Range_1,Given_Range_2,Given_Range_3,Given_Range_4,Given_Range_5]))

Average()