def request():

    num1 = int(input("Input variable num1= "))
    num2 = int(input("Input variable num2= "))
    num3 = int(input("Input variable num3= "))
    print("Addition =", addition(num1, num2, num3))
    print("Average =", average(num1, num2, num3))
    print("Max =", max(num1, num2, num3))
    print("Min =", min(num1, num2, num3))
    print("Product =", product(num1, num2, num3))

def addition(num1, num2, num3):
    sum= int(num1) + int(num2) + int(num3)
    return sum
def average(num1, num2, num3):
    avg= int(num1) + int(num2) + int(num3) / 3
    return avg

def maximum(num1, num2, num3):
    print(max(num1, num2, num3))
    return max(num1, num2, num3)

def minimum(num1, num2, num3):
    print(min(num1, num2, num3))
    return min(num1,num2, num3)

def product(num1,num2,num3):
    multiply = num1 * num2 * num3
    return multiply

request()