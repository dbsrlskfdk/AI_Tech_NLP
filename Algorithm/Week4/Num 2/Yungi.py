import sys
input = sys.stdin.readline

N, M, V = map(int, input().split(" "))
C = list(map(int, input().split(" ")))

for _ in range(M):
    K = int(input())
    if K >= N: # K가 노드 갯수보다 길다는건 -> 꼬리가 연결된 곳을 넘어간 것
        K -= N
        if K >= N-V+1:
            K = K % (N-V+1)
        K += V-1
    print(C[K])


"""
    좋은 문제는 아닌 것 같습니다.
    접근은 너무 쉬운데, 시간초과 오류가 나서 이상했는데, 역시 빠른 입출력 처리를 해주니까 바로 해결되었습니다.
    이런 문제를 가져와서 죄송합니다 ㅠ
"""