def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

def solution(players, callings):
    # 각 선수의 이름과 등수를 저장하는 딕셔너리 생성
    rank_dict = {player: idx+1 for idx, player in enumerate(players)}
    # 경주가 끝난 후 선수들의 이름을 담을 배열
    result = players[:]
    # 해설진이 부른 선수를 확인하면서 등수를 조정
    current_rank = len(players)
    for calling in callings:
        # 해당 선수가 추월한 선수들의 등수를 1씩 감소시킴
        for player, rank in rank_dict.items():
            if rank < rank_dict[calling]:
                rank_dict[player] += 1
        # 해당 선수의 등수를 갱신함
        rank_dict[calling] = 1
    # 딕셔너리를 등수순으로 정렬하고, 각 선수의 이름을 배열에 담아 반환
    sorted_players = sorted(rank_dict.items(), key=lambda x: x[1])
    result = [player[0] for player in sorted_players]
    return result


def solution(players, callings):
    answer = []
    dict_name = {}
    dict_order = {}
    for i in range(len(players)):
        dict_name[players[i]] = i
        dict_order[i] = players[i]

    for calledName in callings:
        # calledName = "kai"
        # 바꿀 대상이 되는 인덱스와 이름을 가져옴
        calledNum = dict_name[calledName]  # 4 (kai의 인덱스)
        targetName = dict_order[calledNum - 1]  # "poe" (스위칭할 대상의 이름)
        targetIdx = calledNum - 1  # 3 (poe의 인덱스)
        dict_name[calledName] -= 1  # kai의 값이 4에서 3으로 바뀜
        dict_order[dict_name[calledName]] = calledName  # 3번째 값이 kai로 바뀜
        # 원래 3번째 자리에 있던 poe의 값을 4로 바꿈
        dict_name[targetName] = calledNum
        dict_order[calledNum] = targetName

    for player in dict_order.values():
        answer.append(player)

    return answer