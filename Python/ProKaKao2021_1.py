def solution(s):
    change_dict = {"0": "zero",
                   "1": "one",
                   "2": "two",
                   "3": "three",
                   "4": "four",
                   "5": "five",
                   "6": "six",
                   "7": "seven",
                   "8": "eight",
                   "9": "nine"}

    for key, value in change_dict.items():
        print(s.replace(value, key))
        s = s.replace(value, key)

    return int(s)



