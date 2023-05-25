import random
#Generate 100 random integers and store them in an array but do not print
randomNumbers =[random.randint(1,200) for i in range(100)]

#Filter and print only odd integers
print("Odd Numbers:")
for num in randomNumbers:
    if num % 2 != 0:
        print(num)


