"""

                                            3회차
리터럴 = 정수형,부동소수점 숫자형, 문자열, 부울형, 리스트형
type함수 = 리터럴의 자료형 확인
정수와 부동소수점 숫자형 리터럴 내의 _는 무시됨

이스케이프 시퀀스
\\=\
\' = '
\"= "
\n = 줄바꿈
\tab = 탭

문자열 포멧팅   ex) "이름: %s" % "홍길동"
                "이름:(name)s\n 나이: %(age)s 세" % {"name":홍길동", "age":20)
                튜플 딕셔너리 활용가능

's' 문자열포맷
'c'문자포맷 정수를 유니코드 문자로 변환해 출력
'd'10진 정수
'o'8진수
'x'16진수
'f'부동소수점 숫자
'%'%문자 자체출력

문자열 출력 폭과 정렬 방향    "%10s"= 10칸을 주고 %오른쪽 문자열 출력
"%10s" % "우측정렬"     "%10s"= 10칸을 주고 %오른쪽 문자열 출력 10칸에 +10 이기때문에 앞에 6칸 남기고 오른쪽끝에 문자나옴
"%-10s" % "좌측정렬"    이건 %-10s 이기때문에 문자 나오고 뒤에 공백 10칸 맞춰서 나옴
"%010.2f" % 3.141592   f이기 때문에 부동소수점 이고 0.2가 들어가서 소수점 2번째 자리까지 나옴
                        10앞에 0이 있는데 이건 빈자리를 0으로 채우는것

str.format()
print("{0:c} => {1}".format(97, 97))
a => 97                                 이렇게 나옴

"{0:*^10}".format("중앙정렬")
***중앙정렬***

--추가 f-string

2-2. f- string 글자 정렬 표현방법

예를들어, 글자 수 10개일 때

왼쪽 정렬 {문자:10s}
가운데 정렬 {정수:^10d}
오른쪽 정렬 {실수:>10f}

소수점 자릿수 지정

2-2) f-string에서 중괄호 출력 방법
print(f'두째자리까지 표현 {x:.2f}')

1
2 num = 10
3 result = f'my age {{{num}}}, {num}'
4 print(result)
my age {10}, 10

# f-string과 딕셔너리
d = {'name': 'BlockDMask', 'gender': 'man', 'age': 100}
result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result)

# f-string과 리스트
n = [100, 200, 300]
print(f'list : {n[0]}, {n[1]}, {n[2]}')
for v in n:
    print(f'list with for : {v}')


                                            4회차
x[] = (),[],{}
 항목  튜플 리스트 셋,딕셔너리

리대 튜소불 항목대 셋중 len항목총숫자 딕:중

리 튜 없는항목 인덱스에러 딕 없는항목 키에러

딕셔너리 새로운 키 추가시 숫자4로 추가하면 항목5번째로 인식하고 변경으로 되지만
실제 5번째 항목이 없기때문에 변경이 되지않고 오류가남
그래서 4를 숫자가 아닌 문자열"4"로 추가해야함
하지만 키를 입력해서 값을 가져오려면 키에 4라는 숫자는 없고 "4"라는 문자열 만 존재하므로
함수["4"] 로 검색하지않으면 나오지않음;; 개불편

null 대신 none값 사용 내용이 빈함수 만들고 싶을 때 사용
none값은 트루 펄스시 펄스값을 가짐

튜플과 리스트를 활용해 한번에 여러 변수 만들기 가능
x,(y, z)= (35,36), (37,38)
print(x) | print(y,z) | print(y) | print(z)
정확히 이해는 안되지만 변수 괄호시 짝이 맞아야함;; 괄호안의 변수 둘이서 하나의 객체를 못담음;



                                      5회차
def sum_a(sum_b):
    sum_A = sum_b * 4
    sum_B = sum_A + (sum_b * 30)
    sum_C = sum_B + (sum_b * 200)
    sum_D = sum_C + (sum_b * 1000)

    print(sum_D)
    print(sum_b)

sum_a(9)

def sum_a(sum_b):
    sum_A = str(sum_b)
    sum_B = str(sum_b) * 2
    sum_C = str(sum_b) * 3
    sum_D = str(sum_b) * 4
    sum_E = int(sum_A) + int(sum_B) + int(sum_C) + int(sum_D)

    print(sum_E)

sum_a(9)


                                    6회차
/ 나누기
// 나누기 몫
% 나누기 나머지
** 제곱

a, b = 3, 2
"{0}+{1}={2}".format(a,b,a+b) 문자열 포멧팅

변수값으로 연산하기
같냐 다르냐 알아내기
and or not 결국 true false찾기


>< 관계 연산자 and or not 논리 연산자
not이 and or 보다 빠름



                                    7회차
T = int(input())
def trs(inch):
    cm_tr = float(inch) * 2.54

    print("{0} inch => {1} cm".format(inch, cm_tr))



x = input('name:')
print(x)
trs(T)
음;; 답은 아니라고 하는데 뭐냐;;


                                    8회차

                                    11회차
def water_(JAA, JAA_water, water):
    JAA_s = JAA_water * (JAA / 100)
    JAA_sum = JAA_s / (JAA_water + water) * 100
    print("혼합된 소금물의 농도:{0:.2f}".format(JAA_sum))

water_(20, 100, 200)
                                    12회차               인풋값이 다 스트링이고 num_1,num_3값이 숫자가 아니면 오류
                                                        뜨는데 이걸 어케막는지 모르겠따 짜증나
                                                        열받는데 걍 숫자빼고 딴거 들가면 다 못하게 막을까 ㅋ
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

                                    13회차
def 약수찾기():
    a = []
    T=float(0)
    T_input = float(input("약수찾을숫자를 입력하세요: "))
    T_mid=T_input//2
    T_min=T_input

    while T < T_mid-1:
        T = T + 1
        T_min=T_min-1
        if ((T_input/T)-(T_input//T))==0:
            a.append(T)
            a.append(T_input//T)
            #print(f"{T}(은)는 {T_input}의 약수입니다.")
            #print(f"{T_input//T}(은)는 {T_input}의 약수입니다.")

    #리스트에 값넣고 중복제거 후 정렬해서 프린트 하면댐 ㅇㅇ

    s=set(a)   #변수에 set 넣을때 s=sorted(set(a))로 해봤는데 안된다..
    print(sorted(s))
    # print(len(s))
    for i in sorted(s):
        print(f"{i}(은)는 {T_input}의 약수입니다.")

약수찾기()


                                    14회차
                                    15회차
16회차
17회차
18회차
19회차
20회차
21회차
22회차
23회차
24회차
25회차
26회차
27회차
28회차
29회차
30회차
31회차
32회차
33회차
34회차
35회차
36회차
37회차
38회차
39회차
40회차
41회차
42회차
43회차
44회차
45회차
46회차
47회차
48회차
49회차
50회차
51회차
52회차
53회차
54회차
55회차
56회차
57회차
58회차
59회차
60회차
61회차
62회차
63회차
64회차
65회차
66회차
67회차
68회차
69회차
70회차
71회차
72회차
73회차
74회차
75회차
76회차
77회차
78회차
79회차
80회차
81회차
82회차
83회차
84회차
85회차
86회차
87회차
88회차
89회차
90회차
91회차
92회차
93회차
94회차
95회차
96회차
97회차
98회차
99회차
100회차

Process finished with exit code 0













"""