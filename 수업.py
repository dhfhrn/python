
# 불
# B1 = Ture
# B2 = False

# 조건문
# a = 'dog'
# b = 'cat'
#비교연산자: < > <= >= == !=
#논리연산자: or and in not
# if len(a) < len(b):
    # print ('hello')
# elif len(a) == len(b):
    # print(b)
# else:
    # print(a)

# h,m = input().split()
# h = int(h)
# m = int(m)
#
# if m - 45 < 0:
#     h -= 1
#     m += 60
#     if h < 0:
#         h = 23
# print(h, m-45)

# h,m = map(int,input().split())
# t = int(input())
# t2 = m + t
#
# if t2 >= 60:
#     h += t2//60
#     m -= (t2//60)*60
#     if h >= 24:
#         h -= 24
# print(h,m+t)

# 반복문
# a = 0
# while
# ex)a가 10이 될 때까지 +1 반복
# while a < 10
#   a += 1
# print(a)
# break 반복문 중지, while문에서만 가능
# while True 무한반복
#continue

# for
# ex)a +1을 10번 반복
# i는 for문 앞에서만 사용될 변수를 하나 만들어준 것
# in 뒤에는 range(정수) or 리스트,문자열,딕셔너리
# for i in range(10):

# d = {1:'one',2:'two',3:'three'}
# for i in d:
#     print(i)

# n = int(input())
# for i in range(1,10):
#     print(n,'*',i,'=',n*i)

x = int(input())
n = 0

for i in range(int(input())):
    a,b = map(int,input().split())
    n += a*b
if n == x:
    print('Yes')
else:
    print('No')