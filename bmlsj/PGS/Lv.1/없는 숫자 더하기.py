# 테스트 케이스
numbers = [1, 2, 3, 4, 6, 7, 8, 0]

def solution(numbers):
    answer = -1
    sum = 0
    for num in numbers:
        sum += num
    answer = 45 - sum
    
    return answer

# 간결한 답안
"""
def solution(numbers):
    return 45 - sum(numbers)
"""
