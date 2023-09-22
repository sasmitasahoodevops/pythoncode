calculation_of_units=24
name_of_units="hours"
def day_of_units(number_of_days):
  try:
    print(f"{number_of_days} are {number_of_days*calculation_of_units} {name_of_units}")
#day_of_units(76)
#day_of_units(760)
#day_of_units(854)
#print("previous statements are right")
user_input=input("enter a number:")
user_input_number=int(user_input)
calculated_value=day_of_units(user_input_number)
print(calculated_value)
except SyntaxError:
print("the block of code is right")