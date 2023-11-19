# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     report_cnt = {}
#
#     for rep in set(report):
#         a, b = rep.split()
#         if b in report_cnt:
#             report_cnt[b].append(a)
#         else:
#             report_cnt[b] = [a]
#
#     for values in report_cnt.values():
#         if len(values) >= k:
#             for v in values:
#                 index = id_list.index(v)
#                 answer[index] += 1
#
#     return answer
#
# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2
# print(solution(id_list, report, k))

def solution(players, callings):
    rank_player = {}
    player_rank = {}
    for i in range(len(players)):
        rank_player[i + 1] = players[i]
        player_rank[players[i]] = i + 1

    for call in callings:
        rank = player_rank[call]
        A = rank_player[rank - 1]
        rank_player[rank - 1],rank_player[rank] = call, A
        player_rank[call], player_rank[A] = rank - 1, rank
    return list(rank_player.values())

숙제 - 프로그래머스
가장 가까운 같은 글자
k번째 수
문자열 내 맘대로 정렬하기