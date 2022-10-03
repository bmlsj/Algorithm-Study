# 스택

### 리스트를 활용해 스택을 생성
```python
stack=[]
```

### 자료의 삽입(Push)
append()메서드 사용
```python
stack.append(1)
```

### 자료의 삭제(Pop)
pop()메서드 사용
```python
stack.pop()
```

### 스택의 최상단 자료의 확인
리스트 인덱싱[-1]을 활용
```python
stack.append(1) # [1]
stack.append(3) # [1,3]
stack[-1]   # 3
```

### 스태깅 비어있는지 확인
조건문 이용
```python
if stack:   #스택이 비어있지 않음
    pass
else:       #스택이 비어있음
    pass
```

### 스택의 크기 확인
len(stack) 활용
```python
len(stack)
```