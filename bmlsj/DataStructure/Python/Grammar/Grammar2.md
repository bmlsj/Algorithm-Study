# 주요 라이브러리 문법과 유의점
## 코딩테스트를 준비하며 반드시 알아야하는 라이브러리 6가지

1. 내장 함수

    ```print()```, ```input()```과 같은 기본 입출력 기능부터 ```sorted()``` 같은 정렬 기능을 포함하고 있는 내장 라이브러리

2. itertools

    파이썬에서 반복되는 형태의 테이터를 처리하는 기능을 제공하는 라이브러리
    
    순열과 조합 라이브러리를 제공

3. heapq

    힙(Heap) 기능을 제공하는 라이브러리

    우선순위 큐 기능을 구현하기 위해 사용

4. bisect

    이진 탐색/이분 탐색(Binary Search) 기능을 제공하는 라이브러리

5. Collections

    덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리

6. math

    필수적인 수학적 기능을 제공하는 라이브러리
    
    - 팩토리억, 제곱근, 최대공약수(GCD), 삼각함수, 파이(pi)

<br>

## 1. 내장 함수
- ```sum()``` : iterable 객체(리스트, 사전 자료형, 튜플 자료형 등)의 모든 원수의 합 반환
- ```min()``` : 파라미터가 2개 이상 들어왔을 때 가장 작은 값 반환
- ```max()``` : 파라미터가 2개 이상 들어왔을 때 가장 큰 값 반환
- ```eval()``` : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환


    ```python
    result = [1, 2, 3, 4, 5]

    # iterable 객체가 들어왔을 때 -> 리스트, 사전, 튜플 등
    sum(result)  # 15
    min(result)  # 1
    max(result)  # 5

    result = eval("(3+5)*7")  # 56
    ```

- ```sorted()``` : Iterable 객체가 들어왔을 때, 정렬된 결과를 반환
    - **key 속성**으로 정렬 기준을 명시할 수 있음
    - **reverse 속성**으로 정렬된 결과 리스트를 뒤집을 지의 여부를 설정 가능
    - 리스트와 같은 iterable 객체는 기본으로 ```sort()```함수를 내장하고 있어 ```sort()```로도 정렬이 가능

        -> ```sort()``` 사용 시, 객체 자체의 값이 변경됨


    ```python
    # 오름차순 정렬
    result = sorted([9, 1, 8, 5, 4])
    result = sorted([9, 1, 5, 1, 4], reverse=True)  # 기존 객체는 변경X, return 값 존재

    result.sort() # 기존 객체가 변경
    ```

    ```python
    # 거꾸로 출력하기

    data = [('홍길동', 35), ('이순신', 17), ('아무개', 88)]

    result = sorted(data, key = lambda x: x[1], reverse=True)
    ## [('아무개', 88), ('홍길동', 35), ('이순신', 17)]


    # 위와 같은 값을 가진다
    data.sort(key = lambda x: x[1], reverse=True)
    ```

- ```join()``` : 리스트를 문자열로 일정하게 합쳐주는 함수
    - ```'구분자'.join(리스트)```

    ```python
    data = ["23", "59", "59"]
    print(":".join(data))

    # 23:59:59
    ```

<br>

## 2. itertools
파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

- **permutations** 
    
    리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산
    - 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 반환하여 사용해야 한다

    ```python
    from itertools import permutations

    data = ["A", "B", "C"]

    # 모든 순열 구하기
    result = list(permutations(data, 3))
    ## [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A, 'B'), ('C', 'B', 'A')]
    ```

- **combinations**
    
    리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산
    - 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 반환하여 사용해야 한다

    ```python
    from itertools import combinations
    
    data = ['A', 'B', 'C']

    # 2개를 뽑는 모든 조합 구하기
    result = list(combinations(data, 2))
    ## [('A', 'B'), ('A', 'C'), ('B', 'C')]
    ```

- **product**

    permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산
    - 원소를 중복하여 뽑음
    - product 객체를 초기화 할 때는 뽑고사 하는 데이터의 수를 **repeat 속성값**으로 넣어줌
    - 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용해야 함


    ```python
    from itertools import product

    data = ['A', 'B', 'C']

    # 2개를 뽑는 모든 순열 구하기(중복 허용)
    result = list(product(data, repeat=2))

    # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
    ```

- **combinations_with_replacement** 
    combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산
        - 원소를 중복하여 뽑음
        - 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용

    ```python
    from itertools import combinations_with_replacment

    data = ['A', 'B', 'C']

    # 2개를 뽑는 모든 조합 구하기(중복 허용)
    result = list(combinations_with_replacement(data, 2))

    # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
    ```

## 3. heapq
파이썬에서 **힙 기능**을 위해 heapq 라이브러리를 제공
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용됨
- heapq 외에도 PriorityQueue 라이브러리를 사용할 수 있지만 코딩테스트 환경에서는 보통 heapq가 더 빠르게 동작한다

파이썬의 힙은 최소 힙으로 구성되어 있다. 보통 최소 힙 자료구조의 최상단 원소는 항상 **'가장 작은'** 원소

- ```heapq.heappush()``` : 힙에 원소 삽입
- ```heapq.heappop()``` : 힙에서 원소 꺼내기

**힙 정렬** : 최소 힙이므로, 단순히 원소를 힙에 전부 넣었다가 빼는 것 만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료됨

```python
# 힙 정렬 heapq로 구현하는 예제

import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

result = heapsort([1, 3, 5, 6, 9, 2, 4, 6, 8, 0])
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# 최대 힙 구현하여 내림차순 힙 정렬 구현
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
<br>

## 4. bisect
**이진 탐색**을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공
- '정렬된 배열'에서 특정한 원소를 찾아야할 때 매우 효과적으로 사용됨

- ```bisect_left(a, x)``` : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드 => O(logN)
- ```bisect_right(a, x)``` : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드 => O(logN)


```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))  # 2
print(bisect_right(a, x)) # 4
```

- '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때 효과적으로 사용됨
```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))  # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6
```

## 5. collections
유용한 자료구조를 제공하는 표준 라이브러리

1. ```deque```
    - 보통 파이썬에서는 deque를 사용해 큐를 구현
    - 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없음
    - 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입, 삭제할 때 매우 효과적

    - ```popleft()``` : 첫번째 원소 제거
    - ```pop()``` : 마지막 원소 제거
    - ```appendleft(x)``` : 첫번째 인덱스에 원소 x를 삽입
    - ```append(x)``` : 마지막 인덱스에 원소 x를 삽입

 **큐 자료구조**를 이용할 때 ```append()```와 ```popleft()```를 사용하기

 ```python
 from collections import deque

 data = deque([2, 3, 4])
 data.appendleft(1)
 data.append(5)

 print(data)        # deque([1, 2, 3, 4, 5])
 print(list(data))  # [1, 2, 3, 4, 5]
```

2. ```Counter```
리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 **내부의 원소가 몇 번씩 등장했는지** 알려줌

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])   # 3
print(counter['green'])  # 1
print(dict(counter))     # {'red' : 2, 'blue' : 3, 'green' : 1}
```
<br>

## 6. math
자주 사용되는 수학적 기능을 포함하고 있는 라이브러리

- ```factorial(x)``` : x! 값 반환
```python
import math

print(math.factorial(5)) # 120
```

- ```sqrt(x)``` : x의 제곱근 반환
```python
import math

print(math.sqrt(7))  # 2.6457513110645907
```

- ```gcd(a, b)``` : a와 b의 최대공약수 반환
```python 
import math

print(math.gcd(21, 14))  # 7
```

- 파이(PI), 자연상수 e
```python
import math

print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
```
