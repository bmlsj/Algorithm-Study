# ```sort()```와 ```sorted()``` 차이

## 1. ```sorted()```

```sorted(리스트명)```

- "내장 함수"
- 원본 리스트에 영향을 주지 않고, 새로운 리스트를 만들어 리턴한다

```python
some_list = [5, 7, 2, 3, 1]

print(sorted(some_list))  # [1, 2, 3, 5, 7]
print(some_list.sort())   # None
```


## 2. ```sort()```

```리스트명.sort()```

- "리스트형의 메소드"
- 기존의 리스트를 정렬시킨다
- ```None```을 리턴시킴

``` python
some_list = [5, 7, 2, 3, 1]

some_list.sort()
print(some_list) # [1, 2, 3, 5, 7]
```


<br>

|   | 정의  | 특징 |
|---|-------|------|
|```sort()```|리스트 메서드|원래 리스트에 영향O|
|```sorted()```|파이썬 표준 내장함수|새로운 정렬결과 반환, 원래 리스트에 영향X|