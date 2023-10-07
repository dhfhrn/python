# 반복문
# for 범위가 정해진 반복문
# while 조건에 따라 반복 횟수 결정

# 함수 def (define)
# def 함수 이름(매개 변수):
#   실행문
# answer = 0
# retrun answer

# 함수이름(인수)
# print()
# range(3,6)

# def solution(str1, str2):
#     answer = ''
#     for i in range(len(str1)):
#         answer += str1[i]
#         answer += str2[i]
#     return answer
#
# print(solution("aaaaa", "bbbbb"))

# def print_coin():
#     print("비트코인")
#
# print_coin()
#
# for i in range(100):
#     print_coin()
#
# def print_coin():
#     for i in range(100):
#         print("비트코인")
#
# # 함수가 정의되기 전에 호출되어서
#
# def message() :
#     print("A")
#     print("B")
#
# message()
# print("C")
# message()
# # ABCAB
#
# print("A")
#
# def message() :
#     print("B")
#
# print("C")
# message()
# # ACB
#
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()
# # ACBED
#
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#     message1()
#
# message2()
# # BA
#
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
#
# message3()
# # BCBCBCA
#
# # 지역변수,전역변수

# def print_reverse(str):
#     print (str[::-1])
#
# def print_score (score_list):
#     pirnt(sum(score_list)/len(score_list))
#
# def print_even(list):
#     for i in list:
#         if i % 2 ==0:
#             pirnt(i)
#
# def print_key(dic):
#     for keys in dic.keys:
#         print(keys)
#
# def print_value_by_key(my_dict,key):
#     print(my_dict[key])

# 재귀함수 자기 자신을 재참조하는 함수
# def print_num(num):
#   print(num,end' ')
#   if num == 1:return   기저 조건(base case) 조건을 만족하면 재귀 호출이 더이상 일어나지 않도록 해줌
#   print(num,end = '->')
#   return print_num(num -1)

# print_num(10)

# 람다 함수
# lambda 매개변수 : 표현식 or 결과값

# def print_5xn(line):
#     chunk_num = int(len(line)/5)
#     for x in range(chunk_num +1):
#         print(line[x * num:x * num + num])
#
# def print_5xn(line,num):
#     chunk_num = int(len(line)/num)
#     for x in range(chunk_num +1):
#         print(line[x * num:x * num + num])
#
# def calc_monthly_salary(pay):
#     monthly_pay = int(pay/12)
#     return monthly_pay
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)
# 왼쪽:100 오른쪽:200
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)
# 왼쪽:200 오른쪽:100