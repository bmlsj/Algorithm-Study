# 코드업 100제 문제 풀이 41-60

# 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기
a, b = map(int, input().split())
print(a%b)

# 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기
f = float(input())
print(round(f, 2))
print(format(f, ".2f"))

# 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기
f1, f2 = map(float, input().split())
print(format(f1/f2, ".3f"))
# round(f1/f2, 3) 은 10.0/0.0001 = 100000.0 으로 소숫점 첫째자리까지만 나온다

# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
a, b, c = map(int, input().split())
sum = a+b+c
print(sum, format(sum/3, ".2f"))


# 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기
a = int(input())
print(a<<1)
# n << 1 : n의 2배
# n >> 1 : n의 1/2배
# n << 2 : n의 4배

# 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기
a, b = map(int, input().split())
print(a << b)

# 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1
a, b = map(int, input().split())
if a < b: print(True) 
else: print(False)

# 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2
a, b = map(int, input().split())
if a == b: print(True)
else: print(False)

# 6050 : [기초-비교연산] 정수 2개 입력받아 비교하기3
a, b = map(int, input().split())
if b >= a: print(True)
else: print(False)
# 답지
print(a<=b)

# 6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4
a, b = map(int, input().split())
# 내 풀이
if a != b: print(True)
else: print(False)
# 답지
print(a!=b)

# 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기
n = int(input())
print(bool(n))

# 6053 : [기초-논리연산] 참 거짓 바꾸기
a = bool(int(input()))
print(not a)

# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기
a, b = input().split()
print(bool(int(a)) != bool(int(b)))

# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
a, b = input().split()
print(bool(int(a)) == bool(int(b)))

# 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
a, b = input().split()
print(not(bool(int(a) or bool(int(b)))))
print(bool(int(a)==False and bool(int(b))==False))

# 6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기
a = int(input())
print(~(a))
# ~ : bitwise not
# & : bitwise and
# ^ : bitwise xor
# << : bitwise left shift
# >> : bitwise right shift

# 6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기
a, b = map(int, input().split())
print(a & b)

