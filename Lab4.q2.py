#Using a loop for the teperatures determine:
#>=50 = Hot
#30-50 = Warm
#0-30 = Cold
#<0 = Extreme cold
# I used a loop of 10


for i in range(10):
 temperature=input('Enter Temperature:')
if(float(temperature) >=50):
    print('Hot')
elif (float(temperature) >=30 and float (temperature)<50):
    print('Warm')
elif (float(temperature) >=0 and float (temperature)<30):
    print('Cold')
elif (float(temperature) <0):
    print('Extreme cold')

