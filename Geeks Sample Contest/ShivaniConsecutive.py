T=int(input().strip())
for t in range (T):
    Sum = 0
    N=int(input().strip())
    A=list(map(int, input().rstrip().split()))
    A.sort(reverse=True)
    while len(A)>0:
        i=0
        ele=A[i]-1
        Sum=Sum+A.pop(i)
        if ele in A:
            A.remove(ele)


    print(Sum)