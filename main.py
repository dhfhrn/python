# n, t, p, c = map(int, input().split())
# print((n - 1)//t * p * c)

# t = int(input())
# for i in range(t):
#     m, n = map(int, input().split())
#
#     if m < 12 or n < 4:
#         print(-1)
#     else:
#         print(11 * n + 4)

while True:
    ans = 0
    N = input()
    if N == '0':
        break
    ans += len(N)+1
    for i in N:
        if i == '0':
            ans += 4
        elif i == '1':
            ans += 2
        else:
            ans += 3

    print(ans)

가장 많이 받은 선물
