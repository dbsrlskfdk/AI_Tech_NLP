import numpy as np

def rotate90(key, n):
    arr=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[j][n-1-i]=key[i][j]
    return arr

def move_arr(key,x,y,n):
    arr=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (0 <= (j+x) and (j+x) < n) and (0 <= (i+y) and (i+y) < n):
                arr[i][j]=key[i+y][j+x]
    return arr

def solution(key, lock):
    n=len(key)
    arr=[[1 for _ in range(len(key))] for _ in range(len(key))]
    np_lock=np.array(lock)
    key90=rotate90(key,n)
    key180=rotate90(key90,n)
    key270=rotate90(key180,n)
    key_array = [key, key90, key180, key270]
    
    for k in key_array:
        for i in range(-n,n):
            for j in range(-n,n):
                tmp=move_arr(k,i,j,n)
                if (np.array(tmp) + np_lock).tolist() == arr:
                    return True

    return False
