# 조건문
'''
if 조건:
    참일 때
else:
    거짓일 때

for
for i in range(숫자):
for i in range(시작,끝):
for i in range(시작,끝,증감):
'''
# apple=30
# orange=20
# if apple>orange:
#     print("사과가 큼")
# else:
#     print("오랜지가 큼")

# for i in range(5):
#     print("안녕!")
# for i in range(5):
#     print(i)
# for i in range(1,11):
#     if i%2==1:
#         print(i)

# for i in range(1,11):
#     if i%2==0:
#         print(i)

# for i in range(20,41):
#     if i%3==0:
#         print(i)

# for i in range(50,101):
#     if i%3==0:
#       if i%4==0:
#         print(i)
# sum=0
# ssum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
#     if i%2==1:
#         ssum+=i
# print(sum-ssum)        
sum=1
for i in range(10,21):
    if i%3==0:
        sum*=i
print(sum)