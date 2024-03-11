# 덧칠하기
# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    """ 문제 분석
    n은 총 길이, m은 롤러의 길이, section은 칠해야할 구역
    n, m의 길이가 10만 이하이기 때문에 n^2 시간 복잡도 발생 시 1000만임 (1초 이내 수행 가능)
    """

    check = 0
    cnt = 0
    for sec in section:
        if sec > check:
            check = sec + m - 1
            cnt += 1

    return cnt
    
print(solution(8, 4, [2, 3, 6]))