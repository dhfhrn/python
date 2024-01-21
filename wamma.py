# 미완
# def solution(n, stages):
#     answer = []
#     r = {}
#     x = len(stages)
#     for i in range(1, n+1):
#         if x == 0:
#             r[i] = 0
#         else:
#             r[i] = stages.count(i) / x
#             r[i] -= stages(i)
#
#     return answer

# 선생님 풀이
# def solution(N,stages):
#     answer = []
#     user = len(stages)
#     x = []
#     for i in range(1, N+1):
#         curr = stages.count(i)
#         if user == 0:
#             rate = 0
#         else:
#             rate = curr / user
#         x.append([rate, -i])
#         user -= curr
#
#     x.sort(reverse= True)
#     for r, s in x:
#         answer.append(-s)
#     return answer

# 완성
# def solution(board, h, w):
#     n = len(board)
#     count = 0
#     dh = [0, 1, -1, 0]
#     dw = [1, 0, 0, -1]
#     for i in range(4):
#         h_check = h + dh[i]
#         w_check = w + dw[i]
#         if 0 <= h_check < n and 0 <= w_check < n:
#             if board[h][w] == board[h_check][w_check]:
#                 count += 1
#     return count

# 선생님 풀이1
# def solution(data, ext, val_ext, sort_by):
#     new_data = []
#     standard = ['code', 'date', 'maximum', 'remain']
#     for i in data:
#         idx = standard.index(ext)
#         if i[idx] < val_ext:
#             new_data.append(i)

#     idx = standard.index(sort_by)
#     for d in range(len(new_data)):
#         new_data[d] = [new_data[d][idx], new_data[d]]

#     new_data.sort()
#     answer = []
#     for _data in new_data:
#         answer.append(_data[1])

#     return answer

# 선생님 풀이2
# def solution(data, ext, val_ext, sort_by):
#     new_data = []
#     standard = ['code', 'date', 'maximum', 'remain']
#     for i in data:
#         idx = standard.index(ext)
#         if i[idx] < val_ext:
#             new_data.append(i)

#     idx = standard.index(sort_by)
#     new_data.sort(key= lambda x : x[idx])

#     return new_data

tkinter
https://076923.github.io/posts/Python-tkinter-1/

백준 2759번 숙제
