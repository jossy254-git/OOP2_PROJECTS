A = int(input('enter maths marks:'))
B = int(input('enter eng marks:'))
C = int(input('enter kis marks:'))
D = int(input('enter phy marks:'))
# create the function
def avarage(A, B, C, D):
    #get avarage
    avg = float((A + B + C + D) / 4)

    #the algorithim
    if avg >= 70 and avg <= 100:
        print('its an A')
    elif avg >= 60 and avg <= 69:
        print('its an A-')
    elif avg >= 50 and avg <= 59:
        print('its a B+')
    elif avg >= 40 and avg <= 49:
        print('its a B')
    elif avg >= 30 and avg <= 39:
        print('its a B-')
    else:
        print('its a FIAL')
    print("Average score is: " + str(avg) + " points")
# calling the function
avarage(A, B, C, D)