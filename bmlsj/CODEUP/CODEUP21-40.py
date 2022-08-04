# 코드업 100제 문제 풀이 21-40

# 1021 : [기초-입출력] 단어 한 개 입력받아 나누어 출력하기
c = input()
for i in range(len(c)):
    print(c[i])

# 1022 : [기초-입출력] 연월일 입력받아 나누어 출력하기
# s = input()
print(f"{s[:2]} {s[2:4]} {s[4:]}")
print(s[:2], s[2:4], s[4:], sep=' ')

# 1023 : [기초-입출력] 시분초 입력받아 분만 출력하기
# 내 풀이
time = list(input().split(":"))
print(time[1])

# 답지
h, m, s = input().split(':')
print(m)

# 1024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기
a, b = map(str, input().split())
print(a+b)

# 1025 : 정수 2개 입력받아 합 계산하기
a, b = map(int, input().split(' '))
print(a+b)

# 1026 : [기초-값변환] 실수 2개 입력받아 합 계산하기
a = float(input())
b = float(input())
print(a+b)

# 1027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1
ten = int(input())
print("%x" %(ten))  # 16진수

# 1028 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2
ten = int(input())
print("%X" %(ten))  # 16진수

# 1029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기
eight = int(input(), 16)
print("%o"%eight)

# 1030 :  [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기
# 입력 문자를 10진수 유니코드 값으로 저장
eng = ord(input())
print(eng)

# 1031 :  [기초-값변환] 정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c))

# 1032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기
d = int(input())
print(-d)

# 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기
s = ord(input())       # 문자를 아스키코드로 변환
print(chr(s+1))

# 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기
a, b = map(int, input().split(" "))
print(a-b)

# 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기
a, b = map(float, input().split(" "))
print(a*b)

# 6036 : [기초-산술연산] 단어 여러 번 출력하기
s, p = input().split()
print(s*int(p))

# 6037 : [기초-산술연산] 문장 여러 번 출력하기
a = int(input())
b = input()
print(a*b)

# 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기
a, b = map(int, input().split())
print(a**b)

# 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기
a, b = map(float, input().split())
print(a**b)

# 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기
a, b = map(int, input().split())
print(a//b)

