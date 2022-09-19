# 코딩테스트를 위한 파이썬 문법 정리

### **실수형**
소수부가 0일 때 0을 생략
```python
a = 5.    # 5.0
```

### **수의 지수 표현**

```python
a = 1e9       # 1,000,000,000
a = 75.25e1   # 752.5
a = 3954e-3   # 3.954
```

### **반올림 round 함수**
```python
round(123.456, 2)    # 123.46
```

<br>

## 리스트 자료형
### **리스트 초기화**
```python
a = [1, 2, 3, 4]

# 빈 리스트 선언
a = list()
a = []


# 크기가 N이고 모든 갓이 0인 1차원 리스트
n = 10
a = [0] * n
## [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

```

## 리스트 인덱싱과 슬라이싱
### **인덱싱**
인덱스 값을 입력해 리스트의 특정한 원소에 접근하는 것
- 음수의 정수를 넣으면 원소를 거꾸로 탐색

```python
a = [1, 2, 3, 4, 5]

print(a[1])  # 2

```

### **슬라이싱**
리스트의 연속적인 위치를 가져와야 할 때 사용

```python
a = [1, 2, 3, 4, 5]

print(a[1:3])   # [2, 3]
print(a[::-1])  # [5, 4, 3, 2, 1]

```

<br>

## 리스트 컴프리헨션
- 리스트를 초기화하는 방법 중 하나
- 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화
- 2차원 리스트를 초기화할 때 매우 효과적

```python
# 0부터 19까지의 수 중 홀수만 포함하는 리스트
## 리스트 컴프리헨션
arr = [i for i in range(20) if i%2 == 1]

## 일반 소스 코드
arr = []
for i in range(20):
    if i % 2 == 1
        arr.append(i)

# 1부터 9까지의 수의 제곱을 포함하는 리스트
## 리스트 컴프리헨션
arr = [i*i for i in range(1, 10)]

# 일반 소스코드
arr = []
for i in range(1, 10):
    arr.append(i*i)

# n*m 크기의 2차원 리스트 초기화
n = 3
m = 4

arr = [[0]*m for _ in range(n)]
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

```

### **특정 크기의 2차원 리스트를 초기화 할 때 반드시 리스트 컴프리헨션을 사용**
- 내부적으로 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문
```python
# 잘못된 방법
n = 3
m = 4
arr[[0] * m] * n    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

arr[1][1] = 5       # [[0,5,0,0],[0,5,0,0], [0,5,0,0]]
```

<br>

## 리스트 관련 기타 메서드
- **append()** : O(1)
- **sort()**
- **reverse()**
- **insert()** : O(n)
- **count()**
- **remove()** : O(n)

```python
a = [1, 3, 4, 5]

# 리스트에 원소 삽입
a.append(2)   # 1, 3, 4, 5, 2

# 오름차순 정렬
a.sort()      # 1, 2, 3, 4, 5

# 내림차순 정렬
a.sort(reverse=True)  # 5, 4, 3, 2, 1

# 원소 뒤집기
a.reverse()           # 1, 2, 3, 4, 5

# 특정 인덱스에 데이터 추가
## 인덱스 2에 3추가
a.insert(2, 3)        # 1, 2, 3, 3, 4, 5

# 특정 값인 데이터 개수 세기
a.count(3)            # 2

# 특정 값 데이터 삭제
## 인덱스가 낮은 것부터 삭제됨
## 인덱스 1 삭제
a.remove(1)           # 2, 3, 3, 4, 5
```
<br>

### **시간 복잡도를 고려해 remove는 사용하지 않은 것을 추천**
```python
a = [1, 2, 3, 4, 5, 5, 5]
rm_set = {3, 5}

# rm_set에 포함되지 않은 값만 저장
result = [i for i in a if i not in rm_set]
# 1, 2, 4
```
<br>

## 튜플 자료형
- 튜플은 한 번 선언된 값을 변경할 수 없음
- 리스트는 [ ], 튜플은 ( ) 
- 그래프 알고리즘 구현할 때 자주 사용
    - 다익스트라 최단 경로 알고리즘(우선순위 큐 사용)
    
        -> (비용, 노드번호) 형태로 튜플을 묶어서 관리

```python
a = (1, 2, 3, 4)
a[2] = 7 # TypeError
```

## 사전 자료형
- key, value의 쌍을 데이터로 가지는 자료형
- 튜플 자료형이 사전 자료형의 키로 사용되는 경우
- 사전 자료형에 특정한 원소가 있는 지 검사할 때 '원소 in 사전' 의 형태를 사용할 수 있다

    -> 리스트나 튜플에서도 사용 가능

