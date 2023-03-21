'''
pip install 모듈이름
pip list
import 모듈이름
{모듈이름.변수
모듈이름.메소드()

plt.figure()


plt.plot([0,1,2],[0,1,2]'r')
plt.title("이름")

plt.show
'''

import matplotlib.pyplot as plt
# plt.figure()
# x1 = [-1, 0]
# y1 = [0, 1]
# x2 = [0, 1]
# y2 = [-1, 0,]
# x3 = [1, 0]
# y3 = [2, 1,]
# x4 = [0, -1]
# y4 = [1, 0,]
# plt.plot(x1, y1, x2, y2, x3, y3, x4, y4)
# plt.show()

# import matplotlib.pyplot as plt
# plt.figure()
# x1 = [0, 1, 2]
# y1 = [0, 1, 2]
# x2 = [0, 1, 2]
# y2 = [0, 1/2, 1]
# x3 = [0, 1, 2]
# y3 = [0, 2, 4]
# plt.plot(x1, y1, x2, y2, x3, y3)
# plt.show()

# plt.figure()
# x1 = []
# y1 = []
# for i in range(6):
#     x1.append(i)
#     y1.append(2*i+3)
# plt.plot(x1, y1)
# plt.show()


plt.figure()
x1 = []
y1 = []
x2 = []
y2 = []
for i in range(6):
    x1.append(i)
    y1.append(2*i+3)
    x1.append(i)
    y1.append()
plt.plot(x1, y1, x2, y2)
plt.show()
