varA, varB =-3, 45

if (type(varA) == str or type(varB) == str):
    print('string involved')
else:
    if (type(varA) and type(varB)) != str:
        if (varA > varB):
            print('bigger')
        elif (varA == varB):
            print('equal')
        else :
            print('smaller')

# More compact code :
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    # If none of the above conditions are true,
    # it must be the case that varA < varB
    print('smaller')

