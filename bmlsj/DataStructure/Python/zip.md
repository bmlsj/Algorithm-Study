# zip 파일

여러 개의 순회 가능한(iterable) 객체를 인자를 받고 각 객체가 담고 있는 원소 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환

```python
numbers = [1, 2, 3]
letters = ["A", "B", "C"]

for pair in zip(numbers, letters):
    print(pair)

# (1, 'A')
# (2, 'B')
# (3, 'C')
```

<br>

# unzip 하기
```zip()``` 함수로 엮어 놓은 데이터를 다시 해체(unzip)하고 싶을 때는 ```zip()``` 함수를 사용할 수 있다

```python
# zip을 사용해 묶기
numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))

print(pairs)   # [(1, 'A'), (2, 'B'), (3, 'C')]


# upzip하기
numbers, letters = zip(*pairs)
print(numbers)    # (1, 2, 3)
print(letters)    # ('A', 'B', 'C')
```