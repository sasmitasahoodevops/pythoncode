'''
fl= open("sample,txt","r")

for i in fl:
 print(i)

'''


with open("sample,txt","a") as fl:
    fl.write("I am Sasmita Sahoo \n")
    fl.write("I am basically from Puri district \n ")


file = open('sample,txt','r')
for i in file:
    print(i)
fl.close()