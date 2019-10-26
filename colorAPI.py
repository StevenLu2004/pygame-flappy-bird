B = dict({bytes([i]).decode() : i for i in range(128)})
# print(B['0'], B['9'], B['A'], B['F'], B['a'], B['f'])

def _ihex(s):
    global B
    # print(s)
    if B['0'] <= s <= B['9']:
        return s - B['0']
    elif B['A'] <= s <= B['F']:
        return s - B['A'] + 10
    elif B['a'] <= s <= B['f']:
        return s - B['a'] + 10
    print("_ihex exception!")
    return 0

def _rgb(s):
    global B
    s = s.encode('utf-8')
    for i in s:
        if not (B['0'] <= i <= B['9'] or B['a'] <= i <= B['f'] or B['A'] <= i <= B['F']):
            print("_rgb exception 2!")
            return (0, 0, 0)
    if len(s) == 3:
        return tuple((_ihex(s[i]) * 17 for i in range(3)))
    elif len(s) == 6:
        return tuple(((_ihex(s[i << 1]) << 4) | (_ihex(s[(i << 1) | 1])) for i in range(3)))
    print("_rgb exception!")
    return (0, 0, 0)

def rgb(s):
    if s[0] == '#'[0]:
        return _rgb(s[1:])
    # print("Doing default.")
    print("rgb exception!")
    return (0, 0, 0)
