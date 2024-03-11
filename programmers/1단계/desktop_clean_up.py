# 바탕화면 정리
# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    """ 문제 분석
    (0, 1) - (2, 3) > [0, 1, 3, 4]
    (1, 3) - (4, 7) - [1, 3, 5, 8]
    width 배열, height 배열 생성
    [width 배열 가장 작은 수, height 배열 가장 작은 수, width 배열 가장 큰 수 + 1, height 배열 가장 큰 수 + 1]
    """
    
    # wallpaper가 x, y 좌표에 있다고 가정
    x = []
    y = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
        
    return [min(x), min(y), max(x) + 1, max(y) + 1]

print(solution([".#...", "..#..", "...#."]))