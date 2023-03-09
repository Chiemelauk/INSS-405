#>=50 -Hot
#30-50 -Warm
#0-30 -Cold
#<0 -Extreme cold


temperature=input('Enter Temperature:')
if(float(temperature) >=50):
    print('Hot')
elif (float(temperature) >=30 and float (temperature)<50):
    print('Warm')
elif (float(temperature) >=0 and float (temperature)<30):
    print('Cold')
elif (float(temperature) <-20):
    print('Extreme chill cold, shelter in place')
else:
    print('Extreme Cold')
