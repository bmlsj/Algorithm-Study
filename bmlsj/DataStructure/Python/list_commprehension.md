## 리스트 컴프리헨션
기존의 리스트를 기반으로 새로운 리스트를 만들어 내는 구문
- 딕셔너리에도 사용이 가능하다

```python
    list(map(lambda x: x+10, [1, 2, 3]))
    # 결과 : [11, 12, 13]
```

```python
    [n*2 for n in range(1, 10+1) if n %2 == 1]
    # 결과 : [2, 6, 10, 14, 18]
    
    # 리스트 컴프리헨션을 사용하지 않을 경우
    a = [] 
    for n in range(1, 10+1):
        if n % 2 == 1:
            a.append(n*2)
```
<br>

**딕셔너리**
```python
    a = {}
    for key, value in original.items():
            a[key] = value
    
    # 리스트 컴프리헨션 사용할 경우
    a = {key, value in original.items()}
```
</br>

## 제너레이터(Generagor)
루프의 반복 동작을 제어할 수 있는 루틴 형태<br>
``` yield``` 구문(여기까지 실행 중이던 값을 내보낸다)을 사용해 제너레이터를 리턴

``` python
    def get_natural_number():
        n = 0
        while True:
            n += 1
            yield n     # 제너레이터를 리턴
    
    g = get_natural_number()
    for _ in range(1, 10):
        print(next(g))
    # 결과: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```
<br>

여러 타입의 값을 하나의 함수에서 생성하는 것도 가능
```python
    def generator():
        yield 1
        yield 'string'
        yield True
    
    g = generator()
    print(g)        
    # <generator object generator at 0x10a47c678>
    print(next(g))
    # 1
    print(next(g))
    # 'string'
    print(next(g))
    # True
```
<br>

## range
제너레이터의 방식을 활용하는 대표적 함수

for 문에서 사용할 경우 내부적으로 제너레이터의 ```next()``` 를 호출 하듯 매번 다음 숫자를 생성해낸다.

``` python
    a = [n for n in range(100)]
    b = range(100)
```

a에는 이미 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재한다. 

b에서는 값의 생성 조건만 보관하고 있기 때문에 숫자를 똑같이 100개 가지고 있지만 range 클래스를 활용하는 b 변수의 메모리 점유율이 훨씬 더 작다.
<br>
<br>

## enumerate
열거하다는 뜻의 함수로, 여러 가지 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴한다


```python
a = [1, 2, 3, 45, 2, 5]

enumerate(a)    
# <enumberate object a 0x1010f83f0>

list(enumerate(a))
# [(1, 0), (1, 2), (2, 3), (4, 45), (5, 2), (6, 5)] : 인덱스를 자동으로 부여
```

<br>

```a = ['a1', 'b2', 'c3']```리스트의 인덱스와 값을 함께 출력하는 방법

```python
# 1 - 값을 가져오기 위해 불필요한 a[i]조회와 len 사용
for i in range(len(a)):
    print(i, a[i])

# 2 - 변수를 별도로 관리하는 형태로 깔끔하지 않음
i = 0
for v in a:
    print(i, v)
    i += 1

# 3 - (인덱스, 값)이 깔끔하게 출력됨
for i, v in enumerate(a):
    print(i, v)
```

<br>

## 나눗셈 연산자

```python
# 나눗셈
print(5/3) # 1

# 몫
print(5//3) # 1

# 나머지
print(5%3)  # 2

# 몫과 나머지 한 번에 출력
print(divmod(5, 3))   # 결과 : (1, 2)
```

<br>

## print
```python

print('a', 'b')             # a b
print('a', 'b', sep=',')    # a,b

print('aa', end = ' ')
print('bb')                 # aa bb

a = ['a','b']
print(' '.join(a))          # a b
```
<br>

출력 포맷
```python
idx = 1
fruit = 'apple'

print('{0}: {1}'.format(idx+1, fruit))      # 2: apple
print('{}: {}'.format(idx+1, fruit))        # 2: apple

# f-string
print(f'{idx+1}: {fruit}')                  # 2: apple
```
<br>

## pass
코딩을 할 때 전체 골격을 잡아 놓고 내부에서 처리할 내용은 차근히 생각하며 만들겠다는 의도

pass 는 null 연산으로 아무것도 하지 않는 기능

```python
class MyClass(object):
    def method_a(self):
        pass
    
    def method_b(self):
        print("method b")

c = MyClass()
```

<br>

## locals
로컬 심볼 테이블 딕셔너리를 가져오는 메소드로 업데이트 또한 가능하다


로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령이므로 디버깅에 도움이 된다. 특히 로컬 스코프에 제한해 정보를 조회할 수 있기 때문에 클래스의 특정 메소드 내부나 함수 내부의 로컬 정보를 조회해 잘못 선언한 부분이 없는 지 확인하는 용도

```python
import pprint
pprint.pprint(locals())
```
클래스 메소드 내부의 모든 로컬 변수를 출력해 주어 디버깅에 좋다

<br>

## 좋은 코딩 스타일
- [Clean Code 클린 코드]
- [프로그래밍 수련법]
- [파이썬의 PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [구글의 파이썬 스타일 가이드](httpL//google.github.io/styleguide/pyguide.html)

간단히 주석을 부여하는 편이 가독성에 좋고, 의미있는 변수명을 사용할  것