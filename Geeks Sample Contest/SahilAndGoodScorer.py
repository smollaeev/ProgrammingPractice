inputList = []
numberOfTestCases = int (input ())

for i in range (numberOfTestCases *3):
    inputList.append (input ())

inputIntList = []
for i in range (len (inputList)):
    inputIntList.append (inputList [i].split ())
    for j in range (len (inputIntList [i])):
        inputIntList [i][j] = int (inputIntList [i][j])

output = []
for t in range (numberOfTestCases):
    s = []
    for i in range (2):
        s.append (sum (inputIntList [i+1+3*t]))
    max_ = max (s)
    index_ = s.index (max_) + 1
    output.append (index_)    

for i in range (len (output)):
    print ('C{}'.format (output [i]))