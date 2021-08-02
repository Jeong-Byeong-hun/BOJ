def solution(clothes):
    test_dict = {}
    for i in clothes:
        if i[1] in test_dict:
            test_dict[i[1]] += 1
        else:
            test_dict[i[1]] = 1

    cnt = 1
    for i in test_dict.values():
        cnt = cnt * (i + 1)

    return cnt - 1


testCase = [["a", "aa"],
            ["b", "aa"],
            ["c", "aa"],
            ["aa", "bb"],
            ["bb", "bb"],
            ["c_c", "bb"],
            ["aaa", "cc"],
            ["bbb", "cc"],
            ["ccc", "cc"]]
solution(testCase)

# testcase
# // 63
# [
# ["a","aa"],
# ["b","aa"],
# ["c","aa"],
# ["aa","bb"],
# ["bb","bb"],
# ["c_c","bb"],
# ["aaa","cc"],
# ["bbb","cc"],
# ["ccc","cc"]
# ]
#
# // 7
# [
# ["a", "a"],
# ["b", "b"],
# ["c", "c"]
# ]
