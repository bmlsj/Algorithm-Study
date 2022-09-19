# 입력받은 각 케이스마다 한 줄씩 평균ㅇ르 넘는 학생의 비율을 반올림하여 소수점 셋째자리까지 기술함
import sys

C=int(input())
for i in range(C):
    data=list(map(int,sys.stdin.readline().split()))
    ave=sum(data[1:])/data[0]
    count=0
    for j in range(1,data[0]+1):
        if data[j]>ave:
            count+=1
    print("%.3f%%"%(count/data[0]*100))