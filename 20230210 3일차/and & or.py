age = int(input("How old are you?"))

print("user answer",age)

print(type(age))
if age < 18:
    print("young!")
elif age>=18 and age<35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("birthday party!")
else:
    print("go ahead!")


