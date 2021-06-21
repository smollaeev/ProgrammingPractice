def printPat(n):
    #Code here
    results = []
    for i in range (n):
        row = []
        for j in range (n):
            for k in range (n - i):
                row.append(str (n - j))
        results.append (' '.join (row))
    result = ' $'.join (results)
    result += ' $'
    return result
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))
# } Driver Code Ends