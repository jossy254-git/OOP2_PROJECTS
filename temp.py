unit = input("enter the type of units you want to change:")
if unit == "celsius":
    temp = int(input("enter temp in celsius:"))
    C_to_F = (9 * temp) / 5 + 32
    print("%s'c is %s in fahreheits"%(str(temp), str(C_to_F)))
elif unit == "fahreheits":
    temp = int(input("enter temp in fahreheits:"))
    F_to_C = 5 / 9 * (temp - 32)
    print("%s'f is %s in celsius"%(str(temp), str(F_to_C)))
else:
    print("error!!!")