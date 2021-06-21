inpt = input ()
inputListStr = inpt.split (sep=' ')
inputList = list (map (int, inputListStr))
if len (inputList) != 3:
    exit ()
else:
    for i in range (len (inputList)):
        if inputList [i] < 1 or inputList [i] > 10:
            exit ()
    
    for i in range (3):
        for j in range (i + 1, 3):
            if inputList [i] == inputList [j]:
                print ('YES')
                exit ()
    
    print ('NO')