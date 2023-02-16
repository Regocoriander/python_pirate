'''
리스트
 열거형 변수를 나타내는
 자료구조 중 하나
[사과]-[귤]-[바보민기]

.리스트는 대괄호를 이용함
.리스트 안의 값들은 쉼표로 구분함
A=10
B=바보민기
C=["사과","귤","바나나"]

특징1,2,3,4,5,6,7,8,9,10,11,12,13
리스트 안의 요소는 대괄호로
접근할 수 있음(indexing)
왼쪽부터 0번째임
오른쪽부터 -1번째임

빈 리스트 만들 수 있음
a=[]

요소를 추가할 때는 append
메소드를 이용함
단,맨뒤에만 추가됨

민기=[][sx=0]
민기.append["못생김"]
print(민기)

요소를 뺄때는 pop 메소드를 
이용함 
단, 맨 마지막 요소만 제거됨

요소값을 이용해서 제거할 때는
remove 메소드를 사용함
e=[1,2,3,4]
e.remove(3)
print(e)

정렬T오름차순
    L내림차순

오름차순 정렬할 때는 sort 메소드를 사용

내림차순 정렬 때는reverse 메소드를 사용

리스트와 니스트를 합칠때 "+" 사용
    메소드는 extend

리스트를 비울때 clear 메소드 사용
d=[100,200]
d.clear()
print(d)

특정 위치에 값을 추가할때 insert 메소드 사용
e=[1,2,3]
e.insert(1,100)
print(e)

값이 몇번째 있는지 찾을때 index 메소드 사용
f=[1,2,3,4,2]
print(f.index(2))

리스트 안에 값이 몇개인지 알아볼때count 메소드 사용
g=[1,2,3,4,2]
print(g.count(2))

리스트의 길이를 알고싶을때
    len 함수 사용
h=[1,2,3,4]
print(len(h))


'''
# A=10
# B="바보민기"
# C=["사과","귤","바나나"]
# D=[1,2,3,4]
# E=["사과",2,"귤",4]
# print(A)
# print(B)
# print(C)
# print(D)
# print(E)

# c=["사과","귤","바나나"]
# print(c[0])
# print(c[1])
# print(c[2])

# print(c[-1])
# print(c[-2])
# print(c[-3])

# d=(1,2,3,4)
# print(d[1]**d[2])
# print(d[-1]%d[1])

# 민기=[]
# print(민기)
# 민기.append("못생김")
# print(민기)
# 민기.append("바보")
# print(민기)
# 민기.pop()
# print(민기)
# 민기.pop()
# print(민기)

# 진우=["뺀질","블랙","모자"]
# print(진우)
# 진우.pop()
# print(진우)
# 진우.remove("뺀질")
# print(진우)
'''
num=[2,4,1,3,]
print(num)
num.sort()
print(num)

fruit=["watermelon","orange","apple","banana"]
print(fruit)
fruit.sort()
print(fruit)

num.reverse()
print(num)

fruit.reverse()
print(fruit)
'''
# e=[1,2,3,4]
# e.remove(3)
# print(e)

# f=[1,3,2,4]
# f.sort()
# print(f)

# g=[1,3,2,4]
# g.reverse()
# print(g)

# g=[1,3,2,4]
# g.sort()
# g.reverse()
# print(g)

# 결과1=[]
# for i in range(1,11):
#     if i % 4 != 0:
#         결과1.append(i)

# 결과1.reverse()
# print(결과1)

# def 구구단(숫자):
#     결과2=[]
#     for i in range(1,11):
#         결과2.append(i*숫자)
#     결과2.reverse()
#     print(결과2)

# 구구단(3)
# 구구단(7)

# def 짝수(숫자):
#     결과3=[]
#     for i in range(1,숫자*2+1):
#         if i%2==0:
#             결과3.append(i)
#     결과3.reverse()
#     print(결과3)

# 짝수(3)
# 짝수(6)
# 짝수(4)


# a=[2,4,1,3]
# a.sort()
# a.reverse()
# print(a)

# a=[1,2]
# b=[3,4]
# c=a+b
# print(c)

# a=[1,2]
# b=[3,4]
# a.extend(b)
# print(a)

# d=[100,200]
# d.clear()
# print(d)

# e=[1,2,3]
# e.insert(1,100)
# print(e)

# f=[1,2,3,4,2]
# print(f.index(2))

# g=[1,2,3,4,2]
# print(g.count(5))

# h=[1,2,3,4]
# print(len(h))

a=["바나나","사과","오렌지"]

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

# 1fruits=["orange","cherry","watermelon","apple","bluberry"]
# fruits.sort()
# fruits.reverse()
# for i in fruits:
#     print(i)

# 2phoneNumber=[0,1,0,1,2,3,4,5,6,7]
# phoneNumber.clear()
# phoneNumber.append(0)
# phoneNumber.append(1)
# phoneNumber.append(0)
# phoneNumber.append(9)
# phoneNumber.append(8)
# phoneNumber.append(7)
# phoneNumber.append(6)
# phoneNumber.append(5)
# phoneNumber.append(4)
# phoneNumber.append(3)
# print(phoneNumber)

# 3너는바보임수고=[]
# for i in 1,21:
#     if i%3==0:
#         너는바보임수고.append()
# 너는바보임수고.sort()
# 너는바보임수고.reverse()
# print(i)

# 4numbers = [num for num in range(1, 21) if num % 3 == 0]
# numbers.sort(reverse=True)
# print(numbers)

# 5def find_common_divisors(a, b):
#     common_divisors = []
#     for i in range(1, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             common_divisors.append(i)
#     return common_divisors