# 평균 구하기
# 백준 1546번

""" 문제 분석
최댓값을 구하고 M이라 정의, 임시로 A, B, C라는 과목이 있다고 가정
1. (A // M * 100 + B // M * 100 + C // M * 100) // 3 = answer
2. ((A + B + C) // M) * 100 // 3 = answer
3. A + B + C = answer * 3 // 100 * M
4. (A + B + C) * 100 = answer * 3 * M
5. (A + B + C) * 100 / M / 3 = answer
"""

N = int(input())
number_list = list(map(int, input().split()))
print(sum(number_list) * 100 / max(number_list) / N)


def sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum