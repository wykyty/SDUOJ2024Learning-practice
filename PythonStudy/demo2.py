# coding=utf-8
# 斐波那契数列
n = int(input("请输入整数n\n"))
a, b = 0, 1
for i in range(n):
    print(b, end=" ")
    a, b = b, a + b
