import sys
N, M, V = map(int,sys.stdin.readline().split())
V-=1
_len=N-V
arr = list(map(int,sys.stdin.readline().split()))
for i in range(M):
    move = int(sys.stdin.readline())
    idx=move if move < N else ((move-V)%_len)+V
    print(arr[idx])