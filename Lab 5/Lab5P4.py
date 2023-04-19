def request():
   temperature = input("Enter temperature:")
   print(determine(temperature))
   return temperature

def determine(temperature):
   if (int(temperature) < 30):
       return "Cold"
   elif (int(temperature) < 40):
       return "Warm"
   elif (int(temperature) < 50):
         return "Hot"

request()

