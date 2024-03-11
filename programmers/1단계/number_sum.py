# 숫자의 합 구하기
# 백준 11720번

N = int(input())
number = input()
cnt = 0

for num in number:
    cnt += int(num)

print(cnt)