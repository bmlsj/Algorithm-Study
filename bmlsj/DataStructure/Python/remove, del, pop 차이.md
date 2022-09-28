# remove, del, pop, clear 차이

## 1. remove
```list.remove(삭제할 문자열)```

특정 인덱스가 아닌 첫번째 일치하는 값을 제거

```python
a = [0, 2, 3, 2]
a.remove(2)
print(a)  # [0, 3, 2]
```

<br>

## 2. del
```del List```

특정 인덱스에서 항목을 제거 혹은 리스트 자체를 삭제


```python
a = [9, 8, 7, 6]
del a[1]
print(a)  # [9, 7, 6]
```

<br>

## 3. pop
```list.pop(인덱스)```

- 인덱스를 지정하면, 지정한 인덱스의 문자열을 삭제
- 인덱스를 지정하지 않으면, 리스트의 마지막 데이터를 삭제

```python
a = [4, 3, 5]
a.pop(1)    # 3
print(a)    # [4, 5]
```

<br>

## 4. clear
```list.clear()```

리스트의 내용을 전부 삭제(초기화)

변수는 남아있다는 것이  ```del```과의 차이점

```python
a = [1, 2, 3]
a.clear()
print(a)    # []
```

<br>

## 시간 복잡도
n개의 요소들 중에서 i번째 요소를 삭제할 때
- **del** : O(n-i)
- **pop** : O(n-i)
- **remove** : O(n)


<br>

---

## 참고사이트

#### [성능 비교](https://brownbears.tistory.com/452)