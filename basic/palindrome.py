import pprint


def str_to_list(palyload: str) -> []:
    strs = []
    for char in palyload:
        if char.isalnum():
            strs.append(char.lower())
    return strs

def isPalindrame(ls: []) -> bool:
    while len(ls) > 1:
        if ls.pop(0) != ls.pop():
            return False
    return True


if __name__ == '__main__':
    ls = str_to_list("A man, a plan, a canal: panama")
    print(ls)
    isPal = isPalindrame(ls)
    print(isPal)
