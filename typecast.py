#typecasting = the process of converting a value of one data type to another
#               (string, integer, float, boolean)
#                Explicit vs Implicit


name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#Explicit cast
age = float(age)
print(type(age))
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age) #if age is 0 then only its false

fname = ""

fname = bool(fname)
print(fname)  # empty string is only false otherwise always true

#Implicit casting

x = 2
y = 2.0

x = x /y
print(type(x))
print(x)