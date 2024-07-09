# score = eval(input("Enter your score: "))
# match score:
#     case 100:
#         print("A")
#     case 90:
#         print("B")
#     case 80:
#         print("D")
#     case 70:
#         print("E")
#     case 60:
#         print("F")
#     case _:
#         print("Invalid score")

for i in range(1, 11):
    print(f"{i} x {i} = {i*i}")

for i in range(100, 1000):
    sd = i % 10
    tens = i // 10 % 10
    hundreds = i // 100 % 10
    if i == sd**3 + tens**3 + hundreds**3:
        print(i)
