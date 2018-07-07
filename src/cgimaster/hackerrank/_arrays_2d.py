import os

def calcSum(arr, row, col):
    v1 = sum(arr[row][col:col+3])
    v2 = sum(arr[row+2][col:col+3])
    v3 = arr[row+1][col+1]
    return v1+v2+v3
# Complete the hourglassSum function below.
def hourglassSum(arr):
    result = None
    for row in range(0,len(arr)-2):
        for col in range(0,len(arr[0])-2):
            s = calcSum(arr,row,col)
            if result == None or result < s:
                result = s
    return result

if __name__ == '__main__':
    inp = """1 1 1 0 0 0
            0 1 0 0 0 0
            1 1 1 0 0 0
            0 9 2 -4 -4 0
            0 0 0 -2 0 0
            0 0 -1 -2 -4 0"""
    arr = []
    for line in inp.split('\n'):
        arr.append(list(map(int, line.strip().split())))

    result = hourglassSum(arr)
    print(result)