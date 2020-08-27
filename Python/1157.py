def a(text):
    li = []
    text = text.upper()
    text_dict = {}
    for i in text:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1

    text_dict = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)

    
    if len(text_dict) == 1 :
        print(text_dict[0][0])
    elif text_dict[0][1] == text_dict[1][1] :
        print("?")
    else:
        print(text_dict[0][0])

text = input()
a(text)
