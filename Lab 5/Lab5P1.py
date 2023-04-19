def request():
    number = int(input("Enter variable number: "))
    print(even(number))

def even(number):
    if (int(number) %2 == 0):
        return "Even number"
    else:
        return 'Odd number'

request()









