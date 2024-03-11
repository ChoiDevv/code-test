# 추억 점수
# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    """ 문제 분석
    photo 배열의 크기가 100까지이므로 n^2 시간 복잡도가 발생해도 타임아웃 x
    1. name 배열에 해당하는 추억 점수를 yearning 배열에서 가져와 딕셔너리로 생성
    2. photo 배열을 반복문을 통해 value 값을 가져와 배열에 append
    """
    answer = []

    memory_score = dict()
    for i in range(len(name)):
        memory_score[name[i]] = yearning[i]
    
    for array in photo:
        cnt = 0
        for i in range(len(array)):
            if array[i] in memory_score:
                cnt += memory_score[array[i]]
            else:
                cnt += 0
        answer.append(cnt)
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))