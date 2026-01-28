#Debug a program with logical and runtime errors.

#Buggy Code

a = 10
b = 0
print(a / b)

#Error:
#ZeroDivisionError


#Debugged Code

a = 10
b = 0

if b == 0:
    print("Cannot divide by zero")
else:
    print(a / b)