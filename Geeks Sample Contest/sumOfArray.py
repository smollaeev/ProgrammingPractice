#User function Template for python3

def sumElement(arr,n):
    result = 0
    for i in range (n):
        result += arr [i]
    return result

if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))