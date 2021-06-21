def is_Strong (s, k):
    if s.islower ():
        count = 0
        for i in range (len (s)):
            if s [i] == '*':
                count += 1
                if count >= k:
                    return True
            if s [i] != '*':
                count = 0
        
        return False
    else:
        return False                

T = int (input ())

if T<1 or T>10:
    exit ()

firstLineStr = []
firstLineListSTR = []
firstLineList = []

secondLineStr = []

for t in range (T):
    firstLineStr.append (input ())
    firstLineListSTR.append (firstLineStr [t].split ())
    if len (firstLineListSTR [t]) != 2:
        exit ()
    firstLineList.append (list (map (int, firstLineListSTR [t])))

    if firstLineList [t][1] > firstLineList [t][0] or firstLineList [t][0] < 1 or firstLineList [t][0] > 1000000 or firstLineList [t][1] <1 or firstLineList [t][1] >1000000:
        exit ()
    
    secondLineStr.append (input ())
    if len (secondLineStr [t])!= firstLineList [t][0]:
        exit ()

for t in range (T):
    if is_Strong (secondLineStr [t], firstLineList [t][1]):
        print ('YES')
    else:
        print ('NO')