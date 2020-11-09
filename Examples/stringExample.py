# String Examples
import datetime
now = datetime.datetime.now()
x = "hello"
print(x)

y = 'Hello'
print(y)

print(x[0])
print(y[2])

x = "Hello world"
s = x[0:3]
print(s)
s = x [:3]
print(s)

myName ="Terminator"
print(myName)

stg = "my lucky number is %d" % 5
print(stg)

stg1 = "My lucky number is " + str(5)
print(stg1)

print(str(now))
print("Today's Date is 09/11/2020")