```python
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

# {'사과':'apple', '바나나':'banana', '코코넛':'coconut'}

if '사과' in data:
        print("'사과'를 키로 가지는 데이터가 존재합니다")
```

### **사전 자료형 관련 함수**
- 키 데이터만 뽑아 리스트로 이용할 때는 ```keys()``` 함수 사용
- 값 데이터만 뽑아서 리스트로 이용할 때는 ```values()```함수를 이용

```python
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
values_list = data.values()

for key in key_list:
    print(data[key])
    # apple banana coconut
```
<br>

## 집합 자료형(Set)
- 중복 허용하지 않는다
- 순서가 없다
- 특정한 데이터가 이미 등장한 적 있는 지 여부를 체크할 때 효과적

```python
data = set([1, 1, 2, 3, 4, 4, 5])
# {1, 2, 3, 4, 5}
```

### **집합 자료형의 연산**
- 합집합, 교집합, 차집합 연산
```python
a = set([1, 2, 3, 4, 5])
b = {3, 4, 5, 6, 7}

print(a|b) # 합집합 {1, 2, 3, 4, 5, 6, 7}
print(a&b) # 교집합 {3, 4, 5}
print(a-b) # 차집합 {1, 2}
```

### **집합 자료형 관련 함수**
```python
data = set([1, 2, 3])

# 새로운 원소추가
data.add(4)   # {1, 2, 3, 4}

# 새로운 원소 여러개 추가
data.updata([5, 6])   # {1, 2, 3, 4, 5, 6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)     # {1, 2, 4, 5, 6}
```

<br>

## 파이썬의 기타 연산자
- ```in 연산자```와 ```not in 연산자```를 제공한다
- 자료형 (리스트, 튜플, 문자열, 사전)에 사용
- pass문 : 조건문의 값이 참이어도 아무것도 처리하고 싶지 않을 때
- 조건부 표현식을 이용하면 ```if ~ else``` 문을 한줄에 작성해 사용 가능
    - 리스트에 있는 원소의 값을 변경해서 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용 가능

```python
# 리스트 안에 x가 들어가 있으면 True
x in 리스트     
# 문자열 안에 x가 들어있지 않으면 True
x not in 문자열

score = 85
if score >= 80:
    pass
else: print('score < 80')

# 1줄일 경우 줄이기
if score >= 80: result = "sucess"
else: result = "fail"

# 조건부 표현식
result = "success" if score >= 80 else "fail"

# 3항 연산자
result = score >= 80 and "sucess" or "fail"

# 리스트에 있는 원소 값을 변경해 다른 리스트를 만들 때
a = [1 2, 3, 4, 5, 5, 5]
rm_set = {3, 5}

## 기본
result = []
for i in a:
    if i not in rm_set:
        result.append(i)

## 간결하게
result = [i for i in a if i not in rm_set]

```


### **이중 for문**
- 플로이드 워셜 알고리즘
- 다이나믹 프로그래밍

### **함수**
- 동일한 알고리즘을 반복적으로 수행해야 할 때 사용

### **global**
- 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우
```python
a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)  # 10
```

### **람다 표현식(Lambda)**
- 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다
- 람다식은 파이썬의 정렬 라이브러리를 사용할 때, 정렬 기준(Key)을 설정할 때에도 자주 사용한다

```python
def add(a, b):
    return a + b
print(add(3, 7))

# 람다 표현식으로 구현한 add()
print((lambda a, b: a+b)(3, 7))
```
<br>

## 입출력
### **입력**
- ```map()``` : 해당 리스트의 모든 원수에 int() 함수를 적용한다
- ```sys.stdin.readline()```
    - 입력을 최대한 빠르게 받아야하는 경우
    - ```readline()``` : 입력 후 엔터가 줄 바꿈 기호로 인식한다
    - ```rstrip()``` : 공백 문자를 제거하려면 같이 사용

```python
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())

# 입력을 최대한 빠르게 받아야 하는 경우
import sys
sys.strin.readlint().rstrip()
```


### **출력**
- ```print()``` : 기본적으로 줄바꿈 수행
    ```python
    answer = 7

    # 틀린 예
    print("정답은" + answer + "입니다") # TypeErrer 발생

    # 올바른 예
    print("정답은" + str(answer) + "입니다")
    print("정답은", str(answer), "입니다")
    ```

- f-string 
    ```python
    a = 7
    print(f"정답은 {a}입니다.")
    ```

