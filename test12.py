"""
id,gmailid,username, password

expected output: password values should be masked
condition: if password value is null empty string it can
"""
import re
userdata={id:123,"gmailid":"example@gmail.com","username":"abcdc","password":"x343$55uuT"}


print (userdata["username"])

txt="on the hozion"
x=re.findall("on",txt)
print(x)
