shopping_list = list()

while True:
   x = int(input("""\bWelcome to the Unit Converter\b
         Select the function you want to perform:
         1) Kilometer to miles
         2) Miles to Kilometers
         3) Celsius to Fahrenheit
         4) Fahrenheit to Celsius
         5) Kilograms to Grams
         6) Grams to Kilograms
         7) Exit                  
          Enter your Selection: """))
   

   if x == 1:
       distance_in_km = int(input("Enter the distance in kilometer: "))
       distance_in_miles = distance_in_km/0.62137
       print(f"The distance {distance_in_km}km is equal to {distance_in_miles}miles")

   elif x == 2:
       distance_in_miles = int(input("Enter the distance in kilometer: "))
       distance_in_km = distance_in_miles*0.62137
       print(f"The distance {distance_in_miles}miles is equal to {distance_in_km}km")

   elif x == 3:
       temp_in_celcius = int(input("Enter the temperature in Celsius: "))
       temp_in_fahrenheit = (1.8*temp_in_celcius)+32
       print(f"The Temperature {temp_in_celcius}°C is equal to {temp_in_fahrenheit}°F")

   elif x == 4:
       temp_in_fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
       temp_in_celcius = (temp_in_fahrenheit-32)*(5/9)
       print(f"The Temperature {temp_in_fahrenheit}°F is equal to {temp_in_celcius}°C")

   elif x == 5:
       weight_in_kg = int(input("Enter weight in Kilograms: "))
       weight_in_g = weight_in_kg*1000
       print(f"{weight_in_kg}kg is equal to {weight_in_g}g")
       
   elif x == 6:
       weight_in_g = int(input("Enter weight in Grams: "))
       weight_in_kg = weight_in_g/1000
       print(f"{weight_in_g}g is equal to {weight_in_kg}kg")
       
   elif x == 7:
       print("Thanks!")
       break
   