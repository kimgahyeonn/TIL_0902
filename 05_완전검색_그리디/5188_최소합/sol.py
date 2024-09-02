import sys
sys.stdin = open('input.txt')
T = int(input())

def bfs(start) :




for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    queue = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    bfs(1)