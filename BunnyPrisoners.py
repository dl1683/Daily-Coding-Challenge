from itertools import combinations


def solution(num_buns, num_required):
    keyrings = [[] for i in range(num_buns)]
    copiesPerKey = num_buns - num_required + 1
    for key, bunnies in enumerate(combinations(range(num_buns), copiesPerKey)):
        for bunny in bunnies:
            keyrings[bunny].append(key)

    return keyrings


if __name__ == "__main__":
    print(solution(5, 3))
    assert all([all([x == y for x, y in zip(a, b)])
                for a, b in zip([[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]], solution(5, 3))])
    assert all([all([x == y for x, y in zip(a, b)])
                for a, b in zip([[0], [1], [2], [3]], solution(4, 4))])