def str_to_list(payload: str) -> []:
    strs = []
    for char in payload:
        if char.isalnum():
            strs.append(char.lower())
    return strs

def reverse_str_list (ls: []) -> []:
    ls = ls[::-1]
    return ls

def list_to_str(ls: []) -> str:
    strs = "".join(ls)
    return strs

if __name__ == '__main__':
    ls = str_to_list('hello would')
    print(ls)
    reverse_ls = reverse_str_list(ls)
    print(reverse_ls)
    print(list_to_str(reverse_ls))
