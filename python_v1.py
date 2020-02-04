def myPostcode(text):
    if len(text) != 6:
        return False
    for i in range(0,2):
        if not text[i].isdecimal():
            return False
    if text[2] != "-":
        return False
    for i in range(3,6):
        if not text[i].isdecimal():
            return False
    return True