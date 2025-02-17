# Author: Michael Beaudet
# Title Week 5 Program 1
# Date: 2/17/25

def kilometer_conversion(kilometers):    
    miles = kilometers * 0.6214
    return miles

if __name__ == '__main__':
    kilometers = float(input("Enter the distance in kilometers to convert to miles: "))
    print('in main')
    # Call kilometer_conversion,
    miles = kilometer_conversion(kilometers)
    
    # Display the miles
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")