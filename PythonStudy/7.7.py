x = 3 + 4j
print("""The value of x is: {}""".format(x))

print("The real part of x is {}".format(x.real))
print("The imag part of x is {}".format(x.imag))

str = "HelloWorld"
substr1 = str[0]
substr2 = str[-10]
substr3 = str[2:5]
substr4 = str[-5:-1]
substr5 = str[-9:]
substr6 = str[1:]
substr7 = str[::]
print(substr1, substr2, substr3, substr4, substr5, substr6, substr7)

print(chr(65))
print(ord('A'))

print(hex(255))
print(oct(255))
print(bin(255))

print("####################")

age = eval(input("Enter your age: "))
print(age, type(age))

height = eval(input("请输入您的身高")) # 相当于float(age)
print(height, type(height))
# 178.6 <class 'float'>

string = "北京欢迎你"
print(string) # 北京欢迎你
print(eval("string")) # 北京欢迎你
# print(eval("北京欢迎你")) # 报错

print(type("sdf"))

