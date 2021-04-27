a = "파이썬"
b = "프로그래밍"
c = '기\'본\''

print(a)
print(b)
print(c)

x = 10
y = 20
print(x < y)

student = ("gh", 2)
print(student)

student = "esdf", 30, "asef", True
print(student)
print(len(student))

student = {1:"one", 3:"two"}
student["4"] = "알라"
print(student)
print(student["4"])

x ,y , z = (34,5,234)
print(x,y,z)
print(x)

print(x)
print(y,z)
print(y)
print(z)

print(x,y,z)



def sum_a(sum_b):
    global sum_D, sum_ALL
    sum_A = sum_b * 4
    sum_B = sum_A + (sum_b * 30)
    sum_C = sum_B + (sum_b * 200)
    sum_D = sum_C + (sum_b * 1000)

    print(sum_D)
    print(sum_b)

sum_a(9)
str(sum_a)

def sum_a(sum_b):
    sum_A = str(sum_b)
    sum_B = str(sum_b) + str(sum_b)
    sum_C = str(sum_b) + str(sum_b) + str(sum_b)
    sum_D = str(sum_b) * 4
    sum_E = int(sum_A) + int(sum_B) + int(sum_C) + int(sum_D)

    print(sum_E)

sum_a(9)


def trs(inch):
    cm_tr = float(inch) * 2.54

    print("{0} inch => {1} cm".format(inch, cm_tr))



num_1 = int(input("첫번째 숫자를 입력하세요:"))
num_2 = input("+,-,*,/ 중 선택하세요:")
num_3 = int(input("두번째 숫자를 입력하세요:"))

print(type(num_1))
print(type(num_3))



if type(num_1) and type(num_3) == int:
    if num_2 == "+":
        print(f"{num_1} {num_2} {num_3} = {num_1 + num_3}")
    elif num_2 == "-":
        print(f"{num_1} {num_2} {num_3} = {num_1 - num_3}")
    elif num_2 == "*":
        print(f"{num_1} {num_2} {num_3} = {num_1 * num_3}")
    elif num_2 == "/":
        print(f"{num_1} {num_2} {num_3} = {num_1 / num_3:.2f}")
    else:
        print(f"{num_2}는 지원하지 않는 기호입니다")
else:
    print("정수만 입력해 주세요")
