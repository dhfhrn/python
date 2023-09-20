#정수 int
#실수 float
#문자열 str
#리스트 []
#몫 //
#나머지 %
#제곱 2**5
#print (len())
# a = ['a',2.0,3]
#print (a[0:2]) 슬라이싱
#print (a[2]) 인덱싱
#print (a.index(2.0))
#print (a.find('x'))
#del a[]
#a.remove()
#print (a.replace('p',''))
#f-string 문자열 안에 변수나 표현식 삽입 가능
#num = input()
#name = input()
#print ("번호:",num)
#print ("나이:",age)
#S1 = (f"번호: {}\n 나이: {}")
#tuple() 소괄호
#dictionary(딕셔너리) 중괄호, 인덱스 번호 대신 key값 지정
#a = 1
#d1 = {a:'one',"b":2,3:"three"}
#print (a in d1)
#print (d1[a])
#list 대괄호
#추가
#d1[4] = 'd'
#print (d1)
#수정
#d1["b"] = 4
#print (d1)
#삭제
#del d1[1]
#print (d1)
#집합 set() 중복 허용하지 않음, 순서가 없음
#s1 = set("hello")
#print(s1)
#s1 = set([1,2,3,4])
#s2 = set([3,4,5])
#s3 = set([6,7,8,])
#합집합 |
#print (s1|s2)
#교집합 &
#print (s2&s3)
#차집합 -
#print (s1-s2)
#대칭 차집합 (합-교)^
#print (s1^s2)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _ = scores
# print(valid_score)
#
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b,*valid_score = scores
# print(valid_score)
#
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,*valid_score = b,scores
# print(valid_score)
#
# temp = { }
#
# 아이스크림 = {"메로나":1000,"폴라포":1200,"빵빠레":1800}
# print (아이스크림)
#
# 아이스크림 = {"메로나":1000,"폴라포":1200,"빵빠레":1800}
# 아이스크림["죠스바"]=1200
# 아이스크림["월드콘"]=1500
# print (아이스크림)
#
# print("메로나 가격: ", 아이스크림["메로나"])
#
# 아이스크림["메로나"] = 1300
#
# del 아이스크림["메로나"]
# print (아이스크림)

#불 (bool)
#a = Ture
#b = False
#print(type(a))
#print (bool("hello"))

a = input()
b = len(a)
if b >= 5:
    print('long')
elif len(a) >= 3 and b < 5:
    print('medium')
elif b < 3:
    print('short')
