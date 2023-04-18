def request():
    number = int(input("Enter a number: "))
    even(number)

def even(num):
    if (int(num) %2 == 0):
        print(even(num))
    else:
        print('Odd number')

request()









