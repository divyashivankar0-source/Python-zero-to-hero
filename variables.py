#Variables in Python

x = 2
print(x)
print(x + 3)
y=3
print(x)
print(x + y)

print(x + 10)

# x = _ + y  #It works only in interactive envrionment
print(x)

name="youtube"
print(name)

print(name+'rocks')

print(name[0])

print(name[6])

#print(name[8])  #Index out of range

print(name[-1])

print(name[-2])

print(name[-7])

#It will exclude last index here 2nd index value will not be printed

print(name[0:2])

print(name[1:4])

#Starts with 1 and go upto ending

print(name[1:])

print(name[1:4])

#Starts with first letter and end with 3rd letter
print(name[:4])

#It will print upto last character
print(name[3:10])

#print(name[0:3])  #Stringss in python are immutable

print('my'+ name[3:7])

#Prints the length of string
myname='Divya Shivankar'
print(len(myname))