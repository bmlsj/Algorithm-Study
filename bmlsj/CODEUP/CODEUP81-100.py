# 코드업 100제 문제 풀이 81-100

# 6081 : [기초-종합] 16진수 구구단 출력하기
s = int(input(), 16)
for i in range(1, 16):
    print("%X*%X=%X"%(s, i, i*s))

# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자
num = int(input())
for i in range(1, num+1):
    if i%10 == 3 or i%10==6 or i%10==9:
        print("X", end=" ")
    else:
        print(i, end=" ")

# 6083 : [기초-종합] 빛 섞어 색 만들기
r, g, b = map(int, input().split())
c = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            c += 1
print(c)


# 6084 : [기초-종합] 소리 파일 저장용량 
h, b, c, s = map(float, input().split())
m = h*b*c*s/8/1024/1024
print("%.1f MB"%m)

# 6085 : [기초-종합] 그림 파일 저장용량 계산하기
w, h, b = map(float, input().split())
m = w*h*b/8/1024/1024
print("%.2f MB"%m)

# 6086 : [기초-종합] 거기까지! 이제 그만~
n = int(input())
s = 0
t = 0
while True:
    t += 1
    s += t
    
    if s >= n:
        print(s)
        break

# 6087 : [기초-종합] 3의 배수는 통과
n = int(input())
for i in range(1, n+1):
    if i%3== 0:
        continue
    print(i, end=' ')

# 6088 : [기초-종합] 수 나열하기1
a, d, n = map(int, input().split())
n = a + (n-1)*d
print(n)

# 6089 : [기초-종합] 수 나열하기2
a, r, n = map(int, input().split())
n = a*(r**(n-1))
print(n)


# 6090 : [기초-종합] 수 나열하기3
a, m, d, n = map(int, input().split())
for i in range(1, n):
    a = a*m + d
print(a)

# 6091 : [기초-종합] 함께 문제 푸는 날
a, b, c = map(int, input().split())
d = 1
# 1
while d%a!=0 or d%b!=0 or d%c !=0:
    d += 1
print(d)
# 2
while True:
    if d%a==0 and d%b==0 and d%c ==0:
        print(d)
        break
    d += 1

# 6092 : [기초-리스트] 이상한 출석 번호 부르기1
n = int(input())
a = list(map(int, input().split()))
r = [0 for i in range(23) ]
for i in range(len(a)):
    r[a[i]-1] += 1

for i in range(len(r)):
    print(r[i], end=" ")

# 6093 : [기초-리스트] 이상한 출석 번호 부르기2
n = int(input())
a = input().split()
# for i in range(n):
#      a[i] = int(a[i])
# for i in range(n-1, -1, -1):
#       print(a[i], end=' ')

list = a[::-1]
print(' '.join(list))

# 6094 : [기초-리스트] 이상한 출석 번호 부르기3
n = int(input())
a = list(map(int, input().split()))
## 함수
print(min(a))
## for문
min = a[0]
for i in range(n):
    if a[i] < min:
        min = a[i]
print(min)

# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기
n = int(input())

d = [[0 for j in range(20)] for i in range(20)] # List Comprehensions

for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

# 6096 : [기초-리스트] 바둑알 십자
d = []
for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)

for i in range(19):
    d[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):    
    x, y = map(int, input().split())

    for j in range(19):
        if d[j][y-1] == 0:
            d[j][y-1] = 1
        else:
            d[j][y-1] = 0

        if d[x-1][j] == 0:
            d[x-1][j] = 1
        else:
            d[x-1][j] = 0

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()

# 6097 : [기초-리스트] 설탕과자 뽑기
# 격자판의 세로(h), 가로(w), 막대 개수(n), 각 막대 길이(l)
# 막대 놓는 방향(d: 가로 0, 세로 1)

w, h = map(int, input().split())
n = int(input())
# arr = [[0 for i in range(w)] for j in range(h)]

arr = [[0] * h for _ in range(w)]
# w와 h 위치 주의

for i in range(n):
    l, d, x, y = map(int, input().split())
    
    for j in range(l):

        if d == 0: # 가로
            arr[x-1][y+j-1] = 1
        else:       # 세로
            arr[x+j-1][y-1] = 1

for i in range(w):
    for j in range(h):
        print(arr[i][j], end=' ')
    print()


# 6098 : [기초-리스트] 성실한 개미
# 0 : 갈 수 있는 곳, 1 : 장애물, 2: 먹이
m = []
m = [[0] * 11 for _ in range(11)]

for i in range(10):
    m[i] = list(map(int, input().split()))

x = 1
y = 1
while True:
    if m[x][y] == 2:
        m[x][y] = 9
        break
    elif m[x][y+1] == 1 and m[x+1][y] == 1:
        m[x][y] = 9
        break
    
    m[x][y] = 9   # start
    if m[x][y+1] == 1:
        x += 1
    elif m[x+1][y] == 1:
        y += 1
    else: 
        y += 1

for i in range(10):
    for j in range(10):
        print(m[i][j], end=' ')
    print()