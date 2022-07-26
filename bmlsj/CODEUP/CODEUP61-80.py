# 코드업 100제 문제 풀이 61-80

# 6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
a, b = map(int, input().split())
print(a | b)

# 6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기
a, b = map(int, input().split())
print(a ^ b)

# 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기
a, b = map(int, input().split())
c = a if a >= b else b
print(c)

# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = map(int, input().split())
min = (a if a < b else b) if ((a if a < b else b) < c) else c
print(min)

# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
a, b, c = map(int, input().split())
def even(i):
    if i % 2 ==0:
        print(i)
for i in a, b, c:
    even(i)

# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
a, b, c = map(int, input().split())
def odd_even(num):
    if num%2 ==0:
        print("even")
    else:
        print("odd")

for i in a, b, c:
    odd_even(i)

# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
a = int(input())
if a<0 and a%2==0: print('A')
elif a<0 and a%2 != 0 : print('B')
elif a > 0 and a%2 ==0 : print('C')
else: print('D')

# 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기
score = int(input())
if 90 <= score <= 100:
    print("A")
elif 70 <= score < 90:
    print("B")
elif 40 <= score < 70:
    print("C")
else: print("D")

# 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
score = input()
if score == 'A':
    print('best!!!')
elif score == 'B':
    print('good!!')
elif score == 'C':
    print('run!')
elif score == 'D':
    print('slowly~')
else: print('what?')

# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
month = int(input())

if month % 12 < 3:
    print("winter")
elif month % 6 < 3:
    print("summer")
elif month % 9 < 3:
    print("fall")
else:
    print("spring")

"""
a=int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")
"""

# 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기
n = 1
while n!=0:
    n = int(input())
    if n != 0:
        print(n)
    else:
        break

# 6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1
m = int(input())
while m > 0:
    print(m)
    m -= 1

# 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2
m = int(input())
while m > 0:
    m -= 1
    print(m)

# 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
s = ord(input())
a = ord('a')
while a <= s:
    print(chr(a), end=' ')
    a += 1

# 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1
n = 0
m = int(input())
while n <= m:
    print(n)
    n += 1

# 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2
n = int(input())
for i in range(n+1):
    print(i)
 
# 6077 : [기초-종합] 짝수 합 구하기
n = int(input())
sum = 0
for i in range(n+1):
    if i % 2 ==0:
        sum += i
print(sum)

# 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
while True:
    c = input()
    print(c)
    if c == 'q':
        break

# 6079 : [기초-종합] 언제까지 더해야 할까?
n = int(input())
sum = 0
tmp = 1
while True:
    sum += tmp
    if sum >= n:
        print(tmp)
        break
    tmp += 1

# 풀이2
t = 0
while sum < n:
    t += 1
    sum += t
print(t)


# 6080 : [기초-종합] 주사위 2개 던지기
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print("{0} {1}".format(i, j))
