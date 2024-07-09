# s = ("hhh"
#      "ttt"
#      "jjj")
# print(s)
# print(s, end="")
# a = 100
# b = 50
# print(a, b, "kk")
#
# print(ord('北'))
# print(ord('京'))
# print((chr(21271)), chr(20140), end="")
# print(1, 2, 3, 4, 5, sep="->", end="")

n = 100
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("1 + 2 + ··· + 100 = ", sum, end="")
print()

a = [1, 2, 3, 4, 5]
i = 0
# print(a.__sizeof__(), end="")
while i < len(a):
    print(i, a[i])
    i += 1

for j in range(10):
    print(j, end=" ")
