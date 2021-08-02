def solution(encrypted_text, key, rotation):
    answer = ''
    text = rota(rotation, encrypted_text)
    list_temp = decode(text, key)

    for i in list_temp:
        answer += chr(i)

    return answer


def rota(rotation, encrypted_text):
    temp_text = encrypted_text
    temp_rotation = rotation
    if rotation < 0:
        temp_rotation = rotation * -1

    temp_rotation = temp_rotation % len(encrypted_text)

    if rotation > 0:
        temp_text = temp_text[temp_rotation:] + temp_text[0:temp_rotation]
    elif rotation < 0:
        temp_text = temp_text[len(encrypted_text) - temp_rotation:] + temp_text[0:len(encrypted_text) - temp_rotation]

    return temp_text


def decode(text, key):
    list1 = []
    temp_x = 0
    temp_y = 0
    decode_text = text

    for i in range(len(text)):
        temp_x = ord(text[i]) % 96
        temp_y = ord(key[i]) % 96

        temp_num = temp_x - temp_y

        temp_num %= 26

        if temp_num == 0:
            temp_num = 26

        list1.append(temp_num + 96)

    return list1


print(solution("bac", "dbc", -3))

