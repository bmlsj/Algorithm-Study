# 힙

## 힙을 이용한 우선순위 큐

### 큐 선언
```python
import heapq

pd=[]
```

### heappush, heappop
- 일반적인 큐와 유사하지만 원소에서 큐를 뺄 때는 언제나 작은값을 내보냄
- heapq.heappush(heap,item)
    - 힙의 형태를 유지하면서 item을 push
- heapq.heappop(heap)
    - 힙의 형태를 유지하면서 가장 작은 항목을 pop
    - 비어있으면 IndexError 발생
    - 반환 없이 접근하려면 heap[0] 사용

```python
heapq.heappush(pq, 1)
heapq.heappush(pq, 5)
heapq.heappush(pq, 2)
heapq.heappush(pq, 4)
heapq.heappush(pq, 3)

print(heapq.heappop(pq)) # 1
print(heapq.heappop(pq)) # 2
print(heapq.heappop(pq)) # 3
print(heapq.heappop(pq)) # 4
print(heapq.heappop(pq)) # 5
```

### 비교대상을 튜플 인자로 받을 때
- 튜플의 원소를 차례로 비교해가며 가장 작은값을 판별함
```python
heapq.heappush(pq, (1, 2, 4))
heapq.heappush(pq, (2, 1, 1))
heapq.heappush(pq, (1, 3, 4))
heapq.heappush(pq, (1, 3, 3))
heapq.heappush(pq, (1, 2, 3))

print(heapq.heappop(pq)) # (1, 2, 3)
print(heapq.heappop(pq)) # (1, 2, 4)
print(heapq.heappop(pq)) # (1, 3, 3)
print(heapq.heappop(pq)) # (1, 3, 4)
print(heapq.heappop(pq)) # (2, 1, 1)
```

### heapify
- heapify(x)
    - 리스트 x를 선형 시간으로 제자리에서 heap으로 변환
```python
import heapq

heap = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# heapq.heapify(list)
heapq.heapify(heap)

print(heap) # Result [1, 2, 3, 6, 5, 4, 7, 8, 9]
```

### nlargest, nsmallest : 힙의 n개의 가장 큰 리스트, n개의 가장 작은 리스트
```python
import heapq

heap = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# heapq.heapify(list)
heapq.heapify(heap)

print(heapq.nsmallest(3, heap)) # Result [1, 2, 3]
print(heapq.nlargest(3, heap)) # Result [9, 8, 7]
```

### 최소힙을 최대힙으로 사용하기
- 가장 큰 수에 제일 높은 우선순위를 부여하고 싶다면 해당 수에 -1곱해줌
- pop할때 다시 -1를 곱해 원래 양수로 만들어줌
```python
import heapq

heap_q = []

heapq.heappush(heap_q, -3)
heapq.heappush(heap_q, -10)
heapq.heappush(heap_q, -1)
heapq.heappush(heap_q, -0)
heapq.heappush(heap_q, -4)

print(-1 * heapq.heappop(heap_q))

# 10
```