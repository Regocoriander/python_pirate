'''
while 조건:
    참일때 실행하는 코드

    hi를 3번출력
    for i in range(3):
        print("hi")
    ^ㅜ둘다같다
    i=0
    while i<3:
        print("hi")
        i+=1
'''
# i=0
# while i<101:
#     print("오늘 화요일")
#     i+=1

# i=1
# while i<11:
#     print(i)
#     i+=1

# i= 0
# while i<11:
#     if i%2==1:
#      print(i)
#     i+=1

# i=1
# while i<11:
#     if i%2==0:
#         print(i)   
#     i+=1

# i=1
# while i<101:
#         print(i)   
#         i+=1

# sum=0
# for i in range(101):
#     sum+=i
# print(sum)

# for i in range(1,101):
#     if i%2==0:
#         if i%3==0:
#             if i%5==0:
#                 print(i)
# sum=1
# for i in range(1,21):
#     if i%7==0:
#         sum*=i
# print(sum)

sum=0
su=0
for i in range(101):
    if i%2==0:
        sum+=i
    elif i%2==1:
        su+=i
print(sum-su)