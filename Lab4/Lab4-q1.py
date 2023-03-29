#To generate 1000 Random numbers in a range:
#For the randomNumber=rand.randint(1,10): This signifies the output range within the loop, This means the numbers who be between 1 to 10 and the total numbers would be 1000.
import random
for x in range(1000):
    print(random.randint(1, 10))

#To find sum and average of the random numbers: Use the function: import random as rand, sum=0.00:
import random as rand
sum=0.00
for i in range(1000):
    print("i=",i)
    randomNumber=rand.randint(1,10)
    print("Random number=", randomNumber)
    sum=sum+randomNumber

print("final sum", sum)
average = sum/1000
print("average", average)
