# 공원 산책
# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    """ 문제 분석
    park의 길이는 50, routes의 길이도 50
    N은 북쪽, S는 서쪽, N은 남쪽, E는 동쪽을 의미
    x, y라고 했을 때, 동쪽으로 움직일 경우 y + 1, 서쪽은 y - 1, 남쪽은 x + 1, 북쪽은 x - 1이 된다.
    1. park 배열에서 S는 시작지점을 의미하므로 반복문을 통해 S가 있으면 위치 저장
    2. routes 배열에서 받는 위치 이동을 시켜서 결과 리턴
    """
    answer = []
    x = 0
    y = 0
    for i in range(len(park)):
        if 'S' in park[i]:
            x = i
            y = park[i].find('S')
    
    for route in routes:
        way = route.split()[0]
        cnt = int(route.split()[1])
        mx = x
        my = y

        for i in range(cnt):
            if (way == 'E'):
                my += 1
            if (way == "W"):
                my -= 1
            if (way == 'S'):
                mx += 1
            if (way == 'N'):
                mx -= 1
            
            if (mx >= 0 and my >= 0 and mx < len(park[0]) and my < len(park[0])):
                if park[mx][my] == 'X':
                    break
                if i == cnt - 1:
                    x = mx
                    y = my
        
    return [x, y]

print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))