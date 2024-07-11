# Code theo hướng dẫn AIO, tuy nhiên
#     báo lỗi SonarLint "Cognitive Complexity of functions should not be too high (python:S3776)"
#     -> Cần chia hàm levenshtein_distance thành những hàm nhỏ để dễ hiểu hơn

def levenshtein_distance(token1, token2):
    distances = [[0]*(len(token2)+1) for _ in range(len(token1)+1)]

    for t1 in range(len(token1)+1):
        distances[0][t1] = t1

    for t2 in range(len(token2)+1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1)+1):
        for t2 in range(1, len(token2)+1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1-1][t2-1]
            else:
                a = distances[t1][t2-1]
                b = distances[t1-1][t2]
                c = distances[t1-1][t2-1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]


# Chia nhỏ hàm levenshtein_distance thành nhiều hàm nhỏ


def levenshtein_distance_v2(token1, token2):
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    iterate_distances(token1, token2, distances)

    return distances[len(token1)][len(token2)]


def iterate_distances(token1, token2, distances):
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            distances[i][j] = calculate_distance(
                token1[i - 1], token2[j - 1], distances[i - 1][j - 1], distances[i][j - 1], distances[i - 1][j])


def calculate_distance(char1, char2, prev_distance, left_distance, top_distance):
    if char1 == char2:
        return prev_distance
    else:
        return 1 + min(left_distance, top_distance, prev_distance)
