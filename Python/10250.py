for i in range(int(input())):
    h, w, n = map(int, input().split(' '))

    ho = n//h
    floor = n % h
    if floor != 0:
        ho += 1
        if ho < 10:
            ho = '0' +str(ho)
    else:
        floor = h
        if ho < 10:
            ho = '0' + str(ho)

    print(str(floor) + str(ho))