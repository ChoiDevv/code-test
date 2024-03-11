# 달리기 경주
# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    """ 문제 분석
    players 배열의 길이는 50,000 || callings 배열의 길이는 1,000,000 > N^2 시간 복잡도 발생 시 타임아웃
    1. players 배열의 등수를 딕셔너리로 구현
    2. callings 배열 반복문을 통해 등수를 변동
    """

    # 초반 등수
    # key-value 형태 : 이름-등수
    ranking = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        # 호출된 사람의 이름 calling
        # 변경해야할 부분 players 배열, ranking 딕셔너리 등수
        calling_player_rank = ranking[calling] # 호출한 사람 등수
        ranking[calling] -= 1
        ranking[players[calling_player_rank - 1]] += 1
        players[calling_player_rank], players[calling_player_rank - 1] = players[calling_player_rank - 1], players[calling_player_rank] # players 배열 swap

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
