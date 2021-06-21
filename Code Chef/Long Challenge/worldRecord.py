import decimal

T = int (input ())
if T < 1 or T > 100000:
    exit ()

inputStr = []
inputListStr = []
for i in range (T):
    inputStr.append (input ())
    inputListStr.append (inputStr [i].split ())
    if len (inputListStr [i]) != 4:
        exit ()

inputList = []
for i in range (T):
    inputList.append (list (map (decimal.Decimal, inputListStr [i])))

for t in range (T):
    for i in range (2):
        if inputList [t][i] <=0 or inputList [t][i] >= 2:
            exit ()
        if inputList [t][i].as_tuple ().exponent != -1:
            exit ()

    if inputList [t][2] <= 0 or inputList [t][2] > 1:
        exit ()
    if inputList [t][2].as_tuple ().exponent != -1:
        exit ()

    if inputList [t][3] >= 11 or inputList [t][3] <= 9:
        exit ()
    if inputList [t][3].as_tuple ().exponent != -2:
        exit ()

for t in range (T):
    finalSpeed = 1
    for i in range (4):
        finalSpeed = finalSpeed * inputList [t][i]

    time = float (format (100 / finalSpeed, ".2f"))
    if time <9.58:
        print ('YES')
    else:
        print ('NO')


