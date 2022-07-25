# 코드업 100제 문제 풀이 1-20

# 포맷팅 형식
# 1. f-string
num=0
print(f"{num}")

# 2. format
num2=10
print("{0} {1}".format(num, num2))

# 3. %
print("%d %d" %(num, num2))


# 1001 : [기초-출력] 출력하기01
print("Hello")

# 1002 : [기초-출력] 출력하기02
print("Hello World")

# 1003 : [기초-출력] 출력하기03
print("Hello\nWorld")

# 1004 : [기초-출력] 출력하기04
print("\'Hello\'")              
print("'Hello'")

# 1005 : [기초-출력] 출력하기05
print("\"Hello World\"")

# 1006 : [기초-출력] 출력하기06
print("\"!@#$%^&*()\"")
print('"!@#$%^&*()"')

# 1007 : [기초-출력] 출력하기07
print('"C:\Download\hello.cpp"')

# 1008 : [기초-출력] 출력하기08
print('\u250C\u252C\u2510')
print('\u251C\u253C\u2524')
print('\u2514\u2534\u2518')

# 1010 : [기초-입출력] 정수 1개 입력받아 그대로 출력하기
a = int(input())
print(a)

# 1011 : [기초-입출력] 문자 1개 입력받아 그대로 출력하기
c = input()
print(c)

# 1012 : [기초-입출력] 실수 1개 입력받아 그대로 출력하기
b = float(input())
print(b)

# 1013 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기
i, j = map(int, input().split())
print(i, j)

# 1014 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기
a, b = map(str, input().split())
print(b, a)

# 1015 : [기초-입출력] 실수 입력받아 둘째자리까지 출력하기
# f"{실수:.표기할 자리수}"
num = float(input())
num = round(num, 3)
print(f"{num:.2f}")

# 1017 : [기초-입출력] 정수 1개 입력받아 3번 출력하기
n1 = int(input())
print(n1, n1, n1)

# 1018 : [기초-입출력] 시간 입력받아 그대로 출력하기
minute, second = input().split(':')
print("{0}:{1}".format(minute, second))

# 1019 : [기초-입출력] 년월일 입력받아 형식에 맞게 출력하기
# zfill : 앞에 0을 붙여주고 싶을 때 사용   # 숫자 
# rjust(width, [fillchar]) : fillchar 문자로 width 길이만큼 채워줌

year, month, day = input().split(".")
print("{0}.{1}.{2}".format(year.zfill(4), month.zfill(2), day.zfill(2)))
print("{0}.{1}.{2}".format(year.rjust(4, "0"), month.rjust(2, "0"), day.rjust(2, "0")))

# 1020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
birth, code = input().split("-")
print(birth+code)