import re

pattern = "^ty"
test_string = 'tyzxrzx'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
