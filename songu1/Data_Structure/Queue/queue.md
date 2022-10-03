# 큐

### deque 생성
```python
from collections import deque

queue=deque()
```

### 오른쪽에 데이터 추가
append 사용
```python
queue.append(3)
```

### 왼쪽에 데이터 추가
appendleft 사용
```python
queue.appendleft(2)
```

### 오른쪽에 데이터 삭제
pop 사용
```python
queue.pop()
```

### 왼쪽에 데이터 삭제
popleft 사용
```python
queue.popleft()
```


# 우선순위 큐

### 우선순위 큐 생성
```python
from queue import PriorityQueue

queue= PriorityQueue()
que=PriorityQueue()
```

### 원소 추가
put
```python
queue.put(4)
queue.put(1)
queue.put(7)

# 튜플 형식
que.put(('3','A'))
que.put(('1','B'))
que.put(('2','C'))
```

### 원소 삭제
get()함수 사용
```python
print(queue.get())  #1
print(queue.get())  #4
print(queue.get())  #7

print(que.get()[1]) # B
print(que.get()[1]) # C
print(que.get()[1]) # A