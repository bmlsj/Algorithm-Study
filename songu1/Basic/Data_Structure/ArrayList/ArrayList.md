# ArrayList

## 1. 리스트 입력 - 한줄에서 띄어쓰기로 입력받기
    
    ```python
    import sys
    data=list(map(int,sys.stdin.readline().split()))
    ```
    
## 2. 리스트 입력 - 한줄에 하나씩 입력 받기
    
    ```python
    import sys
    data=[]
    
    for i in range(10):
    	data.append(int(sys.stdin.readline()))
    	#data.append(sys.stdin.readline().rstrip())  : # 원소가 정수가 아님
    ```
    
## 3. 리스트 관련 함수
    
    ```python
    subway=[10,20,30]
    subway=["가","나","다"]  #인덱스 0, 1, 2
    subway.index("나")  #나의 인덱스값 -> 1
    subway.append("마바")   #맨 뒤에 ()안 값 삽입 -> ['가',....,'마바']
    subway.insert(1,"사")   #index 1자리에 "사"삽입 -> ['가','사','나',..'마바']
    subway.pop()     #리스트 제일 마지막 값 삭제 -> ['가','사','나','다']
    subway.count("가")   #'가'가 몇번 나오는지 출력 -> 1번
    
    num_list=[5,2,4,3,1]
    num_list.sort() # 오름차순 정렬  ->  [1,2,3,4,5]
    num_list.reverse() # 순서 뒤집기   ->[5,4,3,2,1]
    num_list.clear() # 모두 지우기
    ```

## 4. 2차원 배열 입력받기
    ```python
    array = [list(map(int, input().split())) for _ in range(NUM)]
    ```

    