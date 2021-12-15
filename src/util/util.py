# gets i-j as key coordinate
def get_key(i: int, j: int) -> str:
    return str(i) + '-' + str(j)


# unwinds a key to coordinates 1-2 -> 1, 2
def unwind_key(key: str) -> (int, int):
    s = key.split('-')
    return int(s[0]), int(s[1])
