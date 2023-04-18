def temperature():
   temp = int(input("Enter temperature:"))
   return temp

def determine_temperature(temp):
   if temp < 30:
       return "Cold"
   elif temp < 40:
       return "Warm"
   elif temp < 50:
         return "Hot"


def print_temperature(status):
   print("Temperature is", status)

temp = temperature()
status = determine_temperature(temp)
print_temperature(status)

temperature()

