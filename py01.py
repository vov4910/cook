# 파이썬 주석
# 파이썬 한줄 주석은 #을 사용합니다.

# 이것은 파이썬 한줄 주석입니다.

# 여러줄 주석은 """ 또는 ''' 를 사용합니다.

"""
이것은 여러줄 주석입니다.
이것은 여러줄 주석입니다.
이것은 여러줄 주석입니다.
"""

'''
이것은 여러줄 주석입니다.
이것은 여러줄 주석입니다.
이것은 여러줄 주석입니다.
'''

# 파이썬의 변수
x = 10
y = 3.14
z = "PI"
p = 'PI'
a = "this is variable"
b = "he says 'hello'"
c = 'he says "hello"'
c = "he says \"hello\""

# 변수를 화면에 출력
print(x)
print(y)
print(z)


# 변수의 타입 출력
print(type(x))
print(type(y))
print(type(z))


# 변수의 타입 변경
x = 10
print(x, type(x))
x = 3.14
print(x, type(x))
x = "안녕하세요"
print(x, type(x))

# 산술연산자(+, -, *, /, % , //, **)
x = 5
y = 3
#연산 결과가 실수면 실수를 그대로 계산
print(x/y)
#연산 결과를 정수로 변환
print(x//y)
#연산 결과를 강제로 정수로 변환
print(int(x/y))
#** 는 거듭제곱 계산
x = 12 ** 3
print(x)

# * : 수학 - 곱하기, 문자열 - 반복(제곱연산)
x = "학교" * 10
print(x)
print("=" * 40)

#문자열 + 문자열 ==> OK
#문자열 + 숫자  ==> NO
#숫자 + 문자열  ==> NO
s = "홍길동" + "전우치"
print(s)

s = str(18) + "홍길동"
print(s)

#문자열 포멧팅 (1)
name = "성춘향"
age  = 18
home = "남원시"
# 성춘향의 나이는 18세이고 고향은 남원시입니다.
msg = name + "의 나이는 " + str(age) + "세이고 고향은 " + home + "입니다."
print(msg)
print("=" * 40)

#문자열 포멧팅 (2)
msg = "%s의 나이는 %d세이고 고향은 %s입니다." % (name,age,home)
print(msg)
print("=" * 40)

#문자열 포멧팅 : f-string (3) 
msg = f"{name}의 나이는 {age}세이고 고향은 {home}입니다."
print(msg)
print("=" * 40)

# "오늘은 2026년 03월 03일입니다"를 출력하세요.
year  = 2026
month = 3
day   = 3
msg = "오늘은 %04d년 %02d월 %02d일입니다" % (year,month,day)
print(msg)

# print() 함수
x = 10
y = 20
z = 30
print(x,y,z)

#print() 함수에는 sep, end가 있음
#sep : seperate 구분자
#end : 끝

#print() 함수의 sep (seperate 구분자) 연습
print(x,y,z,sep="_")
print(x,y,z,sep=",")
print(x,y,z,sep="")

#print() 함수의 end 연습
print(x,end = ":")
print(y,end = ">")
print(z)

#키보드 입력에서  input()은 문자열 타입입니다.
name = input("이름:")
print("당신의 이름은 " + name + "입니다.")
print("당신의 이름은 %s입니다." % name)
print(f"당신의 이름은 {name}입니다.")

x = int(input("x값:"))
y = int(input("y값:"))
print("%d + %d = %d" % (x,y,x+y))





























